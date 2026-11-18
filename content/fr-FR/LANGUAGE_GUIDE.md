# French: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-fr-FR`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `fr-FR`  
**Scope:** A1–C2-oriented metropolitan French, with a separate domain-specialization layer.

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

Use **educated contemporary metropolitan French (`fr-FR`)** as the production model. Keep pronunciation, everyday vocabulary, writing conventions, and register coherent. Include both ordinary conversational French and careful edited writing, with labels where they differ.

Broaden recognition of unfamiliar accents and region-sensitive usage without making the expected answers a mixture of production standards. Reduced speech is part of the language model, not permission to replace standard written words with arbitrary phonetic spellings.

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

Preserve pronoun antecedents, verb government, and enough time or stance information for tense/mood. Count apostrophe forms using the operational rule below; never alter elision or hyphenation to manipulate the count.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| J'ai laissé mon sac près de la porte. | `près de` | A concrete location supports the prepositional phrase. |
| Son accord reste subordonné à l'obtention d'un financement. | `subordonné à` | An explicit condition supports a formal construction. |
| Il promettait la transparence, mais refuse de publier les chiffres. | `transparence` | The contrasting action makes the abstract sense concrete. |

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

Keep the supplied **DELF-oriented beginner/independent progression** and **DALF C1/C2-oriented advanced progression**. Foundation supports A1; C2 is not a synonym for native social and cultural competence. Examination genres can inform sentence contexts, but completing a collection does not demonstrate a DELF/DALF result or spontaneous professional performance.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **7 stages and exactly 7,600 accepted cards** for French, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** Sound–spelling foundations are integrated into A1. Counts increase to accommodate the expanding lexical, pronoun, mood, collocation, register, and rhetorical inventories, and a separate final stage keeps professional, social, and cultural specialization in scope instead of absorbing it into a short C2 summary.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `01` | French 01 — A1 foundations | Sections 6.1–6.2 | 600 | 15 | 600 |
| `02` | French 02 — A2 everyday communication | Sections 6.3 | 800 | 20 | 1,400 |
| `03` | French 03 — B1 independent communication | Sections 6.4 | 1,000 | 25 | 2,400 |
| `04` | French 04 — B2 extended communication | Sections 6.5 | 1,200 | 30 | 3,600 |
| `05` | French 05 — C1 precise communication | Sections 6.6 | 1,400 | 35 | 5,000 |
| `06` | French 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,600 | 40 | 6,600 |
| `07` | French 07 — Social, professional, and cultural depth | Sections 6.8 | 1,000 | 25 | 7,600 |
| **Total** | **7 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **7,600** | **190** | **7,600** |

