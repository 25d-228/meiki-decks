# Chinese: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-zh-Hans-CN`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `zh-Hans-CN`  
**Scope:** the source’s Band 1–6-oriented and advanced HSK 7–9-oriented Chinese pathway, followed by domain specialization.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 10 stages; 10,000 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **Chinese** as the language name in all project text. The production model is **standard spoken Chinese (Putonghua), `zh-Hans-CN`, with Simplified Chinese characters**. Keep the character, vocabulary, grammar, and pronunciation conventions coherent.

The supplied guide also describes a Taiwan-oriented Traditional Chinese route. That route is not an additional production series in this assignment. Advanced passive recognition of Traditional forms can be planned explicitly without changing Simplified answers or treating script conversion as a complete regional adaptation.

Use Pinyin as pronunciation/lookup support, not as the normal typed answer. Display accurate target Pinyin on the answer side under the project convention. Keep character recognition, correct character selection during typing, and handwriting separate. No amount of typed completion demonstrates handwriting skill.

---

### 2.1. Short sentences: mandatory length contract

Keep **advanced meaning, not advanced length**. The following caps apply to the **entire `common.sentence` field per card**, with its cloze restored. They include both sides of a contrast, all quoted speech, and both turns/sentences of a micro-context. They are not separate allowances per clause. No advanced, literary, domain, quotation, or politeness exception raises a cap.

| Production stages | Preferred full-text length | Hard full-text maximum |
|---|---|---|
| `00–01` | 6–12 characters | **18 characters** |
| `02` | 10–18 characters | **26 characters** |
| `03–09` | 14–28 characters | **40 characters** |

**Hidden span:** normally 1–4 characters; hard maximum **8 characters**. Apply the same ceiling to each explicit accepted answer. This ceiling does not make an arbitrary fragment, entire predicate, or unrelated group of words a good cloze. A compact conventional whole utterance can be an editorially justified exception to the visible-context rule, but not to either length cap.

Preferred bands are drafting guidance, not minimums or quotas. Naturally shorter utterances are welcome. Do not pad them or write every card near the maximum. Advanced stages keep the same upper ceiling; difficulty comes from the selected sense, grammar, collocation, register, or pragmatic distinction.

**Characters:** normalize to NFC, then count every non-whitespace Unicode code point, **including punctuation, digits, and Latin text**. Use `sum(not ch.isspace() for ch in unicodedata.normalize("NFC", text))`. This definition is for the length check only; cloze boundaries still respect grapheme clusters. Do not strip punctuation, change standard spelling, use abbreviations, or compress numerals to game the count. Readings and answer-side notes are not part of `common.sentence`, but must never hide required front-side context.

**Character-based checking:** use the character count below, not whitespace words, model tokens, UTF-8 bytes, inferred syllables, or an unverified word segmenter. Mixed-script words and digits count character by character too. No tokenizer installation is needed.

Use **one short sentence by default**. At most two short sentences or two short conversational turns may form the source text when essential to interpretation; their **combined** text must fit the same cap. Do not add an uncounted preamble, a front-side `context` field, a screenshot, or an answer-side explanation as a way around the limit. Keep one primary target. Avoid stacked relative clauses, embedded chains, several unexplained participants, and unrelated facts. A brief subordinate or contrasting clause is allowed when it demonstrates the target.

Before accepting a card, verify that the source makes the relevant event/referent and the target's sense, relation, time, or social force interpretable. Remove decorative setup, not the governor, antecedent, negation, comparison, condition, or other essential cue. Text need not exclude every imaginable synonym, but the intended target must be natural and demonstrate the assigned use. Do not substitute an arbitrary fragment or ambiguous sense for useful context.

Keep required aspect, classifier, complement, and particle evidence. Count the complete character string rather than using a space-split word counter. Do not turn a short sentence into a list of chengyu or remove the antecedent needed for an omitted participant.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| 我把钥匙放在桌上了。 | `钥匙` | The object and its destination make the situation concrete. |
| 雨停了，我们再出发。 | `再` | The preceding event supports the sequence meaning. |
| 他口头赞成，却迟迟不肯签字。 | `迟迟` | Stated agreement contrasts with a continuing reluctance to sign. |

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

