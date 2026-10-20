"""Chinese 00 contract fixtures; generated text here is not curriculum content."""

import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "chinese_source", Path(__file__).resolve().parents[1] / "scripts/check_source.py")
SOURCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCE)
SCRATCH = Path("/tmp/meiki-decks-zh-00")
ALLOCATION = (("A", 1, 30), ("B", 31, 65), ("C", 66, 100),
              ("D", 101, 130), ("E", 131, 155), ("F", 156, 180),
              ("G", 181, 200))


def card(number=1):
    identifier = "zh-00-{:04d}".format(number)
    return {"id": identifier, "sentence": "编号{:04d}的杯子里有水。".format(number),
            "cloze": "水", "answer": "水", "accepted_answers": [],
            "lemma": "水", "meaning": "water", "part_of_speech": "noun",
            "audio": "audio/{}.mp3".format(identifier), "reading": "shuǐ"}


def check(records, count=1, first=1):
    return SOURCE.check_records(records, count, first, "00", "zh-Hans-CN")


def mapping(number, prerequisite="introduced fixture frame"):
    block = next(b for b, low, high in ALLOCATION if low <= number <= high)
    return ("| zh-00-{:04d} | {} | 水: water, lexical tone 3 | [6.1]({}61-foundation)"
            " | fixture; neutral | P | {} | sound | accepted | none |").format(
                number, block, SOURCE.CHINESE_GUIDE, prerequisite)


def coverage(rows):
    return ("<!-- cards:start -->\n| " + " | ".join(SOURCE.COLUMNS) + " |\n| "
            + " | ".join("---" for _ in SOURCE.COLUMNS) + " |\n"
            + "\n".join(rows) + "\n<!-- cards:end -->\n")


def check_coverage(rows):
    return SOURCE.check_coverage(coverage(rows), 200, "00", "zh-Hans-CN")


