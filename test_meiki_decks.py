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

    def test_stage_02_source_and_coverage_use_the_selected_ids(self):
        ids = ["es-02-0001"]
        card = dict(self.cards[0], id=ids[0], audio="audio/es-02-0001.mp3")
        coverage = self.coverage.replace("es-01-0001", ids[0])
        self.assertEqual(validate_records([card], ids), [])
        self.assertEqual(validate_coverage(coverage, ids), [])
        self.assertTrue(validate_records([card], self.ids))
        self.assertTrue(validate_coverage(self.coverage, ids))
        self.assertTrue(validate_coverage(coverage + "\nSee es-01-0001.\n", ids))

    def test_cross_stage_sentence_duplicates_are_case_insensitive(self):
        self.assertEqual(validate_records(self.cards, self.ids, ["Busco el baño."]), [])
        errors = validate_records(self.cards, self.ids, ["¿DÓNDE ESTÁ EL BAÑO?"])
        self.assertIn("es-01-0001: sentence duplicates an earlier stage", errors)
        self.assertEqual(validate_records(self.cards, self.ids), [])

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

    def test_coverage_fields_require_text_on_their_own_line(self):
        for field, value in (("Prerequisites", "None."),
                             ("Objectives", "Ask about location.")):
            for blank in ("", " \t"):
                with self.subTest(field=field, blank=blank):
                    coverage = self.coverage.replace(f"{field}: {value}", f"{field}:{blank}")
                    self.assertIn(f"Slice 01: missing {field.lower()}",
                                  validate_coverage(coverage, self.ids))

    def test_question_and_exclamation_delimiter_order_and_balance(self):
        for sentence, valid in (
            ("Dónde está el baño? ¿Aquí.", False),
            ("El baño está aquí! ¡Gracias.", False),
            ("¿Dónde está el baño.", False),
            ("¡El baño está aquí.", False),
            ("¿Dónde está el baño? ¡Aquí!", True),
            ("¿Dónde está el baño? ¿Aquí?", True),
            ("¡El baño está aquí! ¡Gracias!", True),
        ):
            with self.subTest(sentence=sentence):
                card = dict(self.cards[0], sentence=sentence, cloze="baño", answer="baño")
                errors = validate_records([card], self.ids)
                if valid:
                    self.assertEqual(errors, [])
                else:
                    self.assertTrue(any("question/exclamation punctuation" in e for e in errors))

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
