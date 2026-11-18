# Portuguese: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-pt-BR`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `pt-BR`  
**Scope:** A1–C2-oriented Brazilian Portuguese, with labeled Lusophone recognition and domain-specific development.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 8 stages; 7,800 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **Brazilian Portuguese (`pt-BR`)**, with educated contemporary **São Paulo** usage as the initial production model. This repository's national variety is settled. European Portuguese is a labeled recognition/comparison scope, not a second productive curriculum or a reason to ask HUMAN to choose the locale again.

Keep sound, rhythm, ordinary vocabulary, address, agreement, clitic placement, and edited/spoken style coherent. The foundation inventory below separates shared, Brazilian, and European material explicitly. **estar + gerund** and **estar a + infinitive** are not to alternate randomly in production.

From B1-oriented work onward, plan labeled recognition of European Portuguese; from C1 onward, the guide also allows selected Angolan, Mozambican, Cape Verdean, Guinean, São Toméan, East Timorese, and diaspora material when relevant. Such material is not automatically approved for productive answers.

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

Preserve Brazilian address, clitic placement, natural contractions, and the condition or subject needed for subjunctive/personal-infinitive interpretation. Do not switch to a different national production construction to save words.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| Preciso de uma caneta para assinar o formulário. | `Preciso de` | A practical purpose makes the need clear. |
| Mesmo que o prazo fosse maior, eu não aceitaria essa condição. | `aceitaria` | The hypothetical condition supports the consequence. |
| A proposta é viável, desde que o custo permaneça dentro do orçamento. | `desde que` | A concrete budget condition supports the connective. |

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

Keep the **CAPLE** route **ACESSO A1 → CIPLE A2 → DEPLE B1 → DIPLE B2 → DAPLE C1 → DUPLE C2** separate from Brazil’s **Celpe-Bras** integrated-performance route. The latter is not an A1–C2 staircase and does not supply a direct Celpe-Bras-to-CEFR conversion in this source.

For the Brazilian route, A1–C2 are the guide’s functional planning labels. For the European route, CAPLE supplies the stated examination reference. Neither card totals nor a certificate establishes unrestricted near-native social, professional, or cross-variety competence.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **8 stages and exactly 7,800 accepted cards** for Portuguese, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** A foundation stage protects variety-specific sound and phrase work. Subsequent stages preserve clitics, contractions, tense/mood, personal infinitive, future subjunctive, social address, and cross-variety recognition. Use these counts for the Brazilian production route while preserving the required labeled recognition scope.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `00` | Portuguese 00 — Sound, variety, and sentence foundations | Sections 6.1 | 200 | 5 | 200 |
| `01` | Portuguese 01 — A1 basic communication | Sections 6.2 | 600 | 15 | 800 |
| `02` | Portuguese 02 — A2 routine communication | Sections 6.3 | 800 | 20 | 1,600 |
| `03` | Portuguese 03 — B1 independent communication | Sections 6.4 | 1,000 | 25 | 2,600 |
| `04` | Portuguese 04 — B2 extended communication | Sections 6.5 | 1,200 | 30 | 3,800 |
| `05` | Portuguese 05 — C1 precise communication | Sections 6.6 | 1,400 | 35 | 5,200 |
| `06` | Portuguese 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,600 | 40 | 6,800 |
| `07` | Portuguese 07 — Lusophone social, professional, and cultural depth | Sections 6.8 | 1,000 | 25 | 7,800 |
| **Total** | **8 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **7,800** | **195** | **7,800** |

