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
        root = Path("/tmp/meiki-decks-es-06")
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
        root = Path("/tmp/meiki-decks-es-06")
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
        root = Path("/tmp/meiki-decks-es-06")
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
        root = Path("/tmp/meiki-decks-es-06")
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



def stage04_card(number=1):
    row = card(number)
    row.update(id="es-04-{:04d}".format(number),
               sentence="La cuarta ficha {:04d} es azul.".format(number),
               audio="audio/es-04-{:04d}.mp3".format(number))
    return row


def stage04_mapping(number, dependency="es-01-0600; es-02-0800; es-03-1000", role="P",
                    situation="fixture; neutral", anchor="65-upper-intermediate-operation"):
    block = next(b for b, lo, hi in SOURCE.STAGE_04_BLOCKS if lo <= number <= hi)
    return ("| es-04-{:04d} | {} | fixture target | [guide]({}{})"
            " | {} | {} | {} | grammar | accepted | none |").format(
                number, block, SOURCE.GUIDE, anchor, situation, role, dependency)


class Stage04Tests(unittest.TestCase):
    def test_complete_count_order_allocation_and_mapping_failures(self):
        rows = [stage04_mapping(n) for n in range(1, 1201)]
        cards = [stage04_card(n) for n in range(1, 1201)]
        self.assertEqual(SOURCE.check_records(cards, 1200, stage="04"), [])
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1200, "04"), [])
        self.assertTrue(SOURCE.check_records([stage04_card(2), stage04_card()], 2, stage="04"))
        self.assertTrue(any("expected 1200" in x for x in SOURCE.check_records(cards[:-1], 1200, stage="04")))
        for number in (180, 340, 490, 630, 770, 900, 1070, 1200):
            broken = list(rows)
            parts = broken[number - 1].split("|")
            parts[2] = " X "
            broken[number - 1] = "|".join(parts)
            self.assertTrue(any("wrong block" in x for x in SOURCE.check_coverage(coverage(broken), 1200, "04")))
        for changed, phrase in ((rows[1:], "missing mapping"),
                                (rows + [rows[0]], "duplicate mapping"),
                                ([rows[0].replace("es-04-0001", "es-04-1201")] + rows[1:], "out-of-range")):
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(coverage(changed), 1200, "04")))

    def test_roles_attribution_guide_and_earlier_role_policy(self):
        rows = [stage04_mapping(n) for n in range(1, 1201)]
        for number, situation, anchor in ((1071, "Spain recognition", "2-production-model-script-and-register"),
                                          (1072, "Colombia recognition", "65-upper-intermediate-operation"),
                                          (1073, "River Plate recognition", "8-listening-support-sentence-composition"),
                                          (1074, "Source/register: formal written notice", "9-reading-script-and-genre-in-sentences")):
            rows[number - 1] = stage04_mapping(number, role="R", situation=situation, anchor=anchor)
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1200, "04"), [])
        for number, role, situation, anchor, phrase in (
                (1, "R", "Spain", "65-upper-intermediate-operation", "recognition"),
                (901, "R", "Source/register: formal written notice", "65-upper-intermediate-operation", "recognition"),
                (1071, "R", "unattributed", "65-upper-intermediate-operation", "recognition"),
                (1071, "R", "Source/register: ", "65-upper-intermediate-operation", "recognition"),
                (1071, "P/R", "Spain", "65-upper-intermediate-operation", "role P"),
                (1071, "P", "neutral", "nonexistent", "guide subsection")):
            text = coverage([stage04_mapping(number, role=role, situation=situation, anchor=anchor)])
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(text, 1200, "04")))
        for stage, make in (("01", mapping), ("02", stage02_mapping)):
            self.assertTrue(any("role P" in x for x in SOURCE.check_coverage(coverage([make(1).replace("| P |", "| R |")]), 1, stage)))
        self.assertEqual(SOURCE.check_coverage(coverage([stage03_mapping(1, role="R", situation="Spain")]), 1, "03"), [])
        self.assertTrue(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage03_mapping(151, role="R", situation="Spain")]), 1000, "03")))

    def test_prerequisite_boundaries_and_malformed_references(self):
        rows = [stage04_mapping(n, "es-01-0001; es-01-0600; es-02-0001; es-02-0800; es-03-0001; es-03-1000" +
                               ("; es-04-{:04d}".format(n - 1) if n > 1 else ""))
                for n in range(1, 1201)]
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1200, "04"), [])
        for dependency in ("es-01-0000", "es-01-0601", "es-02-0000", "es-02-0801", "es-03-0000", "es-03-1001",
                           "es-04-0001", "es-04-0002", "es-05-0001", "es-99-0001", "es-04-bad", "es-04-001",
                           "ES-01-0001", "zh-01-0001", "zh-Hans-01-0001", "en-US-01-0001"):
            with self.subTest(dependency=dependency):
                self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(coverage([stage04_mapping(1, dependency)]), 1, "04")))
        self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(coverage([stage03_mapping(1, "es-04-0001")]), 1, "03")))

    def test_strict_source_invariants_remain_active(self):
        for field, value, phrase in (("meaning", "", "meaning"), ("answer", "rojo", "must equal cloze"),
                                     ("cloze", "zul", "boundary"), ("sentence", "azul azul", "found 2"),
                                     ("sentence", "La ficha cafe\u0301 es azul.", "NFC"),
                                     ("audio", "audio/es-03-0001.mp3", "/audio"),
                                     ("accepted_answers", ["azul"], "canonical answer")):
            row = stage04_card()
            row[field] = value
            if field == "cloze": row["answer"] = value
            self.assertTrue(any(phrase in x for x in SOURCE.check_records([row], 1, stage="04")))
        row = stage04_card()
        row["translation"] = "blue"
        self.assertTrue(any("undocumented" in x for x in SOURCE.check_records([row], 1, stage="04")))

    def test_duplicate_diagnostics_with_every_predecessor(self):
        for prior in (card(), stage02_card(), stage03_card()):
            row = stage04_card()
            row["sentence"] = "  " + prior["sentence"].upper().replace(" ", "  ") + "  "
            self.assertTrue(any("duplicate of " + prior["id"] in x for x in SOURCE.check_cross_stage([prior], [row])))
            row["sentence"] = "La cuarta ficha 0001 es azúl."
            self.assertEqual(SOURCE.check_cross_stage([prior], [row]), [])
            row["id"] = prior["id"]
            self.assertTrue(any("duplicate ID" in x for x in SOURCE.check_cross_stage([prior], [row])))

    def test_cli_four_stages_no_media_predecessor_conflicts_and_count_pairing(self):
        root = Path("/tmp/meiki-decks-es-06")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory)
            (path / "cards/es-MX").mkdir(parents=True)
            (path / "coverage/es-MX").mkdir(parents=True)
            for stage, count, make_card, make_mapping in (("01", 600, card, mapping), ("02", 800, stage02_card, stage02_mapping),
                                                         ("03", 1000, stage03_card, stage03_mapping), ("04", 1200, stage04_card, stage04_mapping)):
                (path / ("cards/es-MX/" + stage + ".json")).write_text(json.dumps([make_card(n) for n in range(1, count + 1)]))
                (path / ("coverage/es-MX/" + stage + ".md")).write_text(coverage([make_mapping(n) for n in range(1, count + 1)]))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", stage, "--expected-count", str(count), "--root", str(path)]), 0)
            self.assertEqual(list(path.rglob("*.mp3")), [])
            for prior in (card(), stage02_card(), stage03_card()):
                row = stage04_card()
                row["sentence"] = prior["sentence"]
                (path / "cards/es-MX/04.json").write_text(json.dumps([row] + [stage04_card(n) for n in range(2, 1201)]))
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", "04", "--expected-count", "1200", "--root", str(path)]), 1)
            for stage, wrong in (("04", "1000"), ("03", "1200")):
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as result:
                        SOURCE.main(["--locale", "es-MX", "--stage", stage, "--expected-count", wrong])
                    self.assertEqual(result.exception.code, 2)


