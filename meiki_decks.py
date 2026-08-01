#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODEL = "mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit"
DEFAULT_DECK = "ja-JP-foundation-1"
DECKS = {
    "ja-JP-foundation-1": {
        "cards_path": ROOT / "cards" / "ja-JP-foundation-1.json",
        "archive_path": ROOT / "dist" / "meiki-ja-jp-foundation-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README.txt",
        "card_prefix": "ja-",
        "count": 150,
        "deck_id": "meiki-ja-jp-foundation-1",
        "name": "Japanese Foundation 1",
        "description": "150 beginner Japanese audio-guided typed-cloze cards.",
        "language_tag": "ja-JP",
        "voice": "Ono_Anna",
        "tts_language": "Japanese",
    },
    "ja-JP-foundation-2": {
        "cards_path": ROOT / "cards" / "ja-JP-foundation-2.json",
        "archive_path": ROOT / "dist" / "meiki-ja-jp-foundation-2-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ja-JP-foundation-2.txt",
        "card_prefix": "ja-f2-",
        "count": 150,
        "deck_id": "meiki-ja-jp-foundation-2",
        "name": "Japanese Foundation 2",
        "description": "150 beginner Japanese audio-guided typed-cloze cards covering the remaining N5 range.",
        "language_tag": "ja-JP",
        "voice": "Ono_Anna",
        "tts_language": "Japanese",
    },
    "ja-JP-elementary-1": {
        "cards_path": ROOT / "cards" / "ja-JP-elementary-1.json",
        "archive_path": ROOT / "dist" / "meiki-ja-jp-elementary-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ja-JP-elementary-1.txt",
        "card_prefix": "ja-e1-",
        "count": 200,
        "deck_id": "meiki-ja-jp-elementary-1",
        "name": "Japanese Elementary 1",
        "description": "200 elementary Japanese audio-guided typed-cloze cards covering the N4 range.",
        "language_tag": "ja-JP",
        "voice": "Ono_Anna",
        "tts_language": "Japanese",
    },
    "ja-JP-intermediate-1": {
        "cards_path": ROOT / "cards" / "ja-JP-intermediate-1.json",
        "archive_path": ROOT / "dist" / "meiki-ja-jp-intermediate-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ja-JP-intermediate-1.txt",
        "card_prefix": "ja-i1-",
        "count": 250,
        "deck_id": "meiki-ja-jp-intermediate-1",
        "name": "Japanese Intermediate 1",
        "description": "250 intermediate Japanese audio-guided typed-cloze cards covering the N3 range.",
        "language_tag": "ja-JP",
        "voice": "Ono_Anna",
        "tts_language": "Japanese",
    },
    "ja-JP-upper-intermediate-1": {
        "cards_path": ROOT / "cards" / "ja-JP-upper-intermediate-1.json",
        "archive_path": ROOT / "dist" / "meiki-ja-jp-upper-intermediate-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ja-JP-upper-intermediate-1.txt",
        "card_prefix": "ja-u1-",
        "count": 250,
        "deck_id": "meiki-ja-jp-upper-intermediate-1",
        "name": "Japanese Upper-Intermediate 1",
        "description": "250 upper-intermediate Japanese audio-guided typed-cloze cards covering the N2 range.",
        "language_tag": "ja-JP",
        "voice": "Ono_Anna",
        "tts_language": "Japanese",
    },
    "ja-JP-advanced-1": {
        "cards_path": ROOT / "cards" / "ja-JP-advanced-1.json",
        "archive_path": ROOT / "dist" / "meiki-ja-jp-advanced-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ja-JP-advanced-1.txt",
        "card_prefix": "ja-a1-",
        "count": 300,
        "deck_id": "meiki-ja-jp-advanced-1",
        "name": "Japanese Advanced 1",
        "description": "300 advanced Japanese audio-guided typed-cloze cards bridging the N1 range and authentic usage.",
        "language_tag": "ja-JP",
        "voice": "Ono_Anna",
        "tts_language": "Japanese",
    },
    "ko-KR-foundation-1": {
        "cards_path": ROOT / "cards" / "ko-KR-foundation-1.json",
        "archive_path": ROOT / "dist" / "meiki-ko-kr-foundation-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ko-KR-foundation-1.txt",
        "card_prefix": "ko-f1-",
        "count": 150,
        "deck_id": "meiki-ko-kr-foundation-1",
        "name": "Korean Foundation 1",
        "description": "150 foundation Korean audio-guided typed-cloze cards for practical contemporary South Korean usage.",
        "language_tag": "ko-KR",
        "voice": "Sohee",
        "tts_language": "Korean",
    },
    "ko-KR-foundation-2": {
        "cards_path": ROOT / "cards" / "ko-KR-foundation-2.json",
        "archive_path": ROOT / "dist" / "meiki-ko-kr-foundation-2-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ko-KR-foundation-2.txt",
        "card_prefix": "ko-f2-",
        "count": 200,
        "deck_id": "meiki-ko-kr-foundation-2",
        "name": "Korean Foundation 2",
        "description": "200 strong-beginner Korean audio-guided typed-cloze cards for practical contemporary South Korean usage.",
        "language_tag": "ko-KR",
        "voice": "Sohee",
        "tts_language": "Korean",
    },
    "ko-KR-intermediate-1": {
        "cards_path": ROOT / "cards" / "ko-KR-intermediate-1.json",
        "archive_path": ROOT / "dist" / "meiki-ko-kr-intermediate-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ko-KR-intermediate-1.txt",
        "card_prefix": "ko-i1-",
        "count": 250,
        "deck_id": "meiki-ko-kr-intermediate-1",
        "name": "Korean Intermediate 1",
        "description": "250 intermediate Korean audio-guided typed-cloze cards for connected contemporary South Korean usage.",
        "language_tag": "ko-KR",
        "voice": "Sohee",
        "tts_language": "Korean",
    },
    "ko-KR-upper-intermediate-1": {
        "cards_path": ROOT / "cards" / "ko-KR-upper-intermediate-1.json",
        "archive_path": ROOT / "dist" / "meiki-ko-kr-upper-intermediate-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ko-KR-upper-intermediate-1.txt",
        "card_prefix": "ko-u1-",
        "count": 250,
        "deck_id": "meiki-ko-kr-upper-intermediate-1",
        "name": "Korean Upper-Intermediate 1",
        "description": "250 upper-intermediate Korean audio-guided typed-cloze cards for sustained contemporary South Korean usage.",
        "language_tag": "ko-KR",
        "voice": "Sohee",
        "tts_language": "Korean",
    },
    "zh-Hans-CN-foundation-1": {
        "cards_path": ROOT / "cards" / "zh-Hans-CN-foundation-1.json",
        "archive_path": ROOT / "dist" / "meiki-zh-hans-cn-foundation-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-zh-Hans-CN-foundation-1.txt",
        "card_prefix": "zh-f1-",
        "count": 150,
        "deck_id": "meiki-zh-hans-cn-foundation-1",
        "name": "Mandarin Foundation 1",
        "description": "150 foundation Mandarin audio-guided typed-cloze cards for practical Mainland Standard Chinese.",
        "language_tag": "zh-Hans-CN",
        "voice": "Vivian",
        "tts_language": "Chinese",
        "requires_reading": True,
    },
    "fr-FR-foundation-1": {
        "cards_path": ROOT / "cards" / "fr-FR-foundation-1.json",
        "archive_path": ROOT / "dist" / "meiki-fr-fr-foundation-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-fr-FR-foundation-1.txt",
        "card_prefix": "fr-f1-",
        "count": 150,
        "deck_id": "meiki-fr-fr-foundation-1",
        "name": "French Foundation 1",
        "description": "150 foundation French audio-guided typed-cloze cards for practical contemporary metropolitan usage.",
        "language_tag": "fr-FR",
        "voice": "Serena",
        "tts_language": "French",
    },
    "es-MX-foundation-1": {
        "cards_path": ROOT / "cards" / "es-MX-foundation-1.json",
        "archive_path": ROOT / "dist" / "meiki-es-mx-foundation-1-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-es-MX-foundation-1.txt",
        "card_prefix": "es-f1-",
        "count": 150,
        "deck_id": "meiki-es-mx-foundation-1",
        "name": "Mexican Spanish Foundation 1",
        "description": "150 foundation Spanish audio-guided typed-cloze cards for practical contemporary central Mexican usage.",
        "language_tag": "es-MX",
        "voice": "Aiden",
        "tts_language": "Spanish",
    },
}
BUNDLES = {
    "ja-JP-complete": {
        "archive_path": ROOT / "dist" / "meiki-ja-jp-complete-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-ja-JP-complete.txt",
        "decks": (
            ("ja-JP-foundation-1", "Japanese 01 — Foundation 1"),
            ("ja-JP-foundation-2", "Japanese 02 — Foundation 2"),
            ("ja-JP-elementary-1", "Japanese 03 — Elementary 1"),
            ("ja-JP-intermediate-1", "Japanese 04 — Intermediate 1"),
            (
                "ja-JP-upper-intermediate-1",
                "Japanese 05 — Upper-Intermediate 1",
            ),
            ("ja-JP-advanced-1", "Japanese 06 — Advanced 1"),
        ),
    },
    "all-current": {
        "archive_path": ROOT / "dist" / "meiki-all-current-v0.1.0.meiki",
        "handoff_path": ROOT / "dist" / "README-all-current.txt",
        "decks": (
            ("ja-JP-foundation-1", "Japanese 01 — Foundation 1"),
            ("ja-JP-foundation-2", "Japanese 02 — Foundation 2"),
            ("ja-JP-elementary-1", "Japanese 03 — Elementary 1"),
            ("ja-JP-intermediate-1", "Japanese 04 — Intermediate 1"),
            (
                "ja-JP-upper-intermediate-1",
                "Japanese 05 — Upper-Intermediate 1",
            ),
            ("ja-JP-advanced-1", "Japanese 06 — Advanced 1"),
            ("ko-KR-foundation-1", "Korean 01 — Foundation 1"),
            ("zh-Hans-CN-foundation-1", "Mandarin 01 — Foundation 1"),
            ("fr-FR-foundation-1", "French 01 — Foundation 1"),
            ("es-MX-foundation-1", "Mexican Spanish 01 — Foundation 1"),
        ),
    },
}
REPLACEMENT_WARNING = (
    "Importing this archive replaces the current Meiki collection. It is intended "
    "for initial installation, not for updating an existing studied collection."
)
REQUIRED_FIELDS = (
    "id",
    "sentence",
    "cloze",
    "answer",
    "accepted_answers",
    "lemma",
    "meaning",
    "audio",
)


