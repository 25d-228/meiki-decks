# Spanish: sentence and card authoring guide

**Production locale:** `es-MX`  
**Scope:** A1–C2-oriented Spanish, with a separate layer for regional, professional, social, and cultural specialization.

## 1. Purpose and required deliverables

**Fixed deliverable: 7 stages; 7,600 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The finished card shows the sentence with that span hidden, provides typed input and the **full-sentence recording on the front**, and reveals the sentence, answer, concise support, and replay on the back. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records, synchronized coverage mappings, and editorial evidence. **Complete and accept all text for all nine project languages before producing any audio.** For this language, finish every planned sentence, cloze, answer, annotation, reading, and coverage mapping, then complete editorial review, corrections, and source checks. Acceptance of this language's text permits the next language's text work, not audio generation. The pronunciation sections describe written sentence/reading requirements and the subsequent audio phase; no representative recordings, auditions, synthesis tests, or denoising runs belong to the text phase. This guide defines authoring scope; it does not certify a learner’s proficiency.

---

## 2. Production model, script, and register

Use **educated contemporary central Mexican Spanish (`es-MX`)** for production. This is the project selection within the supplied guide’s regional options. Keep pronunciation, ordinary vocabulary, address forms, tense distribution, and pragmatic conventions coherent. Use `tú`, `usted`, and `ustedes` where the relationship requires them; do not alternate into productive `vos` or `vosotros`.

From the B1-oriented material onward, plan labeled recognition of other varieties, including the Spain, Colombia, and River Plate routes named by the guide. The production answer should remain compatible with the selected model unless the approved objective explicitly concerns recognition of attributed regional wording. Do not call all non-Mexican usage incorrect or label a shared expression exclusively Mexican. A dictionary’s unmarked entry alone does not establish regional frequency.

---

## 3. Curriculum framework and limits of card evidence

Keep **DELE A1 → A2 → B1 → B2 → C1 → C2** and the additional **SIELE route through C1** distinct. These are the supplied curriculum’s reference routes, not card-completion certificates or a claim that SIELE supplies a C2 qualification. Foundation supports A1; domain specialization remains distinct from C2. Use examination material to identify communicative demands, not to copy test questions or introduce examination score requirements for cards.

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

Create **7 stages and exactly 7,600 accepted cards** for Spanish, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, audio files, or reverse cards as additional cards.

**Allocation basis:** Foundation sound–spelling work is integrated into A1 rather than counted as a separate deck. The allocation grows through narration, mood/pronoun contrasts, lexical breadth, register, and advanced precision; a separate final stage protects regional, social, professional, and cultural depth.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `01` | Spanish 01 — A1 foundations | Sections 6.1–6.2 | 600 | 15 | 600 |
| `02` | Spanish 02 — A2 everyday communication | Sections 6.3 | 800 | 20 | 1,400 |
| `03` | Spanish 03 — B1 independent communication | Sections 6.4 | 1,000 | 25 | 2,400 |
| `04` | Spanish 04 — B2 extended communication | Sections 6.5 | 1,200 | 30 | 3,600 |
| `05` | Spanish 05 — C1 precise communication | Sections 6.6 | 1,400 | 35 | 5,000 |
| `06` | Spanish 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,600 | 40 | 6,600 |
| `07` | Spanish 07 — Regional, social, professional, and cultural depth | Sections 6.8 | 1,000 | 25 | 7,600 |
| **Total** | **7 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **7,600** | **190** | **7,600** |

