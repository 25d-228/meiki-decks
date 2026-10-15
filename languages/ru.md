# Russian: sentence and card authoring guide

**Production locale:** `ru-RU`  
**Scope:** A1–C2/TORFL-oriented Russian with a separate professional, social, and cultural specialization layer.

## 1. Purpose and required deliverables

**Fixed deliverable: 8 stages; 10,100 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The finished card shows the sentence with that span hidden, provides typed input and the **full-sentence recording on the front**, and reveals the sentence, answer, concise support, and replay on the back. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records, synchronized coverage mappings, and editorial evidence. **Complete and accept all text for all nine project languages before producing any audio.** For this language, finish every planned sentence, cloze, answer, annotation, reading, and coverage mapping, then complete editorial review, corrections, and source checks. Acceptance of this language's text permits the next language's text work, not audio generation. The pronunciation sections describe written sentence/reading requirements and the subsequent audio phase; no representative recordings, auditions, synthesis tests, or denoising runs belong to the text phase. This guide defines authoring scope; it does not certify a learner’s proficiency.

---

## 2. Production model, script, and register

Use **educated contemporary Standard Russian (`ru-RU`)** and Cyrillic spelling. Keep normal sentence/answer orthography separate from learner stress annotations. Include **ё** where the selected word requires it; do not erase distinctions or automatically accept Latin lookalikes.

The source includes print, italic, handwritten-form recognition, and typing. Typed cloze cards can support script recognition and typing; they do not certify cursive or handwriting. Use a coherent production model while labeling relevant regional or social recognition. Specify **ты/вы**, names, patronymics, titles, and diminutives when the relationship matters.

---

## 3. Curriculum framework and limits of card evidence

Preserve the supplied **TORFL/ТРКИ** route: Elementary A1, Basic A2, and certification levels I–IV associated with B1–C2 in the guide. Its independent goals include spontaneous interaction, pronunciation, register, professional writing, and cultural competence. The guide’s functional milestones are not official score criteria, and card counts do not establish a TORFL result.

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

Create **8 stages and exactly 10,100 accepted cards** for Russian, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, audio files, or reverse cards as additional cards.

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

