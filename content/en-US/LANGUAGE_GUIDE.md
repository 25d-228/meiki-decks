# American English: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-en-US`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `en-US`  
**Scope:** A1–C2-oriented American English, followed by professional, social, and cultural specialization.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 7 stages; 9,000 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **contemporary American English (`en-US`)** with a coherent rhotic pronunciation model and ordinary American spelling and vocabulary. The source names **color, center, traveling** as convention examples. Use clear conversational speech, not an exaggerated announcer or fictional character voice.

Broaden recognition of American regions, communities, generations, other national varieties, and internationally accented English where relevant. Do not label another variety wrong merely because it is outside the production model. Select actual sound and usage conventions rather than assembling an accent from unrelated features.

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

Preserve article reference, the tense/aspect time frame, complement structure, and the object placement of phrasal verbs. Keep contractions natural; do not add a mini-story to make an idiom or stance label look advanced.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| The meeting starts at nine. | `starts` | A schedule supports the present-tense use. |
| Her apology rang hollow: she blamed everyone else. | `rang hollow` | The second clause supports the idiomatic evaluation. |
| The extension is conditional on funding. | `conditional on` | An explicit condition supports the formal construction. |

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

Keep the supplied **A2 Key → B1 Preliminary → B2 First → C1 Advanced → C2 Proficiency** reference route. The A1 milestone is a functional beginner scope, not an examination added to that sequence. Maintain American production conventions without claiming every examination requires an American accent.

The source distinguishes language proficiency, pronunciation, professional performance, and community participation. Cards support their language components; they do not establish admission-test compliance, a certificate, or near-native identity. Use current test rules only when a specific examination task is separately authorized and verified.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **7 stages and exactly 9,000 accepted cards** for American English, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** Sound–spelling and sentence foundations are integrated into A1. The progression reserves broad space for lexical senses, auxiliary/article systems, tense/aspect, complement and phrasal-verb patterns, collocations, register, and rhetoric, plus a separate community/domain stage. The quantities are not inferred from an English-speaking learner’s study-hour estimates for another language.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `01` | American English 01 — A1 foundations | Sections 6.1–6.2 | 800 | 20 | 800 |
| `02` | American English 02 — A2 everyday communication | Sections 6.3 | 1,000 | 25 | 1,800 |
| `03` | American English 03 — B1 independent communication | Sections 6.4 | 1,200 | 30 | 3,000 |
| `04` | American English 04 — B2 extended communication | Sections 6.5 | 1,400 | 35 | 4,400 |
| `05` | American English 05 — C1 precise communication | Sections 6.6 | 1,600 | 40 | 6,000 |
| `06` | American English 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,800 | 45 | 7,800 |
| `07` | American English 07 — American social, professional, and cultural depth | Sections 6.8 | 1,200 | 30 | 9,000 |
| **Total** | **7 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **9,000** | **225** | **9,000** |

