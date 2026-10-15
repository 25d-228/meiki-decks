# Korean: sentence and card authoring guide

**Production locale:** `ko-KR`  
**Scope:** basic through TOPIK 6-oriented Korean with separate advanced productive and domain-specific coverage.

## 1. Purpose and required deliverables

**Fixed deliverable: 8 stages; 8,800 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The finished card shows the sentence with that span hidden, provides typed input and the **full-sentence recording on the front**, and reveals the sentence, answer, concise support, and replay on the back. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records, synchronized coverage mappings, and editorial evidence. **Complete and accept all text for all nine project languages before producing any audio.** For this language, finish every planned sentence, cloze, answer, annotation, reading, and coverage mapping, then complete editorial review, corrections, and source checks. Acceptance of this language's text permits the next language's text work, not audio generation. The pronunciation sections describe written sentence/reading requirements and the subsequent audio phase; no representative recordings, auditions, synthesis tests, or denoising runs belong to the text phase. This guide defines authoring scope; it does not certify a learner’s proficiency.

---

## 2. Production model, script, and register

Use **contemporary standard South Korean (`ko-KR`)**. Write Hangul directly, preserving standard spacing and spelling. Teach syllable blocks, 받침, relevant sound changes, and typed form without relying on romanization.

Ordinary polite **해요체**, formal polite **합니다체**, and casual forms require clear relationship and setting. Subject honorification is distinct from politeness toward the listener. Do not adopt 반말 or an entertainment character’s register without a suitable context.

---

## 3. Curriculum framework and limits of card evidence

Keep **TOPIK I**, **TOPIK II**, and the separate **TOPIK Speaking** route distinct as presented in the source. Its advanced objective combines TOPIK 6-oriented work with a separate advanced speaking benchmark and real-world skills. The **A1-like, A2-like, B1-like, B2-like, C1-like, and near-C2** labels are functional shorthand, not official CEFR equivalences.

Do not turn an examination’s receptive coverage into proof of oral, honorific, or group-interaction competence. Card review establishes content quality and mapped coverage, not a learner’s TOPIK score.

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

Create **8 stages and exactly 8,800 accepted cards** for Korean, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, audio files, or reverse cards as additional cards.

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