Keep the **international Chinese proficiency standard’s three stages and nine bands** separate from **HSK examinations**. Preserve the guide’s Band 1, 2, 3, 4, 5–6, and advanced groupings. Its advanced endpoint is advanced Chinese/HSK 7–9-oriented development, not an asserted balanced CEFR C2 equivalent.

The source treats strong HSK 6-oriented performance as a checkpoint within a broader pathway and requires separate oral evidence where the selected test does not establish speaking. Test specifications are version-sensitive; the supplied references are not a current verification. Do not invent a Taiwan certification route or turn vocabulary counts into examination guarantees.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **10 stages and exactly 10,000 accepted cards** for Chinese, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** A dedicated sound–character foundation and separate Band 1–4-oriented stages preserve the early progression. The shared Band 5–6 grouping is divided into two production stages, and the advanced grouping into two more, so lexical growth, written/spoken contrasts, mediation, and cultural recognition are not compressed into a single small advanced deck. These splits do not assert separate official examination syllabi.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `00` | Chinese 00 — Sound, characters, and sentence foundations | Sections 6.1 | 200 | 5 | 200 |
| `01` | Chinese 01 — Band 1-oriented basic communication | Sections 6.2 | 400 | 10 | 600 |
| `02` | Chinese 02 — Band 2-oriented routine communication | Sections 6.3 | 600 | 15 | 1,200 |
| `03` | Chinese 03 — Band 3-oriented independent communication | Sections 6.4 | 800 | 20 | 2,000 |
| `04` | Chinese 04 — Band 4-oriented extended communication | Sections 6.5 | 1,000 | 25 | 3,000 |
| `05` | Chinese 05 — Band 5–6-oriented lexical and discourse development | Sections 6.6, part A | 1,000 | 25 | 4,000 |
| `06` | Chinese 06 — Band 5–6-oriented professional and written communication | Sections 6.6, part B | 1,200 | 30 | 5,200 |
| `07` | Chinese 07 — Advanced lexical, rhetorical, and source precision | Sections 6.7, part A | 1,800 | 45 | 7,000 |
| `08` | Chinese 08 — Advanced mediation, literary, and cultural interpretation | Sections 6.7, part B | 1,800 | 45 | 8,800 |
| `09` | Chinese 09 — Social, professional, and cultural depth | Sections 6.8 | 1,200 | 30 | 10,000 |
| **Total** | **10 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **10,000** | **250** | **10,000** |