def load_cards(deck):
    cards_path = deck["cards_path"]
    try:
        cards = json.loads(cards_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"card file not found: {cards_path}")
    except json.JSONDecodeError as error:
        raise ValueError(
            f"invalid JSON in {cards_path}: line {error.lineno}, column {error.colno}"
        )

    if not isinstance(cards, list):
        raise ValueError("card file must contain one JSON array")
    return cards


def validation_errors(cards, require_audio, deck, require_complete=True):
    errors = []
    seen_ids = set()
    seen_audio_paths = set()
    seen_sentences = set()

    if require_complete and len(cards) != deck["count"]:
        errors.append(f"expected {deck['count']} cards, found {len(cards)}")
    elif not require_complete and not cards:
        errors.append("expected at least 1 card")
    elif not require_complete and len(cards) > deck["count"]:
        errors.append(
            f"expected at most {deck['count']} cards, found {len(cards)}"
        )

    for index, card in enumerate(cards, start=1):
        label = f"card {index}"
        if not isinstance(card, dict):
            errors.append(f"{label}: must be an object")
            continue

        card_id = card.get("id")
        if isinstance(card_id, str) and card_id:
            label = card_id

        for field in REQUIRED_FIELDS:
            if field not in card:
                errors.append(f"{label}: missing {field}")
            elif field != "accepted_answers" and (
                not isinstance(card[field], str) or not card[field].strip()
            ):
                errors.append(f"{label}: {field} must be a nonempty string")

        if deck.get("requires_reading") and "reading" not in card:
            errors.append(f"{label}: missing reading")
        if "reading" in card and (
            not isinstance(card["reading"], str) or not card["reading"].strip()
        ):
            errors.append(f"{label}: reading must be a nonempty string")

        accepted_answers = card.get("accepted_answers")
        if not isinstance(accepted_answers, list):
            errors.append(f"{label}: accepted_answers must be an array")
        elif card.get("answer") in accepted_answers:
            errors.append(f"{label}: accepted_answers repeats the canonical answer")

        if isinstance(card_id, str) and card_id:
            if card_id in seen_ids:
                errors.append(f"{label}: duplicate id")
            seen_ids.add(card_id)

        audio_path = card.get("audio")
        if isinstance(audio_path, str) and audio_path:
            if audio_path in seen_audio_paths:
                errors.append(f"{label}: duplicate audio path {audio_path}")
            seen_audio_paths.add(audio_path)

            if require_audio:
                audio_file = ROOT / audio_path
                if not audio_file.is_file():
                    errors.append(f"{label}: audio file not found: {audio_path}")
                elif audio_file.stat().st_size == 0:
                    errors.append(f"{label}: audio file is empty: {audio_path}")
                else:
                    audio_error = check_audio_file(audio_file)
                    if audio_error:
                        errors.append(f"{label}: {audio_error}: {audio_path}")

        sentence = card.get("sentence")
        cloze = card.get("cloze")
        if isinstance(sentence, str) and sentence:
            if sentence in seen_sentences:
                errors.append(f"{label}: duplicate sentence")
            seen_sentences.add(sentence)
        if isinstance(sentence, str) and isinstance(cloze, str) and cloze:
            count = sentence.count(cloze)
            if count != 1:
                errors.append(
                    f"{label}: sentence must contain cloze exactly once (found {count})"
                )

        answer = card.get("answer")
        if isinstance(answer, str) and isinstance(cloze, str) and answer != cloze:
            errors.append(f"{label}: answer must equal cloze")

    expected_ids = [
        f"{deck['card_prefix']}{number:03d}"
        for number in range(
            1, (deck["count"] if require_complete else len(cards)) + 1
        )
    ]
    actual_ids = [
        card.get("id") if isinstance(card, dict) else None for card in cards
    ]
    if actual_ids != expected_ids:
        errors.append(
            f"card IDs must run in order from {expected_ids[0]} through {expected_ids[-1]}"
        )

    return errors


