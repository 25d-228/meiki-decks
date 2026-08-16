# Meiki Decks

Meiki Decks is being rebuilt from scratch. Language stages are added later
under [roadmap issue #56](https://github.com/25d-228/meiki-decks/issues/56).

The toolchain supports these commands:

```bash
python meiki_decks.py check --language <locale> --stage <stage>
python meiki_decks.py check --language <locale> --stage <stage> --require-audio
python meiki_decks.py generate-audio --language <locale> --stage <stage>
python meiki_decks.py build --language <locale>
```

Committed stage sources use `coverage/<locale>/<stage>.md` and
`cards/<locale>/<stage>.json`. Local audio is written under
`work/audio/<locale>/<stage>/`, and complete language archives are written to
`dist/`. Audio, archives, models, and caches remain local and ignored.

Japanese and Korean audio generation runs on a CUDA server with VoxCPM2 Ultimate
Cloning and FFmpeg. Install the required server packages with:

```bash
pip install -U voxcpm soundfile
```

Place each fixed local reference pair at `work/voices/<locale>/reference.wav` and
`work/voices/<locale>/reference.txt`. Configured locales are `ja-JP` and `ko-KR`.
The generator downloads the configured model through the VoxCPM runtime on first
use. It does not use cloud keys or a remote synthesis service.

### Japanese and Korean denoising

[Issue #92](https://github.com/25d-228/meiki-decks/issues/92) selected the
official `MossFormer2_SE_48K` speech-enhancement model for the next complete
Japanese and Korean audio regeneration. Use the Apache-2.0 model with these
immutable upstream revisions:

- ClearerVoice-Studio code commit:
  `6b3774dc79c46ae8bed2a4fa5f706f0ac8c75c61`
- `alibabasglab/MossFormer2_SE_48K` model revision:
  `eff8c97925c8bec812af707814b3e5d777fd4503`
- `last_best_checkpoint.pt` SHA-256:
  `03692b9f773bbd6bb43b9c5a41f96b1e28affd66e13796b7bec66ad3d8b227c6`

The fixed comparison invocation on the designated server was:

```bash
cd /home/Yue_Ziran/workspace/meiki-decks-issue-92
env TMPDIR=/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/temp \
  PYTHONPATH=/mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/relay/mossformer2-se-48k-code/clearvoice \
  CUDA_VISIBLE_DEVICES=0 \
  /mango/homes/YUE_Ziran/workspace/meiki-decks-issue-92/environments/mossformer2-se-48k-py312/bin/python \
  run_mossformer2.py
```

The runner constructs `ClearVoice(task="speech_enhancement",
model_names=["MossFormer2_SE_48K"])` and passes untreated VoxCPM2 output as
48 kHz mono float32 samples. The pinned model configuration uses a 20-second
one-pass decode length and a 4-second decode window. Write 48 kHz mono float32
WAV output with the input frame count preserved; do not normalize, trim,
compress, or otherwise post-process one language differently from the other.