Use source IDs `fr-<stage>-0001` through `fr-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `fr-FR`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 01:** Integrate sound contrasts and liaison planning with articles, gender, present forms, questions, agreement, quantities, basic lexical frames, and useful transactions.
- **Stage 02:** Cover past forms, object/reflexive pronouns, commands, quantities, comparisons, relatives, early y/en, verb prepositions, and chronological narrative.
- **Stage 03:** Cover narrative aspect, conditionals, pronoun order, y/en, subjunctive uses, reporting, clause relations, participle agreement, and expanded lexical families.
- **Stage 04:** Cover tense/mood distinctions, relatives, passive/impersonal/participial forms, concession, qualification, reformulation, spoken reductions, and collocations in varied genres.
- **Stage 05:** Protect broad lexical/collocational development alongside source synthesis, implied attitude, nuanced disagreement, academic/professional expression, and conversational register.
- **Stage 06:** Cover rhetorical and literary interpretation, idioms, irony, understatement, indirect criticism, editing, regional recognition, and informal reduced-language interpretation.
- **Stage 07:** Retain language for selected communities, work, cultural fields, relationships, group interaction, and locally situated meanings beyond the same C2 uses.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Treat English cognates as candidate learning material, not already-known French. Check gender, sound, preposition, collocation, register, and false-friend risk. The source’s **analyse** family illustrates why a bare translation does not supply **une analyse approfondie**, **analyser les résultats**, or **procéder à une analyse de**.

The source encourages increasing use of French definitions and paraphrases. The project’s `common.meaning` field remains concise English support; use natural French paraphrase/definition tasks in suitable advanced sentences and state this representation choice rather than silently changing the support language mid-series.

---

## 5. Essential systems to represent in sentences

### Sound, spelling, and noun phrases
Select real phrases that connect vowels, nasalization, silent letters, liaison, enchaînement, and rhythm to meaning. For nouns, include gender and useful articles in support; test definite, indefinite, partitive, and agreement choices through the intended reference or quantity.

### Verbs and pronouns
Plan present and near future, **passé composé/imparfait**, future, conditional, and subjunctive by function. Record the verb’s prepositions and complements. Distinguish subject, direct-object, and indirect-object pronouns; cover pronoun order, **y**, **en**, and reflexive uses without losing the antecedent.

### Clause relations
Cover questions, negation, relative clauses, reported speech, **si** hypotheses, cause, purpose, consequence, opposition, concession, and qualification. The blank must test that relation or a meaningful component; merely placing a connector in the visible text is not coverage of it.

### Lexical and stylistic precision
Use collocations, discourse markers, spoken reductions, and formal/neutral/informal reformulation. Advanced source comparison, irony, indirect criticism, and rhetorical analysis need a compact original context with visible evidence. Do not confuse rare synonyms with advanced control.

### Annotation boundaries
A gender-plus-collocation target can hide **une décision** inside a full sentence; a target hiding only **une** must have **une**, not **une décision**, as its answer. Verb-frame targets such as **dépendre de** need the actual preposition and contextual complement. Corrective examples must supply a natural alternative rather than only label the learner formulation wrong.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Sound–spelling and basic sentence foundation

#### Required language and situation inventory

- `/u/` versus `/y/`;
- `/e/` versus `/ɛ/`;
- `/ø/` versus `/œ/`;
- nasal vowels;
- silent final consonants;
- syllable grouping;
- basic liaison and *enchaînement*;
- French sentence rhythm.

Specify the intended sound–spelling relationships and phrasing as written learner support for these sentences.

Author greetings, identity, nationality, numbers, basic articles, être, avoir, elementary questions, and clarification language alongside sound coverage.

#### Authoring brief

**Sentence contexts:** Greetings, identity, numbers, clarification, être/avoir, basic questions, and useful article phrases.

**Focused hidden targets:** A short word or expression exposing a stated vowel, spelling, or phrase-boundary feature.

**Authoring criterion:** Do not delay useful sentence authoring until every phonological topic is covered. Check the textual pronunciation guidance that each selected target actually needs.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

- definite, indefinite, and partitive articles;
- noun gender with every noun;
- present tense of regular verbs;
- approximately 20 essential irregular verbs;
- subject pronouns;
- basic adjective agreement;
- negation;
- direct questions and question words;
- possessives and demonstratives;
- basic place and time prepositions;
- *c’est*, *il est*, *il y a*;
- the immediate future;
- numbers, dates, times, prices, and quantities.

#### Authoring brief

**Sentence contexts:** Routine, home, work, family, preferences, plans, quantities, and basic transactions.

**Focused hidden targets:** An article, agreement form, present verb, question component, possessive, or near-future expression.

**Authoring criterion:** Record noun gender and contextual quantity; keep syntax within the stated beginner inventory.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

- *passé composé* with *avoir* and *être*;
- introduction to the imperfect;
- direct and indirect object pronouns;
- reflexive verbs;
- imperative;
- quantities and partitives;
- comparisons and superlatives;
- relative pronouns *qui*, *que*, and *où*;
- introduction to *y* and *en*;
- basic future forms;
- common verb-preposition constructions;
- chronological connectors.

#### Authoring brief

**Sentence contexts:** Recent events, problems, instructions, directions, appointments, comparisons, and short messages.

**Focused hidden targets:** A passé composé form, introductory imperfect, object/reflexive pronoun, relative, y/en use, or verb preposition.

**Authoring criterion:** Provide antecedents and temporal support. Do not collapse all object pronouns into one interchangeable category.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

- *passé composé* versus *imparfait*;
- future and conditional;
- object-pronoun order;
- *y* and *en* in normal speech;
- common subjunctive triggers;
- relative pronouns;
- reported speech;
- cause, consequence, purpose, and opposition;
- hypothesis with *si*;
- agreement of common past participles;
- more precise preposition use.

#### Authoring brief

**Sentence contexts:** Narration, opinion with examples, everyday repair, source summaries, and coherent personal explanation.

**Focused hidden targets:** Aspect contrast, hypothesis component, common subjunctive trigger/use, reported speech, or pronoun sequence.

**Authoring criterion:** Keep cause, purpose, consequence, and opposition faithful to the situation; never conceal the whole explanation.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

- accurate tense and mood selection;
- advanced relative structures;
- passive and impersonal constructions;
- participial constructions;
- concession and qualification;
- logical connectors;
- reformulation;
- hedging;
- formal versus informal language;
- collocations rather than isolated vocabulary;
- frequent spoken reductions.

#### Authoring brief

**Sentence contexts:** Unfamiliar general issues, proposals, complaints, formal messages, source comparison, and reviews.

**Focused hidden targets:** Concession, qualification, hedging, a compact passive/participial component, or register-sensitive collocation.

**Authoring criterion:** Include actual spoken/written differences and natural phrasing rather than a list of formal connectors.

### 6.6. Advanced development

**Curriculum reference:** C1

#### Required language and situation inventory

- synthesis of multiple sources;
- implicit meaning and speaker attitude;
- nuanced agreement and disagreement;
- reformulation without lexical repetition;
- long, organized oral responses;
- formal and academic writing;
- idiomatic collocations;
- conversational discourse markers;
- switching between social registers;
- comprehension of rapid unscripted speech.

#### Authoring brief

**Sentence contexts:** Professional and academic cases, nuanced discussion, implicit attitude, and multi-source positions.

**Focused hidden targets:** A precise source-relation or stance expression, natural reformulation, idiomatic collocation, or conversational marker.

**Authoring criterion:** Attribute views and limits explicitly; a longer sentence or rarer word alone is not new C1 learning.

### 6.7. Proficient integration

**Curriculum reference:** C2

#### Required language and situation inventory

Maintain coverage entries for:

- collocations;
- register;
- idioms;
- discourse markers;
- pronunciation and prosody;
- false friends;
- cultural references;
- recurring personal errors;
- stylistic differences;
- France-specific or region-specific usage.

- synthesizing several long sources;
- reconstructing complex arguments;
- speaking with precise qualification;
- irony, understatement, indirect criticism, and humor;
- stylistically differentiated writing;
- literary and rhetorical analysis;
- debates involving interruptions and rapid turn-taking;
- unfamiliar accents;
- informal, reduced spoken French;
- editing your own writing for elegance.

#### Authoring brief

**Sentence contexts:** Brief original rhetorical, literary, editing, irony, understatement, and indirect-criticism cases.

**Focused hidden targets:** One interpretable rhetorical device in use, precise lexical distinction, or focused editing repair.

**Authoring criterion:** The text must support the interpretation. Do not turn long-paper or debate tasks into whole-paragraph clozes.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected Francophone professional, social, and cultural domains

#### Required language and situation inventory

Include:

1. **One target variety**: for example, educated metropolitan French.
2. **One professional identity** in French.
3. **One real social community**.
4. **Several cultural fields** you follow consistently.

Near-native development requires group interaction, not only one-to-one lessons. Native conversation includes overlapping speech, interruption, implication, humor, disagreement, background assumptions, and rapid topic changes.

Use language situations drawn from:

- living or working in a Francophone environment;
- friendships maintained in French;
- professional tasks completed in French;
- group discussions;
- cultural events;
- reading contemporary literature and essays;
- analyzing comedy and informal conversation;
- advanced prosody coaching;
- regular writing reviewed by an exacting native editor.

#### Authoring brief

**Sentence contexts:** Work, relationships, cultural discussion, disagreement, and messaging in a defined Francophone setting.

**Focused hidden targets:** A useful locally situated expression, domain sense, or audience-dependent choice.

**Authoring criterion:** Keep the target variety and domain explicit; sentence coverage cannot demonstrate natural community participation.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Plan the source’s **/u/–/y/**, **/e/–/ɛ/**, **/ø/–/œ/**, oral/nasal vowels, silent final consonants, syllable groups, liaison, enchaînement, and sentence rhythm. **tout/tu**, **dessus/dessous**, and **peu/peur** are source-listed contrast seeds; embed selected words in original meaningful sentences.

Specify the intended phrasing and register. Distinguish silent letters from pronounced segments and do not infer a liaison solely from adjacent spelling. Check written support for vowel quality, phrase grouping, liaison, consonant behavior, and intonation. Correct typed spelling does not establish a learner’s pronunciation ability.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Select phrases whose written forms can be hard to segment in speech: pronoun chains, silent segments, liaison, enchaînement, and common reductions. Preserve ordinary written forms in the complete source sentence. In advanced material, make stance, irony, or a repaired turn understandable from the text; do not rely only on unprovided prosody or actual overlapping speakers.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Progress from personal messages and practical text to accessible nonfiction, journalism-style argument, contemporary narrative, and specialist writing. Review gender/reference, **y/en**, verb–preposition frames, clause relations, tense/mood, collocations, and audience. Use concise original source situations for synthesis rather than external passages the learner cannot see.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Build nearby alternatives around **passé composé/imparfait**, future/conditional, subjunctive triggers, **si** clauses, direct/indirect pronouns, **y/en**, relative clauses, and complement frames. Change event framing, reference, or communicative purpose so the contrast carries meaning.

For a relative or pronoun target, leave enough of the antecedent and governor visible. For discontinuous negation or a longer construction, select one contiguous learning-bearing component. Do not force all pronouns or a complete subordinate clause into one blank simply to make it unique.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `fr-FR`; source prefix is `fr`; the exact stage IDs are `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "fr-02-0001",
    "locale": "fr-FR",
    "sentence": "J'ai laissé mon sac près de la porte.",
    "cloze": "près de",
    "answer": "près de",
    "accepted_answers": [],
    "lemma": "près de",
    "meaning": "near",
    "part_of_speech": "prepositional phrase"
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| Nous devons prendre une décision avant midi. | `une décision` | An article-plus-noun target hides both words and keeps the verb collocation visible. |
| Le train était déjà parti quand nous sommes arrivés. | `était déjà parti` | Test anteriority with both time points visible; retain the completed subordinate clause as context. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Distinguish correct French from natural French for the relationship and audience. Review requests, disagreement, repair, stance, and formal/informal alternatives. Replace unsupported universal politeness rules with a specified speaker, listener, purpose, and constraint. Model conversational responses as language content, not instructions to schedule tutor sessions.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Review gender, agreement, tense/mood, prepositions, vocabulary, syntax, register, spelling, and collocation. Include original messages, summaries, arguments, proposals, and professional reformulations at the corresponding milestones. An editorial improvement must preserve information, stance, uncertainty, and audience; shorter wording is not automatically better.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **Cosmopolite**, **Grammaire progressive**, and **Phonétique progressive** as the source-listed curriculum, grammar, and sound routes. The source also names TV5MONDE, InnerFrench, RFI, ARTE, France Culture, YouGlish, Le Robert, CNRTL, and DELF/DALF materials. Use dictionaries and genre examples for particular decisions; no course purchase or completion is an authoring prerequisite.

