# Spanish: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-es-MX`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `es-MX`  
**Scope:** A1–C2-oriented Spanish, with a separate layer for regional, professional, social, and cultural specialization.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 7 stages; 7,600 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **educated contemporary central Mexican Spanish (`es-MX`)** for production. This is the project selection within the supplied guide’s regional options. Keep pronunciation, ordinary vocabulary, address forms, tense distribution, and pragmatic conventions coherent. Use `tú`, `usted`, and `ustedes` where the relationship requires them; do not alternate into productive `vos` or `vosotros`.

From the B1-oriented material onward, plan labeled recognition of other varieties, including the Spain, Colombia, and River Plate routes named by the guide. The production answer should remain compatible with the selected model unless the approved objective explicitly concerns recognition of attributed regional wording. Do not call all non-Mexican usage incorrect or label a shared expression exclusively Mexican. A dictionary’s unmarked entry alone does not establish regional frequency.

---

### 2.1. Short sentences: mandatory length contract

Keep **advanced meaning, not advanced length**. The following caps apply to the **entire `common.sentence` field per card**, with its cloze restored. They include both sides of a contrast, all quoted speech, and both turns/sentences of a micro-context. They are not separate allowances per clause. No advanced, literary, domain, quotation, or politeness exception raises a cap.

| Production stages | Preferred full-text length | Hard full-text maximum |
|---|---|---|
| `01` | 4–9 words | **12 words AND 90 characters** |
| `02` | 6–12 words | **16 words AND 120 characters** |
| `03–07` | 8–14 words | **20 words AND 150 characters** |

**Hidden span:** normally 1–3 words; hard maximum **5 words AND 40 characters**. Apply the same ceiling to each explicit accepted answer. This ceiling does not make an arbitrary fragment, entire predicate, or unrelated group of words a good cloze. A compact conventional whole utterance can be an editorially justified exception to the visible-context rule, but not to either length cap.

Preferred bands are drafting guidance, not minimums or quotas. Naturally shorter utterances are welcome. Do not pad them or write every card near the maximum. Advanced stages keep the same upper ceiling; difficulty comes from the selected sense, grammar, collocation, register, or pragmatic distinction.

**Characters:** normalize to NFC, then count every non-whitespace Unicode code point, **including punctuation, digits, and Latin text**. Use `sum(not ch.isspace() for ch in unicodedata.normalize("NFC", text))`. This definition is for the length check only; cloze boundaries still respect grapheme clusters. Do not strip punctuation, change standard spelling, use abbreviations, or compress numerals to game the count. Readings and answer-side notes are not part of `common.sentence`, but must never hide required front-side context.

**Words:** count maximal Unicode letter/number sequences, allowing internal straight or curly apostrophes. Hyphens, slashes, and dashes separate units; punctuation-only pieces do not count as words. Thus contractions/elisions remain natural, while hyphenation cannot join several words into one for this check. Use a small standard-library counter, for example `re.findall(r"[^\W_]+(?:['’][^\W_]+)*", NFC_text)`. This is an operational count, not a linguistic segmentation theory. Both the word limit and character limit must pass.

Use **one short sentence by default**. At most two short sentences or two short conversational turns may form the source text when essential to interpretation; their **combined** text must fit the same cap. Do not add an uncounted preamble, a front-side `context` field, a screenshot, or an answer-side explanation as a way around the limit. Keep one primary target. Avoid stacked relative clauses, embedded chains, several unexplained participants, and unrelated facts. A brief subordinate or contrasting clause is allowed when it demonstrates the target.

Before accepting a card, verify that the source makes the relevant event/referent and the target's sense, relation, time, or social force interpretable. Remove decorative setup, not the governor, antecedent, negation, comparison, condition, or other essential cue. Text need not exclude every imaginable synonym, but the intended target must be natural and demonstrate the assigned use. Do not substitute an arbitrary fragment or ambiguous sense for useful context.

Preserve the governor for a pronoun, the time frame for tense/mood, and the condition for a hypothetical. A short request can still establish urgency and social relationship. Do not replace a tested construction with a simpler different learning point merely to save words.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| El autobús llega a las ocho. | `llega` | A schedule supplies a clear situation for the present form. |
| Aunque me lo hubieran pedido antes, no habría aceptado. | `habría aceptado` | A compact counterfactual preserves the condition and consequence. |
| Su disculpa fue tibia: evitó reconocer el daño. | `tibia` | The explanation makes the figurative judgment interpretable. |

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

Keep **DELE A1 → A2 → B1 → B2 → C1 → C2** and the additional **SIELE route through C1** distinct. These are the supplied curriculum’s reference routes, not card-completion certificates or a claim that SIELE supplies a C2 qualification. Foundation supports A1; domain specialization remains distinct from C2. Use examination material to identify communicative demands, not to copy test questions or introduce examination score requirements for cards.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **7 stages and exactly 7,600 accepted cards** for Spanish, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

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