class ChineseRecordTests(unittest.TestCase):
    def assert_bad(self, row, phrase):
        findings = check([row])
        self.assertTrue(any(phrase in finding for finding in findings), findings)

    def test_unspaced_words_single_character_and_chinese_punctuation(self):
        for sentence, target, reading in (("你喝水吗？", "水", "shuǐ"),
                                          ("这是我的名字。", "名字", "míngzi"),
                                          ("请进！", "进", "jìn")):
            row = card()
            row.update(sentence=sentence, cloze=target, answer=target,
                       lemma=target, reading=reading)
            self.assertEqual(check([row]), [])

    def test_reading_is_required_and_nonempty_but_neutral_syllables_are_valid(self):
        row = card()
        del row["reading"]
        self.assert_bad(row, "/reading")
        for value in ("", " ", None, 3, []):
            row["reading"] = value
            self.assert_bad(row, "/reading")
        row.update(sentence="你喝茶吗？", cloze="吗", answer="吗", lemma="吗", reading="ma")
        self.assertEqual(check([row]), [])
        row.update(sentence="这是桌子。", cloze="桌子", answer="桌子", lemma="桌子", reading="zhuōzi")
        self.assertEqual(check([row]), [])

    def test_spanish_boundaries_and_inverted_punctuation_still_apply(self):
        row = card()
        row.update(id="es-01-0001", sentence="La ficha es azul?", cloze="zul",
                   answer="zul", lemma="azul", audio="audio/es-01-0001.mp3")
        findings = SOURCE.check_records([row], 1)
        self.assertTrue(any("unpaired" in finding for finding in findings), findings)
        self.assertTrue(any("boundary" in finding for finding in findings), findings)

    def test_grapheme_and_punctuation_safety_remains_for_chinese(self):
        row = card()
        row.update(sentence="这是水。", cloze="水。", answer="水。")
        self.assert_bad(row, "boundary")
        row.update(sentence="q\u0301水。", cloze="q", answer="q",
                   grammar="Boundary target: intentional fixture cannot split a combining mark.")
        self.assert_bad(row, "boundary")

    def test_field_types_optional_values_and_unknown_keys(self):
        self.assertTrue(check({}))
        self.assertTrue(check([None]))
        for field in SOURCE.REQUIRED - {"accepted_answers"}:
            for value in (None, 3, [], "", " "):
                row = card()
                row[field] = value
                self.assert_bad(row, field)
        for field in SOURCE.OPTIONAL:
            row = card()
            row[field] = ""
            self.assert_bad(row, field)
        row = card()
        del row["lemma"]
        self.assert_bad(row, "missing fields lemma")
        row = card()
        row["pinyin"] = "shuǐ"
        self.assert_bad(row, "undocumented fields")

    def test_nfc_and_whitespace_for_chinese_and_reading(self):
        for field, value in (("reading", "shui\u030c"), ("sentence", "我喝水。 "),
                             ("reading", " shuǐ"), ("note", "two  spaces")):
            row = card()
            row[field] = value
            self.assert_bad(row, "/" + field)

    def test_count_order_ids_and_duplicates(self):
        self.assertTrue(any("expected 1 records" in x for x in check([])))
        findings = check([card(), card()], 2)
        self.assertTrue(any("duplicate ID" in x for x in findings), findings)
        self.assertTrue(any("expected zh-00-0002" in x for x in findings), findings)
        self.assertTrue(check([card(2), card()], 2))
        row = card(2)
        row["sentence"] = card()["sentence"]
        self.assertTrue(any("duplicate of" in x for x in check([card(), row], 2)))
        self.assertEqual(check([card(41)], first=41), [])

    def test_cloze_occurrence_overlap_and_answer(self):
        row = card()
        for sentence in ("我喝茶。", "水杯里有水。"):
            row["sentence"] = sentence
            self.assert_bad(row, "exact occurrence")
        row.update(sentence="哈哈哈。", cloze="哈哈", answer="哈哈")
        self.assert_bad(row, "found 2")
        row = card()
        row["answer"] = "茶"
        self.assert_bad(row, "must equal cloze")

    def test_alternative_integrity(self):
        for alternatives in ("水", ["水"], ["茶", "茶"], [""], [3],
                             [" 茶"], ["shui\u030c"]):
            row = card()
            row["accepted_answers"] = alternatives
            self.assert_bad(row, "accepted_answers")

    def test_safe_logical_audio_path(self):
        for path in ("/audio/zh-00-0001.mp3", "../audio/zh-00-0001.mp3",
                     "audio/../zh-00-0001.mp3", "audio\\zh-00-0001.mp3",
                     "audio/zh-00-0002.mp3", "https://example.com/zh-00-0001.mp3"):
            row = card()
            row["audio"] = path
            self.assert_bad(row, "/audio")

    def test_strict_json_with_chinese(self):
        SCRATCH.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            path = Path(directory) / "source.json"
            for text in ('[', '[{"reading":"ma","reading":"má"}]', '[NaN]', '[Infinity]'):
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    SOURCE.load_source(path)
            path.write_bytes(b'\xff')
            with self.assertRaises(ValueError):
                SOURCE.load_source(path)


