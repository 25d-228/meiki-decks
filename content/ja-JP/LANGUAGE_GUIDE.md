# Japanese: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-ja-JP`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `ja-JP`  
**Scope:** N5–N1-oriented receptive coverage and a distinct balanced-C1 integration layer, followed by domain specialization.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 10 stages; 13,400 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **contemporary standard Japanese (`ja-JP`) with Tokyo-oriented pronunciation**. Use hiragana, katakana, and kanji through actual vocabulary. Keep normal written forms and target readings separate; do not make rōmaji an accepted substitute for Japanese answers.

Distinguish casual, polite, formal, honorific, and humble expression through roles and relationships. Treat regional, generational, occupational, gender-associated, and fictional role language as attributed recognition where appropriate, not interchangeable production forms. Do not infer a person’s identity from an isolated expression or treat stylized entertainment dialogue as the default.

---

### 2.1. Short sentences: mandatory length contract

Keep **advanced meaning, not advanced length**. The following caps apply to the **entire `common.sentence` field per card**, with its cloze restored. They include both sides of a contrast, all quoted speech, and both turns/sentences of a micro-context. They are not separate allowances per clause. No advanced, literary, domain, quotation, or politeness exception raises a cap.

| Production stages | Preferred full-text length | Hard full-text maximum |
|---|---|---|
| `00–01` | 8–20 characters | **28 characters** |
| `02` | 15–28 characters | **40 characters** |
| `03–09` | 20–42 characters | **60 characters** |

**Hidden span:** normally 2–10 characters; hard maximum **16 characters**. Apply the same ceiling to each explicit accepted answer. This ceiling does not make an arbitrary fragment, entire predicate, or unrelated group of words a good cloze. A compact conventional whole utterance can be an editorially justified exception to the visible-context rule, but not to either length cap.

Preferred bands are drafting guidance, not minimums or quotas. Naturally shorter utterances are welcome. Do not pad them or write every card near the maximum. Advanced stages keep the same upper ceiling; difficulty comes from the selected sense, grammar, collocation, register, or pragmatic distinction.

**Characters:** normalize to NFC, then count every non-whitespace Unicode code point, **including punctuation, digits, and Latin text**. Use `sum(not ch.isspace() for ch in unicodedata.normalize("NFC", text))`. This definition is for the length check only; cloze boundaries still respect grapheme clusters. Do not strip punctuation, change standard spelling, use abbreviations, or compress numerals to game the count. Readings and answer-side notes are not part of `common.sentence`, but must never hide required front-side context.

**Character-based checking:** use the character count below, not whitespace words, model tokens, UTF-8 bytes, inferred syllables, or an unverified word segmenter. Mixed-script words and digits count character by character too. No tokenizer installation is needed.

Use **one short sentence by default**. At most two short sentences or two short conversational turns may form the source text when essential to interpretation; their **combined** text must fit the same cap. Do not add an uncounted preamble, a front-side `context` field, a screenshot, or an answer-side explanation as a way around the limit. Keep one primary target. Avoid stacked relative clauses, embedded chains, several unexplained participants, and unrelated facts. A brief subordinate or contrasting clause is allowed when it demonstrates the target.

Before accepting a card, verify that the source makes the relevant event/referent and the target's sense, relation, time, or social force interpretable. Remove decorative setup, not the governor, antecedent, negation, comparison, condition, or other essential cue. Text need not exclude every imaginable synonym, but the intended target must be natural and demonstrate the assigned use. Do not substitute an arbitrary fragment or ambiguous sense for useful context.

Keep the predicate, particles, viewpoint, beneficiary, and politeness cues needed for interpretation. Count kana and kanji by the same character rule; never replace normal kana with unusual kanji just to shorten the count. Do not concatenate multiple propositions with repeated connective forms.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| 駅の前で友達を待っています。 | `待っています` | A named location and person support an ongoing action. |
| 賛成したものの、費用には不安が残る。 | `したものの` | The concessive relation is clear without an extended explanation. |
| 急な依頼ですが、明日までにお願いできますか。 | `明日までに` | The request retains its deadline and polite frame. |

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

