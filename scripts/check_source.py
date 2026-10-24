#!/usr/bin/env python3
"""Check source contract v1 for Spanish 01–07 and Chinese 00–07 text."""

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


REQUIRED = {
    "id", "sentence", "cloze", "answer", "accepted_answers", "lemma",
    "meaning", "part_of_speech", "audio",
}
OPTIONAL = {"reading", "grammar", "register", "note"}
BLOCKS = (("A", 1, 70), ("B", 71, 145), ("C", 146, 230),
          ("D", 231, 315), ("E", 316, 380), ("F", 381, 450),
          ("G", 451, 525), ("H", 526, 600))
STAGE_02_BLOCKS = (("A", 1, 150), ("B", 151, 260), ("C", 261, 350),
                   ("D", 351, 450), ("E", 451, 530), ("F", 531, 620),
                   ("G", 621, 700), ("H", 701, 800))
STAGE_03_BLOCKS = (("A", 1, 150), ("B", 151, 290), ("C", 291, 430),
                   ("D", 431, 560), ("E", 561, 680), ("F", 681, 780),
                   ("G", 781, 900), ("H", 901, 1000))
STAGE_04_BLOCKS = (("A", 1, 180), ("B", 181, 340), ("C", 341, 490),
                   ("D", 491, 630), ("E", 631, 770), ("F", 771, 900),
                   ("G", 901, 1070), ("H", 1071, 1200))
STAGE_05_BLOCKS = (("A", 1, 240), ("B", 241, 420), ("C", 421, 610),
                   ("D", 611, 790), ("E", 791, 960), ("F", 961, 1110),
                   ("G", 1111, 1270), ("H", 1271, 1400))
STAGE_06_BLOCKS = (("A", 1, 240), ("B", 241, 460), ("C", 461, 680),
                   ("D", 681, 880), ("E", 881, 1070), ("F", 1071, 1240),
                   ("G", 1241, 1430), ("H", 1431, 1600))
STAGE_07_BLOCKS = (("A", 1, 170), ("B", 171, 340), ("C", 341, 500),
                   ("D", 501, 640), ("E", 641, 770), ("F", 771, 890),
                   ("G", 891, 1000))
STAGES = {"01": (600, BLOCKS), "02": (800, STAGE_02_BLOCKS),
          "03": (1000, STAGE_03_BLOCKS), "04": (1200, STAGE_04_BLOCKS),
          "05": (1400, STAGE_05_BLOCKS), "06": (1600, STAGE_06_BLOCKS),
          "07": (1000, STAGE_07_BLOCKS)}
CHINESE_BLOCKS = (("A", 1, 30), ("B", 31, 65), ("C", 66, 100),
                  ("D", 101, 130), ("E", 131, 155), ("F", 156, 180),
                  ("G", 181, 200))
CHINESE_01_BLOCKS = (("A", 1, 65), ("B", 66, 125), ("C", 126, 175),
                     ("D", 176, 230), ("E", 231, 280), ("F", 281, 335),
                     ("G", 336, 400))
CHINESE_02_BLOCKS = (("A", 1, 110), ("B", 111, 205), ("C", 206, 290),
                     ("D", 291, 370), ("E", 371, 445), ("F", 446, 520),
                     ("G", 521, 600))
CHINESE_03_BLOCKS = (("A", 1, 130), ("B", 131, 245), ("C", 246, 355),
                     ("D", 356, 460), ("E", 461, 560), ("F", 561, 680),
                     ("G", 681, 800))
CHINESE_04_BLOCKS = (("A", 1, 190), ("B", 191, 340), ("C", 341, 480),
                     ("D", 481, 630), ("E", 631, 760), ("F", 761, 880),
                     ("G", 881, 1000))
CHINESE_05_BLOCKS = (("A", 1, 220), ("B", 221, 380), ("C", 381, 530),
                     ("D", 531, 660), ("E", 661, 790), ("F", 791, 900),
                     ("G", 901, 1000))
