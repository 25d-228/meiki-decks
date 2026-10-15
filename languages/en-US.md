# American English: sentence and card authoring guide

**Production locale:** `en-US`  
**Scope:** A1–C2-oriented American English, followed by professional, social, and cultural specialization.

## 1. Purpose and required deliverables

**Fixed deliverable: 7 stages; 9,000 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The finished card shows the sentence with that span hidden, provides typed input and the **full-sentence recording on the front**, and reveals the sentence, answer, concise support, and replay on the back. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records, synchronized coverage mappings, and editorial evidence. **Complete and accept all text for all nine project languages before producing any audio.** For this language, finish every planned sentence, cloze, answer, annotation, reading, and coverage mapping, then complete editorial review, corrections, and source checks. Acceptance of this language's text permits the next language's text work, not audio generation. The pronunciation sections describe written sentence/reading requirements and the subsequent audio phase; no representative recordings, auditions, synthesis tests, or denoising runs belong to the text phase. This guide defines authoring scope; it does not certify a learner’s proficiency.

---

## 2. Production model, script, and register

Use **contemporary American English (`en-US`)** with a coherent rhotic pronunciation model and ordinary American spelling and vocabulary. The source names **color, center, traveling** as convention examples. Use clear conversational speech, not an exaggerated announcer or fictional character voice.

Broaden recognition of American regions, communities, generations, other national varieties, and internationally accented English where relevant. Do not label another variety wrong merely because it is outside the production model. Select actual sound and usage conventions rather than assembling an accent from unrelated features.

---

## 3. Curriculum framework and limits of card evidence

Keep the supplied **A2 Key → B1 Preliminary → B2 First → C1 Advanced → C2 Proficiency** reference route. The A1 milestone is a functional beginner scope, not an examination added to that sequence. Maintain American production conventions without claiming every examination requires an American accent.

The source distinguishes language proficiency, pronunciation, professional performance, and community participation. Cards support their language components; they do not establish admission-test compliance, a certificate, or near-native identity. Use current test rules only when a specific examination task is separately authorized and verified.

---

## 4. Prerequisites and whole-language coverage

Messages written by the person may be headed simply **HUMAN**. Treat them as HUMAN instructions for the receiving agent; a recipient suffix is unnecessary. Keep both agents’ HUMAN-facing messages and forwarded handoffs short, and keep plans/issues specific and detailed.

After HUMAN approves starting, ORCHESTRATOR first publishes all nine supplied authoring guides together to the repository's `main` branch under `languages/`, preserving their contents. This reference-only publication precedes writing plan issues. ORCHESTRATOR then writes **one roadmap issue and nine language-plan issues—one per language, ten planning issues in total**—using the committed guides as references. Each language-plan issue links to its guide at the recorded commit and relevant headings. Complete every language's all-stage text plan and later audio/bundle plan before the first executor generation handoff.

For this language, its own language-plan issue must preserve the exact stage IDs, names, card counts, and total in Section 4.1, as well as the complete milestone inventories, sentence/cloze requirements, support fields, prerequisites, scope boundaries, and completion criteria for every stage. Do not use issue writing to select a shorter curriculum or reduce production quantities. A stage title or ‘details later’ is not enough. The roadmap links the nine plans and tracks project order; it does not replace their detailed specifications. The executor follows the assigned execution issue, the already-written language-plan section, and the pinned repository guide, then adds actual card IDs to its coverage inventory as work proceeds. Execution issues are bounded assignments created when needed, not substitutes for the complete upfront plans. For each objective, identify the prior language needed to understand the visible context; do not make every difficult word a new target at once, depend silently on a later stage, or count visible exposure as taught retrieval.

Use a small coverage table outside learner records:

| Inventory item | Required information |
|---|---|
| Identity | Stable objective ID and the relevant guide subsection |
| Learning point | Exact sense, form, construction, or pragmatic distinction |
| Context | Situation, register, production/recognition role, and necessary participants |
| Prerequisites | Earlier targets needed for the sentence and its interpretation |
| Evidence | Authored card IDs, review result, and any unresolved requirement |

