"""Concrete source-contract fixtures, never production cards."""

import contextlib
import copy
import io
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
        root = Path("/tmp/meiki-decks-es-03")
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
        root = Path("/tmp/meiki-decks-es-03")
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


def stage02_card(number=1):
    row = card(number)
    row.update(id="es-02-{:04d}".format(number),
               sentence="La ficha nueva {:04d} es azul.".format(number),
               audio="audio/es-02-{:04d}.mp3".format(number))
    return row


def stage02_mapping(number, dependency="es-01-0600"):
    block = next(b for b, lo, hi in SOURCE.STAGE_02_BLOCKS if lo <= number <= hi)
    return ("| es-02-{:04d} | {} | fixture target | [6.3]({}63-routine-communication)"
            " | fixture; neutral | P | {} | grammar | accepted | none |").format(
                number, block, SOURCE.GUIDE, dependency)


class Stage02Tests(unittest.TestCase):
    def test_valid_allocation_and_prior_stage_prerequisites(self):
        rows = [stage02_mapping(n, "es-01-0600" if n == 1 else "es-02-{:04d}".format(n - 1))
                for n in range(1, 801)]
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 800, "02"), [])
        self.assertEqual(SOURCE.check_records([stage02_card()], 1, stage="02"), [])
        rows[149] = rows[149].replace("| A |", "| B |")
        self.assertTrue(any("wrong block" in x for x in SOURCE.check_coverage(coverage(rows), 800, "02")))

    def test_invalid_self_forward_unknown_and_cross_stage_prerequisites(self):
        for dependency in ("es-02-0001", "es-02-0002", "es-01-0601", "es-01-0000",
                           "es-03-0001", "es-99-0001", "es-02-bad", "ES-01-0601",
                           "zh-01-0001", "zh-Hans-01-0001", "en-US-01-0001"):
            with self.subTest(dependency=dependency):
                text = coverage([stage02_mapping(1, dependency)])
                self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(text, 1, "02")))
        text = coverage([mapping(1).replace("introductory fixture", "es-02-0001")])
        self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(text, 1)))

    def test_stage02_missing_duplicate_out_of_range_and_order(self):
        rows = [stage02_mapping(n) for n in range(1, 801)]
        for changed, phrase in ((rows[1:], "missing mapping"),
                                (rows + [rows[0]], "duplicate mapping"),
                                ([rows[0].replace("es-02-0001", "es-02-0801")] + rows[1:], "out-of-range")):
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(coverage(changed), 800, "02")))
        self.assertTrue(SOURCE.check_records([stage02_card(2), stage02_card()], 2, stage="02"))

    def test_cross_stage_duplicates_and_conservative_accents(self):
        new = stage02_card()
        self.assertEqual(SOURCE.check_cross_stage([card()], [new]), [])
        new["sentence"] = "  " + card()["sentence"].upper().replace(" ", "  ") + "  "
        self.assertTrue(any("duplicate of es-01-0001" in x for x in SOURCE.check_cross_stage([card()], [new])))
        new["sentence"] = "La ficha 0001 es azúl."
        self.assertEqual(SOURCE.check_cross_stage([card()], [new]), [])
        new["id"] = card()["id"]
        self.assertTrue(any("duplicate ID" in x for x in SOURCE.check_cross_stage([card()], [new])))

    def test_cli_both_stages_without_media_and_stage_count_pairing(self):
        root = Path("/tmp/meiki-decks-es-03")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory)
            (path / "cards/es-MX").mkdir(parents=True)
            (path / "coverage/es-MX").mkdir(parents=True)
            for stage, count, make_card, make_mapping in (("01", 600, card, mapping),
                                                         ("02", 800, stage02_card, stage02_mapping)):
                (path / ("cards/es-MX/" + stage + ".json")).write_text(json.dumps([make_card(n) for n in range(1, count + 1)]))
                (path / ("coverage/es-MX/" + stage + ".md")).write_text(coverage([make_mapping(n) for n in range(1, count + 1)]))
                self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", stage,
                                             "--expected-count", str(count), "--root", str(path)]), 0)
            self.assertEqual(list(path.rglob("*.mp3")), [])
            duplicate = stage02_card()
            duplicate["sentence"] = card()["sentence"]
            (path / "cards/es-MX/02.json").write_text(json.dumps([duplicate] + [stage02_card(n) for n in range(2, 801)]))
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", "02", "--expected-count", "800", "--root", str(path)]), 1)
                with self.assertRaises(SystemExit) as result:
                    SOURCE.main(["--locale", "es-MX", "--stage", "02", "--expected-count", "600"])
                self.assertEqual(result.exception.code, 2)