CHINESE_06_BLOCKS = (("A", 1, 240), ("B", 241, 430), ("C", 431, 610),
                     ("D", 611, 780), ("E", 781, 940), ("F", 941, 1080),
                     ("G", 1081, 1200))
CHINESE_07_BLOCKS = (("A", 1, 380), ("B", 381, 650), ("C", 651, 900),
                     ("D", 901, 1140), ("E", 1141, 1370), ("F", 1371, 1590),
                     ("G", 1591, 1800))
CHINESE_STAGES = {"00": (200, CHINESE_BLOCKS), "01": (400, CHINESE_01_BLOCKS),
                  "02": (600, CHINESE_02_BLOCKS), "03": (800, CHINESE_03_BLOCKS),
                  "04": (1000, CHINESE_04_BLOCKS), "05": (1000, CHINESE_05_BLOCKS),
                  "06": (1200, CHINESE_06_BLOCKS), "07": (1800, CHINESE_07_BLOCKS)}
GUIDE = ("https://github.com/25d-228/meiki-decks/blob/"
         "e1d8239b7560f26b092cc7bb97c005738b34361f/languages/es.md#")
ANCHORS = {
    "2-production-model-script-and-register", "64-independent-communication",
    "65-upper-intermediate-operation", "66-advanced-development", "67-proficient-integration",
    "68-domain-specific-near-native-command",
    "5-essential-systems-to-represent-in-sentences", "61-foundation",
    "62-basic-communication", "63-routine-communication",
    "42-language-specific-prerequisite-checks", "13-writing-and-editing-requirements",
    "7-pronunciation-aware-sentence-selection",
    "8-listening-support-sentence-composition", "9-reading-script-and-genre-in-sentences",
    "10-contrastive-cloze-design", "11-lexical-support-and-authoring-records",
    "12-social-context-and-editorial-judgment",
}
CHINESE_GUIDE = GUIDE.replace("languages/es.md#", "languages/zh.md#")
CHINESE_ANCHORS = {
    "2-production-model-script-and-register", "61-foundation",
    "42-language-specific-prerequisite-checks",
    "5-essential-systems-to-represent-in-sentences",
    "7-pronunciation-aware-sentence-selection",
    "8-listening-support-sentence-composition", "9-reading-script-and-genre-in-sentences",
    "10-contrastive-cloze-design", "11-lexical-support-and-authoring-records",
    "12-social-context-and-editorial-judgment", "13-writing-and-editing-requirements",
}
CHINESE_01_ANCHORS = CHINESE_ANCHORS | {"62-basic-communication"}
CHINESE_02_ANCHORS = CHINESE_ANCHORS | {"63-routine-communication"}
CHINESE_03_ANCHORS = (CHINESE_ANCHORS - {"61-foundation"}) | {"64-independent-communication"}
CHINESE_04_ANCHORS = (CHINESE_ANCHORS - {"61-foundation"}) | {"65-upper-intermediate-operation"}
CHINESE_05_ANCHORS = (CHINESE_ANCHORS - {"61-foundation"}) | {"66-advanced-development"}
CHINESE_06_ANCHORS = (CHINESE_ANCHORS - {"61-foundation"}) | {"66-advanced-development"}
CHINESE_07_ANCHORS = (CHINESE_ANCHORS - {"61-foundation"}) | {"67-proficient-integration"}
COLUMNS = ("ID", "Block", "Hidden learning point", "Guide", "Situation / register",
           "Role", "Prerequisites", "Kind", "Review", "Unresolved")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate object key: {!r}".format(key))
        result[key] = value
    return result


def load_source(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"),
                          object_pairs_hook=unique_object,
                          parse_constant=lambda value: _bad_constant(value))
    except (OSError, UnicodeError, ValueError) as exc:
        raise ValueError("{}: {}".format(path, exc)) from exc


