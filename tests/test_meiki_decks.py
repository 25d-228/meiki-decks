import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

import meiki_decks
import mossformer2_batch


class MeikiDecksTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.language = "test-Latn"
        self.stage = "foundation"

    def tearDown(self):
        self.temporary_directory.cleanup()

    def card(self, card_id="test-001", sentence="I am ready.", cloze="ready"):
        return {
            "id": card_id,
            "sentence": sentence,
            "cloze": cloze,
            "answer": cloze,
            "accepted_answers": [],
            "lemma": cloze,
            "meaning": "prepared",
            "audio": f"work/audio/{self.language}/{self.stage}/{card_id}.mp3",
        }

    def write_stage(self, cards):
        coverage_path = self.root / "coverage" / self.language / f"{self.stage}.md"
        cards_path = self.root / "cards" / self.language / f"{self.stage}.json"
        coverage_path.parent.mkdir(parents=True, exist_ok=True)
        cards_path.parent.mkdir(parents=True, exist_ok=True)
        coverage_path.write_text("# Test coverage\n", encoding="utf-8")
        cards_path.write_text(json.dumps(cards), encoding="utf-8")

    def tts_configuration(self):
        return {
            self.language: {
                "model": "local-model",
                "reference_wav": "work/voices/test/reference.wav",
                "reference_text": "work/voices/test/reference.txt",
            }
        }

    def write_voice_reference(self, transcript="Exact reference transcript.\n"):
        reference_directory = self.root / "work" / "voices" / "test"
        reference_directory.mkdir(parents=True, exist_ok=True)
        reference_wav = reference_directory / "reference.wav"
        reference_text = reference_directory / "reference.txt"
        reference_wav.write_bytes(b"reference audio")
        reference_text.write_text(transcript, encoding="utf-8")
        return reference_wav, reference_text

    def denoiser_configuration(self):
        runner = self.root / "mossformer2_batch.py"
        runner.write_text("# test runner\n", encoding="utf-8")
        working_directory = self.root / "mossformer-work"
        working_directory.mkdir()
        return {
            "model": mossformer2_batch.MODEL_NAME,
            "code_commit": mossformer2_batch.CODE_COMMIT,
            "model_revision": mossformer2_batch.MODEL_REVISION,
            "checkpoint_sha256": mossformer2_batch.CHECKPOINT_SHA256,
            "code_path": str(mossformer2_batch.CODE_PATH),
            "checkpoint": str(mossformer2_batch.CHECKPOINT_PATH),
            "one_time_decode_length": mossformer2_batch.ONE_TIME_DECODE_LENGTH,
            "decode_window": mossformer2_batch.DECODE_WINDOW,
            "python": "fake-mossformer-python",
            "working_directory": str(working_directory),
            "runner": runner.name,
        }

    def finish_denoiser_batch(self, command, failed=None):
        failed = {} if failed is None else failed
        manifest_path = Path(command[command.index("--manifest") + 1])
        report_path = Path(command[command.index("--report") + 1])
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        succeeded = []
        for card in manifest["cards"]:
            if card["id"] in failed:
                continue
            Path(card["denoised"]).write_bytes(
                f"denoised {card['id']}".encode()
            )
            succeeded.append(card["id"])
        report_path.write_text(
            json.dumps(
                {
                    "model": mossformer2_batch.MODEL_NAME,
                    "succeeded": succeeded,
                    "failed": failed,
                }
            ),
            encoding="utf-8",
        )
        return subprocess.CompletedProcess(
            command,
            1 if failed else 0,
            stderr="\n".join(
                f"failed card {card_id}: {detail}"
                for card_id, detail in failed.items()
            ),
        )

    def test_valid_card_data_is_accepted(self):
        card = self.card()
        card["reading"] = "ready"
        self.write_stage([card])

        cards = meiki_decks.check_stage(self.root, self.language, self.stage)

        self.assertEqual(cards, [card])

    def test_malformed_card_data_is_rejected(self):
        self.write_stage({"id": "not-an-array"})

        with self.assertRaisesRegex(meiki_decks.DeckError, "top-level array"):
            meiki_decks.check_stage(self.root, self.language, self.stage)

    def test_duplicate_card_ids_are_rejected(self):
        self.write_stage([self.card(), self.card()])

        with self.assertRaisesRegex(meiki_decks.DeckError, "duplicate card ID"):
            meiki_decks.check_stage(self.root, self.language, self.stage)

    def test_absent_or_repeated_cloze_is_rejected(self):
        cases = (
            self.card(sentence="I am prepared."),
            self.card(sentence="ready means ready"),
        )
        for card in cases:
            with self.subTest(sentence=card["sentence"]):
                self.write_stage([card])
                with self.assertRaisesRegex(meiki_decks.DeckError, "exactly once"):
                    meiki_decks.check_stage(self.root, self.language, self.stage)

    def test_answer_that_differs_from_cloze_is_rejected(self):
        card = self.card()
        card["answer"] = "prepared"
        self.write_stage([card])

        with self.assertRaisesRegex(meiki_decks.DeckError, "answer must equal cloze"):
            meiki_decks.check_stage(self.root, self.language, self.stage)

    def test_incorrect_audio_path_is_rejected(self):
        card = self.card()
        card["audio"] = "work/audio/wrong.mp3"
        self.write_stage([card])

        with self.assertRaisesRegex(meiki_decks.DeckError, "audio must equal"):
            meiki_decks.check_stage(self.root, self.language, self.stage)

    def test_probe_audio_requires_48_khz_mono_and_complete_decode(self):
        audio_path = self.root / "audio.mp3"
        audio_path.write_bytes(b"audio")
        commands = []

        def fake_command(command, **arguments):
            commands.append(command)
            if command[0] == "ffprobe":
                return subprocess.CompletedProcess(
                    command,
                    0,
                    stdout=json.dumps(
                        {
                            "streams": [{"sample_rate": "48000", "channels": 1}],
                            "format": {"duration": "1.25"},
                        }
                    ),
                    stderr="",
                )
            return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

        duration_ms = meiki_decks.probe_audio(audio_path, run_command=fake_command)

        self.assertEqual(duration_ms, 1_250)
        self.assertEqual([command[0] for command in commands], ["ffprobe", "ffmpeg"])
        self.assertEqual(commands[1][-2:], ["null", "-"])

    def test_generate_audio_loads_once_and_continues_after_a_failed_card(self):
        cards = [
            self.card("test-001", "First is ready."),
            self.card("test-002", "Second is ready."),
            self.card("test-003", "Third is ready."),
        ]
        self.write_stage(cards)
        reference_wav, _ = self.write_voice_reference()
        commands = []
        generations = []
        import_paths = []
        denoiser_configuration = self.denoiser_configuration()

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                generations.append(arguments)
                import_paths.append(
                    {Path(path or Path.cwd()).resolve() for path in sys.path}
                )
                if arguments["text"] == cards[1]["sentence"]:
                    raise RuntimeError("synthetic failure")
                return [0.0, 0.1]

        def fake_command(command, **arguments):
            commands.append((command, arguments))
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(command)
            Path(command[-1]).write_bytes(b"generated audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        def fake_write(path, waveform, sample_rate):
            self.assertEqual(sample_rate, 48_000)
            path.write_bytes(b"untreated baseline")

        error_output = io.StringIO()
        with (
            contextlib.redirect_stderr(error_output),
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()) as loader,
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write) as writer,
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 1)
        loader.assert_called_once()
        self.assertEqual(
            generations,
            [
                {
                    "text": card["sentence"],
                    "prompt_wav_path": str(reference_wav),
                    "prompt_text": "Exact reference transcript.\n",
                    "reference_wav_path": str(reference_wav),
                }
                for card in cards
            ],
        )
        self.assertEqual(len(commands), 3)
        self.assertEqual(
            sum(command[0][0] == "fake-mossformer-python" for command in commands),
            1,
        )
        self.assertEqual(writer.call_count, 2)
        repository_root = Path(meiki_decks.__file__).resolve().parent
        self.assertTrue(all(repository_root not in paths for paths in import_paths))
        self.assertIn(repository_root, {Path(path or Path.cwd()).resolve() for path in sys.path})
        self.assertTrue((self.root / cards[0]["audio"]).is_file())
        self.assertTrue((self.root / cards[2]["audio"]).is_file())
        stage_workspace = (
            self.root / "work" / "denoiser-temp" / self.language / self.stage
        )
        self.assertTrue(stage_workspace.is_dir())
        self.assertIn("test-002", error_output.getvalue())

    def test_generate_audio_retains_stage_files_after_conversion_failure(self):
        card = self.card()
        self.write_stage([card])
        self.write_voice_reference()
        denoiser_configuration = self.denoiser_configuration()

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                return [0.0, 0.1]

        def failed_command(command, **arguments):
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(command)
            return subprocess.CompletedProcess(command, 1, stderr="conversion failed")

        def fake_write(path, waveform, sample_rate):
            path.write_bytes(b"untreated baseline")

        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()),
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write),
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=failed_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 1)
        stage_workspace = (
            self.root / "work" / "denoiser-temp" / self.language / self.stage
        )
        self.assertTrue((stage_workspace / "baseline" / "test-001.wav").is_file())
        self.assertTrue((stage_workspace / "denoised" / "test-001.wav").is_file())
        self.assertFalse((self.root / card["audio"]).exists())

    def test_generate_audio_retry_reuses_retained_baseline(self):
        card = self.card()
        self.write_stage([card])
        self.write_voice_reference()
        denoiser_configuration = self.denoiser_configuration()
        baseline_path = (
            self.root
            / "work"
            / "denoiser-temp"
            / self.language
            / self.stage
            / "baseline"
            / "test-001.wav"
        )
        baseline_path.parent.mkdir(parents=True)
        baseline_path.write_bytes(b"retained untreated baseline")

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)
            generate = mock.Mock(side_effect=AssertionError("baseline was regenerated"))

        def fake_command(command, **arguments):
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(command)
            Path(command[-1]).write_bytes(b"encoded denoised audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        model = FakeModel()
        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=model) as loader,
            mock.patch.object(meiki_decks, "write_waveform") as writer,
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 0)
        loader.assert_called_once()
        model.generate.assert_not_called()
        writer.assert_not_called()
        self.assertTrue((self.root / card["audio"]).is_file())

    def test_generate_audio_releases_voxcpm_gpu_memory_before_denoising(self):
        card = self.card()
        self.write_stage([card])
        self.write_voice_reference()
        denoiser_configuration = self.denoiser_configuration()
        events = []

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                return [0.0, 0.1]

        class FakeCuda:
            @staticmethod
            def empty_cache():
                events.append("release")

        def fake_write(path, waveform, sample_rate):
            path.write_bytes(b"untreated baseline")

        def fake_command(command, **arguments):
            if command[0] == "fake-mossformer-python":
                events.append("denoise")
                return self.finish_denoiser_batch(command)
            Path(command[-1]).write_bytes(b"encoded denoised audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()),
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write),
            mock.patch.dict(sys.modules, {"torch": mock.Mock(cuda=FakeCuda())}),
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 0)
        self.assertEqual(events, ["release", "denoise"])

    def test_generate_audio_retry_regenerates_baseline_after_clipping_failure(self):
        card = self.card()
        self.write_stage([card])
        self.write_voice_reference()
        denoiser_configuration = self.denoiser_configuration()
        stage_workspace = (
            self.root / "work" / "denoiser-temp" / self.language / self.stage
        )
        baseline_path = stage_workspace / "baseline" / "test-001.wav"
        baseline_path.parent.mkdir(parents=True)
        baseline_path.write_bytes(b"retained untreated baseline")
        (stage_workspace / "report.json").write_text(
            json.dumps(
                {
                    "failed": {
                        "test-001": "denoised output introduces clipped samples",
                    }
                }
            ),
            encoding="utf-8",
        )

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)
            generate = mock.Mock(return_value=[0.0, 0.1])

        def fake_write(path, waveform, sample_rate):
            path.write_bytes(b"replacement untreated baseline")

        def fake_command(command, **arguments):
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(command)
            Path(command[-1]).write_bytes(b"encoded denoised audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        model = FakeModel()
        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=model),
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write) as writer,
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 0)
        model.generate.assert_called_once()
        writer.assert_called_once_with(baseline_path, [0.0, 0.1], 48_000)
        self.assertTrue((self.root / card["audio"]).is_file())

    def test_generate_audio_removes_stage_workspace_once_after_success(self):
        cards = [
            self.card("test-001", "First is ready."),
            self.card("test-002", "Second is ready."),
        ]
        self.write_stage(cards)
        self.write_voice_reference()
        denoiser_configuration = self.denoiser_configuration()
        commands = []
        probed = []

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                return [0.0, 0.1]

        def fake_write(path, waveform, sample_rate):
            path.write_bytes(b"untreated baseline")

        def fake_command(command, **arguments):
            commands.append(command)
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(command)
            self.assertEqual(Path(command[command.index("-i") + 1]).parent.name, "denoised")
            Path(command[-1]).write_bytes(b"encoded denoised audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        stage_workspace = (
            self.root / "work" / "denoiser-temp" / self.language / self.stage
        )
        original_rmtree = meiki_decks.shutil.rmtree
        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()) as loader,
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write),
            mock.patch.object(
                meiki_decks.shutil,
                "rmtree",
                wraps=original_rmtree,
            ) as remove_tree,
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda path: probed.append(path) or 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 0)
        loader.assert_called_once()
        remove_tree.assert_called_once_with(stage_workspace)
        self.assertFalse(stage_workspace.exists())
        self.assertEqual(commands[0][0], "fake-mossformer-python")
        self.assertEqual(sum(command[0] == "ffmpeg" for command in commands), 2)
        self.assertTrue(all((self.root / card["audio"]).is_file() for card in cards))
        self.assertTrue(any(path.parent.name == "encoded" for path in probed))
        self.assertTrue(all(self.root / card["audio"] in probed for card in cards))

    def test_generate_audio_reports_one_denoiser_failure_and_installs_other_cards(self):
        cards = [
            self.card("test-001", "First is ready."),
            self.card("test-002", "Second is ready."),
        ]
        self.write_stage(cards)
        self.write_voice_reference()
        denoiser_configuration = self.denoiser_configuration()

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                return [0.0, 0.1]

        def fake_write(path, waveform, sample_rate):
            path.write_bytes(b"untreated baseline")

        def fake_command(command, **arguments):
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(
                    command,
                    failed={"test-002": "synthetic denoiser failure"},
                )
            Path(command[-1]).write_bytes(b"encoded denoised audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        error_output = io.StringIO()
        with (
            contextlib.redirect_stderr(error_output),
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()),
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write),
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 1)
        self.assertTrue((self.root / cards[0]["audio"]).is_file())
        self.assertFalse((self.root / cards[1]["audio"]).exists())
        stage_workspace = (
            self.root / "work" / "denoiser-temp" / self.language / self.stage
        )
        self.assertTrue(stage_workspace.is_dir())
        self.assertIn("test-002", error_output.getvalue())
        self.assertIn("synthetic denoiser failure", error_output.getvalue())

    def test_mossformer_batch_loads_once_for_multiple_cards(self):
        cards = [
            {
                "id": "test-001",
                "baseline": str(self.root / "test-001-baseline.wav"),
                "denoised": str(self.root / "test-001-denoised.wav"),
            },
            {
                "id": "test-002",
                "baseline": str(self.root / "test-002-baseline.wav"),
                "denoised": str(self.root / "test-002-denoised.wav"),
            },
        ]
        manifest_path = self.root / "manifest.json"
        report_path = self.root / "report.json"
        manifest_path.write_text(
            json.dumps(
                {
                    "model": mossformer2_batch.MODEL_NAME,
                    "code_commit": mossformer2_batch.CODE_COMMIT,
                    "model_revision": mossformer2_batch.MODEL_REVISION,
                    "checkpoint_sha256": mossformer2_batch.CHECKPOINT_SHA256,
                    "code_path": str(mossformer2_batch.CODE_PATH),
                    "checkpoint": str(mossformer2_batch.CHECKPOINT_PATH),
                    "one_time_decode_length": mossformer2_batch.ONE_TIME_DECODE_LENGTH,
                    "decode_window": mossformer2_batch.DECODE_WINDOW,
                    "cards": cards,
                }
            ),
            encoding="utf-8",
        )
        enhancer = object()
        loader = mock.Mock(return_value=enhancer)
        processor = mock.Mock()

        with contextlib.redirect_stdout(io.StringIO()):
            result = mossformer2_batch.process_batch(
                manifest_path,
                report_path,
                load_model=loader,
                process_file=processor,
            )

        self.assertEqual(result, 0)
        loader.assert_called_once_with()
        self.assertEqual(processor.call_count, 2)
        self.assertTrue(all(call.args[0] is enhancer for call in processor.call_args_list))
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(report["succeeded"], ["test-001", "test-002"])
        self.assertEqual(report["failed"], {})

    def test_mossformer_batch_hides_repository_from_lazy_model_imports(self):
        repository_root = Path(mossformer2_batch.__file__).resolve().parent
        original_import_path = sys.path[:]

        def fake_batch(_manifest_path, _report_path):
            resolved_import_path = [
                Path(path or Path.cwd()).resolve() for path in sys.path
            ]
            self.assertNotIn(repository_root, resolved_import_path)
            return 0

        try:
            sys.path.insert(0, str(repository_root))
            with mock.patch.object(
                mossformer2_batch,
                "process_batch",
                side_effect=fake_batch,
            ):
                result = mossformer2_batch.main(
                    [
                        "--manifest",
                        str(self.root / "manifest.json"),
                        "--report",
                        str(self.root / "report.json"),
                    ]
                )
            self.assertEqual(result, 0)
            self.assertEqual(sys.path, [str(repository_root), *original_import_path])
        finally:
            sys.path[:] = original_import_path

    def test_generate_audio_skips_a_nonempty_existing_mp3(self):
        card = self.card()
        self.write_stage([card])
        audio_path = self.root / card["audio"]
        audio_path.parent.mkdir(parents=True)
        audio_path.write_bytes(b"existing audio")

        with mock.patch.object(meiki_decks, "load_tts_model") as loader:
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
            )

        self.assertEqual(failures, 0)
        loader.assert_not_called()
        self.assertEqual(audio_path.read_bytes(), b"existing audio")

    def test_generate_audio_retry_removes_completed_stage_workspace(self):
        card = self.card()
        self.write_stage([card])
        audio_path = self.root / card["audio"]
        audio_path.parent.mkdir(parents=True)
        audio_path.write_bytes(b"validated audio")
        stage_workspace = (
            self.root / "work" / "denoiser-temp" / self.language / self.stage
        )
        stage_workspace.mkdir(parents=True)
        (stage_workspace / "retained.wav").write_bytes(b"diagnostic audio")

        with mock.patch.object(meiki_decks, "load_tts_model") as loader:
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
            )

        self.assertEqual(failures, 0)
        self.assertFalse(stage_workspace.exists())
        loader.assert_not_called()

    def test_generate_audio_rejects_missing_or_empty_reference_wav_before_model_load(self):
        self.write_stage([self.card()])
        configuration = self.tts_configuration()
        reference_wav = self.root / configuration[self.language]["reference_wav"]
        reference_text = self.root / configuration[self.language]["reference_text"]
        reference_text.parent.mkdir(parents=True)
        reference_text.write_text("Reference transcript.", encoding="utf-8")

        with mock.patch.object(meiki_decks, "load_tts_model") as loader:
            with self.assertRaisesRegex(meiki_decks.DeckError, "reference WAV is missing"):
                meiki_decks.generate_audio(
                    self.root,
                    self.language,
                    self.stage,
                    tts_config=configuration,
                )

            reference_wav.write_bytes(b"")
            with self.assertRaisesRegex(meiki_decks.DeckError, "reference WAV is empty"):
                meiki_decks.generate_audio(
                    self.root,
                    self.language,
                    self.stage,
                    tts_config=configuration,
                )

        loader.assert_not_called()

    def test_generate_audio_rejects_missing_or_empty_transcript_before_model_load(self):
        self.write_stage([self.card()])
        configuration = self.tts_configuration()
        reference_wav = self.root / configuration[self.language]["reference_wav"]
        reference_text = self.root / configuration[self.language]["reference_text"]
        reference_wav.parent.mkdir(parents=True)
        reference_wav.write_bytes(b"reference audio")

        with mock.patch.object(meiki_decks, "load_tts_model") as loader:
            with self.assertRaisesRegex(meiki_decks.DeckError, "transcript is missing"):
                meiki_decks.generate_audio(
                    self.root,
                    self.language,
                    self.stage,
                    tts_config=configuration,
                )

            reference_text.write_text("   ", encoding="utf-8")
            with self.assertRaisesRegex(meiki_decks.DeckError, "transcript is empty"):
                meiki_decks.generate_audio(
                    self.root,
                    self.language,
                    self.stage,
                    tts_config=configuration,
                )

        loader.assert_not_called()

    def test_languages_use_voxcpm2_ultimate_reference_files(self):
        self.assertEqual(
            meiki_decks.TTS_CONFIG,
            {
                "fr-FR": {
                    "model": "openbmb/VoxCPM2",
                    "reference_wav": "work/voices/fr-FR/reference.wav",
                    "reference_text": "work/voices/fr-FR/reference.txt",
                },
                "ja-JP": {
                    "model": "openbmb/VoxCPM2",
                    "reference_wav": "work/voices/ja-JP/reference.wav",
                    "reference_text": "work/voices/ja-JP/reference.txt",
                },
                "ko-KR": {
                    "model": "openbmb/VoxCPM2",
                    "reference_wav": "work/voices/ko-KR/reference.wav",
                    "reference_text": "work/voices/ko-KR/reference.txt",
                },
            },
        )

    def test_selected_mossformer_configuration_is_fixed(self):
        self.assertEqual(
            meiki_decks.MOSSFORMER_CONFIG,
            {
                "model": "MossFormer2_SE_48K",
                "code_commit": "6b3774dc79c46ae8bed2a4fa5f706f0ac8c75c61",
                "model_revision": "eff8c97925c8bec812af707814b3e5d777fd4503",
                "checkpoint_sha256": (
                    "03692b9f773bbd6bb43b9c5a41f96b1e28affd66e13796b7bec66ad3d8b227c6"
                ),
                "code_path": (
                    "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/"
                    "mossformer2-se-48k-code"
                ),
                "checkpoint": (
                    "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/"
                    "mossformer2-se-48k-model/last_best_checkpoint.pt"
                ),
                "one_time_decode_length": 20,
                "decode_window": 4,
                "python": (
                    "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/"
                    "environments/mossformer2-se-48k-py312/bin/python"
                ),
                "working_directory": "/home/Yue_Ziran/workspace/meiki-decks-issue-92",
                "runner": "mossformer2_batch.py",
            },
        )

    def test_korean_generation_uses_the_fixed_reference_pair(self):
        self.language = "ko-KR"
        self.stage = "00"
        card = self.card("ko-test-001", "한국어 문장을 연습합니다.", "연습합니다")
        self.write_stage([card])
        reference_directory = self.root / "work" / "voices" / self.language
        reference_directory.mkdir(parents=True)
        reference_wav = reference_directory / "reference.wav"
        reference_wav.write_bytes(b"Korean reference audio")
        reference_text = reference_directory / "reference.txt"
        reference_text.write_text("차분하게 한국어를 연습합니다.\n", encoding="utf-8")
        generations = []
        denoiser_configuration = self.denoiser_configuration()

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                generations.append(arguments)
                return [0.0, 0.1]

        def fake_command(command, **arguments):
            if command[0] == "fake-mossformer-python":
                return self.finish_denoiser_batch(command)
            Path(command[-1]).write_bytes(b"generated audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        def fake_write(path, waveform, sample_rate):
            path.write_bytes(b"untreated baseline")

        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()) as loader,
            mock.patch.object(meiki_decks, "write_waveform", side_effect=fake_write),
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                denoiser_config=denoiser_configuration,
            )

        self.assertEqual(failures, 0)
        loader.assert_called_once_with(meiki_decks.TTS_CONFIG["ko-KR"])
        self.assertEqual(
            generations,
            [
                {
                    "text": card["sentence"],
                    "prompt_wav_path": str(reference_wav),
                    "prompt_text": "차분하게 한국어를 연습합니다.\n",
                    "reference_wav_path": str(reference_wav),
                }
            ],
        )

    def test_model_loader_uses_voxcpm2_without_denoising_or_compilation(self):
        model = object()
        from_pretrained = mock.Mock(return_value=model)
        fake_voxcpm = mock.Mock()
        fake_voxcpm.VoxCPM.from_pretrained = from_pretrained

        with mock.patch.dict(
            "sys.modules",
            {"voxcpm": fake_voxcpm},
        ):
            loaded_model = meiki_decks.load_tts_model(meiki_decks.TTS_CONFIG["ja-JP"])

        self.assertIs(loaded_model, model)
        from_pretrained.assert_called_once_with(
            "openbmb/VoxCPM2",
            load_denoiser=False,
            optimize=False,
        )

    def test_require_audio_uses_probe_for_nonempty_local_file(self):
        card = self.card()
        self.write_stage([card])
        audio_path = self.root / card["audio"]
        audio_path.parent.mkdir(parents=True)
        audio_path.write_bytes(b"local audio")
        probed = []

        cards = meiki_decks.check_stage(
            self.root,
            self.language,
            self.stage,
            require_audio=True,
            probe=lambda path: probed.append(path) or 1_250,
        )

        self.assertEqual(cards, [card])
        self.assertEqual(probed, [audio_path])

    def test_validate_audio_reports_file_inspection_errors(self):
        audio_path = self.root / "inaccessible.mp3"

        with (
            mock.patch.object(Path, "is_file", side_effect=PermissionError("denied")),
            self.assertRaisesRegex(meiki_decks.DeckError, "cannot inspect audio file"),
        ):
            meiki_decks.validate_audio(audio_path, probe=lambda _: 1_000)

    def test_build_creates_verified_version_four_archive_with_deduplicated_media(self):
        cards = [
            self.card("test-001", "First is ready."),
            self.card("test-002", "Second is ready."),
        ]
        self.write_stage(cards)
        audio_bytes = b"shared local audio"
        for card in cards:
            audio_path = self.root / card["audio"]
            audio_path.parent.mkdir(parents=True, exist_ok=True)
            audio_path.write_bytes(audio_bytes)

        summary = meiki_decks.build_language(
            self.root,
            self.language,
            probe=lambda _: 1_500,
        )

        self.assertEqual(summary["card_count"], 2)
        self.assertEqual(summary["media_object_count"], 1)
        with zipfile.ZipFile(summary["path"], "r") as archive:
            manifest = json.loads(archive.read("manifest.json"))
            collection = json.loads(archive.read("collection.json"))
            media_entry = manifest["media"][0]
            self.assertEqual(manifest["format"], "meiki")
            self.assertEqual(manifest["version"], 4)
            self.assertEqual(manifest["scope"], "full_collection")
            self.assertEqual(manifest["counts"]["cards"], 2)
            self.assertEqual(manifest["counts"]["media_objects"], 1)
            self.assertEqual(len(collection["decks"]), 1)
            self.assertEqual(len(collection["notes"]), 2)
            self.assertEqual(collection["notes"][0]["cards"][0]["review_events"], [])
            self.assertEqual(
                collection["notes"][0]["cards"][0]["schedule"]["lifecycle"],
                "unseen",
            )
            self.assertEqual(archive.read(media_entry["path"]), audio_bytes)
            self.assertEqual(
                media_entry["content_hash"],
                f"sha256:{hashlib.sha256(audio_bytes).hexdigest()}",
            )
        with self.assertRaisesRegex(meiki_decks.DeckError, "already exists"):
            meiki_decks.build_language(self.root, self.language, probe=lambda _: 1_500)

    def test_japanese_build_uses_complete_stage_order_and_names(self):
        self.language = "ja-JP"
        for stage in meiki_decks.JAPANESE_COMPLETE_STAGE_NAMES:
            self.stage = stage
            card = self.card(f"ja-{stage}-test")
            self.write_stage([card])
            audio_path = self.root / card["audio"]
            audio_path.parent.mkdir(parents=True)
            audio_path.write_bytes(f"audio {stage}".encode())

        summary = meiki_decks.build_language(self.root, self.language, probe=lambda _: 1_500)

        with zipfile.ZipFile(summary["path"], "r") as archive:
            collection = json.loads(archive.read("collection.json"))
        self.assertEqual(
            [(deck["id"], deck["name"]) for deck in collection["decks"]],
            [
                (f"deck:ja-JP:{stage}", name)
                for stage, name in meiki_decks.JAPANESE_COMPLETE_STAGE_NAMES.items()
            ],
        )

    def test_japanese_sources_have_complete_bundle_card_counts(self):
        repository_root = Path(__file__).resolve().parents[1]
        expected_counts = {
            "00": 300,
            "01": 1_000,
            "02": 1_200,
            "03": 1_800,
            "04": 2_400,
            "05": 3_000,
        }

        actual_counts = {
            stage: len(
                json.loads(
                    (repository_root / "cards" / "ja-JP" / f"{stage}.json").read_text(
                        encoding="utf-8"
                    )
                )
            )
            for stage in expected_counts
        }

        self.assertEqual(actual_counts, expected_counts)

    def test_korean_build_uses_current_stage_order_and_names(self):
        self.language = "ko-KR"
        for stage in meiki_decks.KOREAN_COMPLETE_STAGE_NAMES:
            self.stage = stage
            card = self.card(f"ko-{stage}-test")
            self.write_stage([card])
            audio_path = self.root / card["audio"]
            audio_path.parent.mkdir(parents=True)
            audio_path.write_bytes(f"audio {stage}".encode())

        summary = meiki_decks.build_language(self.root, self.language, probe=lambda _: 1_500)

        with zipfile.ZipFile(summary["path"], "r") as archive:
            collection = json.loads(archive.read("collection.json"))
        self.assertEqual(
            [(deck["id"], deck["name"]) for deck in collection["decks"]],
            [
                (f"deck:ko-KR:{stage}", name)
                for stage, name in meiki_decks.KOREAN_COMPLETE_STAGE_NAMES.items()
            ],
        )

    def test_korean_build_requires_the_complete_stage_set(self):
        self.language = "ko-KR"
        expected_error = "Korean complete bundle requires stages 00, 01, 02, 03, 04, 05, 06"
        archive_path = self.root / "dist" / "meiki-ko-kr-complete-v0.1.0.meiki"

        for stage in ("00", "01", "02", "03", "04", "05"):
            self.stage = stage
            self.write_stage([self.card(f"ko-{stage}-test")])

        with self.assertRaisesRegex(meiki_decks.DeckError, expected_error):
            meiki_decks.build_language(self.root, self.language, probe=lambda _: 1_500)
        self.assertFalse(archive_path.exists())

        self.stage = "six"
        self.write_stage([self.card("ko-six-test")])
        with self.assertRaisesRegex(meiki_decks.DeckError, expected_error):
            meiki_decks.build_language(self.root, self.language, probe=lambda _: 1_500)
        self.assertFalse(archive_path.exists())

        self.stage = "06"
        self.write_stage([self.card("ko-06-test")])
        with self.assertRaisesRegex(meiki_decks.DeckError, expected_error):
            meiki_decks.build_language(self.root, self.language, probe=lambda _: 1_500)
        self.assertFalse(archive_path.exists())

    def test_korean_sources_have_current_bundle_card_counts(self):
        repository_root = Path(__file__).resolve().parents[1]
        expected_counts = {
            "00": 300,
            "01": 1_000,
            "02": 1_280,
            "03": 2_000,
            "04": 2_400,
            "05": 2_800,
            "06": 3_200,
        }

        actual_counts = {
            stage: len(
                json.loads(
                    (repository_root / "cards" / "ko-KR" / f"{stage}.json").read_text(
                        encoding="utf-8"
                    )
                )
            )
            for stage in expected_counts
        }

        self.assertEqual(actual_counts, expected_counts)

    def test_french_source_has_complete_a1_card_count(self):
        repository_root = Path(__file__).resolve().parents[1]
        cards = json.loads(
            (repository_root / "cards" / "fr-FR" / "01.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(len(cards), 800)

    def test_generated_paths_remain_ignored(self):
        repository_root = Path(__file__).resolve().parents[1]
        for ignored_path in ("work/example", "dist/example", ".model-cache/example"):
            with self.subTest(path=ignored_path):
                result = subprocess.run(
                    ["git", "check-ignore", "--quiet", "--no-index", ignored_path],
                    cwd=repository_root,
                    check=False,
                )
                self.assertEqual(result.returncode, 0)

    def test_repository_contract_contains_current_stable_rules(self):
        repository_root = Path(__file__).resolve().parents[1]
        contract = (repository_root / "AGENTS.md").read_text(encoding="utf-8")
        required_rules = (
            "latest explicit `HUMAN → EXECUTOR` instruction",
            "current `ORCHESTRATOR → EXECUTOR` handoff",
            "issue and unresolved review feedback",
            "Apply YAGNI to messages, issues, work, evidence, and validation.",
            "External, interactive, destructive, publishing, installation, launch, upload",
            "Use blocking human verification only when objective evidence cannot establish",
            "authorized external-action state and result",
            "Fresh content author and reviewer contexts use sequential one-shot Codex CLI",
        )

        for rule in required_rules:
            with self.subTest(rule=rule):
                self.assertIn(rule, contract)


if __name__ == "__main__":
    unittest.main()