Use source IDs `zh-<stage>-0001` through `zh-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `zh-Hans-CN`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 00:** Use meaningful words and short sentences to cover initials/finals, tones, tone pairs, sandhi, basic characters, clarification, and early sound–character links.
- **Stage 01:** Cover basic predicates, negation, questions, quantities, classifiers, location, modals, family, routine, food, and ordinary transactions.
- **Stage 02:** Cover completed action versus changed state, experiential/progressive/durative aspect, early complements, comparisons, relatives, and practical explanations.
- **Stage 03:** Develop complement systems, ba/bei constructions, topic–comment, particles, clause relations, narration, and repair while expanding useful word senses.
- **Stage 04:** Allocate substantive lexical/collocational breadth, source comparison, formal/informal reformulation, proposals, and extended discourse; identify authored extensions rather than inventing an official grammar list.
- **Stage 05:** Prioritize precise aspect and complements, idioms in use, cohesive devices, native-style narrative, and broad everyday, social, and nonfiction vocabulary.
- **Stage 06:** Complete the grouping with written/spoken contrasts, abstract positions, professional explanation, qualifications, indirect requests/criticism, and terminology in recoverable contexts.
- **Stage 07:** Develop the advanced lexical inventory, precise source relations, argument structure, formal language, idioms, collocations, and rhetorical choices beyond stages 05–06.
- **Stage 08:** Complete advanced mediation, literary interpretation, layered stance, cultural expressions, regional recognition, and labeled Traditional-character recognition without changing active script.
- **Stage 09:** Cover selected community and domain language, negotiation, relationships, professional responsibilities, conventions, and culturally situated stance with clear scope.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Do not count familiar-looking Japanese kanji as known Chinese words. Check the Chinese reading, tone, Simplified form, word formation, meaning, grammatical behavior, and false-friend risk. Prior experience with another tonal language or Chinese variety does not establish the selected tone categories, sandhi, weak syllables, vocabulary, or prosody.

Introduce characters and meaningful phrases alongside sound work. Do not insert a months-long Pinyin-only sequence, a radical-memorization prerequisite, or an unverified complete character-reading inventory.

---

## 5. Essential systems to represent in sentences

### Sound–word–character links
Connect initials, finals, tones, neutral tone, tone combinations, sandhi, weak syllables, stress, and phrasing to real words. A character is not automatically a word; do not create **开 = open**, **打 = hit**, **上 = up**, or **下 = down** cards as a substitute for their constructions.

### Clause organization and aspect
Cover subject–verb–object and time/location patterns, serial verbs, modification, and topic–comment structure. Distinguish **不/没**, action-completion and change-of-state **了**, experience **过**, progressive **在/正在**, and durative **着**. Keep situation and intended event framing visible; do not label **了** simply “past tense.”

### Complements and grammatical frames
Cover result, direction, degree, and potential complements; **把/被**; **比** comparisons; measure words/classifiers; and pivotal and double-object patterns. Literal and extended directional meanings require distinct contextual objectives. Do not count the presence of a classifier in visible text as successful classifier retrieval coverage.

### Discourse and usage
Include sentence-final particles, ellipsis, cohesive devices, source qualification, natural topic management, polite disagreement, and indirect requests or criticism. Identify speaker stance without invented context.

### Lexical and cultural detail
Select compounds and phonetic/component families through actual vocabulary. For a chengyu or other four-character expression, distinguish literal/historical associations from contemporary meaning, collocation, register, and appropriate use. Cultural references need verified meaning and sufficient visible context; do not invent a quotation, story, or historical fact to make a card work.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Pinyin, tones, characters, and basic sentence foundation

#### Required language and situation inventory

Include:

- `j/q/x` versus `zh/ch/sh`;
- `z/c/s` versus `zh/ch/sh`;
- Chinese `r`;
- `ü` versus `u`;
- `e`, `o`, `uo`, and `ou`;
- `an/ang`;
- `en/eng`;
- `in/ing`;
- `ian/iang`;
- `uan/uang`;
- apical vowels after `z/c/s` and `zh/ch/sh/r`;
- four lexical tones and neutral tone.

Then begin:

- two-syllable tone combinations;
- partial third tone;
- third-tone sandhi;
- tone changes involving 一 and 不;
- neutral-tone words;
- basic sentence stress.

Do not specify Pinyin sounds through English spelling conventions.

Introduce characters, useful beginner chunks, and typed form alongside sound–meaning links. Do not require an isolated Pinyin course as a prerequisite to sentence authoring.

#### Authoring brief

**Sentence contexts:** Identity, clarification, elementary questions, quantities, and useful phrases with direct sound–character links.

**Focused hidden targets:** A meaningful word or short expression exposing a selected initial/final, tone, or spelling distinction.

**Authoring criterion:** Do not make Pinyin the typed answer or require mastery of every character before sentence work.

### 6.2. Basic communication

**Curriculum reference:** Band 1-oriented basic communication

#### Required language and situation inventory

- basic subject–verb–object order;
- time–manner–place ordering;
- 是, 有, 在;
- basic negation with 不 and 没;
- question particles and question words;
- numbers, dates, time, age, prices;
- measure words;
- possession and modification with 的;
- modal verbs;
- basic adjective predicates;
- location phrases;
- simple serial-verb constructions;
- basic comparisons;
- common sentence-final particles.

#### Authoring brief

**Sentence contexts:** Family, routine, preferences, work/study, ordering food, location, and basic transactions.

**Focused hidden targets:** A word, classifier, question component, location frame, modal, or simple predicate from the inventory.

**Authoring criterion:** Pair every selected word with correct characters and Pinyin; keep basic word order and negation contextual.

### 6.3. Routine communication

**Curriculum reference:** Band 2-oriented routine communication

#### Required language and situation inventory

- completed-action 了;
- change-of-state 了;
- experiential 过;
- progressive 在/正在;
- durative 着;
- result complements;
- basic directional complements;
- degree complements;
- more extensive measure-word use;
- comparison with 比;
- relative clauses;
- conjunctions for cause, condition, sequence, and contrast;
- introduction to 把;
- common double-object and pivotal constructions.

Do not label 了 an English-style past-tense ending. Author its functions through complete patterns and situations.

#### Authoring brief

**Sentence contexts:** Recent events, changed situations, practical problems, comparisons, clarification, and simple process explanation.

**Focused hidden targets:** An aspect marker in context, result/directional/degree component, comparison, or compact construction.

**Authoring criterion:** State the event interpretation and distinguish completion from change of state; do not call all 了 past tense.

### 6.4. Independent communication

**Curriculum reference:** Band 3-oriented independent communication

#### Required language and situation inventory

- full use of common result complements;
- directional complements in literal and extended meanings;
- 把 constructions;
- passive 被 constructions;
- potential complements;
- complex noun modification;
- topic–comment structures;
- rhetorical questions;
- increasingly natural sentence-final particles;
- conditional, concessive, causal, and purpose clauses;
- formal versus conversational alternatives;
- basic discourse organization.

#### Authoring brief

**Sentence contexts:** Narration, social explanations, summaries, opinions, literal/extended direction, and practical repair.

**Focused hidden targets:** A complement, topic/comment component, 把/被 expression, particle, or conditional/concessive relation.

**Authoring criterion:** Make agency, reference, and discourse status recoverable; use a new meaning or construction rather than a cosmetic topic change.

### 6.5. Upper-intermediate operation

**Curriculum reference:** Band 4-oriented operation with increasing native input

#### Required language and situation inventory

Consolidate the Band 1–3-oriented grammar systems under greater discourse complexity. Develop pronunciation/prosody, grammatical accuracy, narration, description, discussion, argument, source comparison, and formal versus informal communication. The source does not provide a separate itemized Band 4 grammar inventory; this milestone retains its functional emphasis rather than inventing one.

#### Authoring brief

**Sentence contexts:** General discussion, proposals, complaints, source comparison, and formal/informal reformulation.

**Focused hidden targets:** A substantively extended use of known grammar, more precise collocation, or discourse relation.

**Authoring criterion:** The source supplies no separate exhaustive Band 4 grammar list. Record the inventory gap and justify each selected extension instead of inventing an official list.

### 6.6. Advanced development

**Curriculum reference:** Band 5–6-oriented / strong HSK 6-oriented checkpoint

#### Required language and situation inventory

- precise aspect choice;
- advanced complements;
- natural topic management;
- ellipsis and omission;
- cohesive devices;
- formal written constructions;
- conversational particles;
- four-character expressions used naturally;
- common idioms;
- professional terminology;
- rhetorical structures;
- differences between written and spoken Chinese;
- polite disagreement;
- indirect requests and criticism.

#### Authoring brief

**Sentence contexts:** Professional general tasks plus native-style narrative, abstract positions, evidence, and qualified disagreement.

**Focused hidden targets:** A precise aspect/complement use, cohesive device, useful idiom, written/spoken distinction, or indirect request.

**Authoring criterion:** Keep domain terminology in understandable situations, and distinguish lexical meaning from pragmatic implication.

### 6.7. Proficient integration

**Curriculum reference:** Advanced stage / HSK 7–9-oriented development

#### Required language and situation inventory

Develop broad general and specialist comprehension, synthesis, argument, translation or mediation, formal writing, literary interpretation, group interaction, pronunciation/style, and regional or dialect-influenced Chinese.

Include:

- major twentieth- and twenty-first-century events;
- common literary references;
- frequently used historical figures and stories;
- idiomatic four-character expressions;
- internet slang;
- media discourse;
- regional stereotypes and sensitivities;
- formal etiquette;
- conversational expectations.

Do not author context-free chengyu lists. Document each selected expression with:

- its literal meaning;
- actual contemporary meaning;
- register;
- common collocations;
- one natural example;
- situations in which it sounds pretentious or inappropriate.

For approved broad-literacy coverage, distinguish passive Traditional recognition from Simplified typed production; handwriting remains outside this card format.

#### Authoring brief

**Sentence contexts:** Multi-source argument, mediation, literary interpretation, formal writing, cultural expression, and regional recognition.

**Focused hidden targets:** A compact synthesis relation, rhetorical expression, verified idiom, or natural response/paraphrase.

**Authoring criterion:** Keep literal, historical, and contemporary meanings separate; do not invent cultural facts or silently convert the active script.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Chinese-speaking professional, social, and cultural domains

#### Required language and situation inventory

Include these language and interactional dimensions:

- prosody;
- conversational turn management;
- word choice;
- register;
- rhetorical organization;
- indirectness;
- humor;
- interruption;
- cultural assumptions;
- regional variation;
- group interaction;
- professional identity.

**Situation domains and limits of card evidence**

The source’s real-use domains supply situations, not outcomes a card can certify:

- friendships conducted principally in Chinese;
- group rather than only one-to-one interaction;
- real responsibilities in Chinese;
- work, study, volunteering, or research;
- disagreement and problem-solving;
- repeated contact with the same community;
- exposure to several generations and social backgrounds.

Include the language of these three domain groups:

1. **Ordinary social life**
2. **Your professional or academic field**
3. **One cultural or intellectual field**

Examples of the third area include cinema, literature, technology culture, economics, music, history, or current affairs.

#### Authoring brief

**Sentence contexts:** Relationships, work/study responsibilities, negotiation, cultural discussion, and group decisions in selected communities.

**Focused hidden targets:** A domain-specific sense, convention, phrase, or stance distinction with recoverable social circumstances.

**Authoring criterion:** Name the community/domain scope. Cards do not demonstrate real-world responsibility, handwriting, or broad near-native competence.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Cover **j/q/x vs zh/ch/sh**, **z/c/s vs zh/ch/sh**, **r**, **ü/u**, **e/o/uo/ou**, **an/ang**, **en/eng**, **in/ing**, **ian/iang**, **uan/uang**, and the vowel patterns after **z/c/s** and **zh/ch/sh/r**. Include four lexical tones, neutral tone, real disyllabic combinations, partial third tone, third-tone sandhi, **一/不** changes, weak syllables, and sentence prominence.

Document how Pinyin represents lexical tones and how notes explain connected-speech changes; do not alternate conventions silently. Review every syllable and context-dependent reading. The source’s **经理 jīnglǐ / 经历 jīnglì** pair is a contrast seed, not proof that isolated tone identification covers connected speech. Its learner listening-diagnostic percentages are not text-card acceptance thresholds.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Choose sentences that expose meaningful initials/finals, tones, complements, aspect, particles, omission, and word boundaries. Keep transcription faithful to the accepted characters and utterance. Textual phonological support does not establish understanding of several accents or fast overlapping discussion. Recognition-only regional wording must be attributed and kept distinct from production.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress through messages, signs, menus, dialogues, and graded narrative toward source comparison, explanation, journalism-style text, literature, and professional writing. Use character-first text with answer-side Pinyin. Make compounds and clause relations clear without English character-by-character equations. Treat advanced Traditional recognition as a separate mapped recognition objective; it is neither new vocabulary automatically nor permission to change the active script.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Build full-sentence situations for **不/没**, the two **了** functions, **过**, **在/正在**, **着**, result/potential complements, **把/被**, **比**, and topic–comment organization. Hide a complete useful word or compact grammatical component. Do not reject a valid target because Chinese lacks spaces.

For **感兴趣**, choose a word/construction target that fits the curriculum; do not mechanically hide the arbitrary character **感** or the whole proposition **对这个问题很感兴趣**. The source’s collocation families around **会议** can generate natural original sentences, not lists of verbs sharing a blank. Explain character-level targets only when a deliberate morphemic objective justifies them.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `zh-Hans-CN`; source prefix is `zh`; the exact stage IDs are `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "zh-03-0001",
    "locale": "zh-Hans-CN",
    "sentence": "我把钥匙放在桌上了。",
    "cloze": "钥匙",
    "answer": "钥匙",
    "accepted_answers": [],
    "lemma": "钥匙",
    "meaning": "key; keys",
    "part_of_speech": "noun",
    "note": "The second syllable is neutral-tone in this reading."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| 这件事我已经跟经理说过了。 | `经理` | Check jīnglǐ against the manager sense; do not substitute a visually similar or differently toned word. |