def _bad_constant(value):
    raise ValueError("invalid JSON constant: " + value)


def word_character(character):
    return bool(character) and (unicodedata.category(character)[0] in "LNM"
                                or character == "_")


def check_records(records, expected_count=600, first=1, stage="01", locale="es-MX"):
    """Also usable for cheap checks of a newly accepted consecutive batch."""
    errors = []
    if not isinstance(records, list):
        return ["source: expected an ordered JSON array"]
    if len(records) != expected_count:
        errors.append("source: expected {} records, found {}".format(expected_count, len(records)))
    ids, sentences = set(), {}
    for offset, card in enumerate(records):
        label = "record {}".format(offset + first)
        if not isinstance(card, dict):
            errors.append(label + ": expected an object")
            continue
        if isinstance(card.get("id"), str):
            label = card["id"]
        missing, unknown = REQUIRED - card.keys(), card.keys() - REQUIRED - OPTIONAL
        if missing:
            errors.append(label + ": missing fields " + ", ".join(sorted(missing)))
        if unknown:
            errors.append(label + ": undocumented fields " + ", ".join(sorted(unknown)))
        if locale == "zh-Hans-CN" and "reading" not in card:
            errors.append(label + "/reading: Chinese " + stage + " requires target Pinyin")
        for field in (REQUIRED - {"accepted_answers"}) | (OPTIONAL & card.keys()):
            value = card.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(label + "/" + field + ": expected a nonempty string")
            elif value != unicodedata.normalize("NFC", value):
                errors.append(label + "/" + field + ": text must be NFC")
            elif value != value.strip() or re.search(r"[\t\r\n]| {2,}", value):
                errors.append(label + "/" + field + ": irregular whitespace")
        actual_id = card.get("id")
        prefix = "zh" if locale == "zh-Hans-CN" else "es"
        expected_id = "{}-{}-{:04d}".format(prefix, stage, first + offset)
        if actual_id != expected_id:
            errors.append(label + "/id: expected " + expected_id)
        if isinstance(actual_id, str):
            if actual_id in ids:
                errors.append(label + "/id: duplicate ID")
            ids.add(actual_id)
        alternatives = card.get("accepted_answers")
        if not isinstance(alternatives, list):
            errors.append(label + "/accepted_answers: expected an array")
        else:
            seen = set()
            for alternative in alternatives:
                if not isinstance(alternative, str) or not alternative.strip():
                    errors.append(label + "/accepted_answers: alternatives must be nonempty strings")
                    continue
                if alternative != unicodedata.normalize("NFC", alternative):
                    errors.append(label + "/accepted_answers: alternative must be NFC")
                if alternative != alternative.strip() or re.search(r"[\t\r\n]| {2,}", alternative):
                    errors.append(label + "/accepted_answers: irregular whitespace")
                if alternative in seen or alternative == card.get("answer"):
                    errors.append(label + "/accepted_answers: duplicate or canonical answer")
                seen.add(alternative)
        if card.get("answer") != card.get("cloze"):
            errors.append(label + "/answer: must equal cloze exactly")
        if card.get("audio") != "audio/{}.mp3".format(actual_id):
            errors.append(label + "/audio: expected safe logical path audio/<id>.mp3")
        sentence, cloze = card.get("sentence"), card.get("cloze")
        if isinstance(sentence, str) and sentence:
            # Comparison affects diagnostics only, never the stored display text.
            key = " ".join(unicodedata.normalize("NFC", sentence).casefold().split())
            if key in sentences:
                errors.append(label + "/sentence: duplicate of " + sentences[key])
            sentences[key] = label
            for opening, closing in ((("¿", "?"), ("¡", "!")) if locale == "es-MX" else ()):
                depth = 0
                for char in sentence:
                    if char == opening:
                        depth += 1
                    elif char == closing:
                        depth -= 1
                    if depth < 0:
                        break
                if depth:
                    errors.append(label + "/sentence: unpaired " + opening + closing)
            if isinstance(cloze, str) and cloze:
                starts = [m.start() for m in re.finditer("(?=" + re.escape(cloze) + ")", sentence)]
                if len(starts) != 1:
                    errors.append(label + "/cloze: expected one exact occurrence, found " + str(len(starts)))
                else:
                    start, end = starts[0], starts[0] + len(cloze)
                    justification = card.get("grammar", "")
                    justified = isinstance(justification, str) and justification.startswith("Boundary target: ") and len(justification) > 17
                    # Han adjacency is normal; Chinese word identity needs editorial review.
                    partial = locale == "es-MX" and (
                        (start > 0 and word_character(sentence[start - 1]) and word_character(cloze[0]))
                        or (end < len(sentence) and word_character(sentence[end]) and word_character(cloze[-1])))
                    split_mark = (unicodedata.category(cloze[0]).startswith("M")
                                  or (end < len(sentence) and unicodedata.category(sentence[end]).startswith("M")))
                    punctuation = (unicodedata.category(cloze[0]).startswith("P")
                                   or unicodedata.category(cloze[-1]).startswith("P"))
                    if split_mark or ((partial or punctuation) and not justified):
                        errors.append(label + "/cloze: unjustified word/grapheme/punctuation boundary")
    return errors


