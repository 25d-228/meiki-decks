#!/usr/bin/env python3
"""Check source contract v1 for the assigned Spanish 01–03 text stages."""

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
STAGES = {"01": (600, BLOCKS), "02": (800, STAGE_02_BLOCKS),
          "03": (1000, STAGE_03_BLOCKS)}
GUIDE = ("https://github.com/25d-228/meiki-decks/blob/"
         "e1d8239b7560f26b092cc7bb97c005738b34361f/languages/es.md#")
ANCHORS = {
    "2-production-model-script-and-register", "64-independent-communication",
    "5-essential-systems-to-represent-in-sentences", "61-foundation",
    "62-basic-communication", "63-routine-communication",
    "42-language-specific-prerequisite-checks", "13-writing-and-editing-requirements",
    "7-pronunciation-aware-sentence-selection",
    "8-listening-support-sentence-composition", "9-reading-script-and-genre-in-sentences",
    "10-contrastive-cloze-design", "11-lexical-support-and-authoring-records",
    "12-social-context-and-editorial-judgment",
}
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


def check_records(records, expected_count=600, first=1, stage="01"):
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
        for field in (REQUIRED - {"accepted_answers"}) | (OPTIONAL & card.keys()):
            value = card.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(label + "/" + field + ": expected a nonempty string")
            elif value != unicodedata.normalize("NFC", value):
                errors.append(label + "/" + field + ": text must be NFC")
            elif value != value.strip() or re.search(r"[\t\r\n]| {2,}", value):
                errors.append(label + "/" + field + ": irregular whitespace")
        actual_id = card.get("id")
        expected_id = "es-{}-{:04d}".format(stage, first + offset)
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
            for opening, closing in (("¿", "?"), ("¡", "!")):
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
                    partial = ((start > 0 and word_character(sentence[start - 1]) and word_character(cloze[0]))
                               or (end < len(sentence) and word_character(sentence[end]) and word_character(cloze[-1])))
                    split_mark = (unicodedata.category(cloze[0]).startswith("M")
                                  or (end < len(sentence) and unicodedata.category(sentence[end]).startswith("M")))
                    punctuation = (unicodedata.category(cloze[0]).startswith("P")
                                   or unicodedata.category(cloze[-1]).startswith("P"))
                    if split_mark or ((partial or punctuation) and not justified):
                        errors.append(label + "/cloze: unjustified word/grapheme/punctuation boundary")
    return errors


def check_coverage(text, expected_count=600, stage="01"):
    blocks = STAGES[stage][1]
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
        if any(not value for value in parts):
            errors.append(identifier + "/coverage: empty field")
        if identifier in found:
            errors.append(identifier + "/coverage: duplicate mapping")
        found[identifier] = row
        match = re.fullmatch(r"es-" + stage + r"-(\d{4})", identifier)
        counter = int(match.group(1)) if match else 0
        if not 1 <= counter <= expected_count:
            errors.append(identifier + "/coverage: out-of-range ID")
        expected_block = next((b for b, lo, hi in blocks if lo <= counter <= hi), None)
        if row["Block"] != expected_block:
            errors.append(identifier + "/coverage: wrong block, expected " + str(expected_block))
        if row["Block"] in counts:
            counts[row["Block"]] += 1
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", row["Guide"])
        if not links or any(not link.startswith(GUIDE) or link[len(GUIDE):] not in ANCHORS for link in links):
            errors.append(identifier + "/coverage: expected a pinned guide subsection link")
        recognition = stage == "03" and row["Role"] == "R"
        if recognition:
            if row["Block"] not in {"A", "H"} or not re.search(
                    r"\b(?:Spain|Colombia|River Plate)\b", row["Situation / register"]):
                errors.append(identifier + "/coverage: recognition requires block A/H and explicit region attribution")
        elif row["Role"] != "P":
            errors.append(identifier + "/coverage: Spanish " + stage + " requires production role P")
        if row["Kind"] not in {"sound", "lexical", "grammar", "function", "construction"}:
            errors.append(identifier + "/coverage: invalid kind")
        if row["Review"] != "accepted" or row["Unresolved"] != "none":
            errors.append(identifier + "/coverage: final review is unresolved")
        for dependency in re.findall(r"\b(?:es-[\w-]+|[a-z]+(?:-[A-Z]+)?-\d{2}-[\w-]+)",
                                     row["Prerequisites"], flags=re.IGNORECASE):
            parsed = re.fullmatch(r"es-(01|02|03)-(\d{4})", dependency)
            valid = False
            if parsed:
                dep_stage, dep_number = parsed.group(1), int(parsed.group(2))
                valid = ((dep_stage == stage and 1 <= dep_number < counter)
                         or (dep_stage < stage and 1 <= dep_number <= STAGES[dep_stage][0]))
            if not valid:
                errors.append(identifier + "/coverage: prerequisite must be an earlier card"
                              + (" or valid accepted earlier-stage ID" if stage != "01" else ""))
    expected_ids = {"es-{}-{:04d}".format(stage, n) for n in range(1, expected_count + 1)}
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
                    errors.append(identifier + "/id: duplicate ID across Spanish sources")
                ids.add(identifier)
            if isinstance(sentence, str):
                key = " ".join(unicodedata.normalize("NFC", sentence).casefold().split())
                if key in sentences:
                    errors.append(str(identifier) + "/sentence: duplicate of " + str(sentences[key]))
                sentences[key] = identifier
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locale", required=True, choices=["es-MX"])
    parser.add_argument("--stage", required=True, choices=["01", "02", "03"])
    parser.add_argument("--expected-count", required=True, type=int, choices=[600, 800, 1000])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="source root (also permits isolated test fixtures)")
    args = parser.parse_args(argv)
    if args.expected_count != STAGES[args.stage][0]:
        parser.error("stage {} requires --expected-count {}".format(args.stage, STAGES[args.stage][0]))
    try:
        records = load_source(args.root / "cards/es-MX" / (args.stage + ".json"))
        coverage = (args.root / "coverage/es-MX" / (args.stage + ".md")).read_text(encoding="utf-8")
        errors = (check_records(records, args.expected_count, stage=args.stage)
                  + check_coverage(coverage, args.expected_count, args.stage))
        for previous in ("01", "02"):
            if previous < args.stage:
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
    print("PASS: source schema, ordered IDs, Unicode, clozes, duplicates, logical paths and eight coverage blocks; text only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
