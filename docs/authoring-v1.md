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

Chinese 00 adds exactly 200 ordered records at `cards/zh-Hans-CN/00.json`,
`zh-00-0001`–`zh-00-0200`, conceptual deck `deck:zh-Hans-CN:00`, display name
**Chinese 00 — Sound, characters, and sentence foundations**. It starts with no
prior Chinese; accepted Spanish is a project dependency, not a learner prerequisite.
All 200 targets are Simplified production in standard spoken Chinese (Putonghua).
There are no recording or application prerequisites.

Chinese 01 adds exactly 400 ordered records at `cards/zh-Hans-CN/01.json`,
`zh-01-0001`–`zh-01-0400`, conceptual deck `deck:zh-Hans-CN:01`, display name
**Chinese 01 — Band 1-oriented basic communication**. All 400 are Simplified
production. Accepted Chinese 00 supplies actual prerequisites; distinguish its
hidden targets from merely visible support when identifying new learning.
Chinese source reaches 600 cards; counts do not establish substantive acceptance.

Chinese 02 adds exactly 600 ordered records at `cards/zh-Hans-CN/02.json`,
`zh-02-0001`–`zh-02-0600`, conceptual deck `deck:zh-Hans-CN:02`, display name
**Chinese 02 — Band 2-oriented routine communication**. All are Simplified
production in standard spoken Chinese (Putonghua), following accepted 00–01.
Chinese source reaches 1,200 cards/maps. Actual new learning, aspect interpretation,
complement constraints and practical breadth remain separate acceptance criteria.

Chinese 03 adds exactly 800 ordered records at `cards/zh-Hans-CN/03.json`,
`zh-03-0001`–`zh-03-0800`, conceptual deck `deck:zh-Hans-CN:03`, display name
**Chinese 03 — Band 3-oriented independent communication**. All are Simplified
production in standard spoken Chinese (Putonghua), following accepted 00–02.
Delivered Chinese source reaches 2,000 records/maps. Common result and extended
directional complements, affected/passive/potential frames, reference, stance,
clause relations and register need actual hidden retrieval and editorial review.

Chinese 04 adds exactly 1,000 ordered records at `cards/zh-Hans-CN/04.json`,
`zh-04-0001`–`zh-04-1000`, deck `deck:zh-Hans-CN:04`, display name
**Chinese 04 — Band 4-oriented extended communication**. All are Simplified
production in standard spoken Chinese (Putonghua), following accepted 00–03;
delivered Chinese text reaches 3,000 records/maps. The guide supplies a functional
emphasis, not an exhaustive official Band 4 grammar/vocabulary list. The selected
lexical, narrative, discussion, source-comparison, register and pronunciation-aware
extensions are authored curriculum choices whose real learning must be reviewed.

| Required field | Meaning and constraint |
| --- | --- |
| `id` | Assigned nonempty unique ordered source ID. |
| `sentence` | Exact complete natural target-language utterance; display and later synthesis use these same bytes. |
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

Preserve NFC, accents, ordinary capitalization, and single spacing. Spanish requires
paired question/exclamation punctuation; Chinese allows ordinary `？` and `！`
and unspaced Han text. Never rewrite display text to deduplicate it.
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

Chinese 00–04 require a nonempty `reading` on every card: complete tone-marked
Pinyin of exactly the hidden span, with lexical tones, normal word segmentation,
unmarked neutral syllables, and the actual contextual reading of polyphonic words.
Do not silently replace lexical tones with connected-speech tones. Explain useful
third-tone or 一/不 changes separately in a clearly labeled `note` or `grammar`,
using the conditions in the actual sentence. Verify every syllable editorially;
the checker verifies presence and string integrity, not Pinyin accuracy.
Typed answers retain ordinary Simplified spelling, with no Pinyin alternatives,
automatic script conversion or accent stripping. Meaning covers the hidden unit;
lemma and part of speech describe the whole unit.

Han adjacency is valid and does not require a boundary override. A single-character
word or grammatical unit may be meaningful; an arbitrary substring of a compound
is not. Deliberate morphemic targets need explicit linguistic justification and
review. Chinese retains cloze occurrence, combining-mark and punctuation safety;
semantic word identity and Simplified usage require editorial review. The checker
does not infer them from a tokenizer or character conversion. Spanish alphabetic
word-boundary and inverted-punctuation checks remain unchanged.

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

The supported Spanish pairs are `es-MX` stages 01/600, 02/800, 03/1000,
04/1200, 05/1400, 06/1600 and 07/1000.
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

