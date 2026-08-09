import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
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

    def test_generate_audio_is_sequential_skips_nonempty_and_reports_failures(self):
        cards = [
            self.card("test-001", "First is ready."),
            self.card("test-002", "Second is ready."),
            self.card("test-003", "Third is ready."),
        ]
        self.write_stage(cards)
        skipped_path = self.root / cards[1]["audio"]
        skipped_path.parent.mkdir(parents=True)
        skipped_path.write_bytes(b"existing audio")
        commands = []

        def fake_command(command, **arguments):
            commands.append((command, arguments))
            prefix = command[command.index("--file_prefix") + 1]
            if prefix == "test-003":
                return subprocess.CompletedProcess(command, 1, stderr="synthetic failure")
            output_directory = Path(command[command.index("--output_path") + 1])
            output_format = command[command.index("--audio_format") + 1]
            (output_directory / f"{prefix}.{output_format}").write_bytes(b"generated audio")
            return subprocess.CompletedProcess(command, 0, stdout="")

        error_output = io.StringIO()
        with contextlib.redirect_stderr(error_output):
            failures = meiki_decks.generate_audio(
                self.root,
                self.language,
                self.stage,
                run_command=fake_command,
                probe=lambda _: 1_000,
                tts_config={
                    self.language: {
                        "model": "local-model",
                        "voice": "local-voice",
                        "lang_code": "Test",
                    }
                },
            )

        self.assertEqual(failures, 1)
        self.assertEqual(
            [command[0][command[0].index("--file_prefix") + 1] for command in commands],
            ["test-001", "test-003"],
        )
        self.assertEqual(commands[0][0][commands[0][0].index("--text") + 1], cards[0]["sentence"])
        self.assertEqual(commands[0][1]["env"]["HF_HUB_OFFLINE"], "1")
        self.assertIn("test-003", error_output.getvalue())

    def test_japanese_audio_uses_the_fixed_local_voice(self):
        self.assertEqual(
            meiki_decks.TTS_CONFIG["ja-JP"],
            {
                "model": "mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit",
                "voice": "Ono_Anna",
                "lang_code": "Japanese",
            },
        )

    def test_korean_audio_uses_the_fixed_local_voice(self):
        self.assertEqual(
            meiki_decks.TTS_CONFIG["ko-KR"],
            {
                "model": "mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit",
                "voice": "Sohee",
                "lang_code": "Korean",
            },
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
        for stage in ("00", "01", "02"):
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
            ],
        )

    def test_korean_sources_have_current_bundle_card_counts(self):
        repository_root = Path(__file__).resolve().parents[1]
        expected_counts = {"00": 300, "01": 1_000, "02": 1_280}

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