Use source IDs `es-<stage>-0001` through `es-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `es-MX`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends on the preceding stages of this language, not on knowledge of another project language.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. A different approved batch split must still sum to the same stage count and must not introduce per-batch commits or full test runs.

#### Required distribution across stages

- **Stage 01:** Integrate sound–spelling, survival language, present forms, noun agreement, questions, modal frames, and ordinary household, service, work, and social vocabulary.
- **Stage 02:** Cover past/background contrasts, object and reflexive pronouns, commands, comparisons, duration, periphrases, and expanded practical vocabulary.
- **Stage 03:** Cover narration and aspect, present subjunctive, clitic order, se functions, reporting, conditionals, ser/estar and por/para contrasts, and explanation across everyday domains.
- **Stage 04:** Cover past subjunctive and conditionals, complex reporting and relatives, concession, stance, collocations, register, and regional recognition in varied situations.
- **Stage 05:** Protect broad lexical senses and collocations alongside source synthesis, implied stance, qualification, professional explanation, turn management, and indirectness.
- **Stage 06:** Cover mediation, rhetoric, literary interpretation, idioms, humor, understatement, social variation, editing, and diplomatic language with contextual support.
- **Stage 07:** Retain all five coverage dimensions and develop distinct domain senses, community conventions, negotiations, relationships, and cultural references beyond the same C2 uses.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**Neither agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when both conditions hold: **its exact accepted-card count is met and its complete allocated coverage passes review**. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Do not infer Spanish knowledge from English cognates. For each selected cognate, check sound, gender, complement frame, collocation, register, and relevant regional meaning. The source names `actualmente`, `asistir`, `realizar`, `embarazada`, `sensible`, `éxito`, and region-sensitive `constipado` as useful false-friend investigations; these are candidates to verify in context, not an automatic production list.

Distinguish a familiar construction used as visible support from the new hidden objective. The source names useful frames such as `Quiero que…` and `Me gustaría…` alongside basic high-frequency verbs; this does not place their entire productive mood or conditional systems in the foundation. State whether a form is a limited formula or a prerequisite already taught.

---

## 5. Essential systems to represent in sentences

### Nouns, agreement, and lexical frames
Cover gender and number in complete phrases. Keep noun, article, adjective, and pronoun reference aligned. Select verbs with their real complements and prepositions rather than isolated English glosses.

Prioritize the source’s verbs: **ser, estar, tener, haber, ir, venir, hacer, poder, querer, decir, dar, ver, saber, conocer, poner, salir, traer, llegar, llevar, parecer, necesitar, gustar, quedar, pasar, hablar**. Different inflections count as different cards only when they test a useful form, function, or contrast; they do not automatically count as additional lemmas.

### Tense, aspect, and mood
Build situations that distinguish the principal past tenses, with the selected region’s usage in view. Keep event completion, background, repetition, duration, and present relevance clear. Test indicative/subjunctive choices through the actual clause, assertion, intention, or stance. Do not teach the entire system through one English translation.

### Meaning and pronoun contrasts
Plan **ser/estar**, **por/para**, direct/indirect pronouns and their order, and the distinct constructions with **se**. For accidental or affected-person constructions, make the event and affected participant recoverable. Leave the antecedent visible when it is necessary to interpret a clitic.

### Discourse and social use
Cover reasons, consequences, concession, qualification, reformulation, softening, and informal discourse markers. Advanced sentences must support the claimed irony, understatement, implication, or diplomatic effect through visible circumstances, not a note that invents an unseen conversation.

### Vocabulary as constructions
Use the source’s families as planning seeds: **darse cuenta de que**, **tener algo en cuenta**, **por cuenta propia**, **salirle a cuenta a alguien**; and **llevar + duration + gerund**, **llevarse bien con**, **llevar a cabo**, and clothing uses of **llevar**. Split senses and complement patterns. Do not label every use merely “account” or “carry.”

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **editorial test** are authoring adaptations. They replace learner promotion tests with checks on the created content.

### 6.1. Foundation

**Curriculum reference:** Sound–spelling and basic sentence foundation

#### Required language and situation inventory

- the five stable vowel qualities;
- avoiding English-style vowel reduction;
- word stress;
- syllable grouping;
- tapped **r** versus trilled **rr**;
- Spanish **j**;
- **ñ**;
- **ll/y** according to your target variety;
- dental articulation of **t** and **d**;
- reducing English aspiration on **p, t, k**;
- linking words across boundaries.

A major English-speaker error is replacing unstressed Spanish vowels with an English-like schwa. Spanish vowels should remain comparatively stable even when unstressed.

Author greetings, identity language, articles/gender, numbers, questions, and basic ser, estar, hay, tener, and llamarse patterns alongside sound–spelling coverage.

#### Authoring brief

**Sentence contexts:** Greetings, identity, clarification, and simple quantities with basic ser/estar/hay/tener/llamarse frames.

**Focused hidden targets:** A useful word or compact expression that exposes the selected sound–spelling feature; not a list of letters.

**Editorial test:** Keep elementary grammar and pronounceable phrasing together. Do not require audio generation during content authoring.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

- noun gender and number;
- definite and indefinite articles;
- subject pronouns;
- present tense of regular verbs;
- approximately 25 high-frequency irregular verbs;
- **ser**, **estar**, **hay**, and **tener**;
- **gustar** and similar constructions;
- basic adjective agreement;
- question formation;
- negation;
- possessives and demonstratives;
- numbers, dates, time, and prices;
- **ir a + infinitive**;
- **tener que**, **poder**, **querer**, and **deber**;
- basic prepositions;
- introductory direct-object pronouns.

#### Authoring brief

**Sentence contexts:** Home, work, routine, family, preferences, plans, shopping, and simple personal messages.

**Focused hidden targets:** Present forms, noun/article agreement, a basic question word, a common modal frame, or an introductory object pronoun.

**Editorial test:** Make the blank test the declared objective. Keep any formula containing later grammar narrowly identified rather than expanding the A1 system silently.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

- **pretérito perfecto**;
- **pretérito indefinido**;
- introduction to the imperfect;
- direct and indirect object pronouns;
- reflexive verbs;
- pronoun combinations;
- affirmative and negative commands;
- comparisons and superlatives;
- **por** and **para**;
- common uses of **se**;
- present progressive;
- common verbal periphrases;
- relative pronouns **que**, **quien**, and **donde**;
- expressions of duration with **desde**, **desde hace**, and **hace**.

Past-tense usage varies regionally. Check the selected form in its context and the Mexican production model; do not import another route’s default without a label.

#### Authoring brief

**Sentence contexts:** Recent events, childhood routines, appointments, directions, comparisons, problems, and polite complaints.

**Focused hidden targets:** A past form, pronoun combination, command, comparison, duration frame, or compact periphrasis.

**Editorial test:** Keep time reference and pronoun antecedents clear; preserve Mexican-compatible tense distribution rather than imposing a different national preference.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

- **pretérito indefinido** versus **imperfecto**;
- regional use of **pretérito perfecto**;
- future and conditional;
- present subjunctive foundations;
- commands with pronouns;
- complete direct/indirect pronoun order;
- passive and impersonal **se**;
- accidental constructions such as **se me olvidó**;
- relative clauses;
- reported speech;
- cause, purpose, consequence, and opposition;
- **si** clauses;
- **ser** versus **estar** with adjectives;
- more systematic **por** versus **para**;
- frequent verbal periphrases.

#### Authoring brief

**Sentence contexts:** Connected narrative, explanation, opinion with reasons, practical repair, and hypothetical choices.

**Focused hidden targets:** Aspect/mood choice, a se construction, clitic order, reported-speech frame, or causal/purpose relation.

**Editorial test:** Distinguish background from event and speaker assertion from reported position. Do not hide the complete subordinate proposition.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

- confident subjunctive use;
- past subjunctive;
- conditional sentences;
- reported speech across time frames;
- advanced relative clauses;
- clitic combinations;
- passive, reflexive, reciprocal, impersonal, and accidental **se**;
- concession and qualification;
- stance and hedging;
- logical connectors;
- reformulation;
- register differences;
- natural collocations;
- regional discourse markers.

#### Authoring brief

**Sentence contexts:** Argument, proposals, reports, source comparisons, service interaction, and responses to objections.

**Focused hidden targets:** Concession, hedging, mood sequence, an advanced relative component, or a register-sensitive collocation.

**Editorial test:** The context must support the qualification and the intended relation among claims. Different wording must add a real distinction beyond B1.

### 6.6. Advanced development

**Curriculum reference:** C1

#### Required language and situation inventory

- synthesis of several sources;
- implied meaning and speaker stance;
- precise qualification;
- register control;
- advanced collocations;
- professional terminology;
- long-form argument;
- natural reformulation;
- fast unscripted listening;
- interruption and turn management;
- regional vocabulary recognition;
- pragmatic softening and indirectness.

#### Authoring brief

**Sentence contexts:** Professional explanation plus social and intellectual discussion, with several attributed viewpoints.

**Focused hidden targets:** A precise collocation, source-relation expression, bounded commitment, softening frame, or turn-management move.

**Editorial test:** Do not turn every example into administrative or technology terminology. Preserve source stance, beneficiary, and unresolved disagreement.

### 6.7. Proficient integration

**Curriculum reference:** C2

#### Required language and situation inventory

- synthesis of several long sources;
- complex oral mediation;
- rhetorical structure;
- irony and understatement;
- implicit disagreement;
- literary and stylistic analysis;
- idiomatic and colloquial language;
- humor;
- regional and generational variation;
- professional editing;
- fast group conversation;
- nonstandard but socially important speech;
- persuasive and diplomatic language.

#### Authoring brief

**Sentence contexts:** Original brief cases of mediation, rhetorical contrast, implication, editing, humor, and regional recognition.

**Focused hidden targets:** One learning-bearing rhetorical or idiomatic component, precise editing repair, or natural response to attributed marked wording.

**Editorial test:** The literal situation must support the intended effect. Keep complete syntheses, rewritten paragraphs, and joke punchlines out of oversized blanks.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected regional, professional, social, and cultural domains

#### Required language and situation inventory

Preserve five distinct coverage dimensions:

| Dimension | Target |
|---|---|
| Linguistic | C2 grammar, vocabulary, comprehension, and production |
| Phonological | Stable target-region pronunciation and prosody |
| Pragmatic | Politeness, implication, stance, humor, disagreement |
| Cultural | Shared references, institutions, history, media, and current discourse |
| Social | Natural participation in friendships, workplaces, and groups |

**Situation domains and limits of card evidence**

Use language from these interactional domains; card review does not establish real participation:

- group conversations;
- friendships maintained in Spanish;
- professional responsibilities;
- recurring social contact;
- disagreements and negotiations;
- exposure to different ages and social groups;
- sustained participation in a Spanish-speaking community.

#### Authoring brief

**Sentence contexts:** Relationships, group decisions, professional responsibilities, cultural discussion, and locally situated disagreement.

**Focused hidden targets:** A verified domain-specific sense, social convention, idiom, or register distinction not already covered in the same use.

**Editorial test:** Name the selected domain and relationship. Cards support its language; they do not prove community membership or unrestricted near-native performance.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Record the intended reading, phrase boundary, emphasis, and register when needed for later audio production. A spelling check does not prove pronunciation, and a pronunciation annotation does not prove that audio has been produced.

Keep ordinary written answers separate from phonetic aids. **During the audio phase, after all nine languages' text has been accepted**, validate actual recordings against the exact sentence and investigate omissions, changed words, wrong readings, or inappropriate phrasing. Do not count a fixed-voice sentence set as exhaustive accent or multi-speaker listening coverage.

### Language-specific requirements

Cover five stable vowel qualities, word stress, syllable grouping, tapped **r** and trilled **rr**, **j**, **ñ**, the selected **ll/y** realization, dental **t/d**, limited English-style aspiration of **p/t/k**, and linking across words. Include the source’s **pero/perro** contrast in meaningful contexts, not invented syllable drills.

Select sentences that expose stress and connected phrasing without tongue-twister density. Record the intended question, contrast, or quotation reading when it matters. Review vowel stability, duration, consonant realization, phrase grouping, and intonation during audio work; accurate **rr** alone is not an adequate pronunciation check. Regional **s**, **c/z**, and final-consonant differences belong to the declared production or recognition scope.

---

## 8. Listening-support sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The available front recording intentionally contains the answer. The text need not exclude every imaginable synonym, but the canonical target must be natural, correctly spoken, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Include ordinary pronoun sequences, tense/mood cues, linking, discourse markers, and regional vocabulary in self-contained utterances. A sentence must still make sense when heard without the annotations. Do not rely on a cognate’s apparent English meaning to explain what was spoken. Advanced conversational sentences may model interruption recovery or qualification, but one recording does not establish multi-speaker comprehension.

---

## 9. Reading, script, and genre in sentences

Select an appropriate sentence genre and reading burden, not an arbitrary maximum length. Beginners need useful phrases with controlled supporting language; advanced cards may need more visible context for scope, stance, or reference. Extra length is justified only by meaning, not as a substitute for a more advanced target.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from messages, signs, practical exchanges, and graded narrative to accessible explanation, journalism-style argument, fiction, and professional writing. Use original short cases rather than lifted passages. Make the reference of object pronouns, the function of **se**, and the relation between clauses recoverable. Preserve a clear distinction between a literary or formal register and ordinary conversation.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Use contrast families for **ser/estar**, **por/para**, **indefinido/imperfecto**, regional **perfecto**, indicative/subjunctive, commands with clitics, and the different functions of **se**. Change the situation or interpretation that makes the contrast useful, not just a person’s name.

For a construction such as **darse cuenta de que**, either target a justified compact construction or its learning-bearing preposition with sufficient context. Do not hide the entire realization clause. In a pronoun exercise, hiding **se me** is different from hiding the whole event; state which distinction the card tests. Short repeated forms such as **de** are permissible across genuinely different frames.

---

## 11. Lexical support and authoring records

Record the target’s dictionary head or fixed expression, contextual meaning, whole-span grammatical label, and useful gender, complement, collocation, or register information. If the blank is a conjugated verb, the English gloss must reflect that use; a note may supply the wider construction.

Use concise English support as the project convention. Do not put a full dictionary sense list behind one context. The curriculum basis does not enumerate every Spanish lexical item. This authoring guide defines the exact card totals in Section 4.1; develop the detailed sense/construction inventory within those fixed counts while retaining every required domain and distinction.


Use UTF-8 JSON arrays in the approved source layout. Required fields are `id`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`, and `audio`. Required text is nonempty; `accepted_answers` is an array, ordinarily empty. `audio` is the logical future path `audio/<id>.mp3`, not proof that media exists.