| 行李太多了，我一个人拿不动。 | `拿不动` | The visible load supports a potential-complement target; do not hide the whole explanation. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Review natural omission, request softening, indirect criticism, polite disagreement, turn recovery, and professional explanation. Identify whether a mismatch concerns a tone, grammar, word choice, reference, register, or social relation. Do not classify every misunderstanding as missing vocabulary. No card should require knowing an unseen previous turn or an unstated community convention.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check word order, aspect, complements, classifiers, collocations, register, character choice, punctuation, and translation-shaped phrasing. Use original messages, summaries, reports, and audience-sensitive explanations. Keep the distinction between typed character selection and handwritten form/stroke order explicit. Preserve source stance and conditions when compressing an argument.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **Integrated Chinese** or the source-listed Yoyo route as a scope reference; its advanced alternatives are **Developing Chinese**, **Boya Chinese**, or an appropriate HSK-aligned course. Pleco, Chinese Grammar Wiki, graded-reader catalogues, Du Chinese, The Chairman’s Bao, conversation transcripts, and official Chinese-test materials serve different reference purposes. Handwriting services do not turn typed cards into handwriting exercises.

| Reference | Authoring use |
|---|---|
| [Cheng & Tsui](https://www.cheng-tsui.com/resources/ic) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [HelloChinese — source-listed course entry](https://apps.apple.com/jp/app/hellochinese-learn-chinese/id1001507516?l=en-US&platform=vision) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Yoyo Chinese](https://yoyochinese.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Pleco — source-listed dictionary entry](https://apps.apple.com/jp/app/pleco-chinese-dictionary/id341922306?l=en-US&platform=vision) | Check the selected form, sense, construction, or register. |
| [Allset Learning Resources](https://resources.allsetlearning.com/chinese/grammar/Main_Page) | Check the selected form, sense, construction, or register. |
| [Du Chinese](https://duchinese.net/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Chinese graded-reader catalogue](https://mandarincompanion.com/nclc/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [The Chairman's Bao](https://www.thechairmansbao.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Chinese Test Service](https://www.chinesetest.cn/hsk) | Check the stated task/framework boundary; do not copy examination items. |
| [Chinese advanced-test reference](https://m.chinesetest.cn/HSK/7-9) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| Chinese named inconsistently across artifacts | Use Chinese; preserve the specified zh-Hans-CN locale. |
| A character counted as a complete word inventory | Track words, senses, characters, and retrieval coverage separately. |
| Pinyin loses syllables or uses unchecked tone defaults | Review the exact target reading in context. |
| 了 treated as past tense or complements as interchangeable | Keep event and construction contrasts explicit. |
| Band 4 grammar supplied as an invented official list | State the source gap and identify proposed selections separately. |
| Traditional recognition becomes mixed active spelling | Keep recognition attributed and the expected production in Simplified Chinese. |
| HSK counts presented as C2 or handwriting evidence | Preserve the framework and skill boundaries. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained Chinese authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-zh-Hans-CN`; the guide requires no separate proficiency-plan or conversation attachment.

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
