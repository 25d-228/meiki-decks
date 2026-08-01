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

Real audio generation requires locally installed Qwen3-TTS and FFmpeg tools.
It does not use cloud keys or download models automatically.
