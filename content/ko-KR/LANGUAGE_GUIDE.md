# Korean: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-ko-KR`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `ko-KR`  
**Scope:** basic through TOPIK 6-oriented Korean with separate advanced productive and domain-specific coverage.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 8 stages; 8,800 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **contemporary standard South Korean (`ko-KR`)**. Write Hangul directly, preserving standard spacing and spelling. Teach syllable blocks, 받침, relevant sound changes, and typed form without relying on romanization.

Ordinary polite **해요체**, formal polite **합니다체**, and casual forms require clear relationship and setting. Subject honorification is distinct from politeness toward the listener. Do not adopt 반말 or an entertainment character’s register without a suitable context.

---

### 2.1. Short sentences: mandatory length contract

Keep **advanced meaning, not advanced length**. The following caps apply to the **entire `common.sentence` field per card**, with its cloze restored. They include both sides of a contrast, all quoted speech, and both turns/sentences of a micro-context. They are not separate allowances per clause. No advanced, literary, domain, quotation, or politeness exception raises a cap.

| Production stages | Preferred full-text length | Hard full-text maximum |
|---|---|---|
| `00–01` | 3–6 eojeol | **8 eojeol AND 32 characters** |
| `02` | 4–8 eojeol | **10 eojeol AND 44 characters** |
| `03–07` | 5–9 eojeol | **12 eojeol AND 60 characters** |

**Hidden span:** normally 1–2 eojeol or one meaningful attached ending; hard maximum **3 eojeol AND 16 characters**. Apply the same ceiling to each explicit accepted answer. This ceiling does not make an arbitrary fragment, entire predicate, or unrelated group of words a good cloze. A compact conventional whole utterance can be an editorially justified exception to the visible-context rule, but not to either length cap.

Preferred bands are drafting guidance, not minimums or quotas. Naturally shorter utterances are welcome. Do not pad them or write every card near the maximum. Advanced stages keep the same upper ceiling; difficulty comes from the selected sense, grammar, collocation, register, or pragmatic distinction.

**Characters:** normalize to NFC, then count every non-whitespace Unicode code point, **including punctuation, digits, and Latin text**. Use `sum(not ch.isspace() for ch in unicodedata.normalize("NFC", text))`. This definition is for the length check only; cloze boundaries still respect grapheme clusters. Do not strip punctuation, change standard spelling, use abbreviations, or compress numerals to game the count. Readings and answer-side notes are not part of `common.sentence`, but must never hide required front-side context.

**Eojeol:** split ordinary correctly spaced Korean on whitespace and count pieces containing a letter or number. A punctuation-only dash is not an eojeol. Do not remove legitimate spaces. Both the eojeol limit and character limit must pass; no morphological parser is needed.

Use **one short sentence by default**. At most two short sentences or two short conversational turns may form the source text when essential to interpretation; their **combined** text must fit the same cap. Do not add an uncounted preamble, a front-side `context` field, a screenshot, or an answer-side explanation as a way around the limit. Keep one primary target. Avoid stacked relative clauses, embedded chains, several unexplained participants, and unrelated facts. A brief subordinate or contrasting clause is allowed when it demonstrates the target.

Before accepting a card, verify that the source makes the relevant event/referent and the target's sense, relation, time, or social force interpretable. Remove decorative setup, not the governor, antecedent, negation, comparison, condition, or other essential cue. Text need not exclude every imaginable synonym, but the intended target must be natural and demonstrate the assigned use. Do not substitute an arbitrary fragment or ambiguous sense for useful context.

Use normal Korean spacing: an eojeol is an orthographic space-delimited unit, not a morpheme or an English-equivalent word. The character ceiling also applies. Preserve the relationship, governor, and speech-level evidence; never join words to evade the eojeol cap.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| 선생님, 질문이 있어요. | `질문` | The teacher address supplies the relationship for polite speech. |
| 비가 그치면 같이 산책할까요? | `그치면` | A short conditional supports a natural invitation. |
| 가격은 비싸지만 내구성을 감안하면 합리적인 선택이에요. | `감안하면` | Price and durability support a qualified evaluation. |

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

