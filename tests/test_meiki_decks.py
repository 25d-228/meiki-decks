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
        temporary_directories = []

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
            temporary_directories.append(Path(command[-1]).parent)
            Path(command[-1]).write_bytes(b"generated audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        error_output = io.StringIO()
        with (
            contextlib.redirect_stderr(error_output),
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()) as loader,
            mock.patch.object(meiki_decks, "write_waveform") as writer,
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
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
        self.assertEqual(len(commands), 2)
        self.assertEqual(writer.call_count, 2)
        repository_root = Path(meiki_decks.__file__).resolve().parent
        self.assertTrue(all(repository_root not in paths for paths in import_paths))
        self.assertIn(repository_root, {Path(path or Path.cwd()).resolve() for path in sys.path})
        self.assertTrue((self.root / cards[0]["audio"]).is_file())
        self.assertTrue((self.root / cards[2]["audio"]).is_file())
        self.assertTrue(all(not path.exists() for path in temporary_directories))
        self.assertIn("test-002", error_output.getvalue())

    def test_generate_audio_cleans_temporary_files_after_conversion_failure(self):
        card = self.card()
        self.write_stage([card])
        self.write_voice_reference()
        temporary_directories = []

        class FakeModel:
            tts_model = mock.Mock(sample_rate=48_000)

            def generate(self, **arguments):
                return [0.0, 0.1]

        def failed_command(command, **arguments):
            temporary_directories.append(Path(command[-1]).parent)
            return subprocess.CompletedProcess(command, 1, stderr="conversion failed")

        with (
            mock.patch.object(meiki_decks, "load_tts_model", return_value=FakeModel()),
            mock.patch.object(meiki_decks, "write_waveform"),
        ):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=failed_command,
                probe=lambda _: 1_000,
                tts_config=self.tts_configuration(),
            )

        self.assertEqual(failures, 1)
        self.assertTrue(all(not path.exists() for path in temporary_directories))
        self.assertFalse((self.root / card["audio"]).exists())

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

    def test_japanese_audio_uses_voxcpm2_ultimate_reference_files(self):
        self.assertEqual(
            meiki_decks.TTS_CONFIG["ja-JP"],
            {
                "model": "openbmb/VoxCPM2",
                "reference_wav": "work/voices/ja-JP/reference.wav",
                "reference_text": "work/voices/ja-JP/reference.txt",
            },
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
        for stage in ("00", "01", "02", "03"):
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
                ("deck:ko-KR:00", "Korean 00"),
                ("deck:ko-KR:01", "Korean 01"),
                ("deck:ko-KR:02", "Korean 02"),
                ("deck:ko-KR:03", "Korean 03"),
            ],
        )

    def test_korean_sources_have_current_bundle_card_counts(self):
        repository_root = Path(__file__).resolve().parents[1]
        expected_counts = {"00": 300, "01": 1_000, "02": 1_280, "03": 2_000}

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


if __name__ == "__main__":
    unittest.main()