Chinese 00 coverage is `coverage/zh-Hans-CN/00.md`, using the same ten columns
and markers. Its fixed blocks are A 0001–0030 (30), B 0031–0065 (35),
C 0066–0100 (35), D 0101–0130 (30), E 0131–0155 (25),
F 0156–0180 (25), and G 0181–0200 (20). Every row has role `P`, links to an
actual subsection of `languages/zh.md` at the same pinned guide commit, and cites
strictly earlier `zh-00` IDs or explains newly introduced beginner support.
Malformed, self, forward, later-stage and other-language IDs are rejected.
The coverage introduction maps both sides of every required sound contrast and
the tone, sandhi, weak-syllable, prominence/grouping and basic function objectives
to actual hidden targets. Report cards, target lemmas/expressions/senses, direct
target characters and incidental character exposure separately, with methods.
These are exposure/retrieval measures, not handwriting or proficiency evidence.

Chinese 01 coverage is `coverage/zh-Hans-CN/01.md`, using the same table contract.
Its exact blocks are A 0001–0065 (65), B 0066–0125 (60), C 0126–0175 (50),
D 0176–0230 (55), E 0231–0280 (50), F 0281–0335 (55), G 0336–0400 (65).
All rows follow source-ID order, are P and use pinned Chinese links, including
`62-basic-communication`. Chinese 00 retains its foundation guide-anchor scope.
Prerequisites may cite accepted `zh-00-0001`–`zh-00-0200` and strictly earlier
`zh-01` IDs; invalid bounds, self/forward, malformed, cross-language and later-stage
references fail. The introduction reconciles the entire §6.2 inventory to actual
hidden IDs, progression, lexical breadth and direct versus incidental characters.
Count exact target strings, lemmas and operational lemma/meaning pairs separately;
none is a certified linguistic sense inventory or completed proficiency measure.
The guide's character/word/handwriting landmarks are separate from these counts.

Chinese 02 coverage is `coverage/zh-Hans-CN/02.md`, with the same ordered table.
Its exact blocks are A 0001–0110 (110), B 0111–0205 (95), C 0206–0290 (85),
D 0291–0370 (80), E 0371–0445 (75), F 0446–0520 (75), G 0521–0600 (80).
All 600 rows are P, using pinned Chinese links including `63-routine-communication`
and applicable shared headings; the earlier stages retain their anchor scopes.
Dependencies may cite valid accepted 00/01 IDs and strictly earlier 02 IDs.
Reconcile every §6.3 family and contrast to actual hidden IDs: completion versus
change versus experience, progressive versus durative, result/literal directional/
degree complements, comparison and measures, relatives/conjunctions, introductory
把, double-object and pivotal frames, and practical lexical/problem-solving breadth.
Visible grammar is not a second hidden objective. Retain lexical tones while using
actual neutral grammatical readings (`le`, `guo`, `zhe`), not character defaults.
The 600 new/1,200 cumulative records, exact targets/lemmas/operational sense pairs
and direct versus incidental characters need explicit methods and limits. The
guide's approximately 600 recognized characters, 1,270 words/phrases and 200
handwritten characters are separate landmarks, not quotas or attainment evidence.

Chinese 03 coverage is `coverage/zh-Hans-CN/03.md`, using the same ordered table.
Its exact blocks are A 0001–0130 (130), B 0131–0245 (115), C 0246–0355 (110),
D 0356–0460 (105), E 0461–0560 (100), F 0561–0680 (120), G 0681–0800 (120).
All 800 rows are P and link to pinned `64-independent-communication` or shared
Chinese system headings. Earlier-stage §6.1–6.3 headings are outside 03's scope;
00–02 keep their existing anchor scopes.
Dependencies may cite valid accepted 00/01/02 IDs and strictly earlier 03 IDs.
Reconcile each §6.4 family and important contrast to actual hidden IDs: common
result and literal/extended directional complements with lexical constraints and
viewpoint; 把, 被 and potential with agency/result/nonoccurrence distinctions;
complex modification and topic–comment with recoverable reference; rhetorical
questions and sentence-final stance; conditional/concessive/causal/purpose
relations; formal/conversational alternatives and basic discourse organization.
Broaden useful lexical senses, original narration, explanation and repair without
counting visible grammar twice. Keep source evidence and social context inside
the sentence where interpretation needs them. Report 800 new/2,000 cumulative
records/maps, exact targets/lemmas/operational lemma-meaning pairs and distinct
direct/visible/incidental-only Han sets with explicit methods. The guide's
approximately 900 recognized characters, 2,245 words/phrases and 300 handwritten
characters are separate landmarks, not replacement quotas or demonstrated skills.