Use source IDs `en-US-<stage>-0001` through `en-US-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `en-US`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 01:** Integrate sound/spelling, stress, contractions, be/have, articles/number, pronouns, present frames, do questions, basic modals/plans, and everyday vocabulary.
- **Stage 02:** Cover past and progressive frames, future arrangements, comparison/quantity, modals, infinitive/ing complements, basic relatives, present perfect, and routine practical language.
- **Stage 03:** Cover past/perfect and narrative contrasts, conditionals, passive/reporting, relatives/questions, phrasal/prepositional verbs, and wider explanation and social language.
- **Stage 04:** Develop article/reference precision, tense/aspect, modal/conditional contrasts, participial structures, collocations, hedging, reformulation, and genre/register variety.
- **Stage 05:** Cover substantial lexical/collocational breadth, source synthesis, implied stance, qualification, register switching, professional explanation, and multi-party interaction language.
- **Stage 06:** Cover subtle grammar/sense choices, argument reconstruction, rhetoric, idioms, irony, understatement, editing, cultural interpretation, and turn recovery.
- **Stage 07:** Develop distinct community/domain senses, conventions, negotiation, humor, relationships, professional responsibilities, and cultural discussion without reducing American use to accent.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Build the complete beginner-to-advanced series without assuming all learners are beginners or that advanced readers control articles, auxiliaries, spoken segmentation, and register. Record those prerequisites separately rather than suppressing foundation content for everyone.

English is both a target language and the project’s support language. Use short plain-English definitions or paraphrases that are easier than the target. Avoid tautologies such as **important = important** and avoid a difficult definition that makes a beginner card harder than its sentence.

---

## 5. Essential systems to represent in sentences

### Sound, stress, and spelling
Connect words to verified American pronunciation descriptions, lexical stress, phrase prominence, and contextual meaning. The source’s **PHOtograph → phoTOGraphy → photoGRAPHic** family illustrates stress changes to check separately. Study schwa, weak forms, linking, and connected-speech changes without claiming every unstressed vowel becomes schwa or respelling reductions as ordinary writing.

### Articles and countability
Plan reference and countability together: **a report**, **the report we discussed**, general **reports**, and **some information/a piece of information** are different contextual patterns. Do not assign a permanent article to an English noun. Add plural/noncount behavior and a useful collocation in support.

### Auxiliaries and clause frames
Distinguish statement, direct question, negation, past question, modal question, embedded question, subject question, and object question. Do not insert **do** into every interrogative or invert every embedded question.

### Tense, aspect, and American usage
Use routine/current job, temporary arrangement, finished past period, continuing situation, interrupted activity, and anterior event contexts. Compare simple past and present perfect, including source-listed American uses with **already/yet**, without removing present perfect. Distinguish **get–got–gotten**, development with **gotten**, possession with **have got**, and expressions such as **on the weekend** and **Monday through Friday**. Verify contextual use rather than replacing every **got** mechanically.

### Complements and multiword verbs
Plan **explain something to someone, discuss a problem, depend on, avoid doing, want someone to do, look forward to doing**. For multiword verbs, record meaning, object behavior, pronoun placement, and register: **look up the address/look the address up/look it up**, **look into**, and **put up with** are not the same syntactic pattern.

### Social purpose
Specify urgency, authority, familiarity, and tone in requests, refusals, feedback, and disagreement. Do not apply a blanket “Americans are direct” rule or a universal politeness ranking based on sentence length.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Sound–spelling and sentence foundation

#### Required language and situation inventory

Select essential vowel and consonant contrasts from the prerequisite analysis, word stress, /r/, /l/, /w/, /v/, the two th sounds, final consonants, contractions, and phrase grouping. Include identity, numbers, prices, clarification requests, and basic be, have, and present-tense frames.

#### Authoring brief

**Sentence contexts:** Identity, spelling essential information, numbers, prices, questions, clarification, and basic be/have frames.

**Focused hidden targets:** A short word, auxiliary, contraction, or sound–spelling expression.

**Authoring criterion:** Keep useful sentences alongside sound foundations; do not make letter-name recitation a whole curriculum.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

Develop subject and object pronouns; *be* and *have*; articles and basic noun number; simple present; basic present progressive; *do/does* questions and negatives; possessives; common prepositions; *there is/are*; *can*; and basic plans with *going to*.

#### Authoring brief

**Sentence contexts:** Family, home, routine, work/study, food, shopping, directions, schedules, preferences, and plans.

**Focused hidden targets:** A pronoun, article, simple present/progressive, do/does component, preposition, there is/are, or can form.

**Authoring criterion:** Use simple noncircular English support and distinguish question, negative, and statement frames.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

Add simple past and frequent irregular verbs, past progressive, future arrangements, comparisons, quantities, common modal expressions, infinitive/*-ing* patterns, basic relative clauses, and an introduction to present perfect.

#### Authoring brief

**Sentence contexts:** Recent events, appointments, comparisons, practical problems, solutions, and connected messages.

**Focused hidden targets:** Past/progressive/future component, comparison, quantity, modal, complement, or introductory perfect.

**Authoring criterion:** Keep time and reference explicit enough to support the choice; do not broaden a limited pattern into every use.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

Consolidate simple past versus present perfect, narrative sequencing, first and second conditionals, passive foundations, reported speech, relative clauses, question formation, and frequent verb–preposition and phrasal-verb patterns.

#### Authoring brief

**Sentence contexts:** Narration, explanation, opinions, repair, passive/reporting situations, and everyday group decisions.

**Focused hidden targets:** Past/perfect contrast, first/second conditional, passive component, reported speech, relative, or multiword-verb pattern.

**Authoring criterion:** Check pronoun placement, auxiliary syntax, and the actual situation rather than a tense-table label.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

Work on reliable article choice, tense/aspect under pressure, modal meanings, complex conditionals, reported speech, relative and participial structures, hedging, reformulation, collocations, and register-sensitive phrasing.

#### Authoring brief

**Sentence contexts:** Unfamiliar general arguments, meetings, proposals, complaints, reports, and qualified disagreement.

**Focused hidden targets:** Modal/conditional distinction, article/reference choice, participial component, collocation, hedging, or reformulation.

**Authoring criterion:** Keep plain English support and audience fit; a longer or more academic sentence is not automatically B2 learning.

### 6.6. Advanced development

**Curriculum reference:** C1

#### Required language and situation inventory

Develop source synthesis, implicit meaning, qualification, register switching, advanced collocations, extended argument, professional explanation, and fast multi-speaker listening. Use meaningful professional or academic situations rather than translated terminology lists.

#### Authoring brief

**Sentence contexts:** Professional explanation, multi-source discussion, implicit stance, and formal/social register changes.

**Focused hidden targets:** A source-relation, qualification, advanced collocation, or precise audience-sensitive phrase.

**Authoring criterion:** Preserve claim versus qualification and avoid turning the entire stage into specialized jargon.

### 6.7. Proficient integration

**Curriculum reference:** C2

#### Required language and situation inventory

Maintain coverage entries for collocations, subtle grammar choices, discourse organization, pronunciation, register, idioms, cultural references, and recurring personal errors.

**Advanced work.** Synthesize several long sources, reconstruct competing arguments, edit for precision, analyze rhetoric, interpret irony and understatement, and participate in discussions containing interruptions and rapid topic changes.

#### Authoring brief

**Sentence contexts:** Competing arguments, rhetoric, irony, understatement, editing, questioning, and turn recovery.

**Focused hidden targets:** One compact precision repair, rhetorical/idiomatic component, or pragmatic distinction.

**Authoring criterion:** Make context support the intended reading; do not hide the entire analytical response or require unknown external sources.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected American professional, social, and cultural domains

#### Required language and situation inventory

Cover the language and conventions of ordinary social life, the selected profession, and a cultural or intellectual field. Include humor, negotiation, informal messaging, disagreement, and responsibility for real outcomes.

#### Authoring brief

**Sentence contexts:** Work, study, volunteering, friendships, negotiations, cultural references, and responsibility in selected communities.

**Focused hidden targets:** A verified domain-specific sense, natural convention, or relationship-dependent formulation.

**Authoring criterion:** Do not reduce American usage to accent, or claim real community performance from cards.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Cover the source’s vowel contrasts **ship/sheep, full/fool, bed/bad**, consonant contrasts **light/right, vest/west**, **/θ/–/ð/**, final consonants, lexical stress, **/r/**, weak forms, contractions, and phrase prominence. Check both vowel quality and duration, not labels such as long/short alone.

Review the flap **[ɾ]** only in suitable environments; do not turn every written **t** into a **d**. Include regular **-ed** pronunciations **/t/, /d/, /ɪd/** and their phrase behavior. Keep normal spelling and necessary grammar. When stress changes the intended contrast, provide visible context and document the intended emphasis as textual learner support rather than relying on typography alone.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Choose sentences that make weak function words, contractions, endings, word boundaries, prominence, and speaker stance meaningful. Do not drop an auxiliary or inflection to imitate casual speech. A fixed American voice provides a production model, not proof of broad international or overlapping-speech comprehension.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Use original practical messages and contemporary narratives, then explanation, nonfiction, source comparison, professional prose, and literary/rhetorical examples. Check article reference, countability, tense/aspect, clause relations, argument, and collocation. Do not make every advanced text an academic abstract; include ordinary social and professional language.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Build contexts for articles/countability, direct/embedded/subject/object questions, tense/aspect, infinitive/-ing complements, and multiword-verb placement. Use the source’s **used to work / be used to working / get used to working** as distinct state/change/habit patterns, not a list of visually similar translations.

For a separated phrasal verb, target one compact component or a naturally contiguous useful construction. Preserve pronoun position and the visible situation. For a question, hide the auxiliary or another learning-bearing unit rather than a complete sentence transformation. Avoid adjective or verb targets whose English support merely repeats them.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `en-US`; source prefix is `en-US`; the exact stage IDs are `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "en-US-01-0001",
    "locale": "en-US",
    "sentence": "I need some advice about this job.",
    "cloze": "advice",
    "answer": "advice",
    "accepted_answers": [],
    "lemma": "advice",
    "meaning": "suggestions about what to do",
    "part_of_speech": "noun",
    "note": "Advice is noncount in this use."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| I wrote the address down before I left. | `wrote` | The particle remains visible; a separable multiword verb does not require hiding the object too. |