Keep **TOPIK I**, **TOPIK II**, and the separate **TOPIK Speaking** route distinct as presented in the source. Its advanced objective combines TOPIK 6-oriented work with a separate advanced speaking benchmark and real-world skills. The **A1-like, A2-like, B1-like, B2-like, C1-like, and near-C2** labels are functional shorthand, not official CEFR equivalences.

Do not turn an examination’s receptive coverage into proof of oral, honorific, or group-interaction competence. Card review establishes content quality and mapped coverage, not a learner’s TOPIK score.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **8 stages and exactly 8,800 accepted cards** for Korean, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** A separate Hangul/sound stage precedes six progressively broader communication stages and a distinct specialization stage. Larger intermediate and advanced allocations protect sentence endings, particles, honorific relationships, lexical families, collocations, and written/spoken register; exam labels remain qualified reference labels.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `00` | Korean 00 — Hangul, sound, and sentence foundations | Sections 6.1 | 200 | 5 | 200 |
| `01` | Korean 01 — Basic operational communication | Sections 6.2 | 600 | 15 | 800 |
| `02` | Korean 02 — Routine communication and TOPIK 2-oriented language | Sections 6.3 | 800 | 20 | 1,600 |
| `03` | Korean 03 — Independent communication and TOPIK 3-oriented language | Sections 6.4 | 1,200 | 30 | 2,800 |
| `04` | Korean 04 — Extended communication and TOPIK 4-oriented language | Sections 6.5 | 1,400 | 35 | 4,200 |
| `05` | Korean 05 — Advanced communication and TOPIK 5-oriented language | Sections 6.6 | 1,600 | 40 | 5,800 |
| `06` | Korean 06 — TOPIK 6-oriented precision and pragmatic integration | Sections 6.7 | 1,800 | 45 | 7,600 |
| `07` | Korean 07 — Social, professional, and cultural depth | Sections 6.8 | 1,200 | 30 | 8,800 |
| **Total** | **8 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **8,800** | **220** | **8,800** |