def check_audio_file(audio_file):
    ffprobe = shutil.which("ffprobe")
    if ffprobe:
        result = subprocess.run(
            [
                ffprobe,
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(audio_file),
            ],
            text=True,
            capture_output=True,
        )
        try:
            duration = float(result.stdout.strip())
        except ValueError:
            duration = 0
        if result.returncode != 0:
            return "audio cannot be opened by FFprobe"
        if duration <= 0:
            return "audio duration is not positive"
        return None

    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        result = subprocess.run(
            [ffmpeg, "-v", "error", "-i", str(audio_file), "-f", "null", "-"],
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            return "audio cannot be decoded by FFmpeg"
    return None


def audio_duration_ms(audio_file):
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise ValueError("FFprobe is required to record audio duration")
    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(audio_file),
        ],
        text=True,
        capture_output=True,
    )
    try:
        duration_ms = round(float(result.stdout.strip()) * 1000)
    except ValueError:
        duration_ms = 0
    if result.returncode != 0 or duration_ms <= 0:
        raise ValueError(f"could not read a positive duration from {audio_file}")
    return duration_ms


def print_errors(errors):
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)


def run_check(deck, allow_missing_audio):
    try:
        cards = load_cards(deck)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    errors = validation_errors(
        cards, require_audio=not allow_missing_audio, deck=deck
    )
    if errors:
        print_errors(errors)
        print(f"Check failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    if allow_missing_audio:
        print(f"Check passed: {len(cards)} cards; missing audio was allowed.")
    else:
        print(f"Check passed: {len(cards)} cards and {len(cards)} nonempty MP3 files.")
    return 0


def hugging_face_cache():
    if os.environ.get("HF_HUB_CACHE"):
        return Path(os.environ["HF_HUB_CACHE"]).expanduser()
    if os.environ.get("HF_HOME"):
        return Path(os.environ["HF_HOME"]).expanduser() / "hub"
    return Path.home() / ".cache" / "huggingface" / "hub"


def model_is_cached():
    model_directory = hugging_face_cache() / (
        "models--" + MODEL.replace("/", "--")
    )
    snapshots = model_directory / "snapshots"
    return snapshots.is_dir() and any(
        (snapshot / "config.json").is_file() for snapshot in snapshots.iterdir()
    )


def print_generation_output(result):
    details = "\n".join(
        part.strip() for part in (result.stdout, result.stderr) if part.strip()
    )
    if details:
        print(details, file=sys.stderr)


def run_generate_audio(deck):
    try:
        cards = load_cards(deck)
    except ValueError as error:
        print(f"Setup error: {error}", file=sys.stderr)
        return 1

    errors = validation_errors(
        cards, require_audio=False, deck=deck, require_complete=False
    )
    if errors:
        print_errors(errors)
        return 1

    mlx_audio = shutil.which("mlx_audio.tts.generate")
    if not mlx_audio:
        print(
            "Setup error: mlx_audio.tts.generate was not found. "
            "Install it with: uv tool install mlx-audio --prerelease=allow",
            file=sys.stderr,
        )
        return 1
    if not shutil.which("ffmpeg"):
        print(
            "Setup error: FFmpeg was not found. Install it with: brew install ffmpeg",
            file=sys.stderr,
        )
        return 1
    if not model_is_cached():
        print(
            "Setup error: the Qwen3-TTS model is not cached. Download it explicitly "
            f"with: uvx --from huggingface-hub hf download {MODEL}",
            file=sys.stderr,
        )
        return 1

    failed = []
    total = len(cards)
    for index, card in enumerate(cards, start=1):
        destination = ROOT / card["audio"]
        progress = f"{index}/{total} {card['id']}"

        if destination.is_file() and destination.stat().st_size > 0:
            print(f"{progress}: OK (already exists)")
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=f"{card['id']}-") as temporary:
            command = [
                mlx_audio,
                "--model",
                MODEL,
                "--text",
                card["sentence"],
                "--voice",
                deck["voice"],
                "--lang_code",
                deck["tts_language"],
                "--temperature",
                "0.7",
                "--output_path",
                temporary,
                "--file_prefix",
                card["id"],
                "--audio_format",
                "mp3",
                "--join_audio",
            ]
            environment = os.environ.copy()
            environment["HF_HUB_OFFLINE"] = "1"
            environment["TRANSFORMERS_OFFLINE"] = "1"
            environment["HF_HUB_DISABLE_TELEMETRY"] = "1"
            result = subprocess.run(
                command,
                cwd=ROOT,
                env=environment,
                text=True,
                capture_output=True,
            )
            generated = Path(temporary) / f"{card['id']}.mp3"

            if result.returncode != 0 or not generated.is_file() or generated.stat().st_size == 0:
                print(f"{progress}: FAILED", file=sys.stderr)
                print_generation_output(result)
                failed.append(card["id"])
                continue

            generated.replace(destination)
            print(f"{progress}: OK ({destination.relative_to(ROOT)})")

    if failed:
        print(f"Audio generation failed for: {', '.join(failed)}", file=sys.stderr)
        return 1

    print(f"Audio generation complete: {total} files are present.")
    return 0


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def make_audio_reference(card, media, role, deck):
    return {
        "id": f"{card['id']}-audio-{role.removesuffix('_audio')}",
        "content_hash": f"sha256:{media['digest']}",
        "kind": "audio",
        "role": role,
        "media_type": "audio/mpeg",
        "byte_size": media["byte_size"],
        "original_file_name": Path(card["audio"]).name,
        "alt_text": None,
        "width": None,
        "height": None,
        "duration_ms": media["duration_ms"],
        "language_tag": deck["language_tag"],
        "direction": "auto",
        "created_at_ms": 0,
    }