Use source IDs `pt-<stage>-0001` through `pt-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `pt-BR`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 00:** Cover the chosen variety’s vowels, nasalization, stress, reduction, consonants, basic progressive, contractions, clarification, and useful phrases.
- **Stage 01:** Cover articles/agreement, present/irregular verbs, existence, address forms, contractions, plans, modals/needs, quantities, and the chosen progressive pattern.
- **Stage 02:** Cover past/background, object/reflexive pronouns, commands, comparison, por/para, se, duration, relatives, periphrases, and bounded subjunctive formulas.
- **Stage 03:** Cover present/future subjunctive, personal infinitive, pronoun combinations, se distinctions, reporting, clause relations, conditionals, and target-variety clitic placement.
- **Stage 04:** Develop mood/hypothesis contrasts, complex infinitives and relatives, clitic systems, stance, reformulation, collocations, and edited-versus-conversational norms.
- **Stage 05:** Cover synthesis, implied stance, advanced vocabulary/collocations, professional explanation, meetings, mitigation, register, and wider Lusophone recognition.
- **Stage 06:** Cover mediation, rhetoric, idioms, irony, literary interpretation, editing, diplomacy, and cross-variety understanding without inventing a Brazilian C2 certificate.
- **Stage 07:** Retain one production model while developing distinct domain senses, relationships, responsibilities, negotiation, cultural discussion, and labeled regional interpretation.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Do not assume Spanish or English cognates establish Portuguese pronunciation, vowels, nasalization, syntax, prepositions, or ordinary meaning. Investigate the source’s **pasta, apelido, puxar, pretender, assistir, esquisito** in the selected variety rather than teach them as automatic equivalents.

Record sound, gender, open/closed stressed vowel where necessary, nasalization, collocation, complement, register, and regional meaning. Distinguish **análise/analisar** constructions from a bare translation. Do not postpone the personal infinitive and future subjunctive beyond the B1-oriented inventory.

---

## 5. Essential systems to represent in sentences

### Variety-specific sound and spelling
Cover open/closed **e/o**, oral/nasal vowels, **ão/ãe/õe**, stress/accents, final vowels, **lh/nh**, regional **r/s**, linking, and reduction. The source names **avó/avô, pode/pôde, tem/têm, vem/vêm** as contrast seeds. Review pronunciation in the selected variety rather than imposing Spanish vowels or English diphthongs.

### Contractions and verb government
Cover **do, na, pelos, ao, daquele, nisto** and other selected preposition–article/pronoun combinations as grammar, not optional abbreviations. Include **gostar de**, **precisar de**, **ir ao**, **estar na**, and **falar sobre** frames. Distinguish written **à/às** through actual constructions. For **assistir**, verify the chosen sense, complement, variety, and register; do not present one formal pattern as the only casual Brazilian use.

### Pronouns and register
Cover **me, te, se, o, a, os, as, lhe, lhes, nos, vos** and relevant combinations according to route and register. Brazilian ordinary speech and formal edited writing may use different preferred placements; European affirmative enclisis and triggered proclisis need complete contexts. Treat mesoclisis mainly as advanced formal recognition unless an approved domain requires production.

For Brazilian use, plan **você**, locally appropriate **tu** agreement, **a gente/nós**, **o senhor/a senhora**, and titles. For European use, plan **tu**, third-person address and omitted subjects, names/titles, and context-sensitive overt **você**. Do not infer a universal pronoun chart from either route.

### High-value verb systems and lexical families
Include the **personal infinitive** and **future subjunctive** at B1-oriented level. Make the subject and temporal/conditional relation clear. Distinguish the senses of **ficar** through such families as **ficar em casa**, **ficar preocupado**, **ficar com**, and **ficar de fazer**. For **conta**, distinguish realization, taking into account, independence, and paying a bill. Regional vocabulary such as **ônibus/autocarro, trem/comboio, celular/telemóvel** belongs to labeled recognition or the chosen production route, not random alternation.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Variety, sound, and basic sentence foundation

#### Required language and situation inventory

Include:

- Portuguese spelling-to-sound relationships;
- word stress and written accents;
- open and closed **e/o**;
- oral and nasal vowels;
- **ão** and other nasal diphthongs;
- **lh** and **nh**;
- common realizations of **r** and **s** in your target region;
- linking and resyllabification;
- target-variety rhythm.

**Brazilian production branch**

- final unstressed **e** and **o** behavior;
- **t/d** before an /i/-like vowel in your chosen region;
- final **l** in your target model;
- regional **r** and syllable-final **s**;
- ordinary use of **estar + gerund**.

**European comparison inventory — recognition, not the Brazilian production model**

- central reduced vowel **/ɨ/** and related spelling patterns;
- reduction or loss of unstressed vowels;
- consonant-heavy phrase perception;
- syllable-final **s** patterns;
- ordinary use of **estar a + infinitive**;
- early recognition of enclitic pronouns.

#### Authoring brief

**Sentence contexts:** Identity, clarification, basic questions, and short phrases in the chosen national model.

**Focused hidden targets:** A meaningful word, contraction, sound–spelling distinction, or basic progressive component.

**Authoring criterion:** Apply the Brazilian production branch. Retain the European inventory for labeled comparison/recognition at the appropriate stage, not as interchangeable Brazilian answers or an extra foundation prerequisite.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

- noun gender and number;
- definite and indefinite articles;
- subject pronouns appropriate to your variety;
- present tense of regular verbs;
- approximately 25 high-frequency irregular verbs;
- **ser, estar, ter, haver, ir, vir, fazer, poder, querer, dizer, dar, ver, saber, conhecer, pôr, ficar**;
- **há** for existence, with awareness of common spoken Brazilian **tem** where relevant;
- adjective agreement;
- negation and questions;
- possessives and demonstratives;
- contractions with **de, em, por, a**;
- numbers, dates, time, prices, and quantities;
- **ir + infinitive**;
- **ter de/que**, **poder**, **querer**, and **precisar de**;
- the target-variety progressive;
- introductory direct objects.

#### Authoring brief

**Sentence contexts:** Home, routine, family, work, preferences, plans, quantities, and basic transactions.

**Focused hidden targets:** Present/irregular form, article/agreement, contraction, existence, modal/need frame, or progressive.

**Authoring criterion:** Keep há versus spoken Brazilian tem appropriately labeled; respect the selected address and production system.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

- **pretérito perfeito simples**;
- introduction to **pretérito imperfeito**;
- direct and indirect object pronouns in target-variety patterns;
- reflexive verbs;
- affirmative and negative commands;
- comparisons and superlatives;
- **por** and **para**;
- common uses of **se**;
- relative pronouns **que, quem, onde**;
- duration with **há, faz, desde, desde que**;
- frequent verbal periphrases;
- introductory present subjunctive in high-frequency chunks;
- differences between **ser** and **estar** with common adjectives.

#### Authoring brief

**Sentence contexts:** Events, earlier routines, problems, appointments, directions, comparisons, and polite complaints.

**Focused hidden targets:** Past/background form, object/reflexive pronoun, command, duration, por/para, or frequent periphrasis.

**Authoring criterion:** Use the route’s ordinary clitic and listening patterns; introductory subjunctive chunks do not justify an unrestricted advanced system.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

- **pretérito perfeito** versus **imperfeito**;
- present subjunctive;
- future subjunctive;
- personal infinitive;
- commands with pronouns;
- direct and indirect pronoun combinations;
- passive and impersonal **se**;
- relative clauses;
- reported speech;
- cause, purpose, consequence, condition, and opposition;
- **ser** versus **estar** with wider adjective sets;
- systematic **por** versus **para**;
- conditional forms;
- common verbal periphrases;
- target-variety clitic placement in ordinary contexts.

#### Authoring brief

**Sentence contexts:** Narratives, opinions, explanations, comparisons, hypothetical choices, and practical repair.

**Focused hidden targets:** Future/present subjunctive, personal infinitive, pronoun combination, se function, or reported-speech component.

**Authoring criterion:** Keep future subjunctive and personal infinitive genuinely targeted rather than incidental visible language.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

- stable subjunctive use;
- imperfect and future subjunctive contrasts;
- past conditional and hypothetical structures;
- advanced relative clauses;
- clitic combinations and target-variety placement;
- passive, reflexive, reciprocal, and impersonal **se**;
- personal infinitive in complex clauses;
- concession and qualification;
- stance and hedging;
- logical connectors;
- reformulation;
- natural collocations;
- regional discourse markers;
- formal versus conversational syntax;
- differences between edited writing and ordinary speech.

#### Authoring brief

**Sentence contexts:** Source comparison, proposals, reviews, service/workplace interaction, and qualified argument.

**Focused hidden targets:** Past hypothetical, imperfect/future subjunctive contrast, complex infinitive, clitic pattern, or discourse relation.

**Authoring criterion:** Keep formal edited language distinct from natural speech; do not mix national norms in one unmarked answer.

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
- rapid unscripted listening;
- interruption and turn management;
- pragmatic softening;
- formal correspondence;
- natural use of discourse markers;
- comprehension of Brazil, Portugal, and selected additional Lusophone varieties;
- awareness of when a form is grammatical but regionally or socially unnatural.

#### Authoring brief

**Sentence contexts:** Professional and intellectual work, implied stance, synthesis, meetings, and cross-variety recognition.

**Focused hidden targets:** A precise collocation, source relation, softening or turn move, or register-sensitive phrasing.

**Authoring criterion:** Broaden beyond one technical topic; identify material that is natural elsewhere but not in the production route.

### 6.7. Proficient integration

**Curriculum reference:** C2 functional command; examination route depends on variety

#### Required language and situation inventory

- collocations;
- open and closed vowels;
- nasalization and prosody;
- clitic placement;
- personal infinitive and subjunctive choices;
- formal written syntax;
- conversational reductions;
- register;
- Brazil–Portugal differences;
- African and diaspora variants;
- idioms;
- cultural references;
- recurring personal errors.

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
- persuasive and diplomatic language;
- spontaneous explanation outside your familiar field.

#### Authoring brief

**Sentence contexts:** Mediation, rhetoric, literary/stylistic cases, implication, diplomatic responses, and professional editing.

**Focused hidden targets:** A compact precision repair, idiom, pragmatic component, or natural response to attributed regional wording.

**Authoring criterion:** Do not call a Brazilian functional C2 label a Celpe-Bras C2 certificate or compress a whole long-source task into a blank.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Lusophone professional, social, and cultural domains

#### Required language and situation inventory

Include:

1. **One stable production variety.**
2. **One professional identity in Portuguese.**
3. **One recurring social community.**
4. **Advanced comprehension of the other major variety.**
5. **Several Lusophone cultural fields developed through sustained participation.**

Use language situations drawn from:

- work or study conducted in Portuguese;
- friendships maintained principally in Portuguese;
- recurring group activities;
- disagreement, negotiation, and problem-solving;
- formal and informal messaging;
- literature, journalism, and long-form spoken discourse as sources of sentence-level register and genre distinctions;
- comedy, irony, and social-media discourse;
- exposure to different generations and regions;
- advanced pronunciation coaching;
- native editorial feedback.

#### Authoring brief

**Sentence contexts:** Work/study responsibilities, relationships, negotiations, cultural discussion, and local messaging.

**Focused hidden targets:** A verified domain-specific sense, social convention, or cross-variety interpretation.

**Authoring criterion:** Keep one active variety and label broad recognition; cards cannot establish community participation.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Cover open/closed **e/o**, stressed/unstressed vowels, nasal vowels/diphthongs, stress, **lh/nh**, regional **r/s**, linking, weak pronouns, and phrase rhythm. For the Brazilian route, specify the chosen final **e/o**, **t/d** before an /i/-like vowel, and final **l** realizations. For the European route, specify **/ɨ/**, strong unstressed-vowel reduction, consonant-heavy phrasing, and enclitic sequences.

Do not invent a neutral combined production variety. Check every written accent and grammatical distinction in context. Recognition of reduced speech does not authorize erasing a pronoun or changing ordinary accepted spelling.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Use contractions, clitic sequences, periphrases, reduced vowels, nasalization, and region-sensitive vocabulary in comprehensible original sentences. Keep target-variety detail separate from other-variety recognition. Do not claim that short written examples establish broad Lusophone accent comprehension.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from messages and graded narratives to journalism-style material, argument, fiction, and professional correspondence. Review contractions, clitics, personal infinitive, future subjunctive, and the relation between edited writing and conversation. Mark Brazilian, European, and additional Lusophone usage without treating every difference as an error.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Plan past-event versus background, **ser/estar**, **por/para**, **se** functions, subject-sensitive infinitives, future conditions, and route-specific clitic placement. Keep the subject and reference visible. For an enclitic target, choose a linguistically coherent exact span rather than losing the required hyphen or inflection.

The source’s future-subjunctive patterns support separate contextual cards; do not concatenate Brazilian and European alternatives into one canonical answer. A shared preposition example such as **precisar de** does not decide the project’s national variety.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `pt-BR`; source prefix is `pt`; the exact stage IDs are `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "pt-01-0001",
    "locale": "pt-BR",
    "sentence": "Preciso de uma caneta para assinar o formulário.",
    "cloze": "Preciso de",
    "answer": "Preciso de",
    "accepted_answers": [],
    "lemma": "precisar de",
    "meaning": "I need",
    "part_of_speech": "verb phrase",
    "note": "Precisar de introduces the thing needed in this construction."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| Quando eu tiver tempo, vou revisar o texto. | `tiver` | A compact future-subjunctive form; keep the future condition visible. |
