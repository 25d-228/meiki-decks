# French: sentence and card authoring guide

**Production locale:** `fr-FR`  
**Scope:** A1–C2-oriented metropolitan French, with a separate domain-specialization layer.

## 1. Purpose and required deliverables

**Fixed deliverable: 7 stages; 7,600 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The finished card shows the sentence with that span hidden, provides typed input and the **full-sentence recording on the front**, and reveals the sentence, answer, concise support, and replay on the back. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records, synchronized coverage mappings, and editorial evidence. **Complete and accept all text for all nine project languages before producing any audio.** For this language, finish every planned sentence, cloze, answer, annotation, reading, and coverage mapping, then complete editorial review, corrections, and source checks. Acceptance of this language's text permits the next language's text work, not audio generation. The pronunciation sections describe written sentence/reading requirements and the subsequent audio phase; no representative recordings, auditions, synthesis tests, or denoising runs belong to the text phase. This guide defines authoring scope; it does not certify a learner’s proficiency.

---

## 2. Production model, script, and register

Use **educated contemporary metropolitan French (`fr-FR`)** as the production model. Keep pronunciation, everyday vocabulary, writing conventions, and register coherent. Include both ordinary conversational French and careful edited writing, with labels where they differ.

Broaden recognition of unfamiliar accents and region-sensitive usage without making the expected answers a mixture of production standards. Reduced speech is part of the language model, not permission to replace standard written words with arbitrary phonetic spellings.

---

## 3. Curriculum framework and limits of card evidence

Keep the supplied **DELF-oriented beginner/independent progression** and **DALF C1/C2-oriented advanced progression**. Foundation supports A1; C2 is not a synonym for native social and cultural competence. Examination genres can inform sentence contexts, but completing a collection does not demonstrate a DELF/DALF result or spontaneous professional performance.

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

Create **7 stages and exactly 7,600 accepted cards** for French, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, audio files, or reverse cards as additional cards.

**Allocation basis:** Sound–spelling foundations are integrated into A1. Counts increase to accommodate the expanding lexical, pronoun, mood, collocation, register, and rhetorical inventories, and a separate final stage keeps professional, social, and cultural specialization in scope instead of absorbing it into a short C2 summary.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `01` | French 01 — A1 foundations | Sections 6.1–6.2 | 600 | 15 | 600 |
| `02` | French 02 — A2 everyday communication | Sections 6.3 | 800 | 20 | 1,400 |
| `03` | French 03 — B1 independent communication | Sections 6.4 | 1,000 | 25 | 2,400 |
| `04` | French 04 — B2 extended communication | Sections 6.5 | 1,200 | 30 | 3,600 |
| `05` | French 05 — C1 precise communication | Sections 6.6 | 1,400 | 35 | 5,000 |
| `06` | French 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,600 | 40 | 6,600 |
| `07` | French 07 — Social, professional, and cultural depth | Sections 6.8 | 1,000 | 25 | 7,600 |
| **Total** | **7 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **7,600** | **190** | **7,600** |