def make_note(card, media, deck):
    card_id = card["id"]
    cloze_id = f"{card_id}-cloze"
    prefix, suffix = card["sentence"].split(card["cloze"])
    segments = []
    if prefix:
        segments.append(
            {
                "id": f"{card_id}-segment-{len(segments)}",
                "ordinal": len(segments),
                "content": {"text": prefix},
            }
        )
    segments.append(
        {
            "id": f"{card_id}-segment-{len(segments)}",
            "ordinal": len(segments),
            "content": {
                "cloze": {"cloze_id": cloze_id, "text": card["cloze"]}
            },
        }
    )
    if suffix:
        segments.append(
            {
                "id": f"{card_id}-segment-{len(segments)}",
                "ordinal": len(segments),
                "content": {"text": suffix},
            }
        )

    annotations = [
        {
            "id": f"{card_id}-annotation-lemma",
            "label": "Lemma",
            "value": card["lemma"],
            "language_tag": deck["language_tag"],
            "direction": "auto",
        },
        {
            "id": f"{card_id}-annotation-meaning",
            "label": "Meaning",
            "value": card["meaning"],
            "language_tag": "en",
            "direction": "auto",
        },
    ]
    if card.get("reading"):
        annotations.insert(
            1,
            {
                "id": f"{card_id}-annotation-reading",
                "label": "Reading",
                "value": card["reading"],
                "language_tag": "zh-Latn-pinyin",
                "direction": "auto",
            },
        )

    source_item = {
        "id": f"{card_id}-note",
        "deck_id": deck["deck_id"],
        "segments": segments,
        "language_tag": deck["language_tag"],
        "direction": "auto",
        "tags": [],
        "annotations": annotations,
        "explanation": None,
        "media": [
            make_audio_reference(card, media, "prompt_audio", deck),
            make_audio_reference(card, media, "answer_audio", deck),
        ],
        "created_at_ms": 0,
        "updated_at_ms": 0,
    }
    cloze = {
        "id": cloze_id,
        "source_item_id": source_item["id"],
        "answer": card["answer"],
        "accepted_answers": card["accepted_answers"],
        "hint": None,
        "language_tag": deck["language_tag"],
        "direction": "auto",
        "matching_policy": None,
        "annotations": [],
        "explanation": None,
        "media": [],
        "created_at_ms": 0,
        "updated_at_ms": 0,
    }
    compiled_card = {
        "id": f"{card_id}-card",
        "cloze_id": cloze_id,
        "content_version": 1,
        "suspended": False,
        "created_at_ms": 0,
        "updated_at_ms": 0,
    }
    initial_schedule = {
        "card_id": compiled_card["id"],
        "version": 0,
        "lifecycle": "unseen",
        "due_at_ms": 0,
        "ideal_due_at_ms": 0,
        "interval_milliseconds": 0,
        "interval_seconds": 0,
        "repetitions": 0,
        "stability_milliseconds": 0,
        "difficulty_millipoints": 0,
        "last_reviewed_at_ms": None,
        "last_review_event_id": None,
    }
    return {
        "source_item": source_item,
        "clozes": [cloze],
        "cards": [
            {
                "card": compiled_card,
                "baseline": initial_schedule,
                "schedule": dict(initial_schedule),
                "review_events": [],
            }
        ],
        "deleted_at_ms": None,
    }


