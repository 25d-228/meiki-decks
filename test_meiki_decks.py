"""Focused source-integrity tests, independent of media and model execution."""

import copy
import unittest

from meiki_decks import validate_coverage, validate_records


class SourceChecks(unittest.TestCase):
    def setUp(self):
        self.ids = ["es-01-0001"]
        self.cards = [{
            "id": self.ids[0], "sentence": "¿Dónde está el baño?",
            "cloze": "Dónde", "answer": "Dónde", "accepted_answers": [],
            "lemma": "dónde", "meaning": "where", "part_of_speech": "interrogative adverb",
            "audio": "audio/es-01-0001.mp3",
        }]
        self.coverage = (
            "## Slice 01 — Questions\n\nPrerequisites: None.\n"
            "Objectives: Ask about location.\n\n"
            "| ID | Hidden learning point |\n| --- | --- |\n"
            "| es-01-0001 | Accented interrogative for location. |\n"
        )

    def test_accented_source_and_coverage_without_media(self):
        self.assertEqual(validate_records(self.cards, self.ids), [])
        self.assertEqual(validate_coverage(self.coverage, self.ids), [])

    def test_non_nfc_text_is_rejected(self):
        self.cards[0]["meaning"] = "cafe\u0301"
        self.assertTrue(any("NFC" in e for e in validate_records(self.cards, self.ids)))

    def test_absent_ambiguous_and_partial_word_clozes(self):
        for sentence, target, error in (
            ("Busco el baño.", "Dónde", "exactly once"),
            ("Ana ve a Ana.", "Ana", "exactly once"),
            ("Busco el baño.", "ba", "cuts through a word"),
        ):
            with self.subTest(sentence=sentence):
                card = copy.deepcopy(self.cards[0])
                card.update(sentence=sentence, cloze=target, answer=target)
                self.assertTrue(any(error in e for e in validate_records([card], self.ids)))

    def test_duplicate_identity_and_sentence(self):
        errors = validate_records(self.cards * 2, self.ids + ["es-01-0002"])
        self.assertIn("Duplicate source IDs", errors)
        self.assertIn("Duplicate sentences", errors)

    def test_broken_answer_and_audio_relationships(self):
        self.cards[0].update(answer="dónde", audio="audio/es-01-0002.mp3")
        errors = validate_records(self.cards, self.ids)
        self.assertTrue(any("answer must equal" in e for e in errors))
        self.assertTrue(any("filename must match" in e for e in errors))

    def test_coverage_must_match_source_and_slice(self):
        for coverage in (
            self.coverage.replace("es-01-0001", "es-01-0002"),
            self.coverage.replace("Slice 01", "Slice 02"),
            self.coverage.replace("Accented interrogative for location.", " "),
        ):
            with self.subTest(coverage=coverage):
                self.assertTrue(validate_coverage(coverage, self.ids))

    def test_punctuation_and_invalid_values(self):
        for changes in (
            {"cloze": "¿Dónde", "answer": "¿Dónde"},
            {"sentence": "Dónde está el baño?"},
            {"meaning": ""},
            {"accepted_answers": ["Dónde"]},
        ):
            with self.subTest(changes=changes):
                card = copy.deepcopy(self.cards[0])
                card.update(changes)
                self.assertTrue(validate_records([card], self.ids))


if __name__ == "__main__":
    unittest.main()