Use source IDs `ko-<stage>-0001` through `ko-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `ko-KR`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends on the preceding stages of this language, not on knowledge of another project language.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. A different approved batch split must still sum to the same stage count and must not introduce per-batch commits or full test runs.

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

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**Neither agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when both conditions hold: **its exact accepted-card count is met and its complete allocated coverage passes review**. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

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

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **editorial test** are authoring adaptations. They replace learner promotion tests with checks on the created content.

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

**Editorial test:** The 30–50-expression aspiration is not a forced quota. Do not require every sound rule before meaningful sentences.

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

**Editorial test:** Keep social relations coherent and record whether the target is an attached morpheme or a whole word/phrase.

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

**Editorial test:** Introduce formal speech and quotation in scope; do not drop productive language merely because TOPIK I is receptive.

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

**Editorial test:** Identify who is quoted and who is being honored; avoid repetitive 저는/제가 where reference is already clear.

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

**Editorial test:** Explain the interpersonal or certainty effect of the actual ending; do not treat same-sounding roots as identical.

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

**Editorial test:** Do not make all advanced material bureaucratic; preserve social and narrative coverage as well.

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

**Editorial test:** Keep near-C2 a functional source label, not official equivalence; ensure the text supports the intended implication.

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

**Editorial test:** Do not generalize one age group’s speech to all speakers or claim community competence from sentence coverage.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Record the intended reading, phrase boundary, emphasis, and register when needed for later audio production. A spelling check does not prove pronunciation, and a pronunciation annotation does not prove that audio has been produced.

Keep ordinary written answers separate from phonetic aids. **During the audio phase, after all nine languages' text has been accepted**, validate actual recordings against the exact sentence and investigate omissions, changed words, wrong readings, or inappropriate phrasing. Do not count a fixed-voice sentence set as exhaustive accent or multi-speaker listening coverage.

### Language-specific requirements

Select contexts for plain/aspirated/tense contrasts, **ㅓ/ㅗ**, **ㅡ/ㅜ**, 받침 before vowels or consonants, liaison, nasalization, lateralization, aspiration, tensification, contractions, and phrase rhythm. Keep the written answer in its standard form rather than respelling sound changes as ordinary orthography.

Review consonant strength/release, vowel quality, phrase grouping, ending intonation, timing, and cross-syllable changes in later recordings. A pronunciation note should describe the actual form, not an unchecked rule applied to every environment.

---

## 8. Listening-support sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The available front recording intentionally contains the answer. The text need not exclude every imaginable synonym, but the canonical target must be natural, correctly spoken, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Use actual particles, connective endings, contractions, sentence-final stance, honorification, and natural omitted subjects or objects. A brief exchange may supply the missing social or discourse context; it must not depend on a preceding card. Fixed-voice recordings cannot demonstrate broad group-listening competence.

---

## 9. Reading, script, and genre in sentences

Select an appropriate sentence genre and reading burden, not an arbitrary maximum length. Beginners need useful phrases with controlled supporting language; advanced cards may need more visible context for scope, stance, or reference. Extra length is justified only by meaning, not as a substitute for a more advanced target.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Begin with practical dialogues and messages, then use original accessible informational prose, essays, narrative, and professional writing. Review noun-modifying clauses, quotation, connectors, stance, and plain written endings. Do not use dense comedy or historical drama as the default model for ordinary contemporary production.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Plan **에/에서**, **은/는 vs 이/가** in context, ability/inability, obligation, intention, experience, time relations, honorification, and stance endings. The source’s **-(으)려고 하다** examples illustrate present intention and interrupted past intention; select contexts that make that difference useful rather than changing only a noun.

If the target is an attached ending, show its exact surface form without a dictionary placeholder such as -(으) in the answer. If a longer verb-plus-ending span is necessary for intelligibility or spelling, keep it compact and label the whole span accurately. Do not hide an entire proposition to test a single ending.

---

## 11. Lexical support and authoring records

**Production count:** Section 4.1 defines this guide’s exact stage/card schedule. Any lexical, expression, character, or handwriting quantities below are separate curriculum landmarks; they neither replace that schedule nor authorize a smaller deliverable.

Include dictionary form, contextual meaning, accurate grammatical label, and useful particles, complements, irregularity, speech-level, or honorific support. Do not add default romanization. Distinguish a lexical head from its polite or honorific surface form.

The source’s basic milestone mentions **approximately 700–1,000 high-frequency lemmas and chunks**, and the foundation names **30–50 useful expressions**. These are internal breadth aspirations, not official TOPIK thresholds or exact card counts. The guide supplies no complete advanced vocabulary inventory; inventory development remains required.


Use UTF-8 JSON arrays in the approved source layout. Required fields are `id`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`, and `audio`. Required text is nonempty; `accepted_answers` is an array, ordinarily empty. `audio` is the logical future path `audio/<id>.mp3`, not proof that media exists.

Useful nonempty optional fields are `reading`, `grammar`, `register`, and `note`. Omit unused fields. The reading and grammatical label must describe the **actual hidden span**. Keep the contextual English meaning concise; use notes for wider frames and restrictions. Do not insert curriculum IDs, review counts, agent instructions, or source bookkeeping into learner annotations.

The following original design example illustrates the record shape; it is not a production card or a fixed syllabus requirement. The `example` ID must not be copied into a production inventory.

```json
[
  {
    "id": "ko-example-0001",
    "sentence": "선생님, 질문이 있어요.",
    "cloze": "질문",
    "answer": "질문",
    "accepted_answers": [],
    "lemma": "질문",
    "meaning": "a question",
    "part_of_speech": "noun",
    "audio": "audio/ko-example-0001.mp3",
    "note": "The sentence uses ordinary polite speech to address a teacher."
  }
]
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

Author directly in the target language using the approved content process. A learner exercise that prohibits generated prose is **not** a ban on the executor’s assigned sentence-authoring work. Do not translate one shared list across nine languages.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Review particles, tense/aspect, endings, honorifics, word order, omitted or unnecessary subjects, vocabulary, collocation, spacing, spelling, and register. Include natural reformulation, not just a binary grammaticality label. Preserve reference and stance when converting an informational sentence between conversational and plain written styles.

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

**Content basis:** the supplied `ko.md` proficiency guide in `languages.zip`. Its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks are the basis for this document. The original attachment is not required to use this self-contained authoring guide.

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

**Source-file SHA-256:** `65ca870a8babda3c99b60699220952c8b30734beff62774f23a6db25369faa0d`

