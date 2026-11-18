# Russian: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-ru-RU`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `ru-RU`  
**Scope:** A1–C2/TORFL-oriented Russian with a separate professional, social, and cultural specialization layer.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 8 stages; 10,100 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **educated contemporary Standard Russian (`ru-RU`)** and Cyrillic spelling. Keep normal sentence/answer orthography separate from learner stress annotations. Include **ё** where the selected word requires it; do not erase distinctions or automatically accept Latin lookalikes.

The source includes print, italic, handwritten-form recognition, and typing. Typed cloze cards can support script recognition and typing; they do not certify cursive or handwriting. Use a coherent production model while labeling relevant regional or social recognition. Specify **ты/вы**, names, patronymics, titles, and diminutives when the relationship matters.

---

### 2.1. Short sentences: mandatory length contract

Keep **advanced meaning, not advanced length**. The following caps apply to the **entire `common.sentence` field per card**, with its cloze restored. They include both sides of a contrast, all quoted speech, and both turns/sentences of a micro-context. They are not separate allowances per clause. No advanced, literary, domain, quotation, or politeness exception raises a cap.

| Production stages | Preferred full-text length | Hard full-text maximum |
|---|---|---|
| `00–01` | 4–9 words | **12 words AND 90 characters** |
| `02` | 6–12 words | **16 words AND 120 characters** |
| `03–07` | 8–14 words | **20 words AND 150 characters** |

**Hidden span:** normally 1–3 words; hard maximum **5 words AND 40 characters**. Apply the same ceiling to each explicit accepted answer. This ceiling does not make an arbitrary fragment, entire predicate, or unrelated group of words a good cloze. A compact conventional whole utterance can be an editorially justified exception to the visible-context rule, but not to either length cap.

Preferred bands are drafting guidance, not minimums or quotas. Naturally shorter utterances are welcome. Do not pad them or write every card near the maximum. Advanced stages keep the same upper ceiling; difficulty comes from the selected sense, grammar, collocation, register, or pragmatic distinction.

**Characters:** normalize to NFC, then count every non-whitespace Unicode code point, **including punctuation, digits, and Latin text**. Use `sum(not ch.isspace() for ch in unicodedata.normalize("NFC", text))`. This definition is for the length check only; cloze boundaries still respect grapheme clusters. Do not strip punctuation, change standard spelling, use abbreviations, or compress numerals to game the count. Readings and answer-side notes are not part of `common.sentence`, but must never hide required front-side context.

**Words:** count maximal Unicode letter/number sequences, allowing internal straight or curly apostrophes. Hyphens, slashes, and dashes separate units; punctuation-only pieces do not count as words. Thus contractions/elisions remain natural, while hyphenation cannot join several words into one for this check. Use a small standard-library counter, for example `re.findall(r"[^\W_]+(?:['’][^\W_]+)*", NFC_text)`. This is an operational count, not a linguistic segmentation theory. Both the word limit and character limit must pass.

Use **one short sentence by default**. At most two short sentences or two short conversational turns may form the source text when essential to interpretation; their **combined** text must fit the same cap. Do not add an uncounted preamble, a front-side `context` field, a screenshot, or an answer-side explanation as a way around the limit. Keep one primary target. Avoid stacked relative clauses, embedded chains, several unexplained participants, and unrelated facts. A brief subordinate or contrasting clause is allowed when it demonstrates the target.

Before accepting a card, verify that the source makes the relevant event/referent and the target's sense, relation, time, or social force interpretable. Remove decorative setup, not the governor, antecedent, negation, comparison, condition, or other essential cue. Text need not exclude every imaginable synonym, but the intended target must be natural and demonstrate the assigned use. Do not substitute an arbitrary fragment or ambiguous sense for useful context.

Preserve the context that selects case, aspect, directionality, or information focus. Normal answers use ordinary orthography; stress belongs in support fields. A few very long derived words can still fail the character ceiling.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| После работы я читаю газету. | `газету` | The activity supports the noun in its actual case form. |
| Он согласился лишь при условии полной конфиденциальности. | `при условии` | An explicit restriction supports the conditional expression. |
| Его похвала прозвучала снисходительно, хотя он хотел поддержать коллегу. | `снисходительно` | The contrast supplies a reason to interpret the tone. |

### 2.3. Research basis and limits of the policy

The numerical caps in Section 2.1 are **project authoring decisions**, not experimentally established optimums, official proficiency requirements, or word-for-character equivalences. The reviewed evidence does not validate these exact thresholds for this sentence-card authoring task. The policy deliberately keeps the reading burden small while preserving the target's meaning and context. Do not turn a working-memory span into a sentence-word quota.