Preserve **N5 → N4 → N3 → N2 → N1** as the supplied examination-oriented receptive track. Its independent productive endpoint is **balanced C1**, not a fully specified balanced C2 curriculum. Keep N1/high-receptive work and balanced-C1 integration separate; never relabel the latter C2 merely to match other languages.

The source reports score-dependent JLPT CEFR reference indications, including N1 142+ for a C1 reference and a separate preferred 150+ aspiration. These are source-reported assessment details, not card quotas or a guarantee about current rules. They concern the skills tested and do not establish speaking, writing, or interaction. Card documentation should use the curriculum boundary rather than turn those scores into production acceptance rules.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **10 stages and exactly 13,400 accepted cards** for Japanese, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** The guide describes substantial lexical and kanji breadth through N2- and N1-oriented work, followed by balanced C1 and domain-specific use. N2 and N1 each receive two stages to protect that breadth. The counts leave room for grammar, readings, collocations, and register contrasts in addition to lexical targets; they do not turn the guide’s lexical aspirations into official JLPT quotas.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `00` | Japanese 00 — Kana, sound, and sentence foundations | Sections 6.1 | 200 | 5 | 200 |
| `01` | Japanese 01 — N5-oriented basic communication | Sections 6.2 | 800 | 20 | 1,000 |
| `02` | Japanese 02 — N4-oriented routine communication | Sections 6.3 | 1,200 | 30 | 2,200 |
| `03` | Japanese 03 — N3-oriented independent communication | Sections 6.4 | 1,600 | 40 | 3,800 |
| `04` | Japanese 04 — N2-oriented lexical and reading breadth | Sections 6.5, part A | 1,600 | 40 | 5,400 |
| `05` | Japanese 05 — N2-oriented discourse and social use | Sections 6.5, part B | 1,600 | 40 | 7,000 |
| `06` | Japanese 06 — N1-oriented lexical and register precision | Sections 6.6, part A | 1,800 | 45 | 8,800 |
| `07` | Japanese 07 — N1-oriented argument and interpretation | Sections 6.6, part B | 1,800 | 45 | 10,600 |
| `08` | Japanese 08 — Balanced C1 integration | Sections 6.7 | 1,600 | 40 | 12,200 |
| `09` | Japanese 09 — Social, professional, and cultural depth | Sections 6.8 | 1,200 | 30 | 13,400 |
| **Total** | **10 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **13,400** | **335** | **13,400** |