def make_collection(notes, deck, name=None):
    parameters = [
        0.041,
        2.4175,
        4.1283,
        11.9709,
        5.6385,
        0.4468,
        3.262,
        2.3054,
        0.1688,
        1.3325,
        0.3524,
        0.0049,
        0.7503,
        0.0896,
        0.6625,
        1.3,
        0.882,
        0.3072,
        3.5875,
        0.303,
        0.0107,
        0.2279,
        2.6413,
        0.5594,
        1.3,
        2.5,
        1.0,
        0.0723,
        0.1634,
        0.5,
        0.9555,
        0.2245,
        0.6232,
        0.1362,
        0.3862,
    ]
    return {
        "collection_scheduling_settings": {
            "daily_time_budget_minutes": 30,
            "updated_at_ms": 0,
        },
        "decks": [
            {
                "id": deck["deck_id"],
                "name": name or deck["name"],
                "description": deck["description"],
                "language_tag": deck["language_tag"],
                "direction": "auto",
                "matching_policy": "strict",
                "settings": {
                    "target_retention_basis_points": None,
                    "new_cards_per_day": None,
                    "maximum_interval_days": None,
                },
                "created_at_ms": 0,
                "updated_at_ms": 0,
            }
        ],
        "notes": notes,
        "scheduler_parameter_sets": [
            {
                "id": "fsrs7-default-v1",
                "engine_version": "fsrs-7",
                "created_at_ms": 0,
                "parameters": parameters,
            }
        ],
        "scheduler_profiles": [
            {
                "deck_id": deck["deck_id"],
                "engine_version": "fsrs-7",
                "active_parameter_set_id": "fsrs7-default-v1",
                "scheduling_mode": "automatic",
                "deck_daily_time_budget_minutes": None,
                "controller_version": "time-budget-v1",
                "controller_target_retention_basis_points": 9000,
                "controller_new_cards_per_day": 20,
                "controller_last_evaluated_day_start_ms": None,
                "controller_review_count": 0,
                "controller_unseen_count": deck["count"],
                "controller_forecast_review_seconds_per_day": 0,
                "controller_backlog_exceeds_budget": False,
                "controller_explanation": "",
                "day_boundary_minutes": 240,
                "updated_at_ms": 0,
            }
        ],
    }