def stage03_card(number=1):
    row = card(number)
    row.update(id="es-03-{:04d}".format(number),
               sentence="La tercera ficha {:04d} es azul.".format(number),
               audio="audio/es-03-{:04d}.mp3".format(number))
    return row


def stage03_mapping(number, dependency="es-01-0600; es-02-0800", role="P",
                    situation="fixture; neutral", anchor="64-independent-communication"):
    block = next(b for b, lo, hi in SOURCE.STAGE_03_BLOCKS if lo <= number <= hi)
    return ("| es-03-{:04d} | {} | fixture target | [guide]({}{})"
            " | {} | {} | {} | grammar | accepted | none |").format(
                number, block, SOURCE.GUIDE, anchor, situation, role, dependency)


class Stage03Tests(unittest.TestCase):
    def test_valid_complete_records_allocation_and_repeated_answers(self):
        rows = [stage03_mapping(n) for n in range(1, 1001)]
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1000, "03"), [])
        self.assertEqual(SOURCE.check_records([stage03_card(n) for n in range(1, 1001)],
                                              1000, stage="03"), [])
        for number in (150, 290, 430, 560, 680, 780, 900, 1000):
            broken = list(rows)
            broken[number - 1] = broken[number - 1].replace("| " + rows[number - 1].split("|")[2].strip() + " |", "| X |", 1)
            self.assertTrue(any("wrong block" in x for x in SOURCE.check_coverage(coverage(broken), 1000, "03")))

    def test_count_order_missing_duplicate_and_out_of_range(self):
        rows = [stage03_mapping(n) for n in range(1, 1001)]
        for changed, phrase in ((rows[1:], "missing mapping"),
                                (rows + [rows[0]], "duplicate mapping"),
                                ([rows[0].replace("es-03-0001", "es-03-1001")] + rows[1:], "out-of-range")):
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(coverage(changed), 1000, "03")))
        self.assertTrue(SOURCE.check_records([stage03_card(2), stage03_card()], 2, stage="03"))
        self.assertTrue(any("expected 1000" in x for x in SOURCE.check_records([stage03_card()], 1000, stage="03")))

    def test_recognition_attribution_blocks_and_guide_anchors(self):
        rows = [stage03_mapping(n) for n in range(1, 1001)]
        for number, region, anchor in ((1, "Spain", "64-independent-communication"),
                                      (901, "Colombia", "2-production-model-script-and-register"),
                                      (1000, "River Plate", "8-listening-support-sentence-composition")):
            rows[number - 1] = stage03_mapping(number, role="R", situation=region + " recognition", anchor=anchor)
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1000, "03"), [])
        for number, role, situation, anchor, phrase in (
                (1, "R", "unattributed", "64-independent-communication", "recognition"),
                (151, "R", "Spain recognition", "64-independent-communication", "recognition"),
                (1, "unknown", "Spain", "64-independent-communication", "role P"),
                (1, "P", "neutral", "nonexistent", "guide subsection")):
            text = coverage([stage03_mapping(number, role=role, situation=situation, anchor=anchor)])
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(text, 1000, "03")))
        for stage, make in (("01", mapping), ("02", stage02_mapping)):
            text = coverage([make(1).replace("| P |", "| R |")])
            self.assertTrue(any("role P" in x for x in SOURCE.check_coverage(text, 1, stage)))

    def test_prior_stage_boundaries_and_strictly_earlier_current(self):
        rows = [stage03_mapping(n, "es-01-0001; es-01-0600; es-02-0001; es-02-0800" +
                               ("; es-03-{:04d}".format(n - 1) if n > 1 else ""))
                for n in range(1, 1001)]
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1000, "03"), [])
        for dependency in ("es-01-0000", "es-01-0601", "es-02-0000", "es-02-0801",
                           "es-03-0001", "es-03-0002", "es-04-0001", "es-99-0001",
                           "es-03-bad", "es-03-001", "ES-01-0001", "zh-01-0001",
                           "zh-Hans-01-0001", "en-US-01-0001"):
            with self.subTest(dependency=dependency):
                findings = SOURCE.check_coverage(coverage([stage03_mapping(1, dependency)]), 1, "03")
                self.assertTrue(any("prerequisite" in x for x in findings), findings)

    def test_strict_record_invariants_remain_active(self):
        for field, value, phrase in (("meaning", "", "meaning"),
                                     ("answer", "rojo", "must equal cloze"),
                                     ("cloze", "zul", "boundary"),
                                     ("sentence", "azul azul", "found 2"),
                                     ("sentence", "La ficha cafe\u0301 es azul.", "NFC"),
                                     ("audio", "audio/es-02-0001.mp3", "/audio")):
            row = stage03_card()
            row[field] = value
            if field == "cloze": row["answer"] = value
            self.assertTrue(any(phrase in x for x in SOURCE.check_records([row], 1, stage="03")))
        row = stage03_card()
        row["translation"] = "blue"
        self.assertTrue(any("undocumented" in x for x in SOURCE.check_records([row], 1, stage="03")))

    def test_cli_three_stages_without_media_and_both_predecessor_conflicts(self):
        root = Path("/tmp/meiki-decks-es-03")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory)
            (path / "cards/es-MX").mkdir(parents=True)
            (path / "coverage/es-MX").mkdir(parents=True)
            for stage, count, make_card, make_mapping in (("01", 600, card, mapping),
                                                         ("02", 800, stage02_card, stage02_mapping),
                                                         ("03", 1000, stage03_card, stage03_mapping)):
                (path / ("cards/es-MX/" + stage + ".json")).write_text(json.dumps([make_card(n) for n in range(1, count + 1)]))
                (path / ("coverage/es-MX/" + stage + ".md")).write_text(coverage([make_mapping(n) for n in range(1, count + 1)]))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", stage,
                                                 "--expected-count", str(count), "--root", str(path)]), 0)
            self.assertEqual(list(path.rglob("*.mp3")), [])
            for earlier in (card(), stage02_card()):
                duplicate = stage03_card()
                duplicate["sentence"] = "  " + earlier["sentence"].upper().replace(" ", "  ") + "  "
                # Direct cross-stage comparison preserves accents and reports the actual predecessor.
                self.assertTrue(any("duplicate of " + earlier["id"] in x
                                    for x in SOURCE.check_cross_stage([earlier], [duplicate])))
                duplicate["sentence"] = earlier["sentence"]
                (path / "cards/es-MX/03.json").write_text(json.dumps([duplicate] + [stage03_card(n) for n in range(2, 1001)]))
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", "03",
                                                 "--expected-count", "1000", "--root", str(path)]), 1)
                duplicate["sentence"] = "La tercera ficha 0001 es azúl."
                self.assertEqual(SOURCE.check_cross_stage([earlier], [duplicate]), [])
                duplicate["id"] = earlier["id"]
                self.assertTrue(any("duplicate ID" in x for x in SOURCE.check_cross_stage([earlier], [duplicate])))
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as result:
                    SOURCE.main(["--locale", "es-MX", "--stage", "03", "--expected-count", "800"])
                self.assertEqual(result.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