| Antes de sairmos, precisamos fechar as janelas. | `sairmos` | A personal-infinitive target with a recoverable first-person plural subject. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Specify country/region, relationship, authority, familiarity, urgency, and audience. Review formal writing, ordinary neutral speech, and informal/regional language separately. A form natural in the other national variety is not automatically an error, but it may be unsuitable for this production target. Avoid a universal rule equating longer requests with greater politeness.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check gender, agreement, tense, mood, articles, contractions, clitics, prepositions, order, vocabulary, collocation, register, variety consistency, accents, and punctuation. Distinguish correct formal Portuguese from the natural wording for the selected country and context. Keep the source commitment, subject, time relation, and uncertainty intact during reformulation.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Keep the Brazilian and European routes separate. The source lists **Muito Prazer** or **Novo Avenida Brasil** with the Brazilian **Gramática Ativa** edition, and **Português em Foco** with the European edition. Brazilian dictionaries/orthography and media include Michaelis, ABL VOLP, TV Cultura, Speaking Brazilian, and the university Tá Falado material; European references include Priberam, Infopédia, RTP, Practice Portuguese, and Portuguese Lab. CAPLE and Celpe-Bras remain separate assessment routes.

| Reference | Authoring use |
|---|---|
| [Google Books](https://books.google.com/books/about/Muito_Prazer.html?id=3q5VEAAAQBAJ) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Klett](https://www.klett-sprachen.de/novo-avenida-brasil/r-1/471) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Speaking Brazilian](https://www.speakingbrazilian.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Easy Portuguese](https://www.easyportuguese.org/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [University of Texas](https://www.coerll.utexas.edu/brazilpod/tafalado/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [TV Cultura](https://cultura.uol.com.br/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Michaelis](https://michaelis.uol.com.br/) | Check the selected form, sense, construction, or register. |
| [Academia Brasileira de Letras](https://www.academia.org.br/nossa-lingua/busca-no-vocabulario) | Check the selected form, sense, construction, or register. |
| [Inep](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/celpe-bras) | Check the stated task/framework boundary; do not copy examination items. |
| [Lidel](https://www.lidel.pt/pt/catalogo/portugues-europeu-lingua-estrangeira/metodos/portugues-em-foco-3-livro-do-aluno/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Practice Portuguese](https://www.practiceportuguese.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Portuguese Lab](https://www.portugueselab.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [RTP Play](https://www.rtp.pt/play/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Priberam](https://dicionario.priberam.org/) | Check the selected form, sense, construction, or register. |
| [Infopédia](https://www.infopedia.pt/dicionarios/lingua-portuguesa/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [CAPLE](https://caple.letras.ulisboa.pt/exames) | Check the stated task/framework boundary; do not copy examination items. |
| [YouGlish](https://youglish.com/portuguese) | Check the actual pronunciation, prosody, or variety of selected language. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| Brazilian and European norms mixed silently | Select one production branch and label other-variety recognition. |
| Future subjunctive or personal infinitive absent from B1 scope | Map and author the source’s intermediate functions. |
| Clitics avoided or moved according to another route | Verify placement in the declared variety and register. |
| A contraction treated as an optional abbreviation | Teach the actual preposition/article relation. |
| Cognates assumed to have Spanish sound and sense | Check Portuguese pronunciation, complement, and meaning. |
| Celpe-Bras treated as a direct CEFR staircase | Preserve the separate examination and functional labels. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained Portuguese authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-pt-BR`; the guide requires no separate proficiency-plan or conversation attachment.

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