Use source IDs `ko-<stage>-0001` through `ko-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `ko-KR`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 00:** Cover syllable blocks, useful sound contrasts, batchim and early sound changes, polite survival language, and direct Hangul typing without romanization.
- **Stage 01:** Cover copula/existence, core particles, tense, negation, numbers/counters, requests, irregular forms, introductory honorification, and high-frequency everyday lexical frames.
- **Stage 02:** Cover ability, obligation, conditions, intentions, experience, time relations, noun modifiers, formal polite language, quotation, and expanded honorific uses.
- **Stage 03:** Cover nominalization, quotation types, cause, inference, passive/causative, honorific/humble verbs, omitted reference, softening, and natural response formulas.
- **Stage 04:** Develop stance/evidential endings, contrast and concession, plain written style, professional messages, word families, collocations, and spoken/written distinctions.
- **Stage 05:** Cover precise qualification, argument, synthesis, paraphrase, advanced lexical frames, academic style, hierarchy-sensitive meetings, and indirect criticism.
- **Stage 06:** Cover idioms, emotion, understatement, refusal, literary/formal styles, editing, turn repair, cultural and regional recognition, with recoverable social context.
- **Stage 07:** Develop distinct domain senses, locally appropriate conventions, work/study responsibilities, negotiations, relationships, and cultural discussion beyond the same stage-06 functions.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Do not assume Japanese syntax, Chinese-derived vocabulary, or familiarity with an honorific system establishes Korean usage. Check the actual particle, ending, sound, and social function. English explanations may help, but English word order and obligatory pronouns are not the default sentence plan.

Map Hangul and sound foundations alongside useful polite language. Introduce attached particles/endings as intentional morphological targets only when the objective and boundary are explicit; a validator must distinguish these from accidental substring clozes.

---

## 5. Essential systems to represent in sentences

### Script and sound
Cover consonant/vowel symbols, block positions, 받침, resyllabification, word-boundary changes, and typing. Include plain/aspirated/tense **ㄱ/ㅋ/ㄲ, ㄷ/ㅌ/ㄸ, ㅂ/ㅍ/ㅃ, ㅈ/ㅊ/ㅉ**, **ㅓ/ㅗ**, **ㅡ/ㅜ**, final neutralization, liaison, nasalization, lateralization, aspiration, tensification, and phrase intonation. Reading 학교 letter by letter is not a complete sound specification.

### Socially complete utterances
Specify who speaks, who listens, their relationship, speech level, and subject honorification whenever interpretation depends on them. The source contrasts **먹어요, 먹습니다, 먹어, 드세요, 드십니다**. Each belongs in an appropriate context rather than a mechanical five-form card grid.

### Lexical and grammatical packages
Record dictionary forms, particles/complements, spoken and written use, collocation, and relevant irregular forms. The source’s **관심이 있다/없다, 관심을 가지다/보이다** family illustrates construction-level meaning rather than **관심 = interest** alone.

### Particles, endings, and discourse
Do not use **은/는 = topic** and **이/가 = subject** as complete operating rules. Make contrast, actor identification, or given/new information visible where needed. Cover noun modification, quotation, nominalization, stance, and omission through practical situations. Respect written **-다/-는다** versus conversational patterns.

### Word families
Use productive Sino-Korean families only after checking their actual roots and meaning. The source names **학, 문, 사, 경** families and explicitly warns that identical syllables may represent different roots. Do not turn these into a requirement to memorize thousands of isolated Hanja.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Hangul and phonological foundation

#### Required language and situation inventory

- consonant and vowel symbols;
- syllable-block construction;
- stroke order;
- Korean keyboard layout;

- plain, aspirated, and tense consonants;
- major vowel distinctions;
- basic 받침;
- consonant release;
- simple liaison.

Begin with short words and two-to-four-word phrases, not isolated letters only.

- nasalization;
- tensification;
- aspiration caused by ㅎ;
- lateralization involving ㄴ and ㄹ;
- common contractions;
- phrase-level rhythm.

Use the source’s 30–50 high-frequency foundation expressions as a breadth aspiration. Review each expression’s actual register rather than assuming every listed formula is 해요체:

- 안녕하세요.
- 감사합니다.
- 괜찮아요.
- 잘 모르겠어요.
- 다시 말씀해 주세요.
- 천천히 말씀해 주세요.
- 이게 뭐예요?
- 어디에 있어요?
- 한국어를 배우고 있어요.

#### Authoring brief

**Sentence contexts:** Identity, clarification, basic questions, and survival expressions in suitable polite language.

**Focused hidden targets:** A useful word, block-based form, or compact expression tied to script and sound.

**Authoring criterion:** The 30–50-expression aspiration is not a forced quota. Do not require every sound rule before meaningful sentences.

### 6.2. Basic communication

**Curriculum reference:** A1-like basic operational Korean

#### Required language and situation inventory

- 이에요/예요;
- 있어요/없어요;
- 은/는, 이/가, 을/를;
- 에 and 에서;
- 도, 만;
- present and past tense;
- future or expectation with -(으)ㄹ 거예요;
- 안 and 못 negation;
- 주세요;
- -고 싶어요;
- -(으)세요;
- -고, -아서/어서, -지만;
- native and Sino-Korean numbers;
- counters;
- dates, time, prices, age, telephone numbers;
- basic honorific marker -시-;
- common irregular conjugations.

#### Authoring brief

**Sentence contexts:** Family, routine, food, shopping, transport, location, schedules, requests, past events, and plans.

**Focused hidden targets:** A basic particle, copula/existence form, tense, negation, counter, request, or honorific component.

**Authoring criterion:** Keep social relations coherent and record whether the target is an attached morpheme or a whole word/phrase.

### 6.3. Routine communication

**Curriculum reference:** A2-like routine communication / TOPIK 2-oriented

#### Required language and situation inventory

- -(으)ㄹ 수 있다/없다;
- -아/어야 하다;
- -(으)면;
- -(으)려고 하다;
- -아/어 보다;
- -아/어 본 적이 있다;
- -기 전에 and -(으)ㄴ 후에;
- -보다;
- -처럼;
- 부터 and 까지;
- 밖에 with negation;
- present, past, and future noun modifiers;
- formal polite -습니다/ㅂ니다;
- introductory indirect quotation;
- more complete honorific forms.

Include ordinary polite and formal polite material, distinguishing their productive and recognition roles.

#### Authoring brief

**Sentence contexts:** Appointments, experience, reasons, comparisons, problems, help requests, and simple narration.

**Focused hidden targets:** Ability, obligation, intention, condition, experience, noun-modifier, time relation, or formal-polite form.

**Authoring criterion:** Introduce formal speech and quotation in scope; do not drop productive language merely because TOPIK I is receptive.

### 6.4. Independent communication

**Curriculum reference:** B1-like independent communication / TOPIK 3-oriented

#### Required language and situation inventory

- noun-modifying clauses;
- -는 것 and nominalization;
- indirect speech:
  - -다고 하다;
  - -냐고 하다;
  - -(으)라고 하다;
  - -자고 하다;
- -는데;
- -기 때문에;
- -(으)니까;
- -자마자;
- -(으)면서;
- -는 동안;
- -는 것 같다;
- -나 보다;
- -겠-;
- introductory passive and causative;
- honorific and humble verbs;
- reported experiences;
- contrasting and concessive connectors.

Include:

- when Korean omits the subject;
- why repeating 저는 or 제가 can sound unnatural;
- age and status questions;
- title and kinship-term usage;
- indirect refusal;
- softening requests;
- differences among 네, 예, 맞아요, 그렇군요, 그래요, and 알겠습니다;
- how sentence endings communicate attitude.

#### Authoring brief

**Sentence contexts:** Narration, familiar abstract explanation, repair, status-sensitive requests, and ordinary response formulas.

**Focused hidden targets:** Quotation, nominalization, cause, inference, passive/causative, honorific, or humble component.

**Authoring criterion:** Identify who is quoted and who is being honored; avoid repetitive 저는/제가 where reference is already clear.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2-like upper-intermediate operation / TOPIK 4-oriented

#### Required language and situation inventory

Master common spoken endings and stance markers:

- -잖아요;
- -거든요;
- -더라고요;
- -던데요;
- -나 봐요;
- -기는 하다;
- -(으)ㄹ 텐데;
- -(으)ㄹ 리가 없다;
- -는 셈이다;
- -는 편이다;
- -도록;
- -더라도;
- -는 반면에;
- -에 비해;
- -에 따르면.

Author contexts that make the tone, implication, certainty, and interpersonal effect of each form recoverable.

**Written-register coverage**

Include:

- plain written style ending in -다 or -는다;
- nominal and formal written constructions;
- paragraph development;
- cause, contrast, concession, and conclusion;
- objective versus personal style;
- spacing and spelling;
- formal email and workplace language.

**Vocabulary**

Organize selected Sino-Korean vocabulary by verified roots:

- 학: 학교, 학생, 학습, 학문;
- 문: 문화, 문학, 문법;
- 사: 사회, 회사, 역사—while recognizing that identical sounds may represent different roots;
- 경: 경제, 경험, 환경-related compounds where appropriate.

Do not require thousands of isolated Hanja. Cover productive word families and verify each root’s actual meaning.

#### Authoring brief

**Sentence contexts:** Informational discussion, documentary-style summaries, arguments, workplace messages, and presentations.

**Focused hidden targets:** A stance ending, evidential relation, formal connector, comparison, or verified word-family use.

**Authoring criterion:** Explain the interpersonal or certainty effect of the actual ending; do not treat same-sounding roots as identical.

### 6.6. Advanced development

**Curriculum reference:** C1-like advanced development / TOPIK 5-oriented

#### Required language and situation inventory

- precise qualification;
- formal argumentation;
- source synthesis;
- paraphrasing;
- implicit meaning;
- indirect criticism;
- workplace hierarchy;
- meeting language;
- presentation language;
- academic nominalization;
- advanced collocations;
- register-sensitive synonyms;
- idioms that are genuinely frequent;
- careful versus ordinary pronunciation.

#### Authoring brief

**Sentence contexts:** Professional meetings, academic explanation, source synthesis, indirect criticism, and nuanced discussion.

**Focused hidden targets:** Qualification, paraphrase, nominalization, register-sensitive collocation, or hierarchy-sensitive phrasing.

**Authoring criterion:** Do not make all advanced material bureaucratic; preserve social and narrative coverage as well.

### 6.7. Proficient integration

**Curriculum reference:** TOPIK 6-oriented and near-C2 functional target

#### Required language and situation inventory

Maintain coverage entries for:

- collocations;
- sentence endings and stance;
- social register;
- honorifics;
- workplace expressions;
- pronunciation and prosody;
- idioms;
- Sino-Korean word families;
- cultural references;
- dialectal forms;
- recurring personal errors;
- written style.

**Advanced language functions**

Include:

- humor and irony;
- understatement;
- disagreement without unnecessary directness;
- indirect requests and refusals;
- rapid group interaction;
- interruptions;
- emotionally charged speech;
- different generations’ speaking styles;
- regional accents;
- formal speeches;
- literary prose;
- editing your own writing;
- spontaneous professional explanation.

#### Authoring brief

**Sentence contexts:** Humor, understatement, refusal, emotional stance, literary or formal prose, editing, and turn repair.

**Focused hidden targets:** A compact pragmatic or idiomatic component, precision repair, or attributed marked-language response.

**Authoring criterion:** Keep near-C2 a functional source label, not official equivalence; ensure the text supports the intended implication.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Korean professional, social, and cultural domains

#### Required language and situation inventory

1. **One professional identity in Korean.**
2. **One stable social community.**
3. **One target variety and age-group model.**
4. **Sustained participation in Korean institutions or relationships.**

Use language situations drawn from:

- working or studying in Korean;
- friendships maintained primarily in Korean;
- group activities;
- Korean workplace or university culture;
- conflict, negotiation, and problem-solving in Korean;
- literature and long-form journalism;
- contemporary humor and cultural references;
- advanced pronunciation coaching;
- native editorial feedback.

#### Authoring brief

**Sentence contexts:** Work/study duties, recurring relationships, negotiations, cultural discussion, and locally appropriate messaging.

**Focused hidden targets:** A domain-specific sense, social convention, or register choice within a stated relationship.

**Authoring criterion:** Do not generalize one age group’s speech to all speakers or claim community competence from sentence coverage.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Select contexts for plain/aspirated/tense contrasts, **ㅓ/ㅗ**, **ㅡ/ㅜ**, 받침 before vowels or consonants, liaison, nasalization, lateralization, aspiration, tensification, contractions, and phrase rhythm. Keep the written answer in its standard form rather than respelling sound changes as ordinary orthography.

Document relevant consonant strength/release, vowel quality, phrase grouping, ending intonation, timing, and cross-syllable changes as accurate textual support. A pronunciation note should describe the actual form, not an unchecked rule applied to every environment.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Use actual particles, connective endings, contractions, sentence-final stance, honorification, and natural omitted subjects or objects. A brief exchange may supply the missing social or discourse context; it must not depend on a preceding card. Written sentence cards do not establish broad group-interaction competence.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Begin with practical dialogues and messages, then use original accessible informational prose, essays, narrative, and professional writing. Review noun-modifying clauses, quotation, connectors, stance, and plain written endings. Do not use dense comedy or historical drama as the default model for ordinary contemporary production.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Plan **에/에서**, **은/는 vs 이/가** in context, ability/inability, obligation, intention, experience, time relations, honorification, and stance endings. The source’s **-(으)려고 하다** examples illustrate present intention and interrupted past intention; select contexts that make that difference useful rather than changing only a noun.

If the target is an attached ending, show its exact surface form without a dictionary placeholder such as -(으) in the answer. If a longer verb-plus-ending span is necessary for intelligibility or spelling, keep it compact and label the whole span accurately. Do not hide an entire proposition to test a single ending.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `ko-KR`; source prefix is `ko`; the exact stage IDs are `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "ko-01-0001",
    "locale": "ko-KR",
    "sentence": "선생님, 질문이 있어요.",
    "cloze": "질문",
    "answer": "질문",
    "accepted_answers": [],
    "lemma": "질문",
    "meaning": "a question",
    "part_of_speech": "noun",
    "note": "The sentence uses ordinary polite speech to address a teacher."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| 도서관에서 친구와 같이 공부해요. | `에서` | The visible study activity makes the location-of-action target clear. |