class ChineseCoverageTests(unittest.TestCase):
    def setUp(self):
        self.rows = [mapping(n) for n in range(1, 201)]

    def assert_bad(self, rows, phrase):
        findings = check_coverage(rows)
        self.assertTrue(any(phrase in finding for finding in findings), findings)

    def test_all_seven_blocks_and_complete_allocation(self):
        self.assertEqual(SOURCE.CHINESE_BLOCKS, ALLOCATION)
        self.assertEqual(check_coverage(self.rows), [])

    def test_every_block_start_and_end_is_enforced(self):
        for block, low, high in ALLOCATION:
            for number in (low, high):
                with self.subTest(block=block, number=number):
                    rows = copy.copy(self.rows)
                    rows[number - 1] = rows[number - 1].replace("| " + block + " |", "| Z |")
                    self.assert_bad(rows, "wrong block")
                    self.assert_bad(rows, "coverage block " + block)

    def test_missing_duplicate_malformed_and_out_of_range_mappings(self):
        self.assert_bad(self.rows[1:], "missing mapping")
        self.assert_bad(self.rows + [self.rows[0]], "duplicate mapping")
        for identifier in ("zh-00-0000", "zh-00-0201", "zh-00-bad", "es-01-0001"):
            rows = copy.copy(self.rows)
            rows[0] = rows[0].replace("zh-00-0001", identifier)
            self.assert_bad(rows, "out-of-range")

    def test_markers_header_nonempty_kind_and_review(self):
        for before, after, phrase in (("水: water, lexical tone 3", "", "empty field"),
                                     ("| sound |", "| other |", "invalid kind"),
                                     ("| accepted |", "| pending |", "unresolved"),
                                     ("| none |", "| open |", "unresolved"),
                                     ("tone 3", "cafe\u0301", "must be NFC")):
            rows = copy.copy(self.rows)
            rows[0] = rows[0].replace(before, after)
            self.assert_bad(rows, phrase)
        for text in (coverage(self.rows).replace("cards:start", "other:start"),
                     coverage(self.rows).replace("| ID |", "| Identifier |"),
                     coverage(self.rows) + "<!-- cards:end -->"):
            self.assertTrue(SOURCE.check_coverage(text, 200, "00", "zh-Hans-CN"))

    def test_guide_language_pin_and_anchor(self):
        for guide in (SOURCE.GUIDE + "61-foundation",
                      SOURCE.CHINESE_GUIDE.replace("e1d8239b7560f26b092cc7bb97c005738b34361f", "main") + "61-foundation",
                      SOURCE.CHINESE_GUIDE + "nonexistent-anchor"):
            rows = copy.copy(self.rows)
            rows[0] = rows[0].replace(SOURCE.CHINESE_GUIDE + "61-foundation", guide)
            self.assert_bad(rows, "guide subsection")

    def test_every_chinese_block_requires_production(self):
        for _, low, _ in ALLOCATION:
            rows = copy.copy(self.rows)
            rows[low - 1] = rows[low - 1].replace("| P |", "| R |")
            self.assert_bad(rows, "production role P")

    def test_prerequisites_use_actual_strictly_earlier_chinese_ids(self):
        rows = copy.copy(self.rows)
        rows[1] = mapping(2, "zh-00-0001; introduced fixture support")
        self.assertEqual(check_coverage(rows), [])
        for dependency in ("zh-00-0002", "zh-00-0003", "zh-00-0000", "zh-00-0201",
                           "zh-01-0001", "es-01-0001", "ja-00-0001", "zh-00-bad",
                           "zh-00-001", "zh-00-", "zh-0001", "ZH-00-0001",
                           "zh-Hans-CN-00-0001", "en-US-01-0001"):
            rows[1] = mapping(2, dependency)
            with self.subTest(dependency=dependency):
                self.assert_bad(rows, "earlier card")


class ChineseCliTests(unittest.TestCase):
    def test_unsupported_locale_stage_count_pairs_fail_before_file_loading(self):
        for locale, stage, count in (("es-MX", "00", "200"), ("zh-Hans-CN", "01", "600"),
                                     ("zh-Hans-CN", "00", "600"), ("zh-Hant-TW", "00", "200"),
                                     ("es-MX", "01", "200")):
            with self.subTest(locale=locale, stage=stage, count=count), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    SOURCE.main(["--locale", locale, "--stage", stage, "--expected-count", count])
                self.assertEqual(error.exception.code, 2)

    def test_chinese_cli_passes_without_spanish_or_recordings(self):
        SCRATCH.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            root = Path(directory)
            (root / "cards/zh-Hans-CN").mkdir(parents=True)
            (root / "coverage/zh-Hans-CN").mkdir(parents=True)
            (root / "cards/zh-Hans-CN/00.json").write_text(
                json.dumps([card(n) for n in range(1, 201)], ensure_ascii=False), encoding="utf-8")
            (root / "coverage/zh-Hans-CN/00.md").write_text(
                coverage([mapping(n) for n in range(1, 201)]), encoding="utf-8")
            self.assertFalse((root / "cards/es-MX").exists())
            self.assertEqual(list(root.rglob("*.mp3")), [])
            with contextlib.redirect_stdout(io.StringIO()) as output:
                result = SOURCE.main(["--locale", "zh-Hans-CN", "--stage", "00",
                                      "--expected-count", "200", "--root", str(root)])
            self.assertEqual(result, 0)
            self.assertIn("200 records", output.getvalue())
            self.assertIn("7 coverage blocks; text only", output.getvalue())


if __name__ == "__main__":
    unittest.main()