| Reference | Authoring use |
|---|---|
| [Hachette FLE](https://www.hachettefle.com/livres-collections-cosmopolite/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [CLE International](https://www.cle-international.com/adolescents/grammaire-progressive-du-francais-niveau-perfectionnement-b2c2-livre-2eme-edition-9782090395136.html) | Check the selected form, sense, construction, or register. |
| [Progressive](https://progressive.cle-international.com/9782090384550) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [TV5MONDE Apprendre](https://apprendre.tv5monde.com/en) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [innerFrench](https://innerfrench.com/podcast/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Apple Podcasts](https://podcasts.apple.com/at/podcast/journal-en-fran%C3%A7ais-facile/id1573764973) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [ARTE](https://www.arte.tv/en/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [YouGlish](https://youglish.com/french) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Le Robert Dictionary](https://dictionnaire.lerobert.com/fr/) | Check the selected form, sense, construction, or register. |
| [France Education International](https://www.france-education-international.fr/diplome/delf-tout-public/niveau-b2/exemples-sujets) | Check the stated task/framework boundary; do not copy examination items. |
| [DALF examples](https://www.france-education-international.fr/diplome/dalf/exemples-sujets) | Check the stated task/framework boundary; do not copy examination items. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| Hidden article but article-plus-noun answer | Make the displayed span and canonical answer identical. |
| Bare cognate meaning without gender or construction | Add the contextual lexical package and a meaningful retrieval target. |
| y/en or another pronoun without an antecedent | Make the relevant reference recoverable in the sentence. |
| Spelling used as a complete sound model | Specify liaison, silent material, vowel quality, and register in accurate written learner support. |
| Formal wording presented as the only natural French | Label genre and relationship and distinguish correctness from appropriateness. |
| A complete rewritten proposition hidden in an editing card | Hide the focused repair and keep the source claim visible. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained French authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-fr-FR`; the guide requires no separate proficiency-plan or conversation attachment.

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