Count cards, lemmas, senses, constructions, and incidental exposure separately; add script-specific measures where the language requires them. **The fixed production schedule below defines the exact stage counts and total.** Coverage planning must fill that schedule with the guide’s complete teachable scope, not recalculate a smaller collection from a short selection. A matching card total alone does not prove lexical breadth or proficiency; track those claims separately.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **7 stages and exactly 9,000 accepted cards** for American English, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, audio files, or reverse cards as additional cards.

**Allocation basis:** Sound–spelling and sentence foundations are integrated into A1. The progression reserves broad space for lexical senses, auxiliary/article systems, tense/aspect, complement and phrasal-verb patterns, collocations, register, and rhetoric, plus a separate community/domain stage. The quantities are not inferred from an English-speaking learner’s study-hour estimates for another language.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `01` | American English 01 — A1 foundations | Sections 6.1–6.2 | 800 | 20 | 800 |
| `02` | American English 02 — A2 everyday communication | Sections 6.3 | 1,000 | 25 | 1,800 |
| `03` | American English 03 — B1 independent communication | Sections 6.4 | 1,200 | 30 | 3,000 |
| `04` | American English 04 — B2 extended communication | Sections 6.5 | 1,400 | 35 | 4,400 |
| `05` | American English 05 — C1 precise communication | Sections 6.6 | 1,600 | 40 | 6,000 |
| `06` | American English 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,800 | 45 | 7,800 |
| `07` | American English 07 — American social, professional, and cultural depth | Sections 6.8 | 1,200 | 30 | 9,000 |
| **Total** | **7 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **9,000** | **225** | **9,000** |

