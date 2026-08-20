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

French, Japanese, and Korean audio generation runs on a CUDA server with VoxCPM2 Ultimate
Cloning and FFmpeg. Install the required server packages with:

```bash
pip install -U voxcpm soundfile
```

Place each fixed local reference pair at `work/voices/<locale>/reference.wav` and
`work/voices/<locale>/reference.txt`. Configured locales are `fr-FR`, `ja-JP`, and
`ko-KR`.
The generator downloads the configured model through the VoxCPM runtime on first
use. It does not use cloud keys or a remote synthesis service.

### French, Japanese, and Korean denoising

[Issue #92](https://github.com/25d-228/meiki-decks/issues/92) selected the
official Apache-2.0 `MossFormer2_SE_48K` speech-enhancement model. The same active
`generate-audio` path is used for French, Japanese, and Korean with these
immutable upstream revisions:

- ClearerVoice-Studio code commit:
  `6b3774dc79c46ae8bed2a4fa5f706f0ac8c75c61`
- `alibabasglab/MossFormer2_SE_48K` model revision:
  `eff8c97925c8bec812af707814b3e5d777fd4503`
- `last_best_checkpoint.pt` SHA-256:
  `03692b9f773bbd6bb43b9c5a41f96b1e28affd66e13796b7bec66ad3d8b227c6`

Run the unchanged stage command in the VoxCPM2 environment:

```bash
python meiki_decks.py generate-audio --language <locale> --stage <stage>
```

The command loads VoxCPM2 once and writes every pending untreated waveform for
the stage. It then invokes `mossformer2_batch.py` once in the retained separate
MossFormer2 environment. The runner loads
`ClearVoice(task="speech_enhancement", model_names=["MossFormer2_SE_48K"])`
once, uses a 20-second one-pass decode length and a 4-second decode window, and
preserves each input frame count in 48 kHz mono float32 WAV output. FFmpeg
encodes only validated denoised WAV files to the declared MP3 paths.

Stage baselines and denoised WAV files remain under
`work/denoiser-temp/<locale>/<stage>/` when any card fails. After every final
MP3 in a stage validates, the generator removes that stage temporary directory
once. Valid existing final MP3 files are still skipped during normal
incremental generation.