Use source IDs `ja-<stage>-0001` through `ja-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `ja-JP`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 00:** Cover kana through meaningful words, mora timing, length, gemination, moraic n, introductory prosody, basic preferences, and useful survival expressions.
- **Stage 01:** Cover particles, verbs/adjectives, tense and polarity, te forms, requests, permission, counters, comparison, and ordinary vocabulary with correct readings.
- **Stage 02:** Cover relative clauses, potential/volitional/conditional forms, giving/receiving, transitivity, voice, evidentiality, embedded questions, and introductory social-register distinctions.
- **Stage 03:** Develop subordinate relations, nominalization, aspect, stance, wake/hazu/beki distinctions, endings, omission, reductions, and broad narrative/explanatory vocabulary.
- **Stage 04:** Prioritize word senses, compounds, collocations, kanji readings in real words, contemporary narrative, nonfiction, evidence, and qualification.
- **Stage 05:** Complete source-based argument, spoken/written reformulation, service and telephone language, workplace interaction, keigo, and additional lexical contrasts rather than repeating stage 04.
- **Stage 06:** Develop substantial advanced vocabulary, compound distinctions, contextual readings, formal/informal senses, collocations, and specialist language in understandable situations.
- **Stage 07:** Complete source synthesis, evidentiality, analysis, nuanced disagreement, audience-sensitive explanation, and further advanced lexical breadth; do not substitute connectors for vocabulary.
- **Stage 08:** Cover idioms, sound symbolism, stance, keigo, written/spoken register, cultural references, and labeled role-language recognition across social, professional, and intellectual domains.
- **Stage 09:** Develop community and domain-specific language for relationships, group decisions, implicit refusal, backchannels, humor, service, and responsibilities without claiming a C2 equivalence.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Do not assume prior Chinese-character or Korean knowledge. Map kana, vocabulary readings, particles, aspect, viewpoint, and politeness prerequisites separately. Familiar-looking kanji or katakana are not automatically known words.

The source names **マンション, コンセント, クレーム, サービス, テンション, スマート, リベンジ** as loanword investigations. Check the actual Japanese pronunciation, sense, and use. English grammatical terminology may help explanations, but the sentence must be written naturally in Japanese rather than translated word for word. The project uses concise English support; Japanese definition/paraphrase work can remain language content at suitable milestones.

---

## 5. Essential systems to represent in sentences

### Script, readings, and sound
Introduce kana directly and kanji through words, compounds, and context. Do not create a catalogue of every possible reading for an isolated character. The source’s **学生, 生活, 生まれる, 生きる, 生ビール, 一生** family illustrates word-specific reading rather than a single equation for 生. Keep recognition, typing, and handwriting distinct.

Cover mora timing, vowel length, gemination, moraic ん, relevant high-vowel devoicing, pitch patterns, phrasing, and focus. A pitch number alone is not a complete pronunciation description.

### Grammar and viewpoint
Plan particles as contextual relations, not one-word translations. Cover modification, subordination, nominalization, aspect, transitivity, giving/receiving, passive, causative, and related patterns through recoverable situations. Include the source’s **決まる/決める, 上がる/上げる, 始まる/始める, 開く/開ける, 直る/直す** contrasts where their prerequisites are taught.

### Context and omission
Track actor, beneficiary, viewpoint, quotation, inference, and implied conclusion. Supply enough context without filling every Japanese sentence with unnecessary pronouns. A short utterance can be natural with an omitted subject, but its interpretation must not depend on an unavailable preceding card.

### Similar expressions and social meaning
Contrast overlapping **わけ**, **はず**, **べき**, conditionals, stance markers, and sentence-final particles. Distinguish spoken reductions from formal writing and honorific reference from politeness toward the listener. Keigo must fit a real relationship and function, not simply make a sentence longer.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Kana, phonology, and basic sentence foundation

#### Required language and situation inventory

- hiragana;
- katakana;
- Japanese keyboard input;
- the five-vowel system;
- mora timing;
- long versus short vowels;
- the small っ;
- the moraic ん;
- basic consonant distinctions;
- introductory pitch-accent awareness.

Cover direct kana recognition and typed vocabulary in meaningful sentences without rōmaji answers. Teach elementary grammar alongside script; do not claim handwriting from these cards.

Use the source’s approximately 100–150 useful foundation chunks as a breadth aspiration; listed seeds include:

- お願いします
- 〜てもいいですか
- もう一度お願いします
- どういう意味ですか
- よく分かりません
- 〜が好きです
- 〜と思います

#### Authoring brief

**Sentence contexts:** Greetings, identity, clarification, simple preferences, and survival questions using kana and useful early chunks.

**Focused hidden targets:** A word or compact fixed expression tied to kana, vowel length, gemination, or elementary language.

**Authoring criterion:** Keep sound/script and useful grammar together. Formulaic early material is not permission to introduce every related productive pattern.

### 6.2. Basic communication

**Curriculum reference:** A1-oriented / N5-oriented

#### Required language and situation inventory

- は, が, を, に, で, へ, と, も;
- present and past tense;
- affirmative and negative forms;
- い- and な-adjectives;
- て-form;
- requests and permission;
- progressive and resultant 〜ている;
- plain forms;
- comparison;
- desire;
- experience;
- basic explanation with んです;
- counters and common time expressions.

Do not author particles as one-word English equations. Use sentence patterns and meaningful contrasts.

#### Authoring brief

**Sentence contexts:** Routine, location, possession, invitations, shopping, requests, comparisons, plans, and simple past events.

**Focused hidden targets:** A particle, adjective/verb form, counter, て-form use, request, permission, or basic explanatory component.

**Authoring criterion:** The blank must test the intended distinction, with natural visible support rather than a whole sentence hidden.

### 6.3. Routine communication

**Curriculum reference:** A2-oriented / N4-oriented

#### Required language and situation inventory

- relative clauses;
- potential forms;
- volitional forms;
- conditionals;
- giving and receiving;
- transitive and intransitive pairs;
- passive;
- causative;
- causative-passive recognition;
- purpose and intention;
- hearsay and appearance;
- embedded questions;
- introductory honorific and humble expressions;
- distinctions between casual and polite interaction.

Transitive/intransitive pairs need deliberate practice:

- 決まる／決める
- 上がる／上げる
- 始まる／始める
- 開く／開ける
- 直る／直す

Place each selected pair in complete situations rather than copying an abstract list.

#### Authoring brief

**Sentence contexts:** Problems, follow-up questions, narratives, choices, social requests, and everyday polite/casual contrasts.

**Focused hidden targets:** A transitivity, potential, conditional, giving/receiving, passive/causative, or evidential component.

**Authoring criterion:** Make actor, beneficiary, and social relationship recoverable; keep causative-passive recognition separate from unrestricted production.

### 6.4. Independent communication

**Curriculum reference:** Functional B1-oriented / N3-oriented

#### Required language and situation inventory

- longer subordinate structures;
- contrast and concession;
- probability and uncertainty;
- speaker stance;
- nominalization;
- aspect and completion;
- 〜ようになる and 〜ことになる;
- 〜わけ constructions;
- 〜はず, 〜べき, and related judgment expressions;
- sentence-final particles;
- casual conversational reductions;
- ellipsis and omitted subjects;
- differences between written and spoken Japanese.

Japanese permits context-supported omission. Make the following recoverable in each relevant card:

- who is acting;
- who benefits;
- whose perspective controls the expression;
- whether a statement is direct, inferred, or reported.

#### Authoring brief

**Sentence contexts:** Narration, opinions, explanations, comparisons, reaction, misunderstanding repair, and short source summaries.

**Focused hidden targets:** A stance, probability, nominalization, aspect, わけ/はず/べき, or sentence-ending distinction.

**Authoring criterion:** Avoid unnecessary explicit subjects while keeping omitted information interpretable inside the card.

### 6.5. Upper-intermediate operation

**Curriculum reference:** N2-oriented / receptive B2-oriented with separate production

#### Required language and situation inventory

Consolidate the intermediate grammar inventory and similar-pattern distinctions. Develop extended argument, qualification, evidence, formal versus conversational expression, workplace interaction, keigo in defined roles, and reduced or multi-speaker listening. Use Quartet II and selected advanced-bridge material rather than treating N2 preparation as the entire curriculum.

#### Authoring brief

**Sentence contexts:** Workplace and telephone interaction, evidence, general argument, source-based writing, and contemporary narrative.

**Focused hidden targets:** A developed collocation, qualification, keigo component, or spoken/written reformulation.

**Authoring criterion:** The source gives a functional expansion, not an exhaustive N2 grammar list. Map and justify the actual selected distinctions.

### 6.6. Advanced development

**Curriculum reference:** N1 and high receptive competence

#### Required language and situation inventory

Preserve these source-defined breadth aspirations as inventory references, not card quotas:

- 13,000–18,000 well-understood lexical items;
- recognition of the full common-use kanji range;
- additional names, specialist characters, and non-jōyō characters encountered in your domains.

Japan’s official common-use kanji table contains **2,136 characters**. This is a social writing guideline, not a complete list of every character you will encounter. ([Bunka.go.jp](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/pdf/joyokanjihyo_20101130.pdf))

Do not count character presence alone as lexical coverage. Distinguish actual vocabulary uses:

> 提案、提唱、提示、提供、前提、提起

The advanced distinction is not recognizing 提. It is knowing which compound fits which situation and register.

Develop source synthesis, nuanced agreement and disagreement, professional explanation, keigo, group interaction, and audience-sensitive reformulation. Represent advanced lexical distinctions through actual collocations and register choices.

#### Authoring brief

**Sentence contexts:** Professional explanation, analytical argument, source synthesis, nuanced disagreement, and advanced reading contexts.

**Focused hidden targets:** A precise lexical sense, register choice, evidential relation, or audience-sensitive construction.

**Authoring criterion:** Track the large lexical/kanji aspirations honestly; a few abstract connectors do not constitute the whole advanced inventory.

### 6.7. Proficient integration

**Curriculum reference:** Balanced C1; not a newly asserted C2 equivalence

#### Required language and situation inventory

Include these three Japanese domain groups:

1. **Ordinary and social life**
2. **Your profession or academic field**
3. **One cultural or intellectual field**

Examples for the third domain include literature, film, history, economics, design, philosophy, politics, music, or technology.

Maintain coverage entries for:

- collocations;
- register;
- formal written language;
- casual spoken reductions;
- sentence-final particles;
- keigo;
- stance and evidentiality;
- sound symbolism;
- idioms;
- cultural references;
- dialectal variation;
- male, female, occupational, generational, and fictional role language.

Do not make every recognized form a production target. Attribute forms restricted to relationships, roles, regions, or character types without stereotyping speakers.

#### Authoring brief

**Sentence contexts:** Ordinary/social life, a professional field, and a cultural or intellectual field at balanced-C1 integration.

**Focused hidden targets:** An idiom, sound-symbolic expression, stance distinction, keigo choice, or contextual recognition of role language.

**Authoring criterion:** Keep this endpoint labeled balanced C1. Do not claim C2 or native identity from the card set.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Japanese professional, social, and cultural domains

#### Required language and situation inventory

Use these language and interactional functions as selection criteria:

- knowing when not to state something directly;
- interpreting silence and hesitation;
- managing conversational overlap;
- understanding indirect refusal;
- using backchannels naturally;
- following references that are not fully explained;
- recognizing humor, parody, and understatement;
- distinguishing ordinary spoken Japanese from stylized media speech;
- using keigo without sounding mechanically over-polite;
- varying your Japanese according to relationship and setting.

#### Authoring brief

**Sentence contexts:** Group decisions, relationships, service encounters, professional duties, humor, indirect refusal, and cultural participation.

**Focused hidden targets:** A verified, domain-specific pragmatic or lexical distinction with sufficient visible circumstances.

**Authoring criterion:** Do not ask one card to prove interpretation of actual silence or overlapping conversation; model only the language component.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Select vocabulary and sentences covering long/short vowels, single/doubled consonants, ん before different consonants, high-vowel devoicing, mora timing, pitch drops, phrase boundaries, focus, and intonation. The source supplies **おばさん/おばあさん, ここ/こうこう, きて/きって, かこ/かっこ, びょういん/びよういん** as contrast seeds; choose meaningful original contexts rather than packing them into tongue twisters.

Check the reading of the actual inflected target. Use verified Tokyo-oriented models; do not infer every compound’s reading or accent from its characters. Document phrase-level pronunciation information when it helps explain the actual target, while keeping ordinary spelling in the answer.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Model natural omission, shortened forms, endings, backchannels, quotation, changes in politeness, and implied conclusions. For a repair or unfinished-turn example, keep the intended relation understandable inside the accepted sentence or short exchange. A short written exchange does not establish multi-person interaction ability.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from kana-supported practical sentences and easy narrative to accessible nonfiction, essays, interviews, contemporary stories, journalism, and specialist prose. Avoid gratuitous rare kanji and stylized historical speech in early material. Make clause modification, viewpoint, reference, and the reading of each taught word clear. Answer-side readings must not become an unrequested all-furigana production answer.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Use the source’s **行きたくないわけではない / 行かないわけにはいかない / 行くわけがない / 行くわけだ / 行くというわけだ** family to plan differences in implication, obligation, impossibility, inference, and explanation. These are reference patterns, not a sentence list to copy unchanged.

Keep the actual proposition visible and hide the shortest useful component that tests the distinction. Do not respond to a long-cloze defect by deleting only one word while leaving nearly the entire predicate hidden. Giving/receiving and transitivity contrasts must make the actor or beneficiary recoverable, not merely alternate verb endings.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `ja-JP`; source prefix is `ja`; the exact stage IDs are `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "ja-01-0001",
    "locale": "ja-JP",
    "sentence": "駅の前で友達を待っています。",
    "cloze": "待っています",
    "answer": "待っています",
    "accepted_answers": [],
    "lemma": "待つ",
    "meaning": "am waiting",
    "part_of_speech": "verb",
    "note": "The ている form presents the waiting as ongoing here."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| 風で窓が開きました。 | `開きました` | The wind and window supply an intransitive event; do not change the learner target into a transitive form. |