Use source IDs `fr-<stage>-0001` through `fr-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `fr-FR`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends on the preceding stages of this language, not on knowledge of another project language.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. A different approved batch split must still sum to the same stage count and must not introduce per-batch commits or full test runs.

#### Required distribution across stages

- **Stage 01:** Integrate sound contrasts and liaison planning with articles, gender, present forms, questions, agreement, quantities, basic lexical frames, and useful transactions.
- **Stage 02:** Cover past forms, object/reflexive pronouns, commands, quantities, comparisons, relatives, early y/en, verb prepositions, and chronological narrative.
- **Stage 03:** Cover narrative aspect, conditionals, pronoun order, y/en, subjunctive uses, reporting, clause relations, participle agreement, and expanded lexical families.
- **Stage 04:** Cover tense/mood distinctions, relatives, passive/impersonal/participial forms, concession, qualification, reformulation, spoken reductions, and collocations in varied genres.
- **Stage 05:** Protect broad lexical/collocational development alongside source synthesis, implied attitude, nuanced disagreement, academic/professional expression, and conversational register.
- **Stage 06:** Cover rhetorical and literary interpretation, idioms, irony, understatement, indirect criticism, editing, regional recognition, and informal reduced-language interpretation.
- **Stage 07:** Retain language for selected communities, work, cultural fields, relationships, group interaction, and locally situated meanings beyond the same C2 uses.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**Neither agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when both conditions hold: **its exact accepted-card count is met and its complete allocated coverage passes review**. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Treat English cognates as candidate learning material, not already-known French. Check gender, sound, preposition, collocation, register, and false-friend risk. The source’s **analyse** family illustrates why a bare translation does not supply **une analyse approfondie**, **analyser les résultats**, or **procéder à une analyse de**.

The source encourages increasing use of French definitions and paraphrases. The project’s `meaning` field remains concise English support; use natural French paraphrase/definition tasks in suitable advanced sentences and state this representation choice rather than silently changing the support language mid-series.

---

## 5. Essential systems to represent in sentences

### Sound, spelling, and noun phrases
Select real phrases that connect vowels, nasalization, silent letters, liaison, enchaînement, and rhythm to meaning. For nouns, include gender and useful articles in support; test definite, indefinite, partitive, and agreement choices through the intended reference or quantity.

### Verbs and pronouns
Plan present and near future, **passé composé/imparfait**, future, conditional, and subjunctive by function. Record the verb’s prepositions and complements. Distinguish subject, direct-object, and indirect-object pronouns; cover pronoun order, **y**, **en**, and reflexive uses without losing the antecedent.

### Clause relations
Cover questions, negation, relative clauses, reported speech, **si** hypotheses, cause, purpose, consequence, opposition, concession, and qualification. The blank must test that relation or a meaningful component; merely placing a connector in the visible text is not coverage of it.

### Lexical and stylistic precision
Use collocations, discourse markers, spoken reductions, and formal/neutral/informal reformulation. Advanced source comparison, irony, indirect criticism, and rhetorical analysis need a compact original context with visible evidence. Do not confuse rare synonyms with advanced control.

### Annotation boundaries
A gender-plus-collocation target can hide **une décision** inside a full sentence; a target hiding only **une** must have **une**, not **une décision**, as its answer. Verb-frame targets such as **dépendre de** need the actual preposition and contextual complement. Corrective examples must supply a natural alternative rather than only label the learner formulation wrong.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **editorial test** are authoring adaptations. They replace learner promotion tests with checks on the created content.

### 6.1. Foundation

**Curriculum reference:** Sound–spelling and basic sentence foundation

#### Required language and situation inventory

- `/u/` versus `/y/`;
- `/e/` versus `/ɛ/`;
- `/ø/` versus `/œ/`;
- nasal vowels;
- silent final consonants;
- syllable grouping;
- basic liaison and *enchaînement*;
- French sentence rhythm.

Specify the sound and phrasing expected for these sentences in writing; produce audio only in the audio phase, after all nine languages' complete text has been accepted.

Author greetings, identity, nationality, numbers, basic articles, être, avoir, elementary questions, and clarification language alongside sound coverage.

#### Authoring brief

**Sentence contexts:** Greetings, identity, numbers, clarification, être/avoir, basic questions, and useful article phrases.

**Focused hidden targets:** A short word or expression exposing a stated vowel, spelling, or phrase-boundary feature.

**Editorial test:** Do not delay useful sentences until phonology is complete. No audio production is permitted during text authoring; all nine languages' text must be accepted first.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

- definite, indefinite, and partitive articles;
- noun gender with every noun;
- present tense of regular verbs;
- approximately 20 essential irregular verbs;
- subject pronouns;
- basic adjective agreement;
- negation;
- direct questions and question words;
- possessives and demonstratives;
- basic place and time prepositions;
- *c’est*, *il est*, *il y a*;
- the immediate future;
- numbers, dates, times, prices, and quantities.

#### Authoring brief

**Sentence contexts:** Routine, home, work, family, preferences, plans, quantities, and basic transactions.

**Focused hidden targets:** An article, agreement form, present verb, question component, possessive, or near-future expression.

**Editorial test:** Record noun gender and contextual quantity; keep syntax within the stated beginner inventory.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

- *passé composé* with *avoir* and *être*;
- introduction to the imperfect;
- direct and indirect object pronouns;
- reflexive verbs;
- imperative;
- quantities and partitives;
- comparisons and superlatives;
- relative pronouns *qui*, *que*, and *où*;
- introduction to *y* and *en*;
- basic future forms;
- common verb-preposition constructions;
- chronological connectors.

#### Authoring brief

**Sentence contexts:** Recent events, problems, instructions, directions, appointments, comparisons, and short messages.

**Focused hidden targets:** A passé composé form, introductory imperfect, object/reflexive pronoun, relative, y/en use, or verb preposition.

**Editorial test:** Provide antecedents and temporal support. Do not collapse all object pronouns into one interchangeable category.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

- *passé composé* versus *imparfait*;
- future and conditional;
- object-pronoun order;
- *y* and *en* in normal speech;
- common subjunctive triggers;
- relative pronouns;
- reported speech;
- cause, consequence, purpose, and opposition;
- hypothesis with *si*;
- agreement of common past participles;
- more precise preposition use.

#### Authoring brief

**Sentence contexts:** Narration, opinion with examples, everyday repair, source summaries, and coherent personal explanation.

**Focused hidden targets:** Aspect contrast, hypothesis component, common subjunctive trigger/use, reported speech, or pronoun sequence.

**Editorial test:** Keep cause, purpose, consequence, and opposition faithful to the situation; never conceal the whole explanation.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

- accurate tense and mood selection;
- advanced relative structures;
- passive and impersonal constructions;
- participial constructions;
- concession and qualification;
- logical connectors;
- reformulation;
- hedging;
- formal versus informal language;
- collocations rather than isolated vocabulary;
- frequent spoken reductions.

#### Authoring brief

**Sentence contexts:** Unfamiliar general issues, proposals, complaints, formal messages, source comparison, and reviews.

**Focused hidden targets:** Concession, qualification, hedging, a compact passive/participial component, or register-sensitive collocation.

**Editorial test:** Include actual spoken/written differences and natural phrasing rather than a list of formal connectors.

### 6.6. Advanced development

**Curriculum reference:** C1

#### Required language and situation inventory

- synthesis of multiple sources;
- implicit meaning and speaker attitude;
- nuanced agreement and disagreement;
- reformulation without lexical repetition;
- long, organized oral responses;
- formal and academic writing;
- idiomatic collocations;
- conversational discourse markers;
- switching between social registers;
- comprehension of rapid unscripted speech.

#### Authoring brief

**Sentence contexts:** Professional and academic cases, nuanced discussion, implicit attitude, and multi-source positions.

**Focused hidden targets:** A precise source-relation or stance expression, natural reformulation, idiomatic collocation, or conversational marker.

**Editorial test:** Attribute views and limits explicitly; a longer sentence or rarer word alone is not new C1 learning.

### 6.7. Proficient integration

**Curriculum reference:** C2

#### Required language and situation inventory

Maintain coverage entries for:

- collocations;
- register;
- idioms;
- discourse markers;
- pronunciation and prosody;
- false friends;
- cultural references;
- recurring personal errors;
- stylistic differences;
- France-specific or region-specific usage.

- synthesizing several long sources;
- reconstructing complex arguments;
- speaking with precise qualification;
- irony, understatement, indirect criticism, and humor;
- stylistically differentiated writing;
- literary and rhetorical analysis;
- debates involving interruptions and rapid turn-taking;
- unfamiliar accents;
- informal, reduced spoken French;
- editing your own writing for elegance.

#### Authoring brief

**Sentence contexts:** Brief original rhetorical, literary, editing, irony, understatement, and indirect-criticism cases.

**Focused hidden targets:** One interpretable rhetorical device in use, precise lexical distinction, or focused editing repair.

**Editorial test:** The text must support the interpretation. Do not turn long-paper or debate tasks into whole-paragraph clozes.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Francophone professional, social, and cultural domains

#### Required language and situation inventory

Include:

1. **One target variety**: for example, educated metropolitan French.
2. **One professional identity** in French.
3. **One real social community**.
4. **Several cultural fields** you follow consistently.

Near-native development requires group interaction, not only one-to-one lessons. Native conversation includes overlapping speech, interruption, implication, humor, disagreement, background assumptions, and rapid topic changes.

Use language situations drawn from:

- living or working in a Francophone environment;
- friendships maintained in French;
- professional tasks completed in French;
- group discussions;
- cultural events;
- reading contemporary literature and essays;
- analyzing comedy and informal conversation;
- advanced prosody coaching;
- regular writing reviewed by an exacting native editor.

#### Authoring brief

**Sentence contexts:** Work, relationships, cultural discussion, disagreement, and messaging in a defined Francophone setting.

**Focused hidden targets:** A useful locally situated expression, domain sense, or audience-dependent choice.

**Editorial test:** Keep the target variety and domain explicit; sentence coverage cannot demonstrate natural community participation.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Record the intended reading, phrase boundary, emphasis, and register when needed for later audio production. A spelling check does not prove pronunciation, and a pronunciation annotation does not prove that audio has been produced.

Keep ordinary written answers separate from phonetic aids. **During the audio phase, after all nine languages' text has been accepted**, validate actual recordings against the exact sentence and investigate omissions, changed words, wrong readings, or inappropriate phrasing. Do not count a fixed-voice sentence set as exhaustive accent or multi-speaker listening coverage.

### Language-specific requirements

Plan the source’s **/u/–/y/**, **/e/–/ɛ/**, **/ø/–/œ/**, oral/nasal vowels, silent final consonants, syllable groups, liaison, enchaînement, and sentence rhythm. **tout/tu**, **dessus/dessous**, and **peu/peur** are source-listed contrast seeds; embed selected words in original meaningful sentences.

Specify the intended phrasing and register. Do not pronounce all silent letters to make a recording seem complete, and do not infer a liaison solely from adjacent spelling. Review vowel quality, phrase grouping, liaison, consonant behavior, and intonation in the finished recordings. Typed spelling and successful audio imitation are not a pronunciation assessment of the learner.

---

## 8. Listening-support sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The available front recording intentionally contains the answer. The text need not exclude every imaginable synonym, but the canonical target must be natural, correctly spoken, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Select phrases whose written forms can be hard to segment in speech: pronoun chains, silent segments, liaison, enchaînement, and common reductions. Keep the accepted sentence as the recording input. In advanced material, make stance, irony, or a repaired turn understandable from the text; do not rely only on unprovided prosody or actual overlapping speakers.

---

## 9. Reading, script, and genre in sentences

Select an appropriate sentence genre and reading burden, not an arbitrary maximum length. Beginners need useful phrases with controlled supporting language; advanced cards may need more visible context for scope, stance, or reference. Extra length is justified only by meaning, not as a substitute for a more advanced target.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from personal messages and practical text to accessible nonfiction, journalism-style argument, contemporary narrative, and specialist writing. Review gender/reference, **y/en**, verb–preposition frames, clause relations, tense/mood, collocations, and audience. Use concise original source situations for synthesis rather than external passages the learner cannot see.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Build nearby alternatives around **passé composé/imparfait**, future/conditional, subjunctive triggers, **si** clauses, direct/indirect pronouns, **y/en**, relative clauses, and complement frames. Change event framing, reference, or communicative purpose so the contrast carries meaning.

For a relative or pronoun target, leave enough of the antecedent and governor visible. For discontinuous negation or a longer construction, select one contiguous learning-bearing component. Do not force all pronouns or a complete subordinate clause into one blank simply to make it unique.

---

## 11. Lexical support and authoring records

Supply contextual meaning, useful dictionary form, accurate whole-span grammatical label, and relevant gender, agreement, complement, or register notes. Avoid cognate-only cards such as a bare **important = important**. A French target-language paraphrase is useful content when independently understandable, not an excuse for circular English support.

The curriculum basis does not establish a comprehensive per-level word list. Section 4.1 defines the exact card counts; develop the detailed lexical/construction inventory within those allocations and preserve the complete grammatical, social, professional, and cultural scope.


Use UTF-8 JSON arrays in the approved source layout. Required fields are `id`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`, and `audio`. Required text is nonempty; `accepted_answers` is an array, ordinarily empty. `audio` is the logical future path `audio/<id>.mp3`, not proof that media exists.