Chinese 04 coverage is `coverage/zh-Hans-CN/04.md`, with exact allocations
A 0001–0190 (190), B 0191–0340 (150), C 0341–0480 (140), D 0481–0630 (150),
E 0631–0760 (130), F 0761–0880 (120), G 0881–1000 (120), all P. Link pinned
`65-upper-intermediate-operation` or appropriate shared system headings;
§6.1–6.4 and later milestone anchors are outside 04's scope. Earlier stages keep
their existing scopes. Prerequisites may cite valid accepted 00/01/02/03 IDs or
strictly earlier 04 IDs. Compare duplicate IDs/full sentences with each of all
four predecessor sources, without their coverage, Spanish files or recordings;
each earlier stage remains independent of later files.

Reconcile every §6.5 functional area and each block's actual contrast to hidden
IDs/ranges, separating guide emphasis from authored extensions: substantive
lexical senses/collocations, aspect/complement narration and description, argument
and topic continuity, original source comparison with attribution and evidence
limits, meaningful formal/informal reformulation, pronunciation/discourse choices
and broad adult-life/service/cultural/intellectual description. Actual Chinese
must establish participants, reference, scope and any prominence interpretation;
back-side support cannot invent roles, ownership, sources or missing context.
Report 1,000 new/3,000 cumulative cards/maps, exact target/lemma/operational pairs,
direct/sentence/visible/incidental-only Han sets with explicit methods and limits.
The guide's approximately 1,200–1,500 recognized characters, 3,200–4,300
words/phrases and 400–500 handwritten characters are separate working landmarks;
its stated Band 5 overlap is not a newly certified examination inventory or
attained proficiency. No final ten-stage reconciliation is implied.

The supported Chinese commands are:

```sh
python3 -B scripts/check_source.py --locale zh-Hans-CN --stage 00 --expected-count 200
python3 -B scripts/check_source.py --locale zh-Hans-CN --stage 01 --expected-count 400
python3 -B scripts/check_source.py --locale zh-Hans-CN --stage 02 --expected-count 600
python3 -B scripts/check_source.py --locale zh-Hans-CN --stage 03 --expected-count 800
python3 -B scripts/check_source.py --locale zh-Hans-CN --stage 04 --expected-count 1000
```

Chinese supports only `zh-Hans-CN/00/200`, `zh-Hans-CN/01/400`,
`zh-Hans-CN/02/600`, `zh-Hans-CN/03/800` and `zh-Hans-CN/04/1000` alongside the Spanish pairs above.
Chinese 00 needs no later
files. Chinese 01 loads accepted
Chinese 00 source for conservative duplicate-ID/full-sentence diagnostics, but
needs no predecessor coverage, Spanish files or recordings. Spanish commands
remain independent of Chinese. Chinese 02 compares duplicate IDs/full sentences
with both accepted 00 and 01 sources, without their coverage, Spanish or media;
01 remains independent of 02. Chinese 03 compares against each of all three
accepted predecessor sources without their coverage, Spanish or media; 00–02
remain independent of 03. Other locale/stage/count combinations fail.
No semantic tokenizer, Pinyin converter or Simplified conversion is introduced;
Pinyin accuracy, genuine novelty, semantic boundaries and naturalness remain
editorial judgments.
During Chinese ingestion use
`check_records(new_records, count, first, stage="03", locale="zh-Hans-CN")`
(use the actual `stage="00"`, `stage="01"` or `stage="02"` for earlier Chinese)
plus incremental duplicate and mapping checks. After final review run the one
consolidated Chinese validation and preservation check; use focused Chinese
fixtures locally and exact-head CI for the complete repository suite. The focused
Chinese 01 class is available as:

```sh
python3 -B -m unittest discover -s tests -p test_chinese_source.py -k ChineseStage01Tests
```

Normal source CI retains all accepted fixtures and eight accepted real-stage
commands, adding Chinese 01/400 as the ninth. Do not duplicate that whole suite
locally. Chinese 01 normally uses ten sequential fresh author/editor pairs and
one exhaustive 400-record final pass, followed by affected corrections and one
consolidated completion check.

Chinese 02's focused class command is:

```sh
python3 -B -m unittest discover -s tests -p test_chinese_source.py -k ChineseStage02Tests
```

Normal source CI retains all existing fixture methods and nine accepted real-stage
commands, adding Chinese 02/600 as the tenth. The former unsupported-pair fixture
now uses 05/1000 because 02/600, 03/800 and 04/1000 are implemented. Chinese 02 normally uses fifteen
sequential fresh author/editor pairs and one exhaustive final pass in consecutive
0001–0400 and 0401–0600 partitions. Apply verified findings together, check affected
records, then run focused implementation tests and one consolidated completion
check including both predecessors' duplicate diagnostics and 29 protected files.
Reserve the full repository suite for normal final-head CI.

