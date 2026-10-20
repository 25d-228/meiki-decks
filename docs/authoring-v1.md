# Source-authoring contract v1

This is an editorial JSON source contract. It does not implement or establish
`.meiki` archive serialization, production-import compatibility, scheduling,
recordings, or an exporter. Those require later verified contracts and assignments.

Spanish 01 uses an ordered UTF-8 JSON array at `cards/es-MX/01.json`: exactly 600
records, `es-01-0001` through `es-01-0600`. IDs and order are stable; repairs keep
the same intended objective. Conceptual deck identity is `deck:es-MX:01`, display
name **Spanish 01 — A1 foundations**. No archive objects are produced here.

Spanish 02 extends the same contract at `cards/es-MX/02.json`: exactly 800
records, `es-02-0001` through `es-02-0800`, conceptual deck `deck:es-MX:02`,
display name **Spanish 02 — A2 everyday communication**. Accepted Spanish 01
source and coverage remain unchanged; stage 02 adds new learning and uses their
actual earlier cards as prerequisites.

Spanish 03 adds exactly 1,000 ordered records at `cards/es-MX/03.json`,
`es-03-0001`–`es-03-1000`, conceptual deck `deck:es-MX:03`, display name
**Spanish 03 — B1 independent communication**. Accepted 01/02 source and coverage
remain unchanged; actual earlier learning supports the new stage.

Spanish 04 adds exactly 1,200 ordered records at `cards/es-MX/04.json`,
`es-04-0001`–`es-04-1200`, conceptual deck `deck:es-MX:04`, display name
**Spanish 04 — B2 extended communication**. Accepted 01–03 source and coverage
remain unchanged; use their actual senses/constructions as prerequisite evidence.

Spanish 05 adds exactly 1,400 ordered records at `cards/es-MX/05.json`,
`es-05-0001`–`es-05-1400`, conceptual deck `deck:es-MX:05`, display name
**Spanish 05 — C1 precise communication**. Preserve accepted 01–04 source/coverage
and distinguish their actual hidden objectives from visible supporting language.

Spanish 06 adds exactly 1,600 ordered records at `cards/es-MX/06.json`,
`es-06-0001`–`es-06-1600`, conceptual deck `deck:es-MX:06`, display name
**Spanish 06 — C2 precision, rhetoric, and mediation**. Preserve accepted 01–05
source/coverage and identify genuinely new hidden learning.

Spanish 07 adds exactly 1,000 ordered records at `cards/es-MX/07.json`,
`es-07-0001`–`es-07-1000`, conceptual deck `deck:es-MX:07`, display name
**Spanish 07 — Regional, social, professional, and cultural depth**. Preserve
accepted 01–06. Coverage 07 includes the separate whole-Spanish seven-stage,
7,600-card substantive reconciliation without repeating predecessor audits.

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

`coverage/es-MX/01.md`, `coverage/es-MX/02.md`, `coverage/es-MX/03.md`,
`coverage/es-MX/04.md`, `coverage/es-MX/05.md`, `coverage/es-MX/06.md`, and
`coverage/es-MX/07.md` record objectives, block
budgets/prerequisites, primary reference decisions, actual lexical/sense/construction breadth, and review evidence.
Each single mapping table lies between `<!-- cards:start -->` and
`<!-- cards:end -->`, with these exact columns:

`ID | Block | Hidden learning point | Guide | Situation / register | Role | Prerequisites | Kind | Review | Unresolved`

