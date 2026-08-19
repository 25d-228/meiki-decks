#!/usr/bin/env python3

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


MODEL_NAME = "MossFormer2_SE_48K"
CODE_COMMIT = "6b3774dc79c46ae8bed2a4fa5f706f0ac8c75c61"
MODEL_REVISION = "eff8c97925c8bec812af707814b3e5d777fd4503"
CHECKPOINT_SHA256 = "03692b9f773bbd6bb43b9c5a41f96b1e28affd66e13796b7bec66ad3d8b227c6"
CODE_PATH = Path(
    "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/"
    "mossformer2-se-48k-code"
)
CHECKPOINT_PATH = Path(
    "/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/"
    "mossformer2-se-48k-model/last_best_checkpoint.pt"
)
ONE_TIME_DECODE_LENGTH = 20
DECODE_WINDOW = 4
SAMPLE_RATE = 48_000


def load_enhancer():
    actual_commit = subprocess.check_output(
        ["git", "-C", str(CODE_PATH), "rev-parse", "HEAD"],
        text=True,
    ).strip()
    if actual_commit != CODE_COMMIT:
        raise ValueError(f"ClearerVoice code commit mismatch: {actual_commit}")
    checkpoint_hash = hashlib.sha256()
    with CHECKPOINT_PATH.open("rb") as checkpoint:
        for block in iter(lambda: checkpoint.read(1024 * 1024), b""):
            checkpoint_hash.update(block)
    actual_checkpoint_hash = checkpoint_hash.hexdigest()
    if actual_checkpoint_hash != CHECKPOINT_SHA256:
        raise ValueError(f"MossFormer2 checkpoint mismatch: {actual_checkpoint_hash}")
    configured_checkpoint = (
        Path.cwd() / "checkpoints" / MODEL_NAME / "last_best_checkpoint.pt"
    ).resolve()
    if configured_checkpoint != CHECKPOINT_PATH.resolve():
        raise ValueError(f"ClearVoice checkpoint path mismatch: {configured_checkpoint}")
    from clearvoice import ClearVoice

    return ClearVoice(task="speech_enhancement", model_names=[MODEL_NAME])


def denoise_file(enhancer, baseline_path, denoised_path):
    import numpy as np
    import soundfile

    baseline, sample_rate = soundfile.read(
        baseline_path,
        dtype="float32",
        always_2d=False,
    )
    if sample_rate != SAMPLE_RATE or baseline.ndim != 1 or baseline.size == 0:
        raise ValueError(f"{baseline_path}: baseline must be nonempty 48 kHz mono audio")
    if not np.isfinite(baseline).all():
        raise ValueError(f"{baseline_path}: baseline contains non-finite samples")

    restored = np.asarray(
        enhancer(baseline.reshape(1, -1).astype(np.float32, copy=False), False),
        dtype=np.float32,
    )
    if restored.ndim != 2 or restored.shape[0] != 1:
        raise ValueError(f"{baseline_path}: MossFormer2 returned an invalid tensor shape")
    if restored.shape[1] < baseline.shape[0]:
        raise ValueError(f"{baseline_path}: MossFormer2 output is shorter than its input")
    output = restored[0, : baseline.shape[0]]
    if output.shape[0] != baseline.shape[0]:
        raise ValueError(f"{baseline_path}: denoised frame count does not match baseline")
    if not np.isfinite(output).all():
        raise ValueError(f"{baseline_path}: denoised output contains non-finite samples")
    baseline_clipping = int(np.count_nonzero(np.abs(baseline) >= 1.0))
    output_clipping = int(np.count_nonzero(np.abs(output) >= 1.0))
    if output_clipping > baseline_clipping:
        raise ValueError(f"{baseline_path}: denoised output introduces clipped samples")

    denoised_path.parent.mkdir(parents=True, exist_ok=True)
    partial_path = denoised_path.with_name(f".{denoised_path.stem}.partial.wav")
    soundfile.write(partial_path, output, SAMPLE_RATE, subtype="FLOAT")
    verified, verified_rate = soundfile.read(
        partial_path,
        dtype="float32",
        always_2d=False,
    )
    if (
        verified_rate != SAMPLE_RATE
        or verified.ndim != 1
        or verified.shape[0] != baseline.shape[0]
        or not np.isfinite(verified).all()
        or int(np.count_nonzero(np.abs(verified) >= 1.0)) > baseline_clipping
    ):
        raise ValueError(f"{partial_path}: written denoised WAV failed validation")
    partial_path.replace(denoised_path)


def load_manifest(manifest_path):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    fixed_fields = {
        "model": MODEL_NAME,
        "code_commit": CODE_COMMIT,
        "model_revision": MODEL_REVISION,
        "checkpoint_sha256": CHECKPOINT_SHA256,
        "code_path": str(CODE_PATH),
        "checkpoint": str(CHECKPOINT_PATH),
        "one_time_decode_length": ONE_TIME_DECODE_LENGTH,
        "decode_window": DECODE_WINDOW,
    }
    if any(manifest.get(field) != value for field, value in fixed_fields.items()):
        raise ValueError("manifest does not match the fixed MossFormer2 contract")
    cards = manifest.get("cards")
    if not isinstance(cards, list) or not cards:
        raise ValueError("manifest cards must be a nonempty list")
    card_ids = []
    for card in cards:
        if (
            not isinstance(card, dict)
            or not isinstance(card.get("id"), str)
            or not card["id"]
            or not isinstance(card.get("baseline"), str)
            or not card["baseline"]
            or not isinstance(card.get("denoised"), str)
            or not card["denoised"]
        ):
            raise ValueError("manifest contains an invalid card entry")
        card_ids.append(card["id"])
    if len(card_ids) != len(set(card_ids)):
        raise ValueError("manifest contains duplicate card IDs")
    return cards


def process_batch(
    manifest_path,
    report_path,
    load_model=load_enhancer,
    process_file=denoise_file,
):
    cards = load_manifest(manifest_path)
    succeeded = []
    failed = {}
    try:
        enhancer = load_model()
    except Exception as error:
        detail = f"cannot load {MODEL_NAME}: {error}"
        failed = {card["id"]: detail for card in cards}
    else:
        for card in cards:
            card_id = card["id"]
            try:
                process_file(
                    enhancer,
                    Path(card["baseline"]),
                    Path(card["denoised"]),
                )
            except Exception as error:
                failed[card_id] = str(error)
            else:
                succeeded.append(card_id)

    report = {"model": MODEL_NAME, "succeeded": succeeded, "failed": failed}
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for card_id, detail in failed.items():
        print(f"failed card {card_id}: {detail}", file=sys.stderr)
    print(json.dumps({"succeeded": len(succeeded), "failed": len(failed)}))
    return 1 if failed else 0


def create_parser():
    parser = argparse.ArgumentParser(description="Denoise one Meiki audio stage")
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    return parser


def main(argv=None):
    arguments = create_parser().parse_args(argv)
    repository_root = Path(__file__).resolve().parent
    original_import_path = sys.path[:]
    # coverage/ contains source documentation, but Numba expects the installed
    # coverage package while ClearVoice loads Librosa lazily.
    sys.path[:] = [
        path
        for path in sys.path
        if Path(path or Path.cwd()).resolve() != repository_root
    ]
    try:
        return process_batch(arguments.manifest, arguments.report)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1
    finally:
        sys.path[:] = original_import_path


if __name__ == "__main__":
    raise SystemExit(main())