Chinese 03's focused class command is:

```sh
python3 -B -m unittest discover -s tests -p test_chinese_source.py -k ChineseStage03Tests
```

Its scoped fixtures append to the 99 existing methods and exercise independently
transcribed block endpoints, prior/current dependency bounds, source/mapping
integrity, isolated media-free success, failures from each of the three prior
sources and earlier-stage independence/anchor scope. Only obsolete unsupported
03/800 cases were first moved to 04/1000; Chinese 04 now moves those examples
to unsupported 05/1000. Normal CI retains the full fixture
suite and ten accepted stage commands, adding Chinese 03/800 as the eleventh.
Do not duplicate the full workflow locally. Normally use twenty sequential fresh
author/editor pairs, then one exhaustive final pass in consecutive 0001–0400 and
0401–0800 partitions. Before every launch verify actual prior ingestion, complete
required context and explicit resolution of editor limitations; exit 0 alone is
not structured completion. Apply final corrections together, inspect affected
records, then run focused tests and one consolidated source/coverage/count/order/
allocation/dependency/all-three-predecessor-duplicate/31-file preservation check.
Keep the Spanish fixture module unchanged in addition to the protected files.
Preflight actual prompt plus schema in characters and UTF-16 units; reversible
field tables must preserve every value and optional-field presence. Keep raw
prompts, outputs and diagnostics local under `/tmp`, outside source records.

Chinese 04's focused local command is:

```sh
python3 -B -m unittest discover -s tests -p test_chinese_source.py -k ChineseStage04Tests
```

Its fixtures independently transcribe all seven allocations, cover all block
endpoints, strict prior/current dependencies, source/mapping integrity and retained
invariants, isolated source-only success, missing/duplicate failures from each of
four predecessors, and earlier-stage independence/anchor scopes. Keep all 114
existing fixture methods; only the three obsolete Chinese 04/1000 unsupported
examples in the Stage01/02/03 classes become unsupported 05/1000. New fixture
sentences use a distinct deterministic prefix. CI retains eleven accepted real
stage commands and adds Chinese 04 as the twelfth; reserve the full suite for
normal final-head CI.

Use `check_records(new_records, count, first, stage="04", locale="zh-Hans-CN")`
with lightweight new/changed mapping, dependency and incremental duplicate checks
during ingestion. Normally use 25 fresh Sol 6.1 author/editor pairs, then one
exhaustive final pass over consecutive 0001–0400, 0401–0800, 0801–1000. Each
assigned record/map is complete; retain full relevant dependency/contrast records,
accepted hidden inventory and the full reconciliation. Verify actual prior
ingestion, all ten mapping columns and resolved limitations before every launch.
Preflight actual prompt plus schema in characters and UTF-16 units, retaining
all field values and optional presence in reversible tables; subdivide only still
pending ranges if capacity requires it. Apply verified final corrections together,
inspect affected records/dependent mappings, then run focused implementation
tests and one consolidated source/count/order/coverage/allocation/dependency/
all-four-predecessor-duplicate/33-file preservation check plus syntax/whitespace.
Keep Spanish tests unchanged, reuse valid unchanged evidence, and compute each
final new-file SHA-256 once before index/commit byte comparisons.

During ingestion, reuse `check_records(new_records, expected_count, first, stage="07")`
for new/changed consecutive 07 records (use the actual stage for 02–06; omit for 01), plus
incremental comparisons with actual accepted inventory in all preceding Spanish stages.
After the complete final pass, run one consolidated completion check and compute
SHA-256 of final source/coverage bytes. Focused fixtures exercise failure cases
and successful validation with no MP3s. Source CI uses hosted Ubuntu's existing
Python, runs fixtures and complete source validation, and needs no models, audio,
server, app, or exporter. Scratch/caches belong in the assigned stage’s local
`/tmp` directory. Chinese 00 and its fixtures use `/tmp/meiki-decks-zh-00/`;
Chinese 01 and its new fixtures use `/tmp/meiki-decks-zh-01/`;
Chinese 02 and its new fixtures use `/tmp/meiki-decks-zh-02/`;
Chinese 03 and its new fixtures use `/tmp/meiki-decks-zh-03/`;
Chinese 04 and its new fixtures use `/tmp/meiki-decks-zh-04/`;
unchanged Spanish fixtures retain `/tmp/meiki-decks-es-07/`.
