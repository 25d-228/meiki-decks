# Meiki decks

Original typed-cloze sentence content for Meiki in educated central Mexican Spanish (`es-MX`). Spanish 01 covers A1 foundations; Spanish 02 covers A2 everyday communication. Each stage has 800 cards in 20 ordered slices.

Source records are in `cards/es-MX/01.json` and `02.json`. Each matching file under `coverage/es-MX/` gives prerequisites, objectives, and hidden learning points. The canonical `answer` equals the unique `cloze` span; `accepted_answers` holds only additional equivalent variants, if any. `meaning` explains the target in English. Optional `note` fields give concise learner support.

Run the source-only checks with the installed Python 3 standard library:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 meiki_decks.py check --language es-MX --stage 01
PYTHONDONTWRITEBYTECODE=1 python3 meiki_decks.py check --language es-MX --stage 02
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v
PYTHONPYCACHEPREFIX=/tmp/meiki-decks-es-02/bytecode python3 -m py_compile meiki_decks.py test_meiki_decks.py
git diff --check
```

The checker validates the selected stage's source relationships and coverage, and reports repeated targets for editorial inspection. Spanish 02 also checks for full-sentence duplicates against accepted Spanish 01; the Spanish 01 command works independently. Editorial review assesses naturalness, teaching value, and broader redundancy. Audio paths are logical future filenames; no media files are required for authoring or CI.

## Meiki representation

The authoring array maps to one source note, one focused cloze, and one card per record. Ordered visible and cloze segments must reconstruct the unchanged sentence. Preserve source IDs; future app identities derive from locale, stage, and source ID.

Reserve deck ID `deck:es-MX:01`, name `Spanish 01 — A1 foundations`, and deck ID `deck:es-MX:02`, name `Spanish 02 — A2 everyday communication`. Both use language `es-MX`, direction `auto`, and matching `strict`. Preserve accepted stage 01 identities. English meanings and usage notes are representable as annotations/explanations.

The contract was checked against [`25d-228/meiki` at `2c15d09c3733011518a4218bc112d5ab16922d27`](https://github.com/25d-228/meiki/tree/2c15d09c3733011518a4218bc112d5ab16922d27), including domain entities, archive validation, clean-bundle export/import, portability documentation, and scheduler identifiers/defaults. Meiki supports version-4 clean language bundles and additive stage imports. Serialization, media, hashes, and pristine schedules belong to the later language-wide audio/bundle issue.

Complete and review Spanish content stages 01–06 before generating Spanish audio and its complete bundle. The orchestrator reviews and merges each content stage independently.
