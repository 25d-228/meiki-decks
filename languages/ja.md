# Japanese: sentence and card authoring guide

**Production locale:** `ja-JP`  
**Scope:** N5–N1-oriented receptive coverage and a distinct balanced-C1 integration layer, followed by domain specialization.

## 1. Purpose and required deliverables

**Fixed deliverable: 10 stages; 13,400 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The finished card shows the sentence with that span hidden, provides typed input and the **full-sentence recording on the front**, and reveals the sentence, answer, concise support, and replay on the back. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records, synchronized coverage mappings, and editorial evidence. **Complete and accept all text for all nine project languages before producing any audio.** For this language, finish every planned sentence, cloze, answer, annotation, reading, and coverage mapping, then complete editorial review, corrections, and source checks. Acceptance of this language's text permits the next language's text work, not audio generation. The pronunciation sections describe written sentence/reading requirements and the subsequent audio phase; no representative recordings, auditions, synthesis tests, or denoising runs belong to the text phase. This guide defines authoring scope; it does not certify a learner’s proficiency.

---

## 2. Production model, script, and register

Use **contemporary standard Japanese (`ja-JP`) with Tokyo-oriented pronunciation**. Use hiragana, katakana, and kanji through actual vocabulary. Keep normal written forms and target readings separate; do not make rōmaji an accepted substitute for Japanese answers.

Distinguish casual, polite, formal, honorific, and humble expression through roles and relationships. Treat regional, generational, occupational, gender-associated, and fictional role language as attributed recognition where appropriate, not interchangeable production forms. Do not infer a person’s identity from an isolated expression or treat stylized entertainment dialogue as the default.

---

## 3. Curriculum framework and limits of card evidence

Preserve **N5 → N4 → N3 → N2 → N1** as the supplied examination-oriented receptive track. Its independent productive endpoint is **balanced C1**, not a fully specified balanced C2 curriculum. Keep N1/high-receptive work and balanced-C1 integration separate; never relabel the latter C2 merely to match other languages.

The source reports score-dependent JLPT CEFR reference indications, including N1 142+ for a C1 reference and a separate preferred 150+ aspiration. These are source-reported assessment details, not card quotas or a guarantee about current rules. They concern the skills tested and do not establish speaking, writing, or interaction. Card documentation should use the curriculum boundary rather than turn those scores into production acceptance rules.

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

Create **10 stages and exactly 13,400 accepted cards** for Japanese, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, audio files, or reverse cards as additional cards.

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

