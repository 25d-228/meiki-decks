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
