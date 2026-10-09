"""Validate the Spanish 01 authoring sources without media or dependencies."""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parent
REQUIRED = {
    "id", "sentence", "cloze", "answer", "accepted_answers", "lemma",
    "meaning", "part_of_speech", "audio",
}


def validate_records(records, expected_ids):
    """Return structural errors; expected_ids also defines the source order."""
    errors = []
    if not isinstance(records, list):
        return ["Source must be a JSON array"]
    if len(records) != len(expected_ids):
        errors.append(f"Expected {len(expected_ids)} records, found {len(records)}")
    ids = []
    sentences = []
    for index, card in enumerate(records):
        label = f"Record {index + 1}"
        if not isinstance(card, dict):
            errors.append(f"{label}: must be an object")
            continue
        if REQUIRED - card.keys() or card.keys() - REQUIRED - {"note"}:
            errors.append(f"{label}: missing or unsupported fields")
        strings = REQUIRED - {"accepted_answers"}
        if "note" in card:
            strings = strings | {"note"}
        bad_strings = [k for k in strings if not isinstance(card.get(k), str)
                       or not card[k].strip() or card[k] != card[k].strip()]
        if bad_strings:
            errors.append(f"{label}: invalid text fields {sorted(bad_strings)}")
            continue
        label = card["id"]
        ids.append(label)
        sentences.append(card["sentence"].casefold())
        for key in strings:
            value = card[key]
            if unicodedata.normalize("NFC", value) != value:
                errors.append(f"{label}: {key} must be NFC")
            if any(unicodedata.category(c).startswith("C") for c in value):
                errors.append(f"{label}: {key} contains control characters")
        variants = card.get("accepted_answers")
        if not isinstance(variants, list) or any(
            not isinstance(v, str) or not v.strip() or v != v.strip()
            or unicodedata.normalize("NFC", v) != v
            or any(unicodedata.category(c).startswith("C") for c in v)
            for v in variants
        ):
            errors.append(f"{label}: invalid accepted_answers")
        elif len(set(variants)) != len(variants) or card["answer"] in variants:
            errors.append(f"{label}: redundant accepted_answers")
        sentence, cloze = card["sentence"], card["cloze"]
        if card["answer"] != cloze:
            errors.append(f"{label}: answer must equal cloze")
        # Count overlapping occurrences too: every possible mapping must be unique.
        offsets = [i for i in range(len(sentence)) if sentence.startswith(cloze, i)]
        if len(offsets) != 1:
            errors.append(f"{label}: cloze must occur exactly once")
        else:
            start = offsets[0]
            end = start + len(cloze)
            if sentence[:start] + card["answer"] + sentence[end:] != sentence:
                errors.append(f"{label}: segments do not reconstruct the sentence")
            if ((start and sentence[start - 1].isalnum() and cloze[0].isalnum())
                    or (end < len(sentence) and sentence[end].isalnum()
                        and cloze[-1].isalnum())):
                errors.append(f"{label}: cloze cuts through a word")
        if any(unicodedata.category(c).startswith("P") for c in (cloze[0], cloze[-1])):
            errors.append(f"{label}: keep boundary punctuation outside cloze")
        if sentence[-1] not in ".!?":
            errors.append(f"{label}: missing sentence-ending punctuation")
        if sentence.count("¿") != sentence.count("?") or sentence.count("¡") != sentence.count("!"):
            errors.append(f"{label}: unpaired Spanish question/exclamation punctuation")
        if card["audio"] != f"audio/{label}.mp3":
            errors.append(f"{label}: audio filename must match source ID")
    if ids != list(expected_ids):
        errors.append("Source IDs do not match the required order")
    if len(set(ids)) != len(ids):
        errors.append("Duplicate source IDs")
    if len(set(sentences)) != len(sentences):
        errors.append("Duplicate sentences")
    return errors


def validate_coverage(text, expected_ids):
    """Check one nonempty hidden-point mapping per source in its 40-card slice."""
    errors = []
    if unicodedata.normalize("NFC", text) != text:
        errors.append("Coverage must be NFC")
    sections = list(re.finditer(r"^## Slice (\d{2})\b[^\n]*$", text, re.MULTILINE))
    slice_count = (len(expected_ids) + 39) // 40
    if [int(m[1]) for m in sections] != list(range(1, slice_count + 1)):
        errors.append("Coverage slices are missing, duplicated, or out of order")
    mapped = []
    for n, heading in enumerate(sections):
        end = sections[n + 1].start() if n + 1 < len(sections) else len(text)
        body = text[heading.end():end]
        for field in ("Prerequisites", "Objectives"):
            if not re.search(rf"^{field}:\s*\S.+$", body, re.MULTILINE):
                errors.append(f"Slice {heading[1]}: missing {field.lower()}")
        rows = re.findall(r"^\| (es-01-\d{4}) \| ([^|\n]+) \|$", body, re.MULTILINE)
        row_ids = [row[0] for row in rows]
        begin = (int(heading[1]) - 1) * 40
        if row_ids != list(expected_ids[begin:begin + 40]):
            errors.append(f"Slice {heading[1]}: mapping does not match source IDs")
        if any(not point.strip() for _, point in rows):
            errors.append(f"Slice {heading[1]}: empty learning point")
        mapped.extend(row_ids)
    references = re.findall(r"es-01-\d{4}", text)
    if mapped != list(expected_ids) or Counter(references) != Counter(expected_ids):
        errors.append("Coverage must reference every source ID exactly once")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="Check Spanish 01 content and coverage")
    check.add_argument("--language", required=True, choices=["es-MX"])
    check.add_argument("--stage", required=True, choices=["01"])
    args = parser.parse_args()
    expected = [f"es-01-{i:04d}" for i in range(1, 801)]
    try:
        records = json.loads((ROOT / "cards" / args.language / f"{args.stage}.json").read_text(encoding="utf-8"))
        coverage = (ROOT / "coverage" / args.language / f"{args.stage}.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Cannot read sources: {exc}", file=sys.stderr)
        return 1
    errors = validate_records(records, expected) + validate_coverage(coverage, expected)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    counts = Counter(card["answer"] for card in records)
    repeats = {answer: count for answer, count in sorted(counts.items()) if count > 1}
    print(f"PASS: {len(records)} records, 20 slices, complete coverage; no media required")
    print(f"Repeated targets for editorial inspection ({len(repeats)}): "
          + json.dumps(repeats, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