Use source IDs `ja-<stage>-0001` through `ja-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `ja-JP`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends on the preceding stages of this language, not on knowledge of another project language.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. A different approved batch split must still sum to the same stage count and must not introduce per-batch commits or full test runs.

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

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**Neither agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when both conditions hold: **its exact accepted-card count is met and its complete allocated coverage passes review**. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

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

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **editorial test** are authoring adaptations. They replace learner promotion tests with checks on the created content.

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

**Editorial test:** Keep sound/script and useful grammar together. Formulaic early material is not permission to introduce every related productive pattern.

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

**Editorial test:** The blank must test the intended distinction, with natural visible support rather than a whole sentence hidden.

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

**Editorial test:** Make actor, beneficiary, and social relationship recoverable; keep causative-passive recognition separate from unrestricted production.

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

**Editorial test:** Avoid unnecessary explicit subjects while keeping omitted information interpretable inside the card.

### 6.5. Upper-intermediate operation

**Curriculum reference:** N2-oriented / receptive B2-oriented with separate production

#### Required language and situation inventory

Consolidate the intermediate grammar inventory and similar-pattern distinctions. Develop extended argument, qualification, evidence, formal versus conversational expression, workplace interaction, keigo in defined roles, and reduced or multi-speaker listening. Use Quartet II and selected advanced-bridge material rather than treating N2 preparation as the entire curriculum.

#### Authoring brief

**Sentence contexts:** Workplace and telephone interaction, evidence, general argument, source-based writing, and contemporary narrative.

**Focused hidden targets:** A developed collocation, qualification, keigo component, or spoken/written reformulation.

**Editorial test:** The source gives a functional expansion, not an exhaustive N2 grammar list. Map and justify the actual selected distinctions.

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

**Editorial test:** Track the large lexical/kanji aspirations honestly; a few abstract connectors do not constitute the whole advanced inventory.

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

**Editorial test:** Keep this endpoint labeled balanced C1. Do not claim C2 or native identity from the card set.

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

**Editorial test:** Do not ask one card to prove interpretation of actual silence or overlapping conversation; model only the language component.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Record the intended reading, phrase boundary, emphasis, and register when needed for later audio production. A spelling check does not prove pronunciation, and a pronunciation annotation does not prove that audio has been produced.

Keep ordinary written answers separate from phonetic aids. **During the audio phase, after all nine languages' text has been accepted**, validate actual recordings against the exact sentence and investigate omissions, changed words, wrong readings, or inappropriate phrasing. Do not count a fixed-voice sentence set as exhaustive accent or multi-speaker listening coverage.

### Language-specific requirements

Select vocabulary and sentences covering long/short vowels, single/doubled consonants, ん before different consonants, high-vowel devoicing, mora timing, pitch drops, phrase boundaries, focus, and intonation. The source supplies **おばさん/おばあさん, ここ/こうこう, きて/きって, かこ/かっこ, びょういん/びよういん** as contrast seeds; choose meaningful original contexts rather than packing them into tongue twisters.

Check the reading of the actual inflected target. Use verified Tokyo-oriented models; do not infer every compound’s reading or accent from its characters. Record phrase-level requirements where useful for later audio review, without generating samples during the nine-language text phase.

---

## 8. Listening-support sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The available front recording intentionally contains the answer. The text need not exclude every imaginable synonym, but the canonical target must be natural, correctly spoken, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Model natural omission, shortened forms, endings, backchannels, quotation, changes in politeness, and implied conclusions. For a repair or unfinished-turn example, keep the intended relation understandable inside the accepted sentence or short exchange. Do not represent a single scripted voice as evidence of multi-person listening ability.

---

## 9. Reading, script, and genre in sentences

Select an appropriate sentence genre and reading burden, not an arbitrary maximum length. Beginners need useful phrases with controlled supporting language; advanced cards may need more visible context for scope, stance, or reference. Extra length is justified only by meaning, not as a substitute for a more advanced target.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from kana-supported practical sentences and easy narrative to accessible nonfiction, essays, interviews, contemporary stories, journalism, and specialist prose. Avoid gratuitous rare kanji and stylized historical speech in early material. Make clause modification, viewpoint, reference, and the reading of each taught word clear. Answer-side readings must not become an unrequested all-furigana production answer.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Use the source’s **行きたくないわけではない / 行かないわけにはいかない / 行くわけがない / 行くわけだ / 行くというわけだ** family to plan differences in implication, obligation, impossibility, inference, and explanation. These are reference patterns, not a sentence list to copy unchanged.

Keep the actual proposition visible and hide the shortest useful component that tests the distinction. Do not respond to a long-cloze defect by deleting only one word while leaving nearly the entire predicate hidden. Giving/receiving and transitivity contrasts must make the actor or beneficiary recoverable, not merely alternate verb endings.

---

## 11. Lexical support and authoring records

**Production count:** Section 4.1 defines this guide’s exact stage/card schedule. Any lexical, expression, character, or handwriting quantities below are separate curriculum landmarks; they neither replace that schedule nor authorize a smaller deliverable.

Provide the target’s exact spelling and reading, useful dictionary form, contextual meaning, whole-span grammatical label, and necessary transitivity, particle, collocation, or register support. If the target is a passive or other inflected form, its reading must match that form rather than the lemma.

For **見送る**, distinguish seeing someone off from postponing or abandoning a plan in the selected context. For **提案, 提唱, 提示, 提供, 前提, 提起**, distinguish actual lexical uses rather than treating recognition of 提 as knowledge of every compound. The source’s lexical and kanji aspirations below describe breadth, not official JLPT word lists or a final card total.

### Coverage landmarks from the supplied curriculum

| Source milestone | Lexical coverage | Kanji recognition through vocabulary |
|---|---|---|
| Basic / N5-oriented | Approximately 900–1,200 useful words | Approximately 150–200 |
| Routine / N4-oriented | Approximately 2,000–2,800 words | Approximately 350–500 |
| Independent / N3-oriented | Approximately 4,000–5,500 words | Approximately 700–900 |
| Upper-intermediate / N2-oriented | Approximately 8,000–10,000 words | Approximately 1,300–1,600 |
| N1 / high receptive competence | Approximately 13,000–18,000 lexical items | Common-use range, plus names and domain-specific characters encountered in use |

These are the original guide’s internal coverage aspirations, not validated vocabulary-to-level conversions. Its cited common-use kanji table contains 2,136 characters; recognizing that inventory is not the same as knowing every word or reading containing those characters. ([Agency for Cultural Affairs: common-use kanji table](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/pdf/joyokanjihyo_20101130.pdf))

Use UTF-8 JSON arrays in the approved source layout. Required fields are `id`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`, and `audio`. Required text is nonempty; `accepted_answers` is an array, ordinarily empty. `audio` is the logical future path `audio/<id>.mp3`, not proof that media exists.

Useful nonempty optional fields are `reading`, `grammar`, `register`, and `note`. Omit unused fields. The reading and grammatical label must describe the **actual hidden span**. Keep the contextual English meaning concise; use notes for wider frames and restrictions. Do not insert curriculum IDs, review counts, agent instructions, or source bookkeeping into learner annotations.

The following original design example illustrates the record shape; it is not a production card or a fixed syllabus requirement. The `example` ID must not be copied into a production inventory.

```json
[
  {
    "id": "ja-example-0001",
    "sentence": "駅の前で友達を待っています。",
    "cloze": "待っています",
    "answer": "待っています",
    "accepted_answers": [],
    "lemma": "待つ",
    "meaning": "am waiting",
    "part_of_speech": "verb",
    "audio": "audio/ja-example-0001.mp3",
    "reading": "まっています",
    "note": "The ている form presents the waiting as ongoing here."
  }
]
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

Author directly in the target language using the approved content process. A learner exercise that prohibits generated prose is **not** a ban on the executor’s assigned sentence-authoring work. Do not translate one shared list across nine languages.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Review particles, transitivity, aspect, tense, vocabulary, collocation, clause connection, register, kanji/orthography, excessive explicitness, missing context, and English-shaped pronoun use. Advanced material should include audience-sensitive summaries, arguments, reports, and professional messages, not only personal narrative. Preserve source stance and viewpoint during reformulation.

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

**Content basis:** the supplied `ja.md` proficiency guide in `languages.zip`. Its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks are the basis for this document. The original attachment is not required to use this self-contained authoring guide.

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

**Source-file SHA-256:** `36ac407d558391676fe525af2ab690f042563c5bf856eae3af389cb06253ccd6`