def check_coverage(text, expected_count=600, stage="01", locale="es-MX"):
    chinese = locale == "zh-Hans-CN"
    blocks = CHINESE_STAGES[stage][1] if chinese else STAGES[stage][1]
    prefix = "zh" if chinese else "es"
    guide, anchors = (CHINESE_GUIDE, CHINESE_ANCHORS) if chinese else (GUIDE, ANCHORS)
    if chinese and stage == "01":
        anchors = CHINESE_01_ANCHORS
    elif chinese and stage == "02":
        anchors = CHINESE_02_ANCHORS
    elif chinese and stage == "03":
        anchors = CHINESE_03_ANCHORS
    elif chinese and stage == "04":
        anchors = CHINESE_04_ANCHORS
    elif chinese and stage == "05":
        anchors = CHINESE_05_ANCHORS
    elif chinese and stage == "06":
        anchors = CHINESE_06_ANCHORS
    elif chinese and stage == "07":
        anchors = CHINESE_07_ANCHORS
    errors = []
    if text != unicodedata.normalize("NFC", text):
        errors.append("coverage: text must be NFC")
    start_marker, end_marker = "<!-- cards:start -->", "<!-- cards:end -->"
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        return errors + ["coverage: expected exactly one cards:start/cards:end table"]
    start, end = text.index(start_marker), text.index(end_marker)
    if start >= end:
        return errors + ["coverage: cards:end precedes cards:start"]
    lines = [line.strip() for line in text[start + len(start_marker):end].splitlines() if line.strip()]
    if len(lines) < 2 or tuple(part.strip() for part in lines[0].strip("|").split("|")) != COLUMNS:
        return errors + ["coverage: incorrect table header"]
    if not re.fullmatch(r"\|[\s:|\-]+\|", lines[1]):
        errors.append("coverage: missing Markdown table separator")
    found, counts = {}, {block: 0 for block, _, _ in blocks}
    for number, line in enumerate(lines[2:], 1):
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != len(COLUMNS) or not line.startswith("|") or not line.endswith("|"):
            errors.append("coverage row {}: expected {} columns".format(number, len(COLUMNS)))
            continue
        row = dict(zip(COLUMNS, parts))
        identifier = row["ID"]
        if chinese and stage in {"01", "02", "03", "04", "05", "06", "07"} and identifier != "zh-{}-{:04d}".format(stage, number):
            errors.append(identifier + "/coverage: expected ordered mapping zh-{}-{:04d}".format(stage, number))
        if any(not value for value in parts):
            errors.append(identifier + "/coverage: empty field")
        if identifier in found:
            errors.append(identifier + "/coverage: duplicate mapping")
        found[identifier] = row
        match = re.fullmatch(prefix + "-" + stage + r"-(\d{4})", identifier)
        counter = int(match.group(1)) if match else 0
        if not 1 <= counter <= expected_count:
            errors.append(identifier + "/coverage: out-of-range ID")
        expected_block = next((b for b, lo, hi in blocks if lo <= counter <= hi), None)
        if row["Block"] != expected_block:
            errors.append(identifier + "/coverage: wrong block, expected " + str(expected_block))
        if row["Block"] in counts:
            counts[row["Block"]] += 1
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", row["Guide"])
        if not links or any(not link.startswith(guide) or link[len(guide):] not in anchors for link in links):
            errors.append(identifier + "/coverage: expected a pinned guide subsection link")
        recognition = row["Role"] == "R"
        if chinese:
            if recognition and stage in {"06", "07"}:
                marked_source = re.search(r"\bSource/register:\s*\S", row["Situation / register"], re.IGNORECASE)
                if row["Block"] != "F" or not marked_source:
                    errors.append(identifier + "/coverage: Chinese " + stage + " recognition requires block F and explicit Source/register attribution")
            elif row["Role"] != "P":
                errors.append(identifier + "/coverage: Chinese " + stage + " requires production role P")
        elif recognition and stage == "03":
            if row["Block"] not in {"A", "H"} or not re.search(
                    r"\b(?:Spain|Colombia|River Plate)\b", row["Situation / register"]):
                errors.append(identifier + "/coverage: recognition requires block A/H and explicit region attribution")
        elif recognition and stage in {"04", "05"}:
            attributed = re.search(r"\b(?:Spain|Colombia|River Plate)\b", row["Situation / register"])
            marked_source = re.search(r"\bSource/register:\s*\S", row["Situation / register"], re.IGNORECASE)
            if row["Block"] != "H" or not (attributed or marked_source):
                errors.append(identifier + "/coverage: recognition requires block H and explicit region or Source/register attribution")
        elif recognition and stage == "06":
            attributed = re.search(r"\b(?:Spain|Colombia|River Plate)\b", row["Situation / register"])
            marked_source = re.search(r"\bSource/register:\s*\S", row["Situation / register"], re.IGNORECASE)
            if row["Block"] != "G" or not (attributed or marked_source):
                errors.append(identifier + "/coverage: recognition requires block G and explicit region or Source/register attribution")
        elif recognition and stage == "07":
            marked_source = re.search(r"\bSource/register:\s*\S", row["Situation / register"], re.IGNORECASE)
            if row["Block"] not in {"D", "G"} or not marked_source:
                errors.append(identifier + "/coverage: recognition requires block D/G and explicit Source/register attribution")
        elif row["Role"] != "P":
            errors.append(identifier + "/coverage: Spanish " + stage + " requires production role P")
        if row["Kind"] not in {"sound", "lexical", "grammar", "function", "construction"}:
            errors.append(identifier + "/coverage: invalid kind")
        if row["Review"] != "accepted" or row["Unresolved"] != "none":
            errors.append(identifier + "/coverage: final review is unresolved")
        for dependency in re.findall(r"\b(?:(?:es|zh)-[\w-]+|[a-z]+(?:-[A-Z]+)?-\d{2}-[\w-]+)",
                                     row["Prerequisites"], flags=re.IGNORECASE):
            parsed = re.fullmatch(r"zh-(00|01|02|03|04|05|06|07)-(\d{4})" if chinese else r"es-(01|02|03|04|05|06|07)-(\d{4})", dependency)
            valid = False
            if parsed:
                dep_stage, dep_number = parsed.group(1), int(parsed.group(2))
                stages = CHINESE_STAGES if chinese else STAGES
                valid = ((dep_stage == stage and 1 <= dep_number < counter)
                         or (dep_stage < stage and 1 <= dep_number <= stages[dep_stage][0]))
            if not valid:
                errors.append(identifier + "/coverage: prerequisite must be an earlier card"
                              + (" or valid accepted earlier-stage ID" if (chinese and stage != "00") or (not chinese and stage != "01") else ""))
    expected_ids = {"{}-{}-{:04d}".format(prefix, stage, n) for n in range(1, expected_count + 1)}
    for identifier in sorted(expected_ids - found.keys()):
        errors.append(identifier + "/coverage: missing mapping")
    for block, low, high in blocks:
        expected = max(0, min(high, expected_count) - low + 1)
        if counts[block] != expected:
            errors.append("coverage block {}: expected {}, found {}".format(block, expected, counts[block]))
    return errors


