"""Concrete source-contract fixtures, never production cards."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "check_source", Path(__file__).resolve().parents[1] / "scripts/check_source.py")
SOURCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCE)


def card(number=1):
    identifier = "es-01-{:04d}".format(number)
    return {"id": identifier, "sentence": "La ficha {:04d} es azul.".format(number),
            "cloze": "azul", "answer": "azul", "accepted_answers": [],
            "lemma": "azul", "meaning": "blue", "part_of_speech": "adjective",
            "audio": "audio/{}.mp3".format(identifier)}


def mapping(number):
    block = next(b for b, lo, hi in SOURCE.BLOCKS if lo <= number <= hi)
    return "| es-01-{:04d} | {} | azul: blue, singular adjective | [6.2]({}62-basic-communication) | describing a card; neutral | P | introductory fixture | grammar | accepted | none |".format(number, block, SOURCE.GUIDE)


def coverage(rows):
    return ("<!-- cards:start -->\n| " + " | ".join(SOURCE.COLUMNS) + " |\n| "
            + " | ".join("---" for _ in SOURCE.COLUMNS) + " |\n"
            + "\n".join(rows) + "\n<!-- cards:end -->\n")


class RecordTests(unittest.TestCase):
    def assert_bad(self, value, phrase):
        self.assertTrue(any(phrase in finding for finding in SOURCE.check_records(value, 1)),
                        SOURCE.check_records(value, 1))

    def test_valid_text_without_media(self):
        self.assertEqual(SOURCE.check_records([card()], 1), [])

    def test_malformed_json_duplicate_keys_and_constants(self):
        root = Path("/tmp/meiki-decks-es-01")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory) / "source.json"
            for text in ('[', '[{"id":"a","id":"b"}]', '[NaN]', '[Infinity]'):
                with self.subTest(text=text):
                    path.write_text(text)
                    with self.assertRaises(ValueError):
                        SOURCE.load_source(path)

    def test_record_and_field_types(self):
        self.assert_bad({}, "ordered JSON array")
        self.assert_bad([None], "expected an object")
        for field in SOURCE.REQUIRED - {"accepted_answers"}:
            for value in (None, 3, True, [], "", " "):
                with self.subTest(field=field, value=value):
                    row = card()
                    row[field] = value
                    self.assert_bad([row], field)
        row = card()
        row["accepted_answers"] = "azul"
        self.assert_bad([row], "expected an array")

    def test_missing_unknown_and_optional_fields(self):
        row = card()
        del row["lemma"]
        self.assert_bad([row], "missing fields lemma")
        row = card()
        row["translation"] = "blue"
        self.assert_bad([row], "undocumented fields translation")
        for field in SOURCE.OPTIONAL:
            for value in ("", " ", None, []):
                row = card()
                row[field] = value
                self.assert_bad([row], field)

    def test_ids_order_count_and_duplicates(self):
        self.assert_bad([], "expected 1 records")
        findings = SOURCE.check_records([card(), card()], 2)
        self.assertTrue(any("duplicate ID" in x for x in findings))
        self.assertTrue(any("expected es-01-0002" in x for x in findings))
        self.assertTrue(SOURCE.check_records([card(2), card()], 2))

    def test_sentence_duplicates_preserve_accents(self):
        other = card(2)
        other["sentence"] = card()["sentence"].upper()
        other["cloze"] = other["answer"] = "AZUL"
        self.assertTrue(any("duplicate of" in x for x in SOURCE.check_records([card(), other], 2)))
        row = card()
        row.update(sentence="El café está aquí.", cloze="café", answer="café", lemma="café")
        self.assertEqual(SOURCE.check_records([row], 1), [])
        row["sentence"] = "El cafe\u0301 está aquí."
        self.assert_bad([row], "must be NFC")

    def test_cloze_occurrence_alignment_and_boundaries(self):
        for text in ("La ficha es roja.", "Azul y azul: azul."):
            row = card()
            row["sentence"] = text
            self.assert_bad([row], "exact occurrence")
        row = card()
        row["answer"] = "rojo"
        self.assert_bad([row], "must equal cloze")
        row = card()
        row["cloze"] = row["answer"] = "zul"
        self.assert_bad([row], "boundary")
        row = card()
        row["cloze"] = row["answer"] = "azul."
        self.assert_bad([row], "boundary")
        row["grammar"] = "Boundary target: final punctuation is the explicit test fixture."
        self.assertEqual(SOURCE.check_records([row], 1), [])
        row = card()
        row.update(sentence="aaa", cloze="aa", answer="aa")
        self.assert_bad([row], "found 2")

    def test_alternatives(self):
        for alternatives in (["azul"], ["rojo", "rojo"], [""], [3], ["cafe\u0301"], [" rojo"]):
            row = card()
            row["accepted_answers"] = alternatives
            self.assert_bad([row], "accepted_answers")
        row = card()
        row["accepted_answers"] = ["sí", "si"]
        self.assertEqual(SOURCE.check_records([row], 1), [])

    def test_audio_path_is_exact_and_relative(self):
        for path in ("/audio/es-01-0001.mp3", "../audio/es-01-0001.mp3",
                     "audio/../es-01-0001.mp3", "audio\\es-01-0001.mp3",
                     "audio/es-01-0002.mp3", "https://example.com/a.mp3"):
            row = card()
            row["audio"] = path
            self.assert_bad([row], "/audio")

    def test_spacing_and_spanish_punctuation(self):
        for sentence in ("¿La ficha es azul.", "La ficha es azul?", "¡La ficha es azul.",
                         "La ficha  es azul.", " La ficha es azul."):
            row = card()
            row["sentence"] = sentence
            self.assert_bad([row], "/sentence")


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.rows = [mapping(n) for n in range(1, 601)]

    def test_complete_allocation(self):
        self.assertEqual(SOURCE.check_coverage(coverage(self.rows)), [])

    def test_coverage_requires_nfc_too(self):
        rows = copy.copy(self.rows)
        rows[0] = rows[0].replace("singular adjective", "cafe\u0301")
        self.assertIn("coverage: text must be NFC", SOURCE.check_coverage(coverage(rows)))

    def test_omission_duplicate_out_of_range_and_allocation(self):
        cases = [(self.rows[1:], "missing mapping"),
                 (self.rows + [self.rows[0]], "duplicate mapping"),
                 ([self.rows[0].replace("0001", "0601")] + self.rows[1:], "out-of-range"),
                 ([self.rows[0].replace("| A |", "| B |")] + self.rows[1:], "wrong block")]
        for rows, phrase in cases:
            with self.subTest(phrase=phrase):
                findings = SOURCE.check_coverage(coverage(rows))
                self.assertTrue(any(phrase in x for x in findings), findings)
                if phrase != "out-of-range":
                    self.assertTrue(any("coverage block" in x for x in findings), findings)

    def test_required_mapping_content_and_review(self):
        for before, after, phrase in (("azul: blue, singular adjective", "", "empty field"),
                                     (SOURCE.GUIDE, "https://example.com/", "guide subsection"),
                                     ("accepted", "pending", "unresolved"),
                                     ("introductory fixture", "es-01-0600", "earlier card")):
            rows = copy.copy(self.rows)
            rows[0] = rows[0].replace(before, after)
            findings = SOURCE.check_coverage(coverage(rows))
            self.assertTrue(any(phrase in x for x in findings), findings)

    def test_cli_success_with_no_mp3_files(self):
        root = Path("/tmp/meiki-decks-es-01")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory)
            (path / "cards/es-MX").mkdir(parents=True)
            (path / "coverage/es-MX").mkdir(parents=True)
            (path / "cards/es-MX/01.json").write_text(json.dumps([card(n) for n in range(1, 601)]))
            (path / "coverage/es-MX/01.md").write_text(coverage(self.rows))
            self.assertEqual(list(path.rglob("*.mp3")), [])
            self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", "01",
                                         "--expected-count", "600", "--root", str(path)]), 0)


if __name__ == "__main__":
    unittest.main()