Useful nonempty optional fields are `reading`, `grammar`, `register`, and `note`. Omit unused fields. The reading and grammatical label must describe the **actual hidden span**. Keep the contextual English meaning concise; use notes for wider frames and restrictions. Do not insert curriculum IDs, review counts, agent instructions, or source bookkeeping into learner annotations.

The following original design example illustrates the record shape; it is not a production card or a fixed syllabus requirement. The `example` ID must not be copied into a production inventory.

```json
[
  {
    "id": "es-example-0001",
    "sentence": "El autobús llega a las ocho.",
    "cloze": "llega",
    "answer": "llega",
    "accepted_answers": [],
    "lemma": "llegar",
    "meaning": "arrives",
    "part_of_speech": "verb",
    "audio": "audio/es-example-0001.mp3",
    "note": "The present tense gives the scheduled arrival time here."
  }
]
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| Dejé las llaves en la mesa y ahora no las encuentro. | `las encuentro` | Recover the plural antecedent and the present search; do not hide the whole two-clause event. |
| Aunque la propuesta reduce el costo, todavía no resuelve el problema del horario. | `Aunque` | Test concession while leaving both the benefit and the unresolved limitation visible. |


---

## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Review speaker, listener, authority, familiarity, urgency, beneficiary, and commitment. Formal, neutral, and informal request versions require different contexts, not a universal ranking in which the longest sentence is always most polite. Give priority to meaning-changing errors, recurring structure errors, unnatural phrasing, target-region sound, and register; still correct every verified defect in accepted cards.

---

## 13. Writing and editing requirements

Author directly in the target language using the approved content process. A learner exercise that prohibits generated prose is **not** a ban on the executor’s assigned sentence-authoring work. Do not translate one shared list across nine languages.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check gender, agreement, tense, mood, articles, pronouns, prepositions, word order, vocabulary, collocation, register, and punctuation. Keep grammatical correctness distinct from the wording an educated speaker in the selected setting would naturally use. At advanced levels, a shortened or more diplomatic version must preserve agency, qualification, comparison, and commitment.

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

Use **Aula Internacional Plus/Aula C1** or **AVE Global** for curriculum scope, **Competencia gramatical en uso** and advanced ELE grammar for contrasts, and **Anaya ELE Fonética** for sound. The source also lists Language Transfer, Dreaming Spanish, Easy Spanish, RTVE, Radio Ambulante, RAE/ASALE, YouGlish, and DELE/SIELE references. Keep European media as labeled reference material, not a reason to replace the Mexican production model.

| Reference | Authoring use |
|---|---|
| [Difusión](https://ayuda.difusion.com/portal/en/kb/articles/campus-access-for-teachers-aula-internacional-plus-for-teachers-only) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Instituto Cervantes London](https://londres.cervantes.es/en/courses_spanish/students_spanish/information_virtual_classroom_spanish.htm) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Language Transfer](https://www.languagetransfer.org/complete-spanish) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Edelsa Store](https://tienda.edelsa.es/categorias/470640) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Edelsa Store](https://tienda.edelsa.es/producto/6379028) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Anaya ELE](https://www.anayaele.es/anaya-ele-en) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Dreaming](https://www.dreaming.com/spanish) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Easy Spanish](https://www.easy-spanish.org/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [RTVE.es](https://www.rtve.es/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Radio Ambulante](https://radioambulante.org/tag/transcripcion) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [YouGlish](https://youglish.com/spanish) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Real Academia Española](https://www.rae.es/inicio) | Check the selected form, sense, construction, or register. |
| [Cervantes Albuquerque](https://albuquerque.cervantes.es/en/diplomas_spanish/model_exam.htm) | Check the stated task/framework boundary; do not copy examination items. |
| [Instituto Cervantes Exámenes](https://examenes.cervantes.es/es/siele/preguntas-frecuentes) | Check the stated task/framework boundary; do not copy examination items. |
| [SIELE](https://examenes.cervantes.es/es/presentacion/siele) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

| Reject or investigate | Required repair |
|---|---|
| A1 formulas used to justify unrestricted advanced grammar | Declare formula status and teach productive prerequisites in their mapped milestone. |
| Past forms selected by an imported national default | Verify the contextual use in the Mexican production model. |
| Clitic or se meaning lacks a recoverable participant | Repair the sentence or choose another target. |
| A long synthesis or predicate is hidden | Retarget the useful construction while keeping the claim visible. |
| Regional alternatives called ungrammatical | Label region/register and keep production coherent. |
| Advanced content is mostly one technical topic | Reconcile everyday, social, professional, cultural, and intellectual coverage. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** the supplied `es.md` proficiency guide in `languages.zip`. Its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks are the basis for this document. The original attachment is not required to use this self-contained authoring guide.

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

**Source-file SHA-256:** `31e4197fab8a49558278ac77fd7c28839f4b61011fc13489cf63700efb7d3816`

