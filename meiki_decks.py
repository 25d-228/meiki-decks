#!/usr/bin/env python3

import argparse
import contextlib
import gc
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile


ARCHIVE_FORMAT = "meiki"
ARCHIVE_VERSION = 4
ARCHIVE_RELEASE_VERSION = "0.1.0"
COLLECTION_PATH = "collection.json"
MANIFEST_PATH = "manifest.json"
JAPANESE_COMPLETE_STAGE_NAMES = {
    "00": "Japanese 00 — Kana, sound, and Japanese input",
    "01": "Japanese 01 — N5 / A1 foundation",
    "02": "Japanese 02 — N4 / A2 elementary",
    "03": "Japanese 03 — N3 / B1 intermediate",
    "04": "Japanese 04 — N2 / B2 upper-intermediate",
    "05": "Japanese 05 — N1 / balanced C1 bridge",
}
KOREAN_COMPLETE_STAGE_NAMES = {
    "00": "Korean 00 — Hangul and sound foundation",
    "01": "Korean 01 — Basic operational Korean / TOPIK 1",
    "02": "Korean 02 — Strong beginner Korean / TOPIK 2",
    "03": "Korean 03 — Independent Korean / TOPIK 3",
    "04": "Korean 04 — Upper-intermediate Korean / TOPIK 4",
    "05": "Korean 05 — Advanced Korean / TOPIK 5",
    "06": "Korean 06 — TOPIK 6 and advanced functional Korean bridge",
}
COLLECTION_DAILY_TIME_BUDGET_MINUTES = 30
INITIAL_TIMESTAMP_MS = 0
SCHEDULER_ENGINE = "fsrs-7"
SCHEDULER_PARAMETER_SET_ID = "fsrs7-default-v1"
SCHEDULER_PARAMETERS = [
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
TTS_CONFIG = {
    "ja-JP": {
        "model": "openbmb/VoxCPM2",
        "reference_wav": "work/voices/ja-JP/reference.wav",
        "reference_text": "work/voices/ja-JP/reference.txt",
    },
    "ko-KR": {
        "model": "openbmb/VoxCPM2",
        "reference_wav": "work/voices/ko-KR/reference.wav",
        "reference_text": "work/voices/ko-KR/reference.txt",
    },
}
MOSSFORMER_CONFIG = {
    "model": "MossFormer2_SE_48K",
    "code_commit": "6b3774dc79c46ae8bed2a4fa5f706f0ac8c75c61",
    "model_revision": "eff8c97925c8bec812af707814b3e5d777fd4503",
    "checkpoint_sha256": (
        "03692b9f773bbd6bb43b9c5a41f96b1e28affd66e13796b7bec66ad3d8b227c6"
    ),
    "code_path": (
        "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/"
        "mossformer2-se-48k-code"
    ),
    "checkpoint": (
        "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/"
        "mossformer2-se-48k-model/last_best_checkpoint.pt"
    ),
    "one_time_decode_length": 20,
    "decode_window": 4,
    "python": (
        "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/environments/"
        "mossformer2-se-48k-py312/bin/python"
    ),
    "working_directory": "/home/Yue_Ziran/workspace/meiki-decks-issue-92",
    "runner": "mossformer2_batch.py",
}
PATH_COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
REQUIRED_STRING_FIELDS = (
    "id",
    "sentence",
    "cloze",
    "answer",
    "lemma",
    "meaning",
    "audio",
)
OPTIONAL_STRING_FIELDS = ("reading", "grammar", "register", "note")
CARD_FIELDS = set(REQUIRED_STRING_FIELDS) | {
    "accepted_answers",
    *OPTIONAL_STRING_FIELDS,
}


class DeckError(Exception):
    pass


def validate_path_component(value, label):
    if not PATH_COMPONENT.fullmatch(value):
        raise DeckError(f"{label} must be one filesystem-safe path component: {value!r}")


def load_stage_cards(root, language, stage):
    validate_path_component(language, "language")
    validate_path_component(stage, "stage")
    coverage_path = root / "coverage" / language / f"{stage}.md"
    cards_path = root / "cards" / language / f"{stage}.json"
    missing = [path for path in (coverage_path, cards_path) if not path.is_file()]
    if missing:
        raise DeckError("\n".join(f"required source file is missing: {path}" for path in missing))

    try:
        cards = json.loads(cards_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise DeckError(
            f"{cards_path}: invalid JSON at line {error.lineno}, column {error.colno}"
        ) from error
    except OSError as error:
        raise DeckError(f"{cards_path}: cannot read card data: {error}") from error

    if not isinstance(cards, list):
        raise DeckError(f"{cards_path}: card JSON must be a top-level array")

    errors = []
    seen_ids = set()
    for position, card in enumerate(cards):
        if not isinstance(card, dict):
            errors.append(f"{cards_path}: array position {position}: card must be an object")
            continue
        card_id = card.get("id")
        if isinstance(card_id, str) and card_id:
            location = f"{cards_path}: card {card_id}"
        else:
            location = f"{cards_path}: array position {position}"

        unknown_fields = sorted(set(card) - CARD_FIELDS)
        if unknown_fields:
            errors.append(f"{location}: unknown fields: {', '.join(unknown_fields)}")

        for field in REQUIRED_STRING_FIELDS:
            value = card.get(field)
            if not isinstance(value, str) or not value:
                errors.append(f"{location}: {field} must be a nonempty string")
        for field in OPTIONAL_STRING_FIELDS:
            if field in card and not isinstance(card[field], str):
                errors.append(f"{location}: optional field {field} must be a string")

        accepted_answers = card.get("accepted_answers")
        if not isinstance(accepted_answers, list) or not all(
            isinstance(answer, str) for answer in accepted_answers
        ):
            errors.append(f"{location}: accepted_answers must be a list of strings")

        if isinstance(card_id, str) and card_id:
            if card_id in seen_ids:
                errors.append(f"{location}: duplicate card ID")
            seen_ids.add(card_id)

        sentence = card.get("sentence")
        cloze = card.get("cloze")
        if isinstance(sentence, str) and isinstance(cloze, str) and cloze:
            occurrences = sentence.count(cloze)
            if occurrences != 1:
                errors.append(
                    f"{location}: sentence must contain cloze exactly once; found {occurrences}"
                )
        if isinstance(cloze, str) and isinstance(card.get("answer"), str):
            if card["answer"] != cloze:
                errors.append(f"{location}: answer must equal cloze exactly")

        if isinstance(card_id, str) and card_id:
            expected_audio = f"work/audio/{language}/{stage}/{card_id}.mp3"
            if card.get("audio") != expected_audio:
                errors.append(f"{location}: audio must equal {expected_audio}")
            if ".." in Path(expected_audio).parts:
                errors.append(f"{location}: card ID creates an unsafe audio path")

    if errors:
        raise DeckError("\n".join(errors))
    return cards


def probe_audio(audio_path, run_command=subprocess.run):
    try:
        result = run_command(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "a:0",
                "-show_entries",
                "stream=sample_rate,channels:format=duration",
                "-of",
                "json",
                str(audio_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as error:
        raise DeckError(f"{audio_path}: cannot run FFprobe: {error}") from error
    if result.returncode != 0:
        detail = result.stderr.strip() or "FFprobe could not decode the file"
        raise DeckError(f"{audio_path}: {detail}")
    try:
        metadata = json.loads(result.stdout)
        streams = metadata["streams"]
        duration_seconds = float(metadata["format"]["duration"])
        sample_rate = int(streams[0]["sample_rate"])
        channels = int(streams[0]["channels"])
    except (IndexError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise DeckError(f"{audio_path}: FFprobe returned an invalid duration") from error
    if len(streams) != 1 or sample_rate != 48_000 or channels != 1:
        raise DeckError(f"{audio_path}: audio must be 48 kHz mono")
    if duration_seconds <= 0:
        raise DeckError(f"{audio_path}: audio duration must be positive")
    try:
        decoded = run_command(
            ["ffmpeg", "-v", "error", "-i", str(audio_path), "-f", "null", "-"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as error:
        raise DeckError(f"{audio_path}: cannot run FFmpeg: {error}") from error
    if decoded.returncode != 0:
        detail = decoded.stderr.strip() or "FFmpeg could not decode the complete file"
        raise DeckError(f"{audio_path}: {detail}")
    return max(1, round(duration_seconds * 1_000))


def validate_audio(audio_path, probe=probe_audio):
    try:
        if not audio_path.is_file():
            raise DeckError(f"{audio_path}: audio file is missing")
        byte_size = audio_path.stat().st_size
    except OSError as error:
        raise DeckError(f"{audio_path}: cannot inspect audio file: {error}") from error
    if byte_size == 0:
        raise DeckError(f"{audio_path}: audio file is empty")
    duration_ms = probe(audio_path)
    if not isinstance(duration_ms, int) or duration_ms <= 0:
        raise DeckError(f"{audio_path}: audio probe must return a positive duration")
    return byte_size, duration_ms


def check_stage(root, language, stage, require_audio=False, probe=probe_audio):
    cards = load_stage_cards(root, language, stage)
    if require_audio:
        errors = []
        for card in cards:
            try:
                validate_audio(root / card["audio"], probe)
            except DeckError as error:
                errors.append(f"card {card['id']}: {error}")
        if errors:
            raise DeckError("\n".join(errors))
    return cards


@contextlib.contextmanager
def without_repository_import_path():
    repository_root = Path(__file__).resolve().parent
    original_import_path = sys.path[:]
    # VoxCPM loads Numba lazily, and coverage/ would shadow Numba's optional dependency.
    sys.path[:] = [
        path
        for path in sys.path
        if Path(path or Path.cwd()).resolve() != repository_root
    ]
    try:
        yield
    finally:
        sys.path[:] = original_import_path


def load_tts_model(configuration):
    with without_repository_import_path():
        try:
            from voxcpm import VoxCPM
        except ImportError as error:
            raise DeckError("audio generation requires the voxcpm package") from error

        try:
            return VoxCPM.from_pretrained(
                configuration["model"],
                load_denoiser=False,
                optimize=False,
            )
        except Exception as error:
            raise DeckError(f"cannot load VoxCPM2 model: {error}") from error


def write_waveform(path, waveform, sample_rate):
    try:
        import soundfile
    except ImportError as error:
        raise DeckError("audio generation requires the soundfile package") from error
    soundfile.write(path, waveform, sample_rate)


def generate_audio(
    root,
    language,
    stage,
    run_command=subprocess.run,
    probe=probe_audio,
    tts_config=None,
    denoiser_config=None,
):
    cards = load_stage_cards(root, language, stage)
    stage_workspace = root / "work" / "denoiser-temp" / language / stage
    configuration = (TTS_CONFIG if tts_config is None else tts_config).get(language)
    if configuration is None:
        raise DeckError(f"no local VoxCPM2 configuration exists for {language}")
    required_configuration = ("model", "reference_wav", "reference_text")
    if any(not configuration.get(field) for field in required_configuration):
        raise DeckError(f"local VoxCPM2 configuration is incomplete for {language}")

    failed_card_ids = set()

    def report_failure(card_id, error):
        if card_id not in failed_card_ids:
            failed_card_ids.add(card_id)
            print(f"failed card {card_id}: {error}", file=sys.stderr)

    pending_cards = []
    for card in cards:
        audio_path = root / card["audio"]
        try:
            if audio_path.is_file() and audio_path.stat().st_size > 0:
                try:
                    validate_audio(audio_path, probe)
                except DeckError:
                    pending_cards.append(card)
                else:
                    continue
            elif audio_path.exists() and not audio_path.is_file():
                raise DeckError(f"{audio_path}: output path is not a file")
            else:
                pending_cards.append(card)
        except (DeckError, OSError) as error:
            report_failure(card["id"], error)

    if not pending_cards:
        if not failed_card_ids and stage_workspace.exists():
            try:
                shutil.rmtree(stage_workspace)
            except OSError as error:
                raise DeckError(
                    f"cannot remove completed stage workspace {stage_workspace}: {error}"
                ) from error
        return len(failed_card_ids)

    reference_wav = root / configuration["reference_wav"]
    reference_text_path = root / configuration["reference_text"]
    if not reference_wav.is_file():
        raise DeckError(f"voice reference WAV is missing: {reference_wav}")
    try:
        if reference_wav.stat().st_size == 0:
            raise DeckError(f"voice reference WAV is empty: {reference_wav}")
    except OSError as error:
        raise DeckError(f"cannot inspect voice reference WAV {reference_wav}: {error}") from error
    if not reference_text_path.is_file():
        raise DeckError(f"voice reference transcript is missing: {reference_text_path}")
    try:
        reference_text = reference_text_path.read_text(encoding="utf-8")
    except OSError as error:
        raise DeckError(
            f"cannot read voice reference transcript {reference_text_path}: {error}"
        ) from error
    if not reference_text.strip():
        raise DeckError(f"voice reference transcript is empty: {reference_text_path}")

    selected_denoiser = MOSSFORMER_CONFIG if denoiser_config is None else denoiser_config
    required_denoiser_configuration = (
        "model",
        "code_commit",
        "model_revision",
        "checkpoint_sha256",
        "code_path",
        "checkpoint",
        "one_time_decode_length",
        "decode_window",
        "python",
        "working_directory",
        "runner",
    )
    if any(not selected_denoiser.get(field) for field in required_denoiser_configuration):
        raise DeckError("local MossFormer2 configuration is incomplete")
    runner_path = root / selected_denoiser["runner"]
    if not runner_path.is_file():
        raise DeckError(f"MossFormer2 batch runner is missing: {runner_path}")

    model = load_tts_model(configuration)
    try:
        sample_rate = model.tts_model.sample_rate
    except AttributeError as error:
        raise DeckError("VoxCPM2 model does not expose an output sample rate") from error
    if sample_rate != 48_000:
        raise DeckError("VoxCPM2 model must return a 48 kHz waveform")

    baseline_root = stage_workspace / "baseline"
    denoised_root = stage_workspace / "denoised"
    encoded_root = stage_workspace / "encoded"
    for directory in (baseline_root, denoised_root, encoded_root):
        directory.mkdir(parents=True, exist_ok=True)

    baseline_regeneration_ids = set()
    retained_report_path = stage_workspace / "report.json"
    if retained_report_path.is_file():
        try:
            retained_report = json.loads(retained_report_path.read_text(encoding="utf-8"))
            retained_failures = retained_report["failed"]
            if not isinstance(retained_failures, dict) or not all(
                isinstance(card_id, str) and isinstance(detail, str)
                for card_id, detail in retained_failures.items()
            ):
                raise ValueError("failed must map card IDs to details")
        except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
            raise DeckError(
                f"retained MossFormer2 report is invalid: {retained_report_path}: {error}"
            ) from error
        baseline_regeneration_ids = {
            card_id
            for card_id, detail in retained_failures.items()
            if "denoised output introduces clipped samples" in detail
        }

    generated_cards = []
    for card in pending_cards:
        baseline_path = baseline_root / f"{card['id']}.wav"
        try:
            if (
                card["id"] not in baseline_regeneration_ids
                and baseline_path.is_file()
                and baseline_path.stat().st_size > 0
            ):
                validate_audio(baseline_path, probe)
                generated_cards.append(card)
                continue
        except (DeckError, OSError):
            pass
        try:
            with without_repository_import_path():
                waveform = model.generate(
                    text=card["sentence"],
                    prompt_wav_path=str(reference_wav),
                    prompt_text=reference_text,
                    reference_wav_path=str(reference_wav),
                )
            write_waveform(baseline_path, waveform, sample_rate)
            generated_cards.append(card)
        except Exception as error:
            report_failure(card["id"], error)

    waveform = None
    model = None
    gc.collect()
    torch = sys.modules.get("torch")
    if torch is not None:
        try:
            torch.cuda.empty_cache()
        except (AttributeError, RuntimeError) as error:
            raise DeckError(f"cannot release VoxCPM2 GPU memory: {error}") from error

    if generated_cards:
        manifest_path = stage_workspace / "manifest.json"
        report_path = stage_workspace / "report.json"
        manifest = {
            "model": selected_denoiser["model"],
            "code_commit": selected_denoiser["code_commit"],
            "model_revision": selected_denoiser["model_revision"],
            "checkpoint_sha256": selected_denoiser["checkpoint_sha256"],
            "code_path": selected_denoiser["code_path"],
            "checkpoint": selected_denoiser["checkpoint"],
            "one_time_decode_length": selected_denoiser["one_time_decode_length"],
            "decode_window": selected_denoiser["decode_window"],
            "cards": [
                {
                    "id": card["id"],
                    "baseline": str((baseline_root / f"{card['id']}.wav").resolve()),
                    "denoised": str((denoised_root / f"{card['id']}.wav").resolve()),
                }
                for card in generated_cards
            ],
        }
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        report_path.write_text("", encoding="utf-8")
        environment = os.environ.copy()
        environment["TMPDIR"] = str(stage_workspace.resolve())
        command = [
            selected_denoiser["python"],
            str(runner_path.resolve()),
            "--manifest",
            str(manifest_path.resolve()),
            "--report",
            str(report_path.resolve()),
        ]
        try:
            denoiser_result = run_command(
                command,
                cwd=selected_denoiser["working_directory"],
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError as error:
            denoiser_result = None
            batch_error = f"cannot run MossFormer2 batch: {error}"
        else:
            batch_error = None

        expected_ids = {card["id"] for card in generated_cards}
        try:
            if denoiser_result is None:
                raise DeckError(batch_error)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            succeeded = report["succeeded"]
            failed = report["failed"]
            if (
                report.get("model") != selected_denoiser["model"]
                or not isinstance(succeeded, list)
                or not all(isinstance(card_id, str) for card_id in succeeded)
                or len(set(succeeded)) != len(succeeded)
                or not isinstance(failed, dict)
                or not all(
                    isinstance(card_id, str) and isinstance(detail, str) and detail
                    for card_id, detail in failed.items()
                )
                or set(succeeded) & set(failed)
                or set(succeeded) | set(failed) != expected_ids
                or (denoiser_result.returncode == 0) != (not failed)
            ):
                raise DeckError("MossFormer2 batch returned an invalid report")
        except (DeckError, OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
            detail = batch_error or str(error)
            if denoiser_result is not None and denoiser_result.stderr.strip():
                detail = f"{detail}: {denoiser_result.stderr.strip()}"
            for card in generated_cards:
                report_failure(card["id"], detail)
            succeeded = []
            failed = {}

        for card_id, detail in failed.items():
            report_failure(card_id, detail)

        cards_by_id = {card["id"]: card for card in generated_cards}
        for card_id in succeeded:
            card = cards_by_id[card_id]
            audio_path = root / card["audio"]
            denoised_path = denoised_root / f"{card_id}.wav"
            encoded_path = encoded_root / f"{card_id}.mp3"
            try:
                audio_path.parent.mkdir(parents=True, exist_ok=True)
                result = run_command(
                    [
                        "ffmpeg",
                        "-v",
                        "error",
                        "-y",
                        "-i",
                        str(denoised_path),
                        "-codec:a",
                        "libmp3lame",
                        "-q:a",
                        "2",
                        str(encoded_path),
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode != 0:
                    detail = result.stderr.strip() or "FFmpeg conversion failed"
                    raise DeckError(detail)
                validate_audio(encoded_path, probe)
                encoded_path.replace(audio_path)
            except Exception as error:
                report_failure(card_id, error)

    if not failed_card_ids:
        for card in cards:
            try:
                validate_audio(root / card["audio"], probe)
            except DeckError as error:
                report_failure(card["id"], error)

    if not failed_card_ids:
        try:
            shutil.rmtree(stage_workspace)
        except OSError as error:
            raise DeckError(f"cannot remove completed stage workspace {stage_workspace}: {error}")
    return len(failed_card_ids)


def content_hash(data):
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def media_archive_path(media_hash):
    digest = media_hash.removeprefix("sha256:")
    return f"media/sha256/{digest[:2]}/{digest[2:]}"


def media_reference(reference_id, role, media_hash, audio_path, byte_size, duration_ms, language):
    return {
        "id": reference_id,
        "content_hash": media_hash,
        "kind": "audio",
        "role": role,
        "media_type": "audio/mpeg",
        "byte_size": byte_size,
        "original_file_name": audio_path.name,
        "alt_text": None,
        "width": None,
        "height": None,
        "duration_ms": duration_ms,
        "language_tag": language,
        "direction": "auto",
        "created_at_ms": INITIAL_TIMESTAMP_MS,
    }


def portable_note(language, stage, card, media_hash, audio_path, byte_size, duration_ms):
    identity = f"{language}:{stage}:{card['id']}"
    source_id = f"source:{identity}"
    cloze_id = f"cloze:{identity}"
    archive_card_id = f"card:{identity}"
    before, after = card["sentence"].split(card["cloze"])
    annotations = []
    for field in ("lemma", *OPTIONAL_STRING_FIELDS):
        if field in card:
            annotations.append(
                {
                    "id": f"annotation:{identity}:{field}",
                    "label": field.replace("_", " ").title(),
                    "value": card[field],
                    "language_tag": language,
                    "direction": "auto",
                }
            )
    prompt_audio = media_reference(
        f"media:{identity}:prompt",
        "prompt_audio",
        media_hash,
        audio_path,
        byte_size,
        duration_ms,
        language,
    )
    answer_audio = media_reference(
        f"media:{identity}:answer",
        "answer_audio",
        media_hash,
        audio_path,
        byte_size,
        duration_ms,
        language,
    )
    schedule = {
        "card_id": archive_card_id,
        "version": 0,
        "lifecycle": "unseen",
        "due_at_ms": INITIAL_TIMESTAMP_MS,
        "ideal_due_at_ms": INITIAL_TIMESTAMP_MS,
        "interval_milliseconds": 0,
        "interval_seconds": 0,
        "repetitions": 0,
        "stability_milliseconds": 0,
        "difficulty_millipoints": 0,
        "last_reviewed_at_ms": None,
        "last_review_event_id": None,
    }
    return {
        "source_item": {
            "id": source_id,
            "deck_id": f"deck:{language}:{stage}",
            "segments": [
                {
                    "id": f"segment:{identity}:before",
                    "ordinal": 0,
                    "content": {"text": before},
                },
                {
                    "id": f"segment:{identity}:cloze",
                    "ordinal": 1,
                    "content": {"cloze": {"cloze_id": cloze_id, "text": card["cloze"]}},
                },
                {
                    "id": f"segment:{identity}:after",
                    "ordinal": 2,
                    "content": {"text": after},
                },
            ],
            "language_tag": language,
            "direction": "auto",
            "tags": [],
            "annotations": [],
            "explanation": None,
            "media": [prompt_audio, answer_audio],
            "created_at_ms": INITIAL_TIMESTAMP_MS,
            "updated_at_ms": INITIAL_TIMESTAMP_MS,
        },
        "clozes": [
            {
                "id": cloze_id,
                "source_item_id": source_id,
                "answer": card["answer"],
                "accepted_answers": card["accepted_answers"],
                "hint": None,
                "language_tag": language,
                "direction": "auto",
                "matching_policy": "strict",
                "annotations": annotations,
                "explanation": {
                    "value": card["meaning"],
                    "language_tag": None,
                    "direction": "auto",
                },
                "media": [],
                "created_at_ms": INITIAL_TIMESTAMP_MS,
                "updated_at_ms": INITIAL_TIMESTAMP_MS,
            }
        ],
        "cards": [
            {
                "card": {
                    "id": archive_card_id,
                    "cloze_id": cloze_id,
                    "content_version": 1,
                    "suspended": False,
                    "created_at_ms": INITIAL_TIMESTAMP_MS,
                    "updated_at_ms": INITIAL_TIMESTAMP_MS,
                },
                "baseline": schedule.copy(),
                "schedule": schedule.copy(),
                "review_events": [],
            }
        ],
        "deleted_at_ms": None,
    }


def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def require_archive(condition, archive_path, message):
    if not condition:
        raise DeckError(f"{archive_path}: archive verification failed: {message}")


def verify_archive(archive_path):
    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            names = archive.namelist()
            require_archive(len(names) == len(set(names)), archive_path, "duplicate ZIP entries")
            manifest = json.loads(archive.read(MANIFEST_PATH))
            collection_bytes = archive.read(COLLECTION_PATH)
            collection = json.loads(collection_bytes)

            require_archive(manifest["format"] == ARCHIVE_FORMAT, archive_path, "wrong format")
            require_archive(manifest["version"] == ARCHIVE_VERSION, archive_path, "wrong version")
            require_archive(
                manifest["scope"] == "full_collection",
                archive_path,
                "wrong archive scope",
            )
            require_archive(
                manifest["collection_path"] == COLLECTION_PATH,
                archive_path,
                "wrong collection path",
            )
            require_archive(
                manifest["collection_sha256"] == content_hash(collection_bytes),
                archive_path,
                "collection checksum mismatch",
            )

            media_entries = manifest["media"]
            expected_names = {MANIFEST_PATH, COLLECTION_PATH}
            expected_names.update(entry["path"] for entry in media_entries)
            require_archive(set(names) == expected_names, archive_path, "unexpected ZIP entries")
            require_archive(
                manifest["counts"]["media_objects"] == len(media_entries),
                archive_path,
                "media count mismatch",
            )
            manifest_media = {}
            for entry in media_entries:
                media_hash = entry["content_hash"]
                require_archive(
                    re.fullmatch(r"sha256:[0-9a-f]{64}", media_hash) is not None,
                    archive_path,
                    "noncanonical media hash",
                )
                require_archive(
                    entry["path"] == media_archive_path(media_hash),
                    archive_path,
                    "wrong media path",
                )
                media_bytes = archive.read(entry["path"])
                require_archive(
                    entry["byte_size"] == len(media_bytes),
                    archive_path,
                    "media byte-size mismatch",
                )
                require_archive(
                    content_hash(media_bytes) == media_hash,
                    archive_path,
                    "media checksum mismatch",
                )
                require_archive(
                    media_hash not in manifest_media,
                    archive_path,
                    "duplicate media hash",
                )
                manifest_media[media_hash] = entry

            decks = collection["decks"]
            notes = collection["notes"]
            profiles = collection["scheduler_profiles"]
            parameter_sets = collection["scheduler_parameter_sets"]
            deck_ids = {deck["id"] for deck in decks}
            require_archive(len(deck_ids) == len(decks), archive_path, "duplicate deck IDs")
            require_archive(
                collection["collection_scheduling_settings"]["daily_time_budget_minutes"]
                == COLLECTION_DAILY_TIME_BUDGET_MINUTES,
                archive_path,
                "wrong collection daily budget",
            )
            require_archive(
                len(parameter_sets) == 1
                and parameter_sets[0]["id"] == SCHEDULER_PARAMETER_SET_ID
                and parameter_sets[0]["engine_version"] == SCHEDULER_ENGINE
                and parameter_sets[0]["parameters"] == SCHEDULER_PARAMETERS,
                archive_path,
                "wrong scheduler parameter set",
            )
            require_archive(
                {profile["deck_id"] for profile in profiles} == deck_ids,
                archive_path,
                "scheduler profiles do not match decks",
            )
            require_archive(
                all(
                    profile["scheduling_mode"] == "automatic"
                    and profile["active_parameter_set_id"] == SCHEDULER_PARAMETER_SET_ID
                    for profile in profiles
                ),
                archive_path,
                "scheduler profile configuration mismatch",
            )

            card_count = 0
            review_count = 0
            referenced_media = set()
            global_ids = set()
            for note in notes:
                source = note["source_item"]
                clozes = note["clozes"]
                cards = note["cards"]
                require_archive(source["deck_id"] in deck_ids, archive_path, "missing deck")
                require_archive(
                    len(clozes) == len(cards) == 1,
                    archive_path,
                    "source note must contain one cloze and card",
                )
                require_archive(note["deleted_at_ms"] is None, archive_path, "deleted source note")
                segments = source["segments"]
                require_archive(
                    len(segments) == 3
                    and [segment["ordinal"] for segment in segments] == [0, 1, 2]
                    and set(segments[0]["content"]) == {"text"}
                    and set(segments[1]["content"]) == {"cloze"}
                    and set(segments[2]["content"]) == {"text"},
                    archive_path,
                    "semantic segments are invalid",
                )
                cloze = clozes[0]
                portable_card = cards[0]
                card = portable_card["card"]
                segment_cloze = segments[1]["content"]["cloze"]
                require_archive(
                    cloze["source_item_id"] == source["id"]
                    and segment_cloze["cloze_id"] == cloze["id"]
                    and card["cloze_id"] == cloze["id"],
                    archive_path,
                    "source, cloze, and card relationships are invalid",
                )
                schedule = portable_card["schedule"]
                baseline = portable_card["baseline"]
                require_archive(
                    baseline == schedule
                    and schedule["card_id"] == card["id"]
                    and schedule["version"] == 0
                    and schedule["lifecycle"] == "unseen"
                    and portable_card["review_events"] == [],
                    archive_path,
                    "unseen schedule state is invalid",
                )
                source_media = source["media"]
                require_archive(
                    len(source_media) == 2
                    and [media["role"] for media in source_media]
                    == ["prompt_audio", "answer_audio"]
                    and source_media[0]["content_hash"] == source_media[1]["content_hash"],
                    archive_path,
                    "prompt and answer media references are invalid",
                )
                for media in source_media:
                    media_hash = media["content_hash"]
                    require_archive(
                        media_hash in manifest_media
                        and media["byte_size"] == manifest_media[media_hash]["byte_size"],
                        archive_path,
                        "media reference does not match manifest",
                    )
                    referenced_media.add(media_hash)
                for identity in (
                    source["id"],
                    *(segment["id"] for segment in segments),
                    cloze["id"],
                    card["id"],
                ):
                    require_archive(identity not in global_ids, archive_path, "duplicate entity ID")
                    global_ids.add(identity)
                card_count += 1
                review_count += len(portable_card["review_events"])

            counts = manifest["counts"]
            require_archive(counts["decks"] == len(decks), archive_path, "deck count mismatch")
            require_archive(counts["notes"] == len(notes), archive_path, "note count mismatch")
            require_archive(counts["cards"] == card_count, archive_path, "card count mismatch")
            require_archive(
                counts["review_events"] == review_count,
                archive_path,
                "review-event count mismatch",
            )
            require_archive(
                referenced_media == set(manifest_media),
                archive_path,
                "media inventory does not match references",
            )
            return {
                "card_count": card_count,
                "media_object_count": len(manifest_media),
            }
    except DeckError:
        raise
    except (OSError, KeyError, TypeError, ValueError, zipfile.BadZipFile) as error:
        raise DeckError(f"{archive_path}: archive verification failed: {error}") from error


def build_language(root, language, probe=probe_audio):
    validate_path_component(language, "language")
    normalized_language = language.lower()
    archive_path = (
        root
        / "dist"
        / f"meiki-{normalized_language}-complete-v{ARCHIVE_RELEASE_VERSION}.meiki"
    )
    if archive_path.exists():
        raise DeckError(f"archive destination already exists: {archive_path}")
    stage_files = sorted((root / "cards" / language).glob("*.json"))
    if not stage_files:
        raise DeckError(f"no card stages exist for language {language}")
    if language == "ja-JP":
        actual_stages = tuple(stage_file.stem for stage_file in stage_files)
        expected_stages = tuple(JAPANESE_COMPLETE_STAGE_NAMES)
        if actual_stages != expected_stages:
            raise DeckError(
                "Japanese complete bundle requires stages "
                f"{', '.join(expected_stages)} in order; found {', '.join(actual_stages)}"
            )
    if language == "ko-KR":
        actual_stages = tuple(stage_file.stem for stage_file in stage_files)
        expected_stages = tuple(KOREAN_COMPLETE_STAGE_NAMES)
        if actual_stages != expected_stages:
            raise DeckError(
                "Korean complete bundle requires stages "
                f"{', '.join(expected_stages)} in order; found {', '.join(actual_stages)}"
            )

    decks = []
    notes = []
    profiles = []
    media_objects = {}
    for stage_file in stage_files:
        stage = stage_file.stem
        validate_path_component(stage, "stage")
        cards = load_stage_cards(root, language, stage)
        deck_id = f"deck:{language}:{stage}"
        if language == "ja-JP":
            deck_name = JAPANESE_COMPLETE_STAGE_NAMES[stage]
        elif language == "ko-KR":
            deck_name = KOREAN_COMPLETE_STAGE_NAMES[stage]
        else:
            deck_name = f"{language} {stage}"
        decks.append(
            {
                "id": deck_id,
                "name": deck_name,
                "description": None,
                "language_tag": language,
                "direction": "auto",
                "matching_policy": "strict",
                "settings": {
                    "target_retention_basis_points": None,
                    "new_cards_per_day": None,
                    "maximum_interval_days": None,
                },
                "created_at_ms": INITIAL_TIMESTAMP_MS,
                "updated_at_ms": INITIAL_TIMESTAMP_MS,
            }
        )
        profiles.append(
            {
                "deck_id": deck_id,
                "engine_version": SCHEDULER_ENGINE,
                "active_parameter_set_id": SCHEDULER_PARAMETER_SET_ID,
                "scheduling_mode": "automatic",
                "deck_daily_time_budget_minutes": None,
                "controller_version": "time-budget-v1",
                "controller_target_retention_basis_points": 9_000,
                "controller_new_cards_per_day": 20,
                "controller_last_evaluated_day_start_ms": None,
                "controller_review_count": 0,
                "controller_unseen_count": 0,
                "controller_forecast_review_seconds_per_day": 0,
                "controller_backlog_exceeds_budget": False,
                "controller_explanation": "",
                "day_boundary_minutes": 240,
                "updated_at_ms": INITIAL_TIMESTAMP_MS,
            }
        )
        for card in cards:
            audio_path = root / card["audio"]
            byte_size, duration_ms = validate_audio(audio_path, probe)
            try:
                audio_bytes = audio_path.read_bytes()
            except OSError as error:
                raise DeckError(f"{audio_path}: cannot read audio file: {error}") from error
            media_hash = content_hash(audio_bytes)
            existing = media_objects.get(media_hash)
            if existing is not None and existing["bytes"] != audio_bytes:
                raise DeckError(f"{audio_path}: SHA-256 collision detected")
            media_objects.setdefault(
                media_hash,
                {
                    "bytes": audio_bytes,
                    "byte_size": byte_size,
                },
            )
            notes.append(
                portable_note(
                    language,
                    stage,
                    card,
                    media_hash,
                    audio_path,
                    byte_size,
                    duration_ms,
                )
            )

    collection = {
        "collection_scheduling_settings": {
            "daily_time_budget_minutes": COLLECTION_DAILY_TIME_BUDGET_MINUTES,
            "updated_at_ms": INITIAL_TIMESTAMP_MS,
        },
        "decks": decks,
        "notes": notes,
        "scheduler_parameter_sets": [
            {
                "id": SCHEDULER_PARAMETER_SET_ID,
                "engine_version": SCHEDULER_ENGINE,
                "parameters": SCHEDULER_PARAMETERS,
                "created_at_ms": INITIAL_TIMESTAMP_MS,
            }
        ],
        "scheduler_profiles": profiles,
    }
    collection_bytes = canonical_json(collection)
    manifest_media = [
        {
            "content_hash": media_hash,
            "path": media_archive_path(media_hash),
            "byte_size": media_objects[media_hash]["byte_size"],
        }
        for media_hash in sorted(media_objects)
    ]
    manifest = {
        "format": ARCHIVE_FORMAT,
        "version": ARCHIVE_VERSION,
        "created_at_ms": INITIAL_TIMESTAMP_MS,
        "scope": "full_collection",
        "collection_path": COLLECTION_PATH,
        "collection_sha256": content_hash(collection_bytes),
        "counts": {
            "decks": len(decks),
            "notes": len(notes),
            "cards": len(notes),
            "review_events": 0,
            "media_objects": len(media_objects),
        },
        "media": manifest_media,
    }
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(archive_path, "x", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(MANIFEST_PATH, canonical_json(manifest))
            archive.writestr(COLLECTION_PATH, collection_bytes)
            for entry in manifest_media:
                archive.writestr(
                    entry["path"],
                    media_objects[entry["content_hash"]]["bytes"],
                )
    except OSError as error:
        raise DeckError(f"cannot write archive {archive_path}: {error}") from error

    summary = verify_archive(archive_path)
    try:
        archive_hash = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    except OSError as error:
        raise DeckError(f"cannot hash archive {archive_path}: {error}") from error
    return {
        "path": archive_path,
        "card_count": summary["card_count"],
        "media_object_count": summary["media_object_count"],
        "sha256": archive_hash,
    }


def create_parser():
    parser = argparse.ArgumentParser(description="Validate and build Meiki language decks")
    commands = parser.add_subparsers(dest="command", required=True)

    check = commands.add_parser("check", help="validate one language stage")
    check.add_argument("--language", required=True)
    check.add_argument("--stage", required=True)
    check.add_argument("--require-audio", action="store_true")

    generate = commands.add_parser("generate-audio", help="generate one stage's audio")
    generate.add_argument("--language", required=True)
    generate.add_argument("--stage", required=True)

    build = commands.add_parser("build", help="build one complete language archive")
    build.add_argument("--language", required=True)
    return parser


def main(argv=None):
    arguments = create_parser().parse_args(argv)
    root = Path.cwd()
    try:
        if arguments.command == "check":
            cards = check_stage(
                root,
                arguments.language,
                arguments.stage,
                require_audio=arguments.require_audio,
            )
            print(f"validated {len(cards)} cards")
            return 0
        if arguments.command == "generate-audio":
            failures = generate_audio(root, arguments.language, arguments.stage)
            return 1 if failures else 0
        summary = build_language(root, arguments.language)
        print(f"archive: {summary['path']}")
        print(f"cards: {summary['card_count']}")
        print(f"media objects: {summary['media_object_count']}")
        print(f"sha256: {summary['sha256']}")
        return 0
    except DeckError as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