def make_bundle_collection(compiled_decks):
    collection = None
    for deck, name, notes in compiled_decks:
        deck_collection = make_collection(notes, deck, name)
        if collection is None:
            collection = deck_collection
            continue
        collection["decks"].extend(deck_collection["decks"])
        collection["notes"].extend(deck_collection["notes"])
        collection["scheduler_profiles"].extend(
            deck_collection["scheduler_profiles"]
        )
    return collection


def verify_archive(archive_path, selected_decks):
    expected_note_count = sum(deck["count"] for deck, _ in selected_decks)
    with zipfile.ZipFile(archive_path) as archive:
        manifest = json.loads(archive.read("manifest.json"))
        media = manifest.get("media", [])
        media_paths = {item["path"] for item in media}
        expected_names = {"manifest.json", "collection.json"} | media_paths
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != expected_names:
            raise ValueError("archive entries do not match the required ZIP layout")
        if (
            manifest.get("format") != "meiki"
            or manifest.get("version") != 4
            or manifest.get("scope") != "full_collection"
            or manifest.get("collection_path") != "collection.json"
        ):
            raise ValueError("manifest format, version, or scope is incorrect")
        expected_counts = {
            "decks": len(selected_decks),
            "notes": expected_note_count,
            "cards": expected_note_count,
            "review_events": 0,
            "media_objects": len(media),
        }
        if manifest.get("counts") != expected_counts:
            raise ValueError("manifest counts are incorrect")

        collection_data = archive.read("collection.json")
        if manifest.get("collection_sha256") != f"sha256:{sha256(collection_data)}":
            raise ValueError("collection hash does not match collection.json")
        collection = json.loads(collection_data)
        notes = collection.get("notes", [])
        if len(collection.get("decks", [])) != len(selected_decks) or len(
            notes
        ) != expected_note_count:
            raise ValueError(
                f"archive must contain {len(selected_decks)} decks and "
                f"{expected_note_count} notes"
            )
        expected_deck_identity = [
            (deck["deck_id"], name) for deck, name in selected_decks
        ]
        actual_deck_identity = [
            (deck.get("id"), deck.get("name"))
            for deck in collection.get("decks", [])
        ]
        if actual_deck_identity != expected_deck_identity:
            raise ValueError("deck IDs, names, or order are incorrect")
        if not isinstance(collection.get("collection_scheduling_settings"), dict):
            raise ValueError("collection scheduling settings are missing")

        parameter_sets = collection.get("scheduler_parameter_sets", [])
        if len(parameter_sets) != 1 or parameter_sets[0].get("id") != "fsrs7-default-v1":
            raise ValueError("archive must contain one shared FSRS parameter set")
        profiles = collection.get("scheduler_profiles", [])
        if len(profiles) != len(selected_decks):
            raise ValueError("archive must contain one scheduler profile per deck")
        for profile, (deck, _) in zip(profiles, selected_decks):
            if (
                profile.get("deck_id") != deck["deck_id"]
                or profile.get("active_parameter_set_id") != "fsrs7-default-v1"
                or profile.get("controller_unseen_count") != deck["count"]
                or profile.get("controller_review_count") != 0
            ):
                raise ValueError(
                    f"scheduler profile mismatch for {deck['deck_id']}"
                )

        media_hashes = [item["content_hash"] for item in media]
        if (
            len(media_hashes) != len(set(media_hashes))
            or media_hashes != sorted(media_hashes)
        ):
            raise ValueError("manifest media entries are incomplete or unsorted")
        for item in media:
            data = archive.read(item["path"])
            digest = sha256(data)
            if item["content_hash"] != f"sha256:{digest}":
                raise ValueError(f"media hash mismatch for {item['path']}")
            if item["path"] != f"media/sha256/{digest[:2]}/{digest[2:]}":
                raise ValueError(f"media path mismatch for {item['path']}")
            if item["byte_size"] != len(data):
                raise ValueError(f"media byte size mismatch for {item['path']}")

        entity_ids = set()
        referenced_media_hashes = set()

        def record_entity_id(entity_id, label):
            if not isinstance(entity_id, str) or not entity_id:
                raise ValueError(f"{label} has no ID")
            if entity_id in entity_ids:
                raise ValueError(f"duplicate entity ID: {entity_id}")
            entity_ids.add(entity_id)

        for deck, _ in selected_decks:
            record_entity_id(deck["deck_id"], "deck")
        record_entity_id(parameter_sets[0]["id"], "scheduler parameter set")

        card_count = 0
        note_offset = 0
        for deck, _ in selected_decks:
            deck_notes = notes[note_offset : note_offset + deck["count"]]
            note_offset += deck["count"]
            for number, note in enumerate(deck_notes, start=1):
                source = note["source_item"]
                expected_prefix = f"{deck['card_prefix']}{number:03d}"
                if source["id"] != f"{expected_prefix}-note":
                    raise ValueError(f"source item ID mismatch for {expected_prefix}")
                if source["deck_id"] != deck["deck_id"]:
                    raise ValueError(
                        f"deck relationship mismatch for {expected_prefix}"
                    )
                record_entity_id(source["id"], "source item")
                for segment in source.get("segments", []):
                    record_entity_id(segment.get("id"), "segment")
                for annotation in source.get("annotations", []):
                    record_entity_id(annotation.get("id"), "annotation")
                if len(note["clozes"]) != 1 or len(note["cards"]) != 1:
                    raise ValueError(
                        f"portable note shape mismatch for {expected_prefix}"
                    )

                cloze = note["clozes"][0]
                portable_card = note["cards"][0]
                card = portable_card["card"]
                if cloze["id"] != f"{expected_prefix}-cloze":
                    raise ValueError(f"cloze ID mismatch for {expected_prefix}")
                if cloze["source_item_id"] != source["id"]:
                    raise ValueError(
                        f"cloze source relationship mismatch for {expected_prefix}"
                    )
                if card["id"] != f"{expected_prefix}-card":
                    raise ValueError(f"card ID mismatch for {expected_prefix}")
                if card["cloze_id"] != cloze["id"]:
                    raise ValueError(
                        f"card cloze relationship mismatch for {expected_prefix}"
                    )
                record_entity_id(cloze["id"], "cloze")
                record_entity_id(card["id"], "card")

                source_media = source["media"]
                roles = {reference["role"] for reference in source_media}
                hashes = {reference["content_hash"] for reference in source_media}
                if (
                    len(source_media) != 2
                    or roles != {"prompt_audio", "answer_audio"}
                    or len(hashes) != 1
                ):
                    raise ValueError(
                        f"audio references mismatch for {expected_prefix}"
                    )
                for reference in source_media:
                    record_entity_id(reference.get("id"), "media reference")
                    referenced_media_hashes.add(reference["content_hash"])

                baseline = portable_card["baseline"]
                schedule = portable_card["schedule"]
                if baseline != schedule:
                    raise ValueError(
                        f"initial schedules differ for {expected_prefix}"
                    )
                if (
                    baseline["card_id"] != card["id"]
                    or baseline["lifecycle"] != "unseen"
                    or baseline["version"] != 0
                    or baseline["due_at_ms"] != 0
                    or baseline["ideal_due_at_ms"] != 0
                    or baseline["interval_milliseconds"] != 0
                    or baseline["interval_seconds"] != 0
                    or baseline["repetitions"] != 0
                    or baseline["stability_milliseconds"] != 0
                    or baseline["difficulty_millipoints"] != 0
                    or baseline["last_reviewed_at_ms"] is not None
                    or baseline["last_review_event_id"] is not None
                    or portable_card["review_events"]
                ):
                    raise ValueError(
                        f"card does not start unseen for {expected_prefix}"
                    )
                card_count += 1

        if card_count != expected_note_count:
            raise ValueError(
                f"archive does not contain {expected_note_count} cards"
            )
        if referenced_media_hashes != set(media_hashes):
            raise ValueError("manifest media does not match card audio references")