Use source IDs `en-US-<stage>-0001` through `en-US-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `en-US`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends on the preceding stages of this language, not on knowledge of another project language.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. A different approved batch split must still sum to the same stage count and must not introduce per-batch commits or full test runs.

#### Required distribution across stages

- **Stage 01:** Integrate sound/spelling, stress, contractions, be/have, articles/number, pronouns, present frames, do questions, basic modals/plans, and everyday vocabulary.
- **Stage 02:** Cover past and progressive frames, future arrangements, comparison/quantity, modals, infinitive/ing complements, basic relatives, present perfect, and routine practical language.
- **Stage 03:** Cover past/perfect and narrative contrasts, conditionals, passive/reporting, relatives/questions, phrasal/prepositional verbs, and wider explanation and social language.
- **Stage 04:** Develop article/reference precision, tense/aspect, modal/conditional contrasts, participial structures, collocations, hedging, reformulation, and genre/register variety.
- **Stage 05:** Cover substantial lexical/collocational breadth, source synthesis, implied stance, qualification, register switching, professional explanation, and multi-party interaction language.
- **Stage 06:** Cover subtle grammar/sense choices, argument reconstruction, rhetoric, idioms, irony, understatement, editing, cultural interpretation, and turn recovery.
- **Stage 07:** Develop distinct community/domain senses, conventions, negotiation, humor, relationships, professional responsibilities, and cultural discussion without reducing American use to accent.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**Neither agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when both conditions hold: **its exact accepted-card count is met and its complete allocated coverage passes review**. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Build the complete beginner-to-advanced series without assuming all learners are beginners or that advanced readers control articles, auxiliaries, spoken segmentation, and register. Record those prerequisites separately rather than suppressing foundation content for everyone.

English is both a target language and the project’s support language. Use short plain-English definitions or paraphrases that are easier than the target. Avoid tautologies such as **important = important** and avoid a difficult definition that makes a beginner card harder than its sentence.

---

## 5. Essential systems to represent in sentences

### Sound, stress, and spelling
Connect words to verified American audio, lexical stress, phrase prominence, and meaning. The source’s **PHOtograph → phoTOGraphy → photoGRAPHic** family illustrates stress changes to check separately. Study schwa, weak forms, linking, and connected-speech changes without claiming every unstressed vowel becomes schwa or respelling reductions as ordinary writing.

### Articles and countability
Plan reference and countability together: **a report**, **the report we discussed**, general **reports**, and **some information/a piece of information** are different contextual patterns. Do not assign a permanent article to an English noun. Add plural/noncount behavior and a useful collocation in support.

### Auxiliaries and clause frames
Distinguish statement, direct question, negation, past question, modal question, embedded question, subject question, and object question. Do not insert **do** into every interrogative or invert every embedded question.

### Tense, aspect, and American usage
Use routine/current job, temporary arrangement, finished past period, continuing situation, interrupted activity, and anterior event contexts. Compare simple past and present perfect, including source-listed American uses with **already/yet**, without removing present perfect. Distinguish **get–got–gotten**, development with **gotten**, possession with **have got**, and expressions such as **on the weekend** and **Monday through Friday**. Verify contextual use rather than replacing every **got** mechanically.

### Complements and multiword verbs
Plan **explain something to someone, discuss a problem, depend on, avoid doing, want someone to do, look forward to doing**. For multiword verbs, record meaning, object behavior, pronoun placement, and register: **look up the address/look the address up/look it up**, **look into**, and **put up with** are not the same syntactic pattern.

### Social purpose
Specify urgency, authority, familiarity, and tone in requests, refusals, feedback, and disagreement. Do not apply a blanket “Americans are direct” rule or a universal politeness ranking based on sentence length.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **editorial test** are authoring adaptations. They replace learner promotion tests with checks on the created content.

### 6.1. Foundation

**Curriculum reference:** Sound–spelling and sentence foundation

#### Required language and situation inventory

Select essential vowel and consonant contrasts from the prerequisite analysis, word stress, /r/, /l/, /w/, /v/, the two th sounds, final consonants, contractions, and phrase grouping. Include identity, numbers, prices, clarification requests, and basic be, have, and present-tense frames.

#### Authoring brief

**Sentence contexts:** Identity, spelling essential information, numbers, prices, questions, clarification, and basic be/have frames.

**Focused hidden targets:** A short word, auxiliary, contraction, or sound–spelling expression.

**Editorial test:** Keep useful sentences alongside sound foundations; do not make letter-name recitation a whole curriculum.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

Develop subject and object pronouns; *be* and *have*; articles and basic noun number; simple present; basic present progressive; *do/does* questions and negatives; possessives; common prepositions; *there is/are*; *can*; and basic plans with *going to*.

#### Authoring brief

**Sentence contexts:** Family, home, routine, work/study, food, shopping, directions, schedules, preferences, and plans.

**Focused hidden targets:** A pronoun, article, simple present/progressive, do/does component, preposition, there is/are, or can form.

**Editorial test:** Use simple noncircular English support and distinguish question, negative, and statement frames.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

Add simple past and frequent irregular verbs, past progressive, future arrangements, comparisons, quantities, common modal expressions, infinitive/*-ing* patterns, basic relative clauses, and an introduction to present perfect.

#### Authoring brief

**Sentence contexts:** Recent events, appointments, comparisons, practical problems, solutions, and connected messages.

**Focused hidden targets:** Past/progressive/future component, comparison, quantity, modal, complement, or introductory perfect.

**Editorial test:** Keep time and reference explicit enough to support the choice; do not broaden a limited pattern into every use.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

Consolidate simple past versus present perfect, narrative sequencing, first and second conditionals, passive foundations, reported speech, relative clauses, question formation, and frequent verb–preposition and phrasal-verb patterns.

#### Authoring brief

**Sentence contexts:** Narration, explanation, opinions, repair, passive/reporting situations, and everyday group decisions.

**Focused hidden targets:** Past/perfect contrast, first/second conditional, passive component, reported speech, relative, or multiword-verb pattern.

**Editorial test:** Check pronoun placement, auxiliary syntax, and the actual situation rather than a tense-table label.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

Work on reliable article choice, tense/aspect under pressure, modal meanings, complex conditionals, reported speech, relative and participial structures, hedging, reformulation, collocations, and register-sensitive phrasing.

#### Authoring brief

**Sentence contexts:** Unfamiliar general arguments, meetings, proposals, complaints, reports, and qualified disagreement.

**Focused hidden targets:** Modal/conditional distinction, article/reference choice, participial component, collocation, hedging, or reformulation.

**Editorial test:** Keep plain English support and audience fit; a longer or more academic sentence is not automatically B2 learning.

### 6.6. Advanced development

**Curriculum reference:** C1

#### Required language and situation inventory

Develop source synthesis, implicit meaning, qualification, register switching, advanced collocations, extended argument, professional explanation, and fast multi-speaker listening. Use meaningful professional or academic situations rather than translated terminology lists.

#### Authoring brief

**Sentence contexts:** Professional explanation, multi-source discussion, implicit stance, and formal/social register changes.

**Focused hidden targets:** A source-relation, qualification, advanced collocation, or precise audience-sensitive phrase.

**Editorial test:** Preserve claim versus qualification and avoid turning the entire stage into specialized jargon.

### 6.7. Proficient integration

**Curriculum reference:** C2

#### Required language and situation inventory

Maintain coverage entries for collocations, subtle grammar choices, discourse organization, pronunciation, register, idioms, cultural references, and recurring personal errors.

**Advanced work.** Synthesize several long sources, reconstruct competing arguments, edit for precision, analyze rhetoric, interpret irony and understatement, and participate in discussions containing interruptions and rapid topic changes.

#### Authoring brief

**Sentence contexts:** Competing arguments, rhetoric, irony, understatement, editing, questioning, and turn recovery.

**Focused hidden targets:** One compact precision repair, rhetorical/idiomatic component, or pragmatic distinction.

**Editorial test:** Make context support the intended reading; do not hide the entire analytical response or require unknown external sources.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected American professional, social, and cultural domains

#### Required language and situation inventory

Cover the language and conventions of ordinary social life, the selected profession, and a cultural or intellectual field. Include humor, negotiation, informal messaging, disagreement, and responsibility for real outcomes.

#### Authoring brief

**Sentence contexts:** Work, study, volunteering, friendships, negotiations, cultural references, and responsibility in selected communities.

**Focused hidden targets:** A verified domain-specific sense, natural convention, or relationship-dependent formulation.

**Editorial test:** Do not reduce American usage to accent, or claim real community performance from cards.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Record the intended reading, phrase boundary, emphasis, and register when needed for later audio production. A spelling check does not prove pronunciation, and a pronunciation annotation does not prove that audio has been produced.

Keep ordinary written answers separate from phonetic aids. **During the audio phase, after all nine languages' text has been accepted**, validate actual recordings against the exact sentence and investigate omissions, changed words, wrong readings, or inappropriate phrasing. Do not count a fixed-voice sentence set as exhaustive accent or multi-speaker listening coverage.

### Language-specific requirements

Cover the source’s vowel contrasts **ship/sheep, full/fool, bed/bad**, consonant contrasts **light/right, vest/west**, **/θ/–/ð/**, final consonants, lexical stress, **/r/**, weak forms, contractions, and phrase prominence. Check both vowel quality and duration, not labels such as long/short alone.

Review the flap **[ɾ]** only in suitable environments; do not turn every written **t** into a **d**. Include regular **-ed** pronunciations **/t/, /d/, /ɪd/** and their phrase behavior. Keep normal spelling and necessary grammar. When stress changes the intended contrast, provide visible context and specify the audio reading rather than relying on typography alone.

---

## 8. Listening-support sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The available front recording intentionally contains the answer. The text need not exclude every imaginable synonym, but the canonical target must be natural, correctly spoken, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Choose sentences that make weak function words, contractions, endings, word boundaries, prominence, and speaker stance meaningful. Do not drop an auxiliary or inflection to imitate casual speech. A fixed American voice provides a production model, not proof of broad international or overlapping-speech comprehension.

---

## 9. Reading, script, and genre in sentences

Select an appropriate sentence genre and reading burden, not an arbitrary maximum length. Beginners need useful phrases with controlled supporting language; advanced cards may need more visible context for scope, stance, or reference. Extra length is justified only by meaning, not as a substitute for a more advanced target.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Use original practical messages and contemporary narratives, then explanation, nonfiction, source comparison, professional prose, and literary/rhetorical examples. Check article reference, countability, tense/aspect, clause relations, argument, and collocation. Do not make every advanced text an academic abstract; include ordinary social and professional language.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Build contexts for articles/countability, direct/embedded/subject/object questions, tense/aspect, infinitive/-ing complements, and multiword-verb placement. Use the source’s **used to work / be used to working / get used to working** as distinct state/change/habit patterns, not a list of visually similar translations.

For a separated phrasal verb, target one compact component or a naturally contiguous useful construction. Preserve pronoun position and the visible situation. For a question, hide the auxiliary or another learning-bearing unit rather than a complete sentence transformation. Avoid adjective or verb targets whose English support merely repeats them.

---

## 11. Lexical support and authoring records

Provide the contextual sense, dictionary form, actual whole-span label, and useful countability, complement, object-placement, stress, register, or American-usage information. The **make/reach a decision**, **a difficult decision**, and **decide whether to proceed** family supplies different constructions, not automatic synonym interchangeability.

The curriculum basis does not enumerate a complete per-level lexical list. Section 4.1 fixes the stage/card schedule. Build the detailed sense/construction inventory within those counts and preserve ordinary, professional, and cultural breadth. English support must remain comprehensible at the intended stage.


Use UTF-8 JSON arrays in the approved source layout. Required fields are `id`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`, and `audio`. Required text is nonempty; `accepted_answers` is an array, ordinarily empty. `audio` is the logical future path `audio/<id>.mp3`, not proof that media exists.