def stage05_card(number=1):
    row = card(number)
    row.update(id="es-05-{:04d}".format(number),
               sentence="La quinta ficha {:04d} es azul.".format(number),
               audio="audio/es-05-{:04d}.mp3".format(number))
    return row


def stage05_mapping(number, dependency="es-01-0600; es-02-0800; es-03-1000; es-04-1200", role="P",
                    situation="fixture; neutral", anchor="66-advanced-development"):
    block = next(b for b, lo, hi in SOURCE.STAGE_05_BLOCKS if lo <= number <= hi)
    return ("| es-05-{:04d} | {} | fixture target | [guide]({}{})"
            " | {} | {} | {} | grammar | accepted | none |").format(
                number, block, SOURCE.GUIDE, anchor, situation, role, dependency)


class Stage05Tests(unittest.TestCase):
    def test_complete_count_order_allocation_and_mapping_failures(self):
        rows = [stage05_mapping(n) for n in range(1, 1401)]
        cards = [stage05_card(n) for n in range(1, 1401)]
        self.assertEqual(SOURCE.check_records(cards, 1400, stage="05"), [])
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1400, "05"), [])
        self.assertTrue(SOURCE.check_records([stage05_card(2), stage05_card()], 2, stage="05"))
        self.assertTrue(any("expected 1400" in x for x in SOURCE.check_records(cards[:-1], 1400, stage="05")))
        for number in (240, 420, 610, 790, 960, 1110, 1270, 1400):
            broken = list(rows)
            parts = broken[number - 1].split("|")
            parts[2] = " X "
            broken[number - 1] = "|".join(parts)
            self.assertTrue(any("wrong block" in x for x in SOURCE.check_coverage(coverage(broken), 1400, "05")))
        for changed, phrase in ((rows[1:], "missing mapping"),
                                (rows + [rows[0]], "duplicate mapping"),
                                ([rows[0].replace("es-05-0001", "es-05-1401")] + rows[1:], "out-of-range")):
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(coverage(changed), 1400, "05")))

    def test_roles_attribution_guide_and_earlier_role_policy(self):
        rows = [stage05_mapping(n) for n in range(1, 1401)]
        for number, situation, anchor in ((1271, "Spain recognition", "2-production-model-script-and-register"),
                                          (1272, "Colombia recognition", "66-advanced-development"),
                                          (1273, "River Plate recognition", "8-listening-support-sentence-composition"),
                                          (1274, "Source/register: formal written notice", "9-reading-script-and-genre-in-sentences")):
            rows[number - 1] = stage05_mapping(number, role="R", situation=situation, anchor=anchor)
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1400, "05"), [])
        for number, role, situation, anchor, phrase in (
                (1, "R", "Spain", "66-advanced-development", "recognition"),
                (901, "R", "Source/register: formal written notice", "66-advanced-development", "recognition"),
                (1271, "R", "unattributed", "66-advanced-development", "recognition"),
                (1271, "R", "Source/register: ", "66-advanced-development", "recognition"),
                (1271, "P/R", "Spain", "66-advanced-development", "role P"),
                (1271, "P", "neutral", "nonexistent", "guide subsection")):
            text = coverage([stage05_mapping(number, role=role, situation=situation, anchor=anchor)])
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(text, 1400, "05")))
        for stage, make in (("01", mapping), ("02", stage02_mapping)):
            self.assertTrue(any("role P" in x for x in SOURCE.check_coverage(coverage([make(1).replace("| P |", "| R |")]), 1, stage)))
        self.assertEqual(SOURCE.check_coverage(coverage([stage03_mapping(1, role="R", situation="Spain")]), 1, "03"), [])
        self.assertTrue(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage03_mapping(151, role="R", situation="Spain")]), 1000, "03")))
        self.assertEqual(SOURCE.check_coverage(coverage([stage04_mapping(1)]), 1, "04"), [])
        self.assertTrue(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage04_mapping(1, role="R", situation="Spain")]), 1, "04")))

    def test_prerequisite_boundaries_and_malformed_references(self):
        rows = [stage05_mapping(n, "es-01-0001; es-01-0600; es-02-0001; es-02-0800; es-03-0001; es-03-1000; es-04-0001; es-04-1200" +
                               ("; es-05-{:04d}".format(n - 1) if n > 1 else ""))
                for n in range(1, 1401)]
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1400, "05"), [])
        for dependency in ("es-01-0000", "es-01-0601", "es-02-0000", "es-02-0801", "es-03-0000", "es-03-1001",
                           "es-04-0000", "es-04-1201", "es-05-0001", "es-05-0002", "es-06-0001", "es-99-0001", "es-05-bad", "es-05-001",
                           "ES-01-0001", "zh-01-0001", "zh-Hans-01-0001", "en-US-01-0001"):
            with self.subTest(dependency=dependency):
                self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(coverage([stage05_mapping(1, dependency)]), 1, "05")))
        self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(coverage([stage03_mapping(1, "es-05-0001")]), 1, "03")))

    def test_strict_source_invariants_remain_active(self):
        for field, value, phrase in (("meaning", "", "meaning"), ("answer", "rojo", "must equal cloze"),
                                     ("cloze", "zul", "boundary"), ("sentence", "azul azul", "found 2"),
                                     ("sentence", "La ficha cafe\u0301 es azul.", "NFC"),
                                     ("audio", "audio/es-04-0001.mp3", "/audio"),
                                     ("accepted_answers", ["azul"], "canonical answer")):
            row = stage05_card()
            row[field] = value
            if field == "cloze": row["answer"] = value
            self.assertTrue(any(phrase in x for x in SOURCE.check_records([row], 1, stage="05")))
        row = stage05_card()
        row["translation"] = "blue"
        self.assertTrue(any("undocumented" in x for x in SOURCE.check_records([row], 1, stage="05")))

    def test_duplicate_diagnostics_with_every_predecessor(self):
        for prior in (card(), stage02_card(), stage03_card(), stage04_card()):
            row = stage05_card()
            row["sentence"] = "  " + prior["sentence"].upper().replace(" ", "  ") + "  "
            self.assertTrue(any("duplicate of " + prior["id"] in x for x in SOURCE.check_cross_stage([prior], [row])))
            row["sentence"] = "La quinta ficha 0001 es azúl."
            self.assertEqual(SOURCE.check_cross_stage([prior], [row]), [])
            row["id"] = prior["id"]
            self.assertTrue(any("duplicate ID" in x for x in SOURCE.check_cross_stage([prior], [row])))

    def test_cli_five_stages_no_media_predecessor_conflicts_and_count_pairing(self):
        root = Path("/tmp/meiki-decks-es-06")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory)
            (path / "cards/es-MX").mkdir(parents=True)
            (path / "coverage/es-MX").mkdir(parents=True)
            for stage, count, make_card, make_mapping in (("01", 600, card, mapping), ("02", 800, stage02_card, stage02_mapping),
                                                         ("03", 1000, stage03_card, stage03_mapping), ("04", 1200, stage04_card, stage04_mapping),
                                                         ("05", 1400, stage05_card, stage05_mapping)):
                (path / ("cards/es-MX/" + stage + ".json")).write_text(json.dumps([make_card(n) for n in range(1, count + 1)]))
                (path / ("coverage/es-MX/" + stage + ".md")).write_text(coverage([make_mapping(n) for n in range(1, count + 1)]))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", stage, "--expected-count", str(count), "--root", str(path)]), 0)
            self.assertEqual(list(path.rglob("*.mp3")), [])
            for prior in (card(), stage02_card(), stage03_card(), stage04_card()):
                row = stage05_card()
                row["sentence"] = prior["sentence"]
                (path / "cards/es-MX/05.json").write_text(json.dumps([row] + [stage05_card(n) for n in range(2, 1401)]))
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", "05", "--expected-count", "1400", "--root", str(path)]), 1)
            for stage, wrong in (("05", "1000"), ("03", "1400")):
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as result:
                        SOURCE.main(["--locale", "es-MX", "--stage", stage, "--expected-count", wrong])
                    self.assertEqual(result.exception.code, 2)