def check_cross_stage(earlier, current):
    """Compare two source arrays conservatively, without rewriting display text."""
    errors, ids, sentences = [], set(), {}
    for records in (earlier, current):
        if not isinstance(records, list):
            errors.append("cross-stage: expected source arrays")
            continue
        for card in records:
            if not isinstance(card, dict):
                continue
            identifier, sentence = card.get("id"), card.get("sentence")
            if isinstance(identifier, str):
                if identifier in ids:
                    errors.append(identifier + "/id: duplicate ID across sources")
                ids.add(identifier)
            if isinstance(sentence, str):
                key = " ".join(unicodedata.normalize("NFC", sentence).casefold().split())
                if key in sentences:
                    errors.append(str(identifier) + "/sentence: duplicate of " + str(sentences[key]))
                sentences[key] = identifier
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locale", required=True, choices=["es-MX", "zh-Hans-CN"])
    parser.add_argument("--stage", required=True, choices=["00", "01", "02", "03", "04", "05", "06", "07"])
    parser.add_argument("--expected-count", required=True, type=int, choices=[200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="source root (also permits isolated test fixtures)")
    args = parser.parse_args(argv)
    chinese = args.locale == "zh-Hans-CN"
    if (chinese and args.stage not in CHINESE_STAGES) or (not chinese and args.stage not in STAGES):
        parser.error("unsupported locale/stage pair: {}/{}".format(args.locale, args.stage))
    expected_count, blocks = CHINESE_STAGES[args.stage] if chinese else STAGES[args.stage]
    if args.expected_count != expected_count:
        parser.error("stage {} requires --expected-count {}".format(args.stage, expected_count))
    try:
        records = load_source(args.root / "cards" / args.locale / (args.stage + ".json"))
        coverage = (args.root / "coverage" / args.locale / (args.stage + ".md")).read_text(encoding="utf-8")
        errors = (check_records(records, args.expected_count, stage=args.stage, locale=args.locale)
                  + check_coverage(coverage, args.expected_count, args.stage, locale=args.locale))
        for previous in ("00", "01", "02", "03", "04", "05", "06"):
            if chinese and previous < args.stage:
                earlier = load_source(args.root / "cards/zh-Hans-CN" / (previous + ".json"))
                errors += check_cross_stage(earlier, records)
        for previous in ("01", "02", "03", "04", "05", "06"):
            if not chinese and previous < args.stage:
                earlier = load_source(args.root / "cards/es-MX" / (previous + ".json"))
                errors += check_cross_stage(earlier, records)
    except (OSError, UnicodeError, ValueError) as exc:
        errors = [str(exc)]
        records = []
    count = len(records) if isinstance(records, list) else 0
    valid_ids = [row.get("id") for row in records if isinstance(row, dict) and isinstance(row.get("id"), str)] if isinstance(records, list) else []
    print("{} records; actual ordered range {}–{}".format(count, valid_ids[0] if valid_ids else "none", valid_ids[-1] if valid_ids else "none"))
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print("FAILED: {} finding(s)".format(len(errors)), file=sys.stderr)
        return 1
    print("PASS: source schema, ordered IDs, Unicode, clozes, duplicates, logical paths and {} coverage blocks; text only".format(len(blocks)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