| 説明は分かりましたが、提案のすべてに賛成するわけではありません。 | `わけではありません` | The qualified agreement remains visible; the compact negative explanatory pattern is the target. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Check viewpoint, omitted participants, titles, backchannels, degree of formality, and who is being honored or humbled. Require a natural response, request, refusal, repair, or explanation for the situation. Do not impose an English-style explicit subject or demand keigo without specifying the roles that license it.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Review particles, transitivity, aspect, tense, vocabulary, collocation, clause connection, register, kanji/orthography, excessive explicitness, missing context, and English-shaped pronoun use. Advanced material should include audience-sensitive summaries, arguments, reports, and professional messages, not only personal narrative. Preserve source stance and viewpoint during reformulation.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **Genki I–II → Quartet I–II → Authentic Japanese** as the source-listed scope sequence. The Basic/Intermediate/Advanced grammar dictionaries support contrasts; Shin Kanzen Master and official JLPT material are examination-reference layers. OJAD supports pronunciation investigation; Tadoku and Satori Reader support text/genre progression. Irodori, Marugoto, and Minato are the source’s alternative practical route. Do not require completion of several courses or copy their readings.

| Reference | Authoring use |
|---|---|
| [Genki Online](https://genki3.japantimes.co.jp/en/intro/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Quartet — publisher](https://bookclub.japantimes.co.jp/en/book/b456886.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Authentic Japanese — publisher](https://bookclub.japantimes.co.jp/en/book/b663835.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Japanese grammar reference — publisher](https://bookclub.japantimes.co.jp/en/book/b664332.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [スリーエーネットワーク](https://www.3anet.co.jp/en/catalogue.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [JLPT](https://www.jlpt.jp/e/samples/sampleindex.html) | Check the stated task/framework boundary; do not copy examination items. |
| [GAVO](https://www.gavo.t.u-tokyo.ac.jp/ojad/eng/pages/home) | Check the actual pronunciation, prosody, or variety of selected language. |
| [NPO多言語多読](https://tadoku.org/japanese/en/free-books-en/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Satori Reader](https://www.satorireader.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Irodori](https://www.irodori.jpf.go.jp/en/about.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [JLPT CEFR reference](https://www.jlpt.jp/e/about/cefr_reference.html) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| All readings of a kanji treated as a lexical curriculum | Select real words and verify each contextual reading. |
| Reading annotation belongs to the lemma rather than target | Align it with the exact inflected span. |
| Keigo or giving/receiving lacks roles | Supply recoverable actor, beneficiary, and audience. |
| An English subject is inserted into every utterance | Check natural Japanese omission and reference. |
| Fictional role language treated as neutral speech | Attribute and label recognition-only usage. |
| Balanced C1 relabeled C2 for symmetry | Preserve the stated endpoint and separate domain layer. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained Japanese authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-ja-JP`; the guide requires no separate proficiency-plan or conversation attachment.

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