def run_build(deck):
    if run_check(deck, allow_missing_audio=False) != 0:
        print("Build stopped because check failed.", file=sys.stderr)
        return 1

    try:
        cards = load_cards(deck)
        notes = []
        media_objects = {}
        for card in cards:
            audio_file = ROOT / card["audio"]
            data = audio_file.read_bytes()
            digest = sha256(data)
            media = {
                "digest": digest,
                "byte_size": len(data),
                "duration_ms": audio_duration_ms(audio_file),
                "path": f"media/sha256/{digest[:2]}/{digest[2:]}",
                "data": data,
            }
            media_objects.setdefault(digest, media)
            notes.append(make_note(card, media, deck))

        if len(media_objects) != deck["count"]:
            raise ValueError(
                f"expected {deck['count']} unique audio objects, found {len(media_objects)}"
            )

        collection_data = json_bytes(make_collection(notes, deck))
        media_entries = [
            {
                "content_hash": f"sha256:{media['digest']}",
                "path": media["path"],
                "byte_size": media["byte_size"],
            }
            for media in sorted(
                media_objects.values(), key=lambda item: item["digest"]
            )
        ]
        manifest = {
            "format": "meiki",
            "version": 4,
            "created_at_ms": 0,
            "scope": "full_collection",
            "collection_path": "collection.json",
            "collection_sha256": f"sha256:{sha256(collection_data)}",
            "counts": {
                "decks": 1,
                "notes": deck["count"],
                "cards": deck["count"],
                "review_events": 0,
                "media_objects": deck["count"],
            },
            "media": media_entries,
        }

        archive_path = deck["archive_path"]
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(
            archive_path, "w", compression=zipfile.ZIP_DEFLATED
        ) as archive:
            archive.writestr("manifest.json", json_bytes(manifest))
            archive.writestr("collection.json", collection_data)
            for media in sorted(
                media_objects.values(), key=lambda item: item["digest"]
            ):
                archive.writestr(
                    media["path"], media["data"], compress_type=zipfile.ZIP_STORED
                )

        verify_archive(archive_path, [(deck, deck["name"])])
        archive_digest = sha256(archive_path.read_bytes())
        handoff = (
            f"Archive: {archive_path.name}\n"
            f"SHA-256: {archive_digest}\n"
            "Decks: 1\n"
            f"Notes: {deck['count']}\n"
            f"Cards: {deck['count']}\n"
            "Review events: 0\n"
            f"Media objects: {deck['count']}\n\n"
            "Please test importing this archive in the Meiki application.\n"
        )
        deck["handoff_path"].write_text(handoff, encoding="utf-8")
    except (KeyError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Build failed: {error}", file=sys.stderr)
        return 1

    print(f"Built and verified {archive_path.relative_to(ROOT)}")
    print(f"SHA-256: {archive_digest}")
    return 0


def run_build_bundle(bundle):
    selected_decks = [
        (DECKS[deck_key], name) for deck_key, name in bundle["decks"]
    ]
    for deck, _ in selected_decks:
        if run_check(deck, allow_missing_audio=False) != 0:
            print("Bundle build stopped because check failed.", file=sys.stderr)
            return 1

    try:
        compiled_decks = []
        media_objects = {}
        for deck, name in selected_decks:
            notes = []
            for card in load_cards(deck):
                audio_file = ROOT / card["audio"]
                data = audio_file.read_bytes()
                digest = sha256(data)
                media = {
                    "digest": digest,
                    "byte_size": len(data),
                    "duration_ms": audio_duration_ms(audio_file),
                    "path": f"media/sha256/{digest[:2]}/{digest[2:]}",
                    "data": data,
                }
                media_objects.setdefault(digest, media)
                notes.append(make_note(card, media, deck))
            compiled_decks.append((deck, name, notes))

        collection_data = json_bytes(make_bundle_collection(compiled_decks))
        sorted_media = sorted(
            media_objects.values(), key=lambda item: item["digest"]
        )
        media_entries = [
            {
                "content_hash": f"sha256:{media['digest']}",
                "path": media["path"],
                "byte_size": media["byte_size"],
            }
            for media in sorted_media
        ]
        note_count = sum(deck["count"] for deck, _ in selected_decks)
        manifest = {
            "format": "meiki",
            "version": 4,
            "created_at_ms": 0,
            "scope": "full_collection",
            "collection_path": "collection.json",
            "collection_sha256": f"sha256:{sha256(collection_data)}",
            "counts": {
                "decks": len(selected_decks),
                "notes": note_count,
                "cards": note_count,
                "review_events": 0,
                "media_objects": len(media_objects),
            },
            "media": media_entries,
        }

        archive_path = bundle["archive_path"]
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(
            archive_path, "w", compression=zipfile.ZIP_DEFLATED
        ) as archive:
            archive.writestr("manifest.json", json_bytes(manifest))
            archive.writestr("collection.json", collection_data)
            for media in sorted_media:
                archive.writestr(
                    media["path"], media["data"], compress_type=zipfile.ZIP_STORED
                )

        verify_archive(archive_path, selected_decks)
        archive_digest = sha256(archive_path.read_bytes())
        included_decks = "\n".join(
            f"- {deck_key}: {name}" for deck_key, name in bundle["decks"]
        )
        handoff = (
            f"Archive: {archive_path.name}\n"
            f"SHA-256: {archive_digest}\n"
            f"Decks: {len(selected_decks)}\n"
            f"Notes: {note_count}\n"
            f"Cards: {note_count}\n"
            "Review events: 0\n"
            f"Media objects: {len(media_objects)}\n\n"
            f"Included decks:\n{included_decks}\n\n"
            f"{REPLACEMENT_WARNING}\n"
        )
        bundle["handoff_path"].write_text(handoff, encoding="utf-8")
    except (KeyError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Bundle build failed: {error}", file=sys.stderr)
        return 1

    print(f"Built and verified {archive_path.relative_to(ROOT)}")
    print(f"SHA-256: {archive_digest}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Build Meiki audio-cloze decks.")
    parser.add_argument(
        "command", choices=("generate-audio", "check", "build", "build-bundle")
    )
    parser.add_argument("--deck", choices=DECKS, default=DEFAULT_DECK)
    parser.add_argument("--bundle", choices=BUNDLES)
    parser.add_argument("--allow-missing-audio", action="store_true")
    args = parser.parse_args()
    deck = DECKS[args.deck]

    if args.command == "build-bundle":
        if args.allow_missing_audio:
            parser.error("--allow-missing-audio is only valid with check")
        if args.bundle is None:
            parser.error("--bundle is required with build-bundle")
        return run_build_bundle(BUNDLES[args.bundle])
    if args.bundle is not None:
        parser.error("--bundle is only valid with build-bundle")
    if args.command == "generate-audio":
        if args.allow_missing_audio:
            parser.error("--allow-missing-audio is only valid with check")
        return run_generate_audio(deck)
    if args.command == "check":
        return run_check(deck, args.allow_missing_audio)
    if args.allow_missing_audio:
        parser.error("--allow-missing-audio is only valid with check")
    return run_build(deck)


if __name__ == "__main__":
    sys.exit(main())