Use source IDs `es-<stage>-0001` through `es-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `es-MX`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 01:** Integrate sound–spelling, survival language, present forms, noun agreement, questions, modal frames, and ordinary household, service, work, and social vocabulary.
- **Stage 02:** Cover past/background contrasts, object and reflexive pronouns, commands, comparisons, duration, periphrases, and expanded practical vocabulary.
- **Stage 03:** Cover narration and aspect, present subjunctive, clitic order, se functions, reporting, conditionals, ser/estar and por/para contrasts, and explanation across everyday domains.
- **Stage 04:** Cover past subjunctive and conditionals, complex reporting and relatives, concession, stance, collocations, register, and regional recognition in varied situations.
- **Stage 05:** Protect broad lexical senses and collocations alongside source synthesis, implied stance, qualification, professional explanation, turn management, and indirectness.
- **Stage 06:** Cover mediation, rhetoric, literary interpretation, idioms, humor, understatement, social variation, editing, and diplomatic language with contextual support.
- **Stage 07:** Retain all five coverage dimensions and develop distinct domain senses, community conventions, negotiations, relationships, and cultural references beyond the same C2 uses.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

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

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

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

**Authoring criterion:** Keep elementary grammar, natural phrasing, and useful written pronunciation support together.

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

**Authoring criterion:** Make the blank test the declared objective. Keep any formula containing later grammar narrowly identified rather than expanding the A1 system silently.

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

**Authoring criterion:** Keep time reference and pronoun antecedents clear; preserve Mexican-compatible tense distribution rather than imposing a different national preference.

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

**Authoring criterion:** Distinguish background from event and speaker assertion from reported position. Do not hide the complete subordinate proposition.

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

**Authoring criterion:** The context must support the qualification and the intended relation among claims. Different wording must add a real distinction beyond B1.

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

**Authoring criterion:** Do not turn every example into administrative or technology terminology. Preserve source stance, beneficiary, and unresolved disagreement.

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

**Authoring criterion:** The literal situation must support the intended effect. Keep complete syntheses, rewritten paragraphs, and joke punchlines out of oversized blanks.

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

**Authoring criterion:** Name the selected domain and relationship. Cards support its language; they do not prove community membership or unrestricted near-native performance.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Cover five stable vowel qualities, word stress, syllable grouping, tapped **r** and trilled **rr**, **j**, **ñ**, the selected **ll/y** realization, dental **t/d**, limited English-style aspiration of **p/t/k**, and linking across words. Include the source’s **pero/perro** contrast in meaningful contexts, not invented syllable drills.

Select sentences that expose stress and connected phrasing without tongue-twister density. Record the intended question, contrast, or quotation reading when it matters. Document relevant vowel stability, duration, consonant realization, phrase grouping, and intonation in the written support; accurate **rr** alone is not the whole pronunciation inventory. Regional **s**, **c/z**, and final-consonant differences belong to the declared production or recognition scope.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Include ordinary pronoun sequences, tense/mood cues, linking, discourse markers, and regional vocabulary in self-contained utterances. A sentence must still make sense when heard without the annotations. Do not rely on a cognate’s apparent English meaning to explain what was spoken. Advanced conversational sentences may model interruption recovery or qualification, but a short written example does not establish multi-speaker comprehension.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from messages, signs, practical exchanges, and graded narrative to accessible explanation, journalism-style argument, fiction, and professional writing. Use original short cases rather than lifted passages. Make the reference of object pronouns, the function of **se**, and the relation between clauses recoverable. Preserve a clear distinction between a literary or formal register and ordinary conversation.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Use contrast families for **ser/estar**, **por/para**, **indefinido/imperfecto**, regional **perfecto**, indicative/subjunctive, commands with clitics, and the different functions of **se**. Change the situation or interpretation that makes the contrast useful, not just a person’s name.

For a construction such as **darse cuenta de que**, either target a justified compact construction or its learning-bearing preposition with sufficient context. Do not hide the entire realization clause. In a pronoun exercise, hiding **se me** is different from hiding the whole event; state which distinction the card tests. Short repeated forms such as **de** are permissible across genuinely different frames.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `es-MX`; source prefix is `es`; the exact stage IDs are `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "es-01-0001",
    "locale": "es-MX",
    "sentence": "El autobús llega a las ocho.",
    "cloze": "llega",
    "answer": "llega",
    "accepted_answers": [],
    "lemma": "llegar",
    "meaning": "arrives",
    "part_of_speech": "verb",
    "note": "The present tense gives the scheduled arrival time here."
  },
  "language_specific": {}
}
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

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check gender, agreement, tense, mood, articles, pronouns, prepositions, word order, vocabulary, collocation, register, and punctuation. Keep grammatical correctness distinct from the wording an educated speaker in the selected setting would naturally use. At advanced levels, a shortened or more diplomatic version must preserve agency, qualification, comparison, and commitment.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

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

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

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

**Content basis:** this self-contained Spanish authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-es-MX`; the guide requires no separate proficiency-plan or conversation attachment.

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