| I used to work nights, but now I work during the day. | `used to` | The visible contrast supports a past habit, not present familiarity with a routine. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Review purpose, authority, urgency, familiarity, turn management, and audience. Use natural American requests, feedback, clarification, professional explanation, and disagreement without stereotyped nationality rules. Keep a character’s written or spoken style consistent with the situation, and attribute marked recognition rather than making every colloquial form a required answer.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check articles/countability, tense/aspect, auxiliaries, complements, prepositions, collocations, organization, register, spelling, and punctuation. Distinguish correctness from effective wording for the actual audience. Advanced editing must preserve argument, source qualification, temporal relations, and commitment; a reviewer’s stylistic preference is not a universal grammar rule.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **American English File**, **Basic Grammar in Use**, and **Grammar in Use Intermediate** for the source-listed curriculum and grammar routes. Rachel’s English and the Color Vowel Chart support pronunciation investigation; VOA material supports beginner contexts; Oxford Learner’s Dictionaries and COCA support usage; Purdue OWL supports writing decisions; Cambridge materials supply the stated assessment reference. None is a new installation or purchasing requirement.

| Reference | Authoring use |
|---|---|
| [Cambridge English, “Should my child learn American or British English?”](https://www.cambridgeenglish.org/learning-english/parents-and-children/how-to-support-your-child/should-my-child-learn-american-or-british-english/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cambridge English, “C2 Proficiency”](https://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/) | Check the stated task/framework boundary; do not copy examination items. |
| [Cambridge English, “Preparing for C2 Proficiency”](https://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/preparation/) | Check the stated task/framework boundary; do not copy examination items. |
| [Oxford University Press, “American English File: 3rd Edition”](https://www.oupjapan.co.jp/en/products/list/2385) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cambridge University Press, “Basic Grammar in Use Student’s Book with Answers,” Fourth Edition](https://shop.cambridge.org/english/product/2700190087) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cambridge University Press catalog, “Grammar in Use Intermediate,” Fourth Edition, American English, B1–B2](https://www.cambridge.org/us/search?iFeelLucky=false&page=2&query=vocabulary+in+use&site=CE) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Rachel’s English, American English pronunciation resources](https://rachelsenglish.com/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [U.S. Department of State, American English, “The Color Vowel Chart”](https://americanenglish.state.gov/resources/color-vowel-chart) | Check the actual pronunciation, prosody, or variety of selected language. |
| [VOA Learning English, “Let’s Learn English 1”](https://learningenglish.voanews.com/p/5644.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Oxford Learner’s Dictionaries](https://www.oxfordlearnersdictionaries.com/us/) | Check the selected form, sense, construction, or register. |
| [English-Corpora.org, “A short tour of the COCA corpus”](https://www.english-corpora.org/coca/help/tour.asp) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [English-Corpora.org, corpus sections and genre comparisons](https://www.english-corpora.org/help/sections.asp) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Purdue OWL, “Academic Writing Introduction”](https://owl.purdue.edu/owl/general_writing/academic_writing/index.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Rachel’s English, “English Pronunciation Study: What did you do Today?”](https://rachelsenglish.com/english-pronunciation-study-today/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Purdue OWL, “How to Use Articles (a/an/the)”](https://owl.purdue.edu/owl/general_writing/grammar/using_articles.html) | Check the selected form, sense, construction, or register. |
| [Purdue OWL, “Count and Noncount Nouns: Basic Rules”](https://owl.purdue.edu/owl/general_writing/grammar/count_and_noncount_nouns/index.html) | Check the selected form, sense, construction, or register. |
| [Cambridge Dictionary, English Grammar Today, “British and American English”](https://dictionary.cambridge.org/grammar/british-grammar/british-and-american-english) | Check the selected form, sense, construction, or register. |
| [Cambridge Dictionary, English Grammar Today, “Verb patterns: verb + infinitive or verb + -ing”](https://dictionary.cambridge.org/grammar/british-grammar/verb-patterns-verb-infinitive-or-verb-ing) | Check the selected form, sense, construction, or register. |
| [Cambridge Dictionary, English Grammar Today, “Phrasal verbs and multi-word verbs”](https://dictionary.cambridge.org/grammar/british-grammar/phrasal-verbs-and-multi-word-verbs) | Check the selected form, sense, construction, or register. |
| [Rachel’s English, “The TH sound Up Close and in Slow Motion”](https://rachelsenglish.com/the-th-sound/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Rachel’s English, “The Flap T!”](https://rachelsenglish.com/flap-t/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Rachel’s English, “ED Endings (1/3)”](https://rachelsenglish.com/ed-endings-2020-1-3/) | Check the actual pronunciation, prosody, or variety of selected language. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| An English definition simply repeats the answer | Use an easier contextual paraphrase. |
| Every question receives do or subject–auxiliary inversion | Distinguish direct, embedded, subject, and object frames. |
| A phrasal verb lacks object-placement information | Verify meaning, separability, and pronoun behavior. |
| Casual speech used to delete necessary written grammar | Retain ordinary spelling and the accepted utterance. |
| Every got mechanically replaced with gotten | Check the actual American construction and sense. |
| Advanced English reduced to academic jargon or accent | Reconcile ordinary, professional, pragmatic, and cultural coverage. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained American English authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-en-US`; the guide requires no separate proficiency-plan or conversation attachment.

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