Sentence-length research notes supplied with this guide, dated 25 October 2026:

| Source | What it informs here |
|---|---|
| [Mulder et al. (2019), Applied Psycholinguistics](https://doi.org/10.1017/S0142716418000504) | Supportive sentence contexts improved vocabulary gains. |
| [van den Broek et al. (2018), Language Learning](https://doi.org/10.1111/lang.12285) | Context inference and retrieval produced different retention outcomes. |
| [Futrell et al. (2015), PNAS](https://doi.org/10.1073/pnas.1502134112) | Cross-linguistic dependency evidence; not a flashcard-length trial. |
| [Woźniak, SuperMemo formulation guidance](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge) | Practitioner guidance: focused retrieval and economical wording. |
| [US Veterans Affairs, sentence guidance](https://design.va.gov/content-style-guide/plain-language/use-short-sentences) | General-content advice: at most 25 words, not a learning optimum. |

These sources address different tasks and populations. Their use here is a design synthesis, not a direct experiment on these cards. More context is not automatically better retention, and less context is not automatically better teaching. Preserve interpretable meaning and a focused target; do not infer a requirement for context-free guessing from a different experimental task. The exact caps, stage mapping, counting method, and rejection rules are the project policy.

---

## 3. Curriculum framework and limits of card evidence

Preserve the supplied **TORFL/ТРКИ** route: Elementary A1, Basic A2, and certification levels I–IV associated with B1–C2 in the guide. Its independent goals include spontaneous interaction, pronunciation, register, professional writing, and cultural competence. The guide’s functional milestones are not official score criteria, and card counts do not establish a TORFL result.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **8 stages and exactly 10,100 accepted cards** for Russian, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** A dedicated Cyrillic/sound foundation precedes six broad proficiency-oriented stages and specialization. The allocation explicitly reserves extensive space for useful lexical senses with stress, case government, aspect and motion contrasts, derivation, participial syntax, register, and cultural interpretation rather than reducing these systems to charts or one example per rule.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `00` | Russian 00 — Cyrillic, sound, and sentence foundations | Sections 6.1 | 200 | 5 | 200 |
| `01` | Russian 01 — A1 basic communication | Sections 6.2 | 800 | 20 | 1,000 |
| `02` | Russian 02 — A2 routine communication | Sections 6.3 | 1,100 | 28 (27 × 40 + 20) | 2,100 |
| `03` | Russian 03 — B1 independent communication | Sections 6.4 | 1,400 | 35 | 3,500 |
| `04` | Russian 04 — B2 extended communication | Sections 6.5 | 1,600 | 40 | 5,100 |
| `05` | Russian 05 — C1 precise communication | Sections 6.6 | 1,800 | 45 | 6,900 |
| `06` | Russian 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 2,000 | 50 | 8,900 |
| `07` | Russian 07 — Social, professional, and cultural depth | Sections 6.8 | 1,200 | 30 | 10,100 |
| **Total** | **8 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **10,100** | **253** | **10,100** |

Use source IDs `ru-<stage>-0001` through `ru-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `ru-RU`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 00:** Cover direct Cyrillic reading/typing in phrases, stress, softness, reduction, voicing, consonant clusters, and useful survival language without transliteration dependence.
- **Stage 01:** Cover noun/agreement patterns, present/past/future, high-frequency case functions, numbers, questions, negation, commands, initial aspect, and ordinary lexical frames.
- **Stage 02:** Cover all common case patterns, animacy, comparison, reflexives, aspect in time and commands, unprefixed motion, conditions, pronouns, numerical government, and impersonal uses.
- **Stage 03:** Cover wider government, aspect narratives, prefixed motion, voice, hypotheses, reporting/relatives, participial recognition, focus, particles, and colloquial alternatives.
- **Stage 04:** Develop aspectual nuance, figurative motion, participles, impersonal/passive choices, numerals, derivation, nominal style, collocations, and register-sensitive discourse.
- **Stage 05:** Cover advanced lexical frames, synthesis, stance, qualification, formal/conversational syntax, professional meetings, social address, register shifts, and editing for clarity.
- **Stage 06:** Cover aspect/Aktionsart and usage precision, rhetoric, idioms, euphemism, implication, emotion, literary interpretation, editing, and regional/cultural recognition.
- **Stage 07:** Develop distinct domain senses, social conventions, responsibilities, negotiations, cultural references, and locally appropriate language beyond the same C2 uses.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Prior Slavic-language knowledge can create apparent familiarity without correct Russian stress, aspect, case government, motion, or register. Check these systems independently and record false-friend risks.

Introduce useful sentences alongside Cyrillic and sound. Preserve the source’s distinction between a high-frequency case function and mastery of all endings. Do not skip sound or morphology because a word resembles another language, and do not delay meaningful sentences until a complete declension chart is memorized.

---

## 5. Essential systems to represent in sentences

### Cyrillic and stress
Connect spelling, sound, and lexical meaning directly. Avoid Latin transliteration as the answer. Check stress in the **actual inflected form**, including movement across a paradigm; a stressed lemma alone is insufficient. Preserve standard spelling in `common.sentence`, `common.cloze`, and `common.answer`, with pedagogical acute marks in `reading` or clearly labeled support.

### Cases as functions and government
Cover possession/absence, quantity, recipient/experiencer, instrument/role, location/topic, direction/object, time, and governors. The source’s **нет времени, помогать другу, интересоваться музыкой, говорить о работе, ждать автобус** are frame seeds. Do not infer a single case rule from an English preposition or a list of endings.

### Aspectual packages
Record aspect, relevant partner(s), stress, conjugation, common objects/cases, past/future behavior, and useful imperatives. Contrast process, repetition, intention, completion, and result in the visible situation. **делать/сделать** is a planning example, not a rule that every verb has one perfectly symmetric partner. Verify lexicalized prefixed senses.

### Motion and derivation
Introduce **идти/ходить, ехать/ездить, нести/носить, вести/водить, лететь/летать** through route, directionality, habituality, and means of travel. Then develop **при-, у-, в-/вы-, под-, пере-, за-, до-** as specified in the intermediate inventory. Keep literal spatial use distinct from extended meaning.

The source’s **писать → написать/записать/подписать/переписать/опись/подпись** and **решать → решить/разрешить/решение/нерешительный** illustrate families to verify, not transparent equations.

### Information structure and relationships
Use neutral beginner word order before marked focus and contrast. Flexible order is not free interchangeability. Supply the contextual reason for marked order. Address, patronymics, titles, diminutives, and **ты/вы** must fit the social situation.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Cyrillic and phonological foundation

#### Required language and situation inventory

- printed Cyrillic;
- uppercase and lowercase forms;
- misleading Latin lookalikes;
- Russian keyboard layout;
- basic handwriting;
- direct reading of simple syllables and words;

- stressed vowel letters and their sound values;
- hard and soft consonant contrasts;
- **ы**;
- **й**;
- soft sign and hard sign functions;
- final devoicing;
- basic word stress.

- vowel reduction;
- voicing assimilation;
- common consonant clusters;
- **ш / щ**, **ч / ц**, **х**;
- phrase stress;
- basic intonation patterns;
- recognition of learner stress marks.

Use the source’s 80–120 high-frequency foundation expressions as a breadth aspiration; listed seeds include:

> Здра́вствуйте.  
> Спаси́бо.  
> Пожа́луйста.  
> Извини́те.  
> Я не понима́ю.  
> Повтори́те, пожа́луйста.  
> Говори́те медле́ннее, пожа́луйста.  
> Что э́то зна́чит?  
> Как э́то по-ру́сски?  
> Я изуча́ю ру́сский язы́к.

#### Authoring brief

**Sentence contexts:** Identity, thanks, clarification, basic questions, and survival expressions linked to Cyrillic and sound.

**Focused hidden targets:** A useful word or compact expression exposing stress, softness, spelling, or a basic phrase.

**Authoring criterion:** Do not make stress annotations part of the ordinary typed answer or pretend typed input assesses handwriting.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

- noun gender and number;
- personal and possessive pronouns;
- present-tense conjugation;
- past tense and gender agreement;
- compound future with **быть**;
- nominative functions;
- accusative objects and basic animacy;
- prepositional case for location and topic;
- genitive for possession, absence, origin, and quantity;
- dative for recipients and age in common frames;
- instrumental in frequent identity and accompaniment patterns;
- negation;
- basic imperative;
- adjective agreement;
- numbers, dates, time, prices, and age;
- introduction to aspect as paired vocabulary.

Do not assign equal beginner quotas to every case ending. Prioritize high-frequency functions and expand the inventory systematically.

#### Authoring brief

**Sentence contexts:** Family, home, routine, work/study, transactions, help requests, simple past events, and plans.

**Focused hidden targets:** A high-frequency case phrase, present/past/future form, agreement, number, negation, or imperative.

**Authoring criterion:** Prioritize functions rather than equal mastery of all case endings; keep aspect introduction contextual.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

- all six cases in common singular and plural patterns;
- animate accusative;
- adjective and pronoun declension;
- comparative forms;
- reflexive verbs;
- aspect in past, future, and commands;
- common imperfective/perfective pairs;
- unprefixed verbs of motion;
- conditional with **бы**;
- clauses of cause, condition, purpose, time, and contrast;
- indirect questions;
- indefinite and negative pronouns;
- numerical government in frequent expressions;
- common impersonal constructions.

#### Authoring brief

**Sentence contexts:** Problems, follow-up questions, comparisons, narration, commands, conditions, and routine motion.

**Focused hidden targets:** A case/declension form, aspect choice, unprefixed motion form, numerical phrase, or impersonal construction.

**Authoring criterion:** Keep route, animacy, event framing, and case governor explicit enough to support the choice.

### 6.4. Independent communication

**Curriculum reference:** B1 / TORFL-I-oriented

#### Required language and situation inventory

- case government of common verbs, adjectives, and prepositions;
- aspect in narration, sequence, repetition, intention, and result;
- prefixed verbs of motion;
- reflexive and passive meanings;
- conditional and hypothetical language;
- reported speech;
- relative clauses;
- participles in frequent written patterns;
- adverbial participles in recognition and controlled use;
- impersonal constructions;
- comparisons and degree;
- word-order changes that mark topic and focus;
- conversational particles and response formulas;
- neutral versus colloquial alternatives.

**Motion-verb progression**

Train one prefix at a time through situations:

- **при-** arrival;
- **у-** departure;
- **в- / вы-** entering and exiting;
- **под-** approaching;
- **пере-** crossing or transferring;
- **за-** brief visit or movement behind/into;
- **до-** reaching a limit.

Introduce common extended meanings after the literal spatial prerequisites are represented.

#### Authoring brief

**Sentence contexts:** Narration, familiar abstract topics, source reports, polite repair, and formal/informal messages.

**Focused hidden targets:** A prefixed motion use, reported or relative component, participial recognition, focus, or conversational particle.

**Authoring criterion:** Introduce motion prefixes through situations and keep recognition versus productive use explicit.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2 / TORFL-II-oriented

#### Required language and situation inventory

- nuanced aspect choice in narrative and argument;
- prefixed motion verbs in literal and figurative use;
- full participial constructions;
- adverbial participles in appropriate written and formal spoken contexts;
- passive and impersonal alternatives;
- complex numerical expressions;
- nominalization and formal written syntax;
- colloquial reductions and particles;
- word order for emphasis, contrast, and cohesion;
- derivational families;
- register-sensitive synonyms;
- polite disagreement, criticism, and requests;
- idioms that are genuinely frequent.

**Vocabulary families**

Organize vocabulary by productive roots and prefixes:

> писа́ть → написа́ть, записа́ть, подписа́ть, переписа́ть, о́пись, по́дпись  
> реша́ть → реши́ть, разре́шить, реше́ние, нереши́тельный

Do not assume every morphological relative has a transparent or current meaning. Confirm usage and register.

#### Authoring brief

**Sentence contexts:** Professional role-play, source comparison, general argument, proposals, reviews, and contemporary narrative.

**Focused hidden targets:** Nuanced aspect, figurative motion, participial/nominal component, collocation, or register-sensitive synonym.

**Authoring criterion:** Verify derived meanings and subject/reference relations; do not treat every prefix as transparent.

### 6.6. Advanced development

**Curriculum reference:** C1 / TORFL-III-oriented

#### Required language and situation inventory

- precise qualification;
- source synthesis;
- formal argumentation;
- implicit meaning and stance;
- advanced collocations;
- academic and bureaucratic nominal style;
- contrast between written and conversational syntax;
- indirect criticism;
- register switching;
- professional meetings and presentations;
- culturally appropriate forms of address;
- fast multi-speaker comprehension;
- accent and generational variation;
- editing for clarity rather than mere grammaticality.

#### Authoring brief

**Sentence contexts:** Professional meetings, academic sources, qualified argument, synthesis, and indirect criticism.

**Focused hidden targets:** A precise collocation, stance relation, register shift, or meaning-preserving clarification.

**Authoring criterion:** Keep conversational and formal written syntax distinct and preserve source uncertainty.

### 6.7. Proficient integration

**Curriculum reference:** C2 / TORFL-IV-oriented

#### Required language and situation inventory

Maintain coverage entries for:

- aspect and Aktionsart;
- case government;
- verbs of motion;
- participial syntax;
- collocations;
- word order and focus;
- discourse particles;
- formal written style;
- colloquial reductions;
- pronunciation and prosody;
- idioms;
- cultural references;
- regional and generational variation;
- recurring personal errors.

**Advanced language functions**

Include:

- humor and irony;
- understatement;
- euphemism;
- indirect disagreement;
- emotionally charged speech;
- rapid group interaction;
- interruptions and unfinished clauses;
- literary prose;
- formal speeches;
- unfamiliar professional topics;
- self-editing for style and rhetorical effect;
- interpretation of historical and cultural allusions.

#### Authoring brief

**Sentence contexts:** Rhetoric, euphemism, irony, emotional stance, literary analysis, editing, and objection handling.

**Focused hidden targets:** A compact aspect/Aktionsart distinction, pragmatic expression, or focused stylistic repair.

**Authoring criterion:** Make the implication or allusion interpretable without invented history; do not hide a whole professional explanation.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Russian-speaking professional, social, and cultural domains

#### Required language and situation inventory

Include:

1. **One professional identity in Russian.**
2. **One stable Russian-speaking community.**
3. **One target social and regional model.**
4. **Broad cultural literacy.**
5. **Substantive responsibilities conducted in Russian.**

Use language situations drawn from:

- work, study, research, or volunteering in Russian;
- friendships maintained primarily in Russian;
- recurring group activities;
- disagreement, negotiation, and problem-solving;
- formal and informal correspondence;
- contemporary literature and long-form nonfiction;
- several generations’ speaking styles;
- comedy, irony, and cultural references;
- native editorial feedback;
- advanced pronunciation coaching.

#### Authoring brief

**Sentence contexts:** Work/study responsibilities, community interaction, negotiations, relationships, and cultural discussion.

**Focused hidden targets:** A verified domain-specific sense or social/register convention in context.

**Authoring criterion:** Name the relevant domain/community scope; card evidence is not a native-participation assessment.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Cover hard/soft consonants, **ы/и**, stressed versus reduced **о/а**, unstressed **е/я**, **ш/щ**, **ц/ч**, **х**, voicing assimilation, final devoicing, clusters, stress, phrasing, and intonation. The source’s **был/бил, мат/мать, угол/уголь, лук/люк, брат/брать** are meaningful contrast seeds.

Do not equate written vowels with fully articulated sounds in every position. Review stress and vowel reduction together with consonant softness and phrase boundaries. A stress mark copied from the lemma may be wrong for an inflection; verify the exact form before authoring its reading annotation.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Select sentences with real reductions, case endings, aspect contrasts, motion forms, particles, and marked focus where appropriate. Keep the accepted text distinct from a phonetic transcription. Preserve the morphology carrying the target and explain relevant reductions separately where useful. Social or regional variation requires attributed recognition rather than a mixed production norm.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Use contemporary practical language and accessible narratives before dense literary prose. Advance into nonfiction, argument, professional text, and literary/stylistic analysis. Make case governors, participial relations, aspect, motion, and information structure recoverable. Stress support belongs in annotations, not mandatory ordinary orthography; handwriting/cursive recognition is separately scoped.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Plan case contrasts by governor and meaning, aspect contrasts by event framing, and motion contrasts by route and habituality. Do not generate complete noun or verb tables merely by changing endings. The source’s reading/process-completion examples and present/habitual motion examples are contrast patterns to adapt into original contexts.

Hide a useful inflected word or compact phrase, not a whole English-to-Russian translation. Keep the governor visible when case selection is the target. For a stress-and-inflection objective, the hidden answer is ordinary written Russian and the support contains the correct stressed form. Word-order targets must leave a meaningful contrast visible rather than shuffle a full sentence without purpose.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `ru-RU`; source prefix is `ru`; the exact stage IDs are `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "ru-01-0001",
    "locale": "ru-RU",
    "sentence": "После работы я читаю газету.",
    "cloze": "газету",
    "answer": "газету",
    "accepted_answers": [],
    "lemma": "газета",
    "meaning": "a newspaper",
    "part_of_speech": "noun",
    "note": "Accusative singular of the feminine noun газета."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| Сейчас я иду в библиотеку. | `иду` | The current on-foot journey supports this motion choice; use ordinary unaccented spelling in the answer. |
| Мы интересуемся современной архитектурой. | `архитектурой` | The visible governor and adjective support an instrumental noun target. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Review forms of address, informal/formal relations, indirectness, professional explanation, disagreement, and emotional stance. A sentence may be grammatical but abrupt, overly intimate, or stylistically inappropriate. Avoid making all advanced Russian bureaucratic or literary; maintain ordinary social and neutral professional language.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check stress support, spelling, case, agreement, aspect, motion verbs, word order, government, vocabulary, collocation, register, punctuation, and translation-shaped phrasing. Preserve actors and reference in participial constructions. Editing for concision must not remove an aspectual or scope distinction that changes the claim.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **Поехали!** or **Между нами** as alternative curriculum scope references. The source names **A Comprehensive Russian Grammar**, **Русский язык в упражнениях**, OpenRussian, Грамота.ру, Russian for Free, Russian With Max, Easy Russian, Arzamas, PostNauka, YouGlish, and university TORFL material. Dictionary stress and government require checking the selected form, not copying an unsupported table.

| Reference | Authoring use |
|---|---|
| [Между нами](https://mezhdunami.org/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [OpenRussian](https://en.openrussian.org/) | Check the selected form, sense, construction, or register. |
| [Грамота.ру](https://gramota.ru/) | Check the selected form, sense, construction, or register. |
| [Russian for Free](https://www.russianforfree.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Russian With Max](https://www.russianwithmax.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Easy Russian](https://www.easy-languages.org/easy-russian) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Arzamas](https://arzamas.academy/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [YouGlish](https://youglish.com/russian) | Check the actual pronunciation, prosody, or variety of selected language. |
| [SPbU Testing Centre](https://testingcenter.spbu.ru/en/exam-preparation.html) | Check the stated task/framework boundary; do not copy examination items. |
| [St Petersburg University Language Testing Centre](https://testingcenter.spbu.ru/en/exams/russian/torfl.html) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| Lemma stress copied into every inflection | Verify the actual target’s stressed form. |
| Latin transliteration or lookalikes in the answer | Use the correct Cyrillic characters. |
| Aspect reduced to past/present or one perfective partner | Record the actual event framing and lexical partner relationship. |
| Motion prefixes introduced without route meaning | Establish directionality and spatial use before extensions. |
| Any word order treated as interchangeable | Provide the intended topic/focus/contrast. |
| Handwriting or TORFL competence claimed from typed cards | Keep those evidence categories separate. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained Russian authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-ru-RU`; the guide requires no separate proficiency-plan or conversation attachment.

**Authoring adaptations:** sentence briefs, focused-target rules, JSON design examples, coverage mapping, and authoring quality requirements implement the Meiki project’s card interaction. They are not official examination criteria or claims that the supplied proficiency guide specified this exact card format. Project production choices and English support are explicit in Sections 2–4 and 11. The exact stage counts and stage splits in Section 4.1 are explicit project production allocations, not official examination quotas or measured optimal learning quantities. Where the curriculum does not enumerate every lexical item, develop that inventory transparently within the fixed allocation; do not reduce the count or silently replace the curriculum.

| Supplied guide sections | Authoring treatment |
|---|---|
| 1–3: goal, variety, framework | Retained as production scope, recognition boundaries, and limits on proficiency claims. |
| 4–5: diagnosis and essential systems | Converted to prerequisite analysis and sentence-selection requirements. |
| 6: eight milestone inventories | Knowledge topics and endpoint distinctions retained; learner comprehension/production tasks become sentence briefs and focused targets. |
| 7–11: sound, listening, reading, grammar, vocabulary | Converted to sentence composition, cloze design, annotations, and written pronunciation support. |
| 12–13: interaction, feedback, writing | Converted to social-context and editorial criteria used in the shared author/editor/final-pass process, not separate topic audits or tutor/learner assignments. |
| 14: assessment | Converted to card-acceptance criteria, separate batch editing, one complete final editorial pass and basic completion checks; no native-human review or learner performance certification is claimed. |
| 15–16: resources and failures | Kept as reference roles and card-rejection/repair criteria, without purchasing or study schedules. |
| 17: source notes | Replaced by this self-contained basis and adaptation record; no absent chat or earlier guide is required. |

**Reference boundary:** Section 15 preserves curriculum and usage references; their current availability and every linguistic claim have not been rechecked for this package. Section 2.3 separately identifies the research consulted for the length policy. Verify material uncertain usage before production through permitted tools. A reference list does not authorize installations or release publication.

---