Useful nonempty optional fields are `reading`, `grammar`, `register`, and `note`. Omit unused fields. The reading and grammatical label must describe the **actual hidden span**. Keep the contextual English meaning concise; use notes for wider frames and restrictions. Do not insert curriculum IDs, review counts, agent instructions, or source bookkeeping into learner annotations.

The following original design example illustrates the record shape; it is not a production card or a fixed syllabus requirement. The `example` ID must not be copied into a production inventory.

```json
[
  {
    "id": "fr-example-0001",
    "sentence": "J'ai laissé mon sac près de la porte.",
    "cloze": "près de",
    "answer": "près de",
    "accepted_answers": [],
    "lemma": "près de",
    "meaning": "near",
    "part_of_speech": "prepositional phrase",
    "audio": "audio/fr-example-0001.mp3"
  }
]
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| Nous devons prendre une décision avant midi. | `une décision` | An article-plus-noun target hides both words and keeps the verb collocation visible. |
| Le train était déjà parti quand nous sommes arrivés. | `était déjà parti` | Test anteriority with both time points visible; retain the completed subordinate clause as context. |


---

## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Distinguish correct French from natural French for the relationship and audience. Review requests, disagreement, repair, stance, and formal/informal alternatives. Replace unsupported universal politeness rules with a specified speaker, listener, purpose, and constraint. Model conversational responses as language content, not instructions to schedule tutor sessions.

---

## 13. Writing and editing requirements

Author directly in the target language using the approved content process. A learner exercise that prohibits generated prose is **not** a ban on the executor’s assigned sentence-authoring work. Do not translate one shared list across nine languages.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Review gender, agreement, tense/mood, prepositions, vocabulary, syntax, register, spelling, and collocation. Include original messages, summaries, arguments, proposals, and professional reformulations at the corresponding milestones. An editorial improvement must preserve information, stance, uncertainty, and audience; shorter wording is not automatically better.

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

Use **Cosmopolite**, **Grammaire progressive**, and **Phonétique progressive** as the source-listed curriculum, grammar, and sound routes. The source also names TV5MONDE, InnerFrench, RFI, ARTE, France Culture, YouGlish, Le Robert, CNRTL, and DELF/DALF materials. Use dictionaries and genre examples for particular decisions; no course purchase or completion is an authoring prerequisite.

| Reference | Authoring use |
|---|---|
| [Hachette FLE](https://www.hachettefle.com/livres-collections-cosmopolite/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [CLE International](https://www.cle-international.com/adolescents/grammaire-progressive-du-francais-niveau-perfectionnement-b2c2-livre-2eme-edition-9782090395136.html) | Check the selected form, sense, construction, or register. |
| [Progressive](https://progressive.cle-international.com/9782090384550) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [TV5MONDE Apprendre](https://apprendre.tv5monde.com/en) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [innerFrench](https://innerfrench.com/podcast/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Apple Podcasts](https://podcasts.apple.com/at/podcast/journal-en-fran%C3%A7ais-facile/id1573764973) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [ARTE](https://www.arte.tv/en/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [YouGlish](https://youglish.com/french) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Le Robert Dictionary](https://dictionnaire.lerobert.com/fr/) | Check the selected form, sense, construction, or register. |
| [France Education International](https://www.france-education-international.fr/diplome/delf-tout-public/niveau-b2/exemples-sujets) | Check the stated task/framework boundary; do not copy examination items. |
| [DALF examples](https://www.france-education-international.fr/diplome/dalf/exemples-sujets) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

| Reject or investigate | Required repair |
|---|---|
| Hidden article but article-plus-noun answer | Make the displayed span and canonical answer identical. |
| Bare cognate meaning without gender or construction | Add the contextual lexical package and a meaningful retrieval target. |
| y/en or another pronoun without an antecedent | Make the relevant reference recoverable in the sentence. |
| Spelling used as a complete sound model | Specify liaison, silent material, vowel quality, and register for audio review. |
| Formal wording presented as the only natural French | Label genre and relationship and distinguish correctness from appropriateness. |
| A complete rewritten proposition hidden in an editing card | Hide the focused repair and keep the source claim visible. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** the supplied `fr.md` proficiency guide in `languages.zip`. Its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks are the basis for this document. The original attachment is not required to use this self-contained authoring guide.

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

**Source-file SHA-256:** `b365b0a2720a5fe51eab6c5d841be352fd5edb4eec035e3fe7dc629691106d82`