Use source IDs `ru-<stage>-0001` through `ru-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `ru-RU`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends on the preceding stages of this language, not on knowledge of another project language.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. A different approved batch split must still sum to the same stage count and must not introduce per-batch commits or full test runs.

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

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**Neither agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when both conditions hold: **its exact accepted-card count is met and its complete allocated coverage passes review**. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Prior Slavic-language knowledge can create apparent familiarity without correct Russian stress, aspect, case government, motion, or register. Check these systems independently and record false-friend risks.

Introduce useful sentences alongside Cyrillic and sound. Preserve the source’s distinction between a high-frequency case function and mastery of all endings. Do not skip sound or morphology because a word resembles another language, and do not delay meaningful sentences until a complete declension chart is memorized.

---

## 5. Essential systems to represent in sentences

### Cyrillic and stress
Connect spelling, sound, and lexical meaning directly. Avoid Latin transliteration as the answer. Check stress in the **actual inflected form**, including movement across a paradigm; a stressed lemma alone is insufficient. Preserve standard spelling in `sentence`, `cloze`, and `answer`, with pedagogical acute marks in `reading` or clearly labeled support.

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

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **editorial test** are authoring adaptations. They replace learner promotion tests with checks on the created content.

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

**Editorial test:** Do not make stress annotations part of the ordinary typed answer or pretend typed input assesses handwriting.

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

**Editorial test:** Prioritize functions rather than equal mastery of all case endings; keep aspect introduction contextual.

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

**Editorial test:** Keep route, animacy, event framing, and case governor explicit enough to support the choice.

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

**Editorial test:** Introduce motion prefixes through situations and keep recognition versus productive use explicit.

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

**Editorial test:** Verify derived meanings and subject/reference relations; do not treat every prefix as transparent.

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

**Editorial test:** Keep conversational and formal written syntax distinct and preserve source uncertainty.

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

**Editorial test:** Make the implication or allusion interpretable without invented history; do not hide a whole professional explanation.

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

**Editorial test:** Name the relevant domain/community scope; card evidence is not a native-participation assessment.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Record the intended reading, phrase boundary, emphasis, and register when needed for later audio production. A spelling check does not prove pronunciation, and a pronunciation annotation does not prove that audio has been produced.

Keep ordinary written answers separate from phonetic aids. **During the audio phase, after all nine languages' text has been accepted**, validate actual recordings against the exact sentence and investigate omissions, changed words, wrong readings, or inappropriate phrasing. Do not count a fixed-voice sentence set as exhaustive accent or multi-speaker listening coverage.

### Language-specific requirements

Cover hard/soft consonants, **ы/и**, stressed versus reduced **о/а**, unstressed **е/я**, **ш/щ**, **ц/ч**, **х**, voicing assimilation, final devoicing, clusters, stress, phrasing, and intonation. The source’s **был/бил, мат/мать, угол/уголь, лук/люк, брат/брать** are meaningful contrast seeds.

Do not equate written vowels with fully articulated sounds in every position. Review stress and vowel reduction together with consonant softness and phrase boundaries. A stress mark copied from the lemma may be wrong for an inflection; verify the exact form before authoring its reading annotation.

---

## 8. Listening-support sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The available front recording intentionally contains the answer. The text need not exclude every imaginable synonym, but the canonical target must be natural, correctly spoken, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Select sentences with real reductions, case endings, aspect contrasts, motion forms, particles, and marked focus where appropriate. Keep the accepted text distinct from a phonetic transcription. A recording must retain the morphology carrying the target, even when ordinary speech reduces other segments. Social or regional variation requires attributed recognition rather than a mixed voice specification.

---

## 9. Reading, script, and genre in sentences

Select an appropriate sentence genre and reading burden, not an arbitrary maximum length. Beginners need useful phrases with controlled supporting language; advanced cards may need more visible context for scope, stance, or reference. Extra length is justified only by meaning, not as a substitute for a more advanced target.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Use contemporary practical language and accessible narratives before dense literary prose. Advance into nonfiction, argument, professional text, and literary/stylistic analysis. Make case governors, participial relations, aspect, motion, and information structure recoverable. Stress support belongs in annotations, not mandatory ordinary orthography; handwriting/cursive recognition is separately scoped.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Plan case contrasts by governor and meaning, aspect contrasts by event framing, and motion contrasts by route and habituality. Do not generate complete noun or verb tables merely by changing endings. The source’s reading/process-completion examples and present/habitual motion examples are contrast patterns to adapt into original contexts.

Hide a useful inflected word or compact phrase, not a whole English-to-Russian translation. Keep the governor visible when case selection is the target. For a stress-and-inflection objective, the hidden answer is ordinary written Russian and the support contains the correct stressed form. Word-order targets must leave a meaningful contrast visible rather than shuffle a full sentence without purpose.

---

## 11. Lexical support and authoring records

**Production count:** Section 4.1 defines this guide’s exact stage/card schedule. Any lexical, expression, character, or handwriting quantities below are separate curriculum landmarks; they neither replace that schedule nor authorize a smaller deliverable.

Supply the actual target’s stress, dictionary form, contextual meaning, grammatical category, and relevant gender, conjugation, case frame, aspect, or motion information. Add only useful partners/collocations in notes; do not hide a complete aspect-pair table.

The source specifies **80–120 foundation expressions** and **approximately 2,000–2,800 useful lexical items/chunks at A2** as internal breadth aspirations. They are not official TORFL requirements or a fixed number of cards. It does not supply an exhaustive inventory for every stage; record that selection work honestly.


Use UTF-8 JSON arrays in the approved source layout. Required fields are `id`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`, and `audio`. Required text is nonempty; `accepted_answers` is an array, ordinarily empty. `audio` is the logical future path `audio/<id>.mp3`, not proof that media exists.

Useful nonempty optional fields are `reading`, `grammar`, `register`, and `note`. Omit unused fields. The reading and grammatical label must describe the **actual hidden span**. Keep the contextual English meaning concise; use notes for wider frames and restrictions. Do not insert curriculum IDs, review counts, agent instructions, or source bookkeeping into learner annotations.

The following original design example illustrates the record shape; it is not a production card or a fixed syllabus requirement. The `example` ID must not be copied into a production inventory.

```json
[
  {
    "id": "ru-example-0001",
    "sentence": "После работы я читаю газету.",
    "cloze": "газету",
    "answer": "газету",
    "accepted_answers": [],
    "lemma": "газета",
    "meaning": "a newspaper",
    "part_of_speech": "noun",
    "audio": "audio/ru-example-0001.mp3",
    "reading": "газе́ту",
    "note": "Accusative singular of the feminine noun газета."
  }
]
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

Author directly in the target language using the approved content process. A learner exercise that prohibits generated prose is **not** a ban on the executor’s assigned sentence-authoring work. Do not translate one shared list across nine languages.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check stress support, spelling, case, agreement, aspect, motion verbs, word order, government, vocabulary, collocation, register, punctuation, and translation-shaped phrasing. Preserve actors and reference in participial constructions. Editing for concision must not remove an aspectual or scope distinction that changes the claim.

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

**Content basis:** the supplied `ru.md` proficiency guide in `languages.zip`. Its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks are the basis for this document. The original attachment is not required to use this self-contained authoring guide.

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

**Source-file SHA-256:** `1edc0d587492aa18f69b420469188ac05ecfa22e0066718795d216368a6beb8a`

