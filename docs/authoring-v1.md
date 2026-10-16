# Source-authoring contract v1

This is an editorial JSON source contract. It does not implement or establish
`.meiki` archive serialization, production-import compatibility, scheduling,
recordings, or an exporter. Those require later verified contracts and assignments.

Spanish 01 uses an ordered UTF-8 JSON array at `cards/es-MX/01.json`: exactly 600
records, `es-01-0001` through `es-01-0600`. IDs and order are stable; repairs keep
the same intended objective. Conceptual deck identity is `deck:es-MX:01`, display
name **Spanish 01 — A1 foundations**. No archive objects are produced here.

| Required field | Meaning and constraint |
| --- | --- |
| `id` | Assigned nonempty unique ordered source ID. |
| `sentence` | Exact complete natural Spanish utterance; display and later synthesis use these same bytes. |
| `cloze` | One focused contiguous meaningful span appearing exactly once. |
| `answer` | Exactly equal to `cloze`. |
| `accepted_answers` | Array of nonempty strings, normally empty; only editorially verified valid alternatives. No duplicate or canonical duplication, automated synonyms, or accent stripping. |
| `lemma` | Dictionary form or compact fixed expression describing the actual hidden unit. |
| `meaning` | Concise English contextual meaning of that unit. |
| `part_of_speech` | Accurate whole-span grammatical label, including phrases when appropriate. |
| `audio` | Exact safe logical relative path `audio/<id>.mp3`; no recording-existence requirement. |

All required textual values are nonempty strings. The only optional fields are
nonempty useful `reading`, `grammar`, `register`, and `note` strings. Omit unused
fields. Reading, if present, must be independently verified for the exact hidden
form; Spanish 01 does not need phonetic respelling. Explain gender, complements,
inflection, and register where useful. Keep curriculum IDs and process bookkeeping
outside learner annotations.

Preserve NFC, accents, ordinary capitalization, single spacing, and paired Spanish
question/exclamation punctuation. Never rewrite display text to deduplicate it.
The checker diagnoses sentence duplicates after NFC/case folding/whitespace
comparison while preserving accents. Repeated answers are allowed for distinct
useful senses, functions, constructions, or contrasts, subject to editorial review.

Keep word/grapheme boundaries intact and boundary punctuation outside targets.
The checker counts overlapping exact substring occurrences, including occurrences
inside words. An intentional punctuation or morphological boundary target requires
useful `grammar` beginning `Boundary target: ` plus an explicit explanation and
editorial approval; this never permits a split combining mark. Spanish 01 uses
whole words and compact phrases. There is no arbitrary cloze-length limit:
editorial review rejects whole propositions or nearly entire predicates and
justifies compact fixed greetings with meaningful visible context.

## Coverage

`coverage/es-MX/01.md` records objectives, block budgets/prerequisites, primary
reference decisions, actual lexical/sense/construction breadth, and review evidence.
Its single mapping table lies between `<!-- cards:start -->` and
`<!-- cards:end -->`, with these exact columns:

`ID | Block | Hidden learning point | Guide | Situation / register | Role | Prerequisites | Kind | Review | Unresolved`

Each ID occurs once with all columns nonempty. Do not put literal pipe characters
inside cells. Block A is 0001–0070 (70), B 0071–0145 (75), C 0146–0230 (85),
D 0231–0315 (85), E 0316–0380 (65), F 0381–0450 (70), G 0451–0525 (75),
H 0526–0600 (75). Each row names the actual hidden sense/form/construction and a
Markdown link to the relevant subsection of `languages/es.md` pinned at
`e1d8239b7560f26b092cc7bb97c005738b34361f`. Context includes register and relevant
participants; role is `P` for Mexican-compatible production. Prerequisites cite
actual earlier IDs or explain an introductory frame. Kind is one of `sound`,
`lexical`, `grammar`, `function`, `construction`; visible exposure adds no second
primary count. After author/editor and final review, `Review` is `accepted` and
`Unresolved` is `none`; unresolved rows cannot pass completion validation.

The table records learning rather than duplicating all sentences or transcripts.
Block objectives and final inventory distinguish guide requirements, independently
verified language decisions, and authored lexical expansion. Card, lemma, sense,
construction, and incidental-exposure claims are separate. Counts do not prove
exhaustive vocabulary knowledge or learner proficiency.

## Text-only checks

Use the installed Python 3 standard library, without dependency installations:

```sh
python3 -B scripts/check_source.py --locale es-MX --stage 01 --expected-count 600
python3 -B -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

The current CLI deliberately supports only this assigned locale/stage/count.
`--root <directory>` permits isolated fixtures. It rejects malformed JSON,
duplicate object keys, bad fields/types/empty values, invalid alternatives,
incorrect order/count/IDs, duplicate sentences, non-NFC text, mismatched or
repeated clozes, detectable boundary/punctuation defects, incorrect logical audio
paths, and incomplete/duplicate/out-of-range/misallocated coverage. Findings name
the affected ID/field and report actual count/range. Naturalness, genuine
alternative validity, curricular breadth, and contextual cloze focus remain
explicit editorial judgments; passing code does not certify them.

During ingestion, reuse `check_records(new_records, expected_count, first)` only
for new/changed consecutive records, plus comparisons with accepted inventory.
After the complete final pass, run one consolidated completion check and compute
SHA-256 of final source/coverage bytes. Focused fixtures exercise failure cases
and successful validation with no MP3s. Source CI uses hosted Ubuntu's existing
Python, runs fixtures and complete source validation, and needs no models, audio,
server, app, or exporter. Scratch/caches belong in `/tmp/meiki-decks-es-01/`.