Useful nonempty optional fields are `reading`, `grammar`, `register`, and `note`. Omit unused fields. The reading and grammatical label must describe the **actual hidden span**. Keep the contextual English meaning concise; use notes for wider frames and restrictions. Do not insert curriculum IDs, review counts, agent instructions, or source bookkeeping into learner annotations.

The following original design example illustrates the record shape; it is not a production card or a fixed syllabus requirement. The `example` ID must not be copied into a production inventory.

```json
[
  {
    "id": "en-US-example-0001",
    "sentence": "The meeting starts at nine.",
    "cloze": "starts",
    "answer": "starts",
    "accepted_answers": [],
    "lemma": "start",
    "meaning": "begins",
    "part_of_speech": "verb",
    "audio": "audio/en-US-example-0001.mp3",
    "note": "The simple present gives a scheduled starting time."
  }
]
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| I wrote the address down before I left. | `wrote` | The particle remains visible; a separable multiword verb does not require hiding the object too. |
| I used to work nights, but now I work during the day. | `used to` | The visible contrast supports a past habit, not present familiarity with a routine. |


---

## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Review purpose, authority, urgency, familiarity, turn management, and audience. Use natural American requests, feedback, clarification, professional explanation, and disagreement without stereotyped nationality rules. Keep a character’s written or spoken style consistent with the situation, and attribute marked recognition rather than making every colloquial form a required answer.

---

## 13. Writing and editing requirements

Author directly in the target language using the approved content process. A learner exercise that prohibits generated prose is **not** a ban on the executor’s assigned sentence-authoring work. Do not translate one shared list across nine languages.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check articles/countability, tense/aspect, auxiliaries, complements, prepositions, collocations, organization, register, spelling, and punctuation. Distinguish correctness from effective wording for the actual audience. Advanced editing must preserve argument, source qualification, temporal relations, and commitment; a reviewer’s stylistic preference is not a universal grammar rule.

---

## 14. Content acceptance and coverage reconciliation

Acceptance concerns the **cards**, not a learner’s speaking or examination result.

| Review area | Required evidence |
|---|---|
| Fixed counts | Every stage has exactly the count and ID range in Section 4.1; stage allocations sum to the language total. Repair or replace rejected cards rather than reducing the deliverable. |
| Coverage | Every approved objective maps to actual hidden learning; omissions, redundancy, and recognition-only scope are reconciled across the language. |
| Sentence | Original, natural, self-contained, suitable for the milestone, with correct reference and social setting. |
| Cloze | Focused, useful, exactly aligned with the answer, and not an arbitrary substring or oversized proposition. |
| Support | Correct contextual meaning, lemma, whole-span label, and any reading/register/grammar note. |
| Progression | Visible prerequisites are available; repeated forms add a defensible distinction. |
| Technical integrity | Unique IDs/sentences, normalization, language-appropriate spelling/punctuation, valid fields, and declared audio paths. |
| Audio phase, after all nine text sets are accepted | Actual sentence/recording agreement and review of relevant pronunciation; no audio production or claims of verified recordings during the text phase. |

Every agent launched by the executor must use **Sol 6.1**, including authors, editors, final auditors, and any other permitted child agents. Keep the orchestrator prompt’s high reasoning effort, sequential ephemeral execution, read-only sandbox, structured JSON output, and no nested agents or child repository edits. Use the exact Sol 6.1 CLI identifier established once for the authorized environment; do not guess it or silently substitute another model.

Use a fresh author and separate editor for each manageable batch, ordinarily around 40 records, without treating batch size as a topic quota. Save accepted records and mappings as work proceeds, using only lightweight new/changed-record checks during ingestion. After authoring the stage, perform one final editorial pass in consecutive partitions covering every record and mapping, ordinarily no more than 400 records per partition. Apply verified findings together, check the affected records, and run one consolidated final source/coverage check. The orchestrator reviews the submitted changes and evidence; a narrow correction does not require rewriting or reauditing unchanged material.

Normally make **one implementation commit and one push per completed stage**, plus one correction commit/push per requested review round. Do not commit per batch, editor response, audit partition, or progress update. Save progress in normal files and temporary material under local `/tmp`; make a recovery commit only for a concrete interruption or risk, not on a fixed schedule. Use focused local tests when implementation changes and normal CI for the full suite. Do not run the complete repository checks repeatedly during authoring, duplicate valid CI locally, or add prompt/review/checkpoint infrastructure. Follow the orchestrator specification's detailed commit and check cadence; retain required content reviews and final integrity checks.

Keep concise counts, reviewed ID ranges, verified corrections, source hashes, and unresolved requirements in the PR. Reconcile this language's complete coverage before accepting its text; passing each stage’s self-written checklist alone is not sufficient. The orchestrator confirms accepted text and coverage for **all nine languages** before assigning any audio or bundle work. Text acceptance does not require recordings, audio-runtime access, or an installable archive. Activities such as sustained conversation, handwriting, long-form writing, live mediation, and community participation remain outside-card outcomes, not missing tests to invent inside the card app.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Cite material decisions in production evidence. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **American English File**, **Basic Grammar in Use**, and **Grammar in Use Intermediate** for the source-listed curriculum and grammar routes. Rachel’s English and the Color Vowel Chart support pronunciation investigation; VOA material supports beginner contexts; Oxford Learner’s Dictionaries and COCA support usage; Purdue OWL supports writing decisions; Cambridge materials supply the stated assessment reference. None is a new installation or purchasing requirement.

| Reference | Authoring use |
|---|---|
| [Cambridge English, “Should my child learn American or British English?”](https://www.cambridgeenglish.org/learning-english/parents-and-children/how-to-support-your-child/should-my-child-learn-american-or-british-english/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cambridge English, “C2 Proficiency”](https://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/) | Check the stated task/framework boundary; do not copy examination items. |
| [Cambridge English, “Preparing for C2 Proficiency”](https://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/preparation/) | Check the stated task/framework boundary; do not copy examination items. |
| [Oxford University Press, “American English File: 3rd Edition”](https://www.oupjapan.co.jp/en/products/list/2385) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cambridge University Press, “Basic Grammar in Use Student’s Book with Answers,” Fourth Edition](https://shop.cambridge.org/english/product/2700190087) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cambridge University Press catalog, “Grammar in Use Intermediate,” Fourth Edition, American English, B1–B2](https://www.cambridge.org/us/search?iFeelLucky=false&page=2&query=vocabulary+in+use&site=CE) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Rachel’s English, American English pronunciation resources](https://rachelsenglish.com/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [U.S. Department of State, American English, “The Color Vowel Chart”](https://americanenglish.state.gov/resources/color-vowel-chart) | Check the actual pronunciation, prosody, or variety of selected language. |
| [VOA Learning English, “Let’s Learn English 1”](https://learningenglish.voanews.com/p/5644.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Oxford Learner’s Dictionaries](https://www.oxfordlearnersdictionaries.com/us/) | Check the selected form, sense, construction, or register. |
| [English-Corpora.org, “A short tour of the COCA corpus”](https://www.english-corpora.org/coca/help/tour.asp) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [English-Corpora.org, corpus sections and genre comparisons](https://www.english-corpora.org/help/sections.asp) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Purdue OWL, “Academic Writing Introduction”](https://owl.purdue.edu/owl/general_writing/academic_writing/index.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Rachel’s English, “English Pronunciation Study: What did you do Today?”](https://rachelsenglish.com/english-pronunciation-study-today/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Purdue OWL, “How to Use Articles (a/an/the)”](https://owl.purdue.edu/owl/general_writing/grammar/using_articles.html) | Check the selected form, sense, construction, or register. |
| [Purdue OWL, “Count and Noncount Nouns: Basic Rules”](https://owl.purdue.edu/owl/general_writing/grammar/count_and_noncount_nouns/index.html) | Check the selected form, sense, construction, or register. |
| [Cambridge Dictionary, English Grammar Today, “British and American English”](https://dictionary.cambridge.org/grammar/british-grammar/british-and-american-english) | Check the selected form, sense, construction, or register. |
| [Cambridge Dictionary, English Grammar Today, “Verb patterns: verb + infinitive or verb + -ing”](https://dictionary.cambridge.org/grammar/british-grammar/verb-patterns-verb-infinitive-or-verb-ing) | Check the selected form, sense, construction, or register. |
| [Cambridge Dictionary, English Grammar Today, “Phrasal verbs and multi-word verbs”](https://dictionary.cambridge.org/grammar/british-grammar/phrasal-verbs-and-multi-word-verbs) | Check the selected form, sense, construction, or register. |
| [Rachel’s English, “The TH sound Up Close and in Slow Motion”](https://rachelsenglish.com/the-th-sound/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Rachel’s English, “The Flap T!”](https://rachelsenglish.com/flap-t/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Rachel’s English, “ED Endings (1/3)”](https://rachelsenglish.com/ed-endings-2020-1-3/) | Check the actual pronunciation, prosody, or variety of selected language. |

---

## 16. Card failure modes and repairs

| Reject or investigate | Required repair |
|---|---|
| An English definition simply repeats the answer | Use an easier contextual paraphrase. |
| Every question receives do or subject–auxiliary inversion | Distinguish direct, embedded, subject, and object frames. |
| A phrasal verb lacks object-placement information | Verify meaning, separability, and pronoun behavior. |
| Casual speech used to delete necessary written grammar | Retain ordinary spelling and the accepted utterance. |
| Every got mechanically replaced with gotten | Check the actual American construction and sense. |
| Advanced English reduced to academic jargon or accent | Reconcile ordinary, professional, pragmatic, and cultural coverage. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** the supplied `en-US.md` proficiency guide in `languages.zip`. Its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks are the basis for this document. The original attachment is not required to use this self-contained authoring guide.

**Authoring adaptations:** sentence briefs, focused-target rules, JSON design examples, coverage mapping, and editorial acceptance requirements implement the Meiki project’s card interaction. They are not official examination criteria or claims that the supplied proficiency guide specified this exact card format. Project production choices and English support are explicit in Sections 2–4 and 11. The exact stage counts and stage splits in Section 4.1 are explicit project production allocations, not official examination quotas or measured optimal learning quantities. Where the curriculum does not enumerate every lexical item, develop that inventory transparently within the fixed allocation; do not reduce the count or silently replace the curriculum.

| Supplied guide sections | Authoring treatment |
|---|---|
| 1–3: goal, variety, framework | Retained as production scope, recognition boundaries, and limits on proficiency claims. |
| 4–5: diagnosis and essential systems | Converted to prerequisite analysis and sentence-selection requirements. |
| 6: eight milestone inventories | Knowledge topics and endpoint distinctions retained; learner comprehension/production tasks become sentence briefs and focused targets. |
| 7–11: sound, listening, reading, grammar, vocabulary | Converted to sentence composition, cloze design, annotations, and later audio requirements. |
| 12–13: interaction, feedback, writing | Converted to social-context and editorial checks, not tutor or learner assignments. |
| 14: assessment | Replaced with content acceptance evidence; no learner performance certification is claimed. |
| 15–16: resources and failures | Kept as reference roles and card-rejection/repair criteria, without purchasing or study schedules. |
| 17: source notes | Replaced by this self-contained basis and adaptation record; no absent chat or earlier guide is required. |

**Reference boundary:** external links are carried from the supplied material for traceability; this conversion did not revalidate their content or current availability. Verify uncertain linguistic claims before production. No model/runtime installation, audio generation, or publication is authorized by a reference list.

**Source-file SHA-256:** `3ea5245ff25c394143edb50e16dff4173933248db03f2345fc5d1c0ed590856a`