| 운동하려고 했는데 시간이 없었어요. | `하려고 했는데` | A compact intended-action-plus-contrast target; retain the activity and actual obstacle as context. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Review friend, stranger, professor, customer, manager, and relative situations without stereotyping age or status. Check whether a sentence is grammatically valid but socially blunt, overly intimate, or needlessly deferential. Source knowledge about omitted subjects, titles, indirect refusal, response formulas, and endings must affect the actual sentence, not only a post hoc note.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Review particles, tense/aspect, endings, honorifics, word order, omitted or unnecessary subjects, vocabulary, collocation, spacing, spelling, and register. Include natural reformulation, not just a binary grammaticality label. Preserve reference and stance when converting an informational sentence between conversational and plain written styles.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

The source lists **Sogang**, **Online King Sejong**, **Integrated Korean**, and a university-course alternative as distinct curriculum routes, not simultaneous requirements. **Korean Grammar in Use**, the **NIKL learner dictionary**, KBS material, TTMIK, selected introductory university courses, pronunciation examples, and official TOPIK sources support targeted decisions. Mirinae is an analytical aid, not an unquestioned authority.

| Reference | Authoring use |
|---|---|
| [KLEC](https://klec.sogang.ac.kr/?lang=eng) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [IKSI](https://www.iksi.or.kr/lms/main/about.do) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [UH Press](https://uhpress.hawaii.edu/klear/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Source-listed Korean university-course catalogue](https://www.yskli.com/course.php?mid=E01_02) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Darakwon](https://www.darakwon.co.kr/koreanbooks/book_view.asp?bookid=57&lg=en) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Coursera](https://www.coursera.org/learn/learn-korean) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Coursera](https://www.coursera.org/learn/learn-speak-korean1) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Talk To Me In Korean](https://courses.talktomeinkorean.com/course-curriculum) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Korean Dictionary](https://krdict.korean.go.kr/eng) | Check the selected form, sense, construction, or register. |
| [YouGlish](https://youglish.com/korean) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Mirinae Korean Language Explorer](https://mirinae.io/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [KBS World Radio](https://world.kbs.co.kr/service/contents_list.htm?lang=e&menu_cate=learnkorean) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [TOPIK](https://www.topik.go.kr/) | Check the stated task/framework boundary; do not copy examination items. |
| [Study in Korea](https://www.studyinkorea.go.kr/ko/plan/examAndKoreanStudy.do) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| An ending is written with dictionary placeholders in the answer | Use the exact surface form found in the sentence. |
| Honorific and listener politeness are treated as the same feature | Check subject reference and addressee separately. |
| 반말 is used without a fitting relationship | Repair the context or select an appropriate speech level. |
| A syllable or substring is hidden accidentally | Document the morphological objective and validate the boundary. |
| Sino-Korean homophones treated as the same root | Verify each lexical family rather than infer it from spelling alone. |
| An English subject appears in every Korean sentence | Review natural omission and recoverable reference. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained Korean authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-ko-KR`; the guide requires no separate proficiency-plan or conversation attachment.

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