def stage06_card(number=1):
    row = card(number)
    row.update(id="es-06-{:04d}".format(number),
               sentence="La sexta ficha {:04d} es azul.".format(number),
               audio="audio/es-06-{:04d}.mp3".format(number))
    return row


def stage06_mapping(number, dependency="es-01-0600; es-02-0800; es-03-1000; es-04-1200; es-05-1400", role="P",
                    situation="fixture; neutral", anchor="67-proficient-integration"):
    block = next(b for b, lo, hi in SOURCE.STAGE_06_BLOCKS if lo <= number <= hi)
    return ("| es-06-{:04d} | {} | fixture target | [guide]({}{})"
            " | {} | {} | {} | grammar | accepted | none |").format(
                number, block, SOURCE.GUIDE, anchor, situation, role, dependency)


class Stage06Tests(unittest.TestCase):
    def test_complete_count_order_allocation_and_mapping_failures(self):
        rows = [stage06_mapping(n) for n in range(1, 1601)]
        cards = [stage06_card(n) for n in range(1, 1601)]
        self.assertEqual(SOURCE.check_records(cards, 1600, stage="06"), [])
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1600, "06"), [])
        self.assertTrue(SOURCE.check_records([stage06_card(2), stage06_card()], 2, stage="06"))
        self.assertTrue(SOURCE.check_records([stage06_card(1601)], 1, stage="06"))
        self.assertTrue(any("expected 1600" in x for x in SOURCE.check_records(cards[:-1], 1600, stage="06")))
        for number in (240, 460, 680, 880, 1070, 1240, 1430, 1600):
            broken = list(rows)
            parts = broken[number - 1].split("|")
            parts[2] = " X "
            broken[number - 1] = "|".join(parts)
            self.assertTrue(any("wrong block" in x for x in SOURCE.check_coverage(coverage(broken), 1600, "06")))
        for changed, phrase in ((rows[1:], "missing mapping"),
                                (rows + [rows[0]], "duplicate mapping"),
                                ([rows[0].replace("es-06-0001", "es-06-1601")] + rows[1:], "out-of-range")):
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(coverage(changed), 1600, "06")))

    def test_roles_attribution_guide_and_earlier_role_policy(self):
        rows = [stage06_mapping(n) for n in range(1, 1601)]
        for number, situation, anchor in ((1241, "Spain recognition", "2-production-model-script-and-register"),
                                          (1242, "Colombia recognition", "67-proficient-integration"),
                                          (1243, "River Plate recognition", "8-listening-support-sentence-composition"),
                                          (1244, "Source/register: explicitly nonstandard quoted agreement", "9-reading-script-and-genre-in-sentences")):
            rows[number - 1] = stage06_mapping(number, role="R", situation=situation, anchor=anchor)
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1600, "06"), [])
        for number, role, situation, anchor, phrase in (
                (1, "R", "Spain", "67-proficient-integration", "recognition"),
                (1431, "R", "Source/register: formal written notice", "67-proficient-integration", "recognition"),
                (1241, "R", "unattributed", "67-proficient-integration", "recognition"),
                (1241, "R", "Source/register: ", "67-proficient-integration", "recognition"),
                (1241, "P/R", "Spain", "67-proficient-integration", "role P"),
                (1241, "P", "neutral", "nonexistent", "guide subsection")):
            text = coverage([stage06_mapping(number, role=role, situation=situation, anchor=anchor)])
            self.assertTrue(any(phrase in x for x in SOURCE.check_coverage(text, 1600, "06")))
        unpinned = stage06_mapping(1).replace("e1d8239b7560f26b092cc7bb97c005738b34361f", "main")
        self.assertTrue(any("guide" in x for x in SOURCE.check_coverage(coverage([unpinned]), 1, "06")))
        for stage, make in (("01", mapping), ("02", stage02_mapping)):
            self.assertTrue(any("role P" in x for x in SOURCE.check_coverage(coverage([make(1).replace("| P |", "| R |")]), 1, stage)))
        self.assertEqual(SOURCE.check_coverage(coverage([stage03_mapping(1, role="R", situation="Spain")]), 1, "03"), [])
        self.assertTrue(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage03_mapping(151, role="R", situation="Spain")]), 1000, "03")))
        self.assertEqual(SOURCE.check_coverage(coverage([stage04_mapping(1)]), 1, "04"), [])
        self.assertTrue(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage04_mapping(1, role="R", situation="Spain")]), 1, "04")))
        self.assertFalse(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage05_mapping(1271, role="R", situation="Spain")]), 1400, "05")))
        self.assertTrue(any("recognition" in x for x in SOURCE.check_coverage(coverage([stage05_mapping(1111, role="R", situation="Spain")]), 1400, "05")))

    def test_prerequisite_boundaries_and_malformed_references(self):
        rows = [stage06_mapping(n, "es-01-0001; es-01-0600; es-02-0001; es-02-0800; es-03-0001; es-03-1000; es-04-0001; es-04-1200; es-05-0001; es-05-1400" +
                               ("; es-06-{:04d}".format(n - 1) if n > 1 else ""))
                for n in range(1, 1601)]
        self.assertEqual(SOURCE.check_coverage(coverage(rows), 1600, "06"), [])
        for dependency in ("es-01-0000", "es-01-0601", "es-02-0000", "es-02-0801", "es-03-0000", "es-03-1001",
                           "es-04-0000", "es-04-1201", "es-05-0000", "es-05-1401", "es-06-0000", "es-06-0001", "es-06-0002", "es-06-1601", "es-07-0001", "es-99-0001", "es-06-bad", "es-06-001",
                           "ES-01-0001", "zh-01-0001", "zh-Hans-01-0001", "en-US-01-0001"):
            with self.subTest(dependency=dependency):
                self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(coverage([stage06_mapping(1, dependency)]), 1, "06")))
        self.assertTrue(any("prerequisite" in x for x in SOURCE.check_coverage(coverage([stage03_mapping(1, "es-06-0001")]), 1, "03")))

    def test_strict_source_invariants_remain_active(self):
        for field, value, phrase in (("meaning", "", "meaning"), ("answer", "rojo", "must equal cloze"),
                                     ("cloze", "zul", "boundary"), ("sentence", "azul azul", "found 2"),
                                     ("sentence", "La ficha cafe\u0301 es azul.", "NFC"),
                                     ("audio", "audio/es-04-0001.mp3", "/audio"),
                                     ("accepted_answers", ["azul"], "canonical answer")):
            row = stage06_card()
            row[field] = value
            if field == "cloze": row["answer"] = value
            self.assertTrue(any(phrase in x for x in SOURCE.check_records([row], 1, stage="06")))
        row = stage06_card()
        row["translation"] = "blue"
        self.assertTrue(any("undocumented" in x for x in SOURCE.check_records([row], 1, stage="06")))

    def test_duplicate_diagnostics_with_every_predecessor(self):
        for prior in (card(), stage02_card(), stage03_card(), stage04_card(), stage05_card()):
            row = stage06_card()
            row["sentence"] = "  " + prior["sentence"].upper().replace(" ", "  ") + "  "
            self.assertTrue(any("duplicate of " + prior["id"] in x for x in SOURCE.check_cross_stage([prior], [row])))
            row["sentence"] = "La sexta ficha 0001 es azúl."
            self.assertEqual(SOURCE.check_cross_stage([prior], [row]), [])
            row["id"] = prior["id"]
            self.assertTrue(any("duplicate ID" in x for x in SOURCE.check_cross_stage([prior], [row])))

    def test_cli_six_stages_no_media_predecessor_conflicts_and_count_pairing(self):
        root = Path("/tmp/meiki-decks-es-06")
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as directory:
            path = Path(directory)
            (path / "cards/es-MX").mkdir(parents=True)
            (path / "coverage/es-MX").mkdir(parents=True)
            for stage, count, make_card, make_mapping in (("01", 600, card, mapping), ("02", 800, stage02_card, stage02_mapping),
                                                         ("03", 1000, stage03_card, stage03_mapping), ("04", 1200, stage04_card, stage04_mapping),
                                                         ("05", 1400, stage05_card, stage05_mapping), ("06", 1600, stage06_card, stage06_mapping)):
                (path / ("cards/es-MX/" + stage + ".json")).write_text(json.dumps([make_card(n) for n in range(1, count + 1)]))
                (path / ("coverage/es-MX/" + stage + ".md")).write_text(coverage([make_mapping(n) for n in range(1, count + 1)]))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", stage, "--expected-count", str(count), "--root", str(path)]), 0)
            self.assertEqual(list(path.rglob("*.mp3")), [])
            for prior in (card(), stage02_card(), stage03_card(), stage04_card(), stage05_card()):
                row = stage06_card()
                row["sentence"] = prior["sentence"]
                (path / "cards/es-MX/06.json").write_text(json.dumps([row] + [stage06_card(n) for n in range(2, 1601)]))
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(SOURCE.main(["--locale", "es-MX", "--stage", "06", "--expected-count", "1600", "--root", str(path)]), 1)
            for stage, wrong in (("06", "1000"), ("03", "1600")):
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as result:
                        SOURCE.main(["--locale", "es-MX", "--stage", stage, "--expected-count", wrong])
                    self.assertEqual(result.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