Each ID occurs once with all columns nonempty. Do not put literal pipe characters
inside cells. Block A is 0001–0070 (70), B 0071–0145 (75), C 0146–0230 (85),
D 0231–0315 (85), E 0316–0380 (65), F 0381–0450 (70), G 0451–0525 (75),
H 0526–0600 (75) for Spanish 01. Spanish 02 allocates A 0001–0150 (150),
B 0151–0260 (110), C 0261–0350 (90), D 0351–0450 (100), E 0451–0530 (80),
F 0531–0620 (90), G 0621–0700 (80), H 0701–0800 (100). Spanish 03 allocates A 0001–0150 (150),
B 0151–0290 (140), C 0291–0430 (140), D 0431–0560 (130), E 0561–0680 (120),
F 0681–0780 (100), G 0781–0900 (120), H 0901–1000 (100). Spanish 04 allocates
A 0001–0180 (180), B 0181–0340 (160), C 0341–0490 (150), D 0491–0630 (140),
E 0631–0770 (140), F 0771–0900 (130), G 0901–1070 (170), H 1071–1200 (130).
Spanish 05 allocates
A 0001–0240 (240), B 0241–0420 (180), C 0421–0610 (190), D 0611–0790 (180),
E 0791–0960 (170), F 0961–1110 (150), G 1111–1270 (160), H 1271–1400 (130).
Spanish 06 allocates
A 0001–0240 (240), B 0241–0460 (220), C 0461–0680 (220), D 0681–0880 (200),
E 0881–1070 (190), F 1071–1240 (170), G 1241–1430 (190), H 1431–1600 (170).
Spanish 07 allocates A 0001–0170 (170), B 0171–0340 (170), C 0341–0500 (160),
D 0501–0640 (140), E 0641–0770 (130), F 0771–0890 (120), G 0891–1000 (110).
Each row names the actual
hidden sense/form/construction and a Markdown link to the relevant subsection of `languages/es.md` pinned at
`e1d8239b7560f26b092cc7bb97c005738b34361f`. Context includes register and relevant
participants; role is `P` for Mexican-compatible production. Stage 03 also
permits `R` in blocks A/H, with explicit Spain, Colombia or River Plate attribution
in Situation / register; the ordinary table records recognition without adding a
study mode. Stages 04/05 allow `R` only in H, with explicit Spain/Colombia/River Plate
attribution for regional recognition or `Source/register:` followed by the actual
marked source/register in Situation / register. Editorial review verifies the
claimed attribution and coherent response; a label alone is not language evidence.
Stage 06 permits `R` only in G, with explicit Spain/Colombia/River Plate
attribution or `Source/register:` followed by the actual marked regional,
generational-context or nonstandard source/register and its limitation. Merely
naming a generation or participant age does not verify usage. A–F and H remain P.
Stage 07 permits `R` only in D/G, always with explicit `Source/register:`
attribution: an actual attributed cultural reference in D, or the actual
regional/marked source in G. A/B/C/E/F remain P. Semantic attribution and its
verified scope remain editorial judgments. Section 6.8 uses pinned anchor
`68-domain-specific-near-native-command`.
Stages 01/02 remain production-only. Prerequisites cite
actual earlier IDs or explain an introductory frame. Stage 02 permits valid
accepted `es-01-0001`–`es-01-0600` and earlier stage-02 IDs. Stage 03 permits
those accepted 01 IDs, accepted `es-02-0001`–`es-02-0800`, and strictly earlier
stage-03 IDs. Stage 04 additionally permits accepted `es-03-0001`–`es-03-1000`
and strictly earlier stage-04 IDs. Stage 05 also permits accepted
`es-04-0001`–`es-04-1200` and strictly earlier stage-05 IDs. Stage 06 additionally
permits accepted `es-05-0001`–`es-05-1400` and strictly earlier stage-06 IDs.
Stage 07 additionally permits accepted `es-06-0001`–`es-06-1600` and strictly
earlier stage-07 IDs. Unknown, malformed, self,
forward and later-stage references are rejected. Kind is one of `sound`,
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
python3 -B scripts/check_source.py --locale es-MX --stage 02 --expected-count 800
python3 -B scripts/check_source.py --locale es-MX --stage 03 --expected-count 1000
python3 -B scripts/check_source.py --locale es-MX --stage 04 --expected-count 1200
python3 -B scripts/check_source.py --locale es-MX --stage 05 --expected-count 1400
python3 -B scripts/check_source.py --locale es-MX --stage 06 --expected-count 1600
python3 -B scripts/check_source.py --locale es-MX --stage 07 --expected-count 1000
python3 -B -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

The CLI supports only `es-MX` stages 01/600, 02/800, 03/1000, 04/1200, 05/1400,
06/1600 and 07/1000.
Stage 02 also loads accepted 01 for duplicate IDs and full sentences; stage 03
compares against both accepted stages, stage 04 against all three predecessors,
stage 05 against all four, stage 06 against all five, and stage 07 against all six predecessors,
using the same conservative normalization. Each earlier stage remains usable
without later-stage files. No recording bytes are required.
`--root <directory>` permits isolated fixtures. It rejects malformed JSON,
duplicate object keys, bad fields/types/empty values, invalid alternatives,
incorrect order/count/IDs, duplicate sentences, non-NFC text, mismatched or
repeated clozes, detectable boundary/punctuation defects, incorrect logical audio
paths, and incomplete/duplicate/out-of-range/misallocated coverage. Findings name
the affected ID/field and report actual count/range. Naturalness, genuine
alternative validity, curricular breadth, and contextual cloze focus remain
explicit editorial judgments; passing code does not certify them.

During ingestion, reuse `check_records(new_records, expected_count, first, stage="07")`
for new/changed consecutive 07 records (use the actual stage for 02–06; omit for 01), plus
incremental comparisons with actual accepted inventory in all preceding Spanish stages.
After the complete final pass, run one consolidated completion check and compute
SHA-256 of final source/coverage bytes. Focused fixtures exercise failure cases
and successful validation with no MP3s. Source CI uses hosted Ubuntu's existing
Python, runs fixtures and complete source validation, and needs no models, audio,
server, app, or exporter. Scratch/caches belong in the assigned stage’s local
`/tmp` directory; Spanish 07 and current fixtures use `/tmp/meiki-decks-es-07/`.
