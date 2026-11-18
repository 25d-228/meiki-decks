## Language-specific fields
Keep the shared `common` fields exactly as defined in workflow Section 5: required `schema_version: 2`, `id`, `locale`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`; optional nonempty `register`, `note`. Each record has exactly `common` and `language_specific`. Do not add context or process fields.

| Specific key | Type / scope | Required use and notation |
|---|---|---|
| `reading` | string; actual hidden span | Required on every card. Cyrillic target with U+0301 acute on stressed vowels of polysyllabic lexical words, including inflected forms; ё itself indicates stress, without an added acute. Monosyllables normally remain unmarked. Preserve spelling, spaces and punctuation when removing acute marks; this is stress support, not IPA or transliteration. |
| `morphology` | string; actual target, English explanation with Russian forms | Required for inflected targets and grammatical constructions, including nouns/adjectives in sentence-use nominatives whose spelling matches the dictionary form. Identify relevant case/number/gender/person/tense/mood, animacy, agreement, reflexivity or participial relation; explain only distinctions useful here. Invariant lexical targets may omit it. |
| `verb` | string; target lemma and selected use | Required when the target is a verb or verbal construction. State aspect, a relevant contextual partner or explicitly no simple partner, target conjugation/stress, object/case frame and the relevant temporal/imperative behavior. For motion, also state directionality, means and prefix sense. Do not force a symmetric pair or invent one for a lexicalized sense. |
| `pronunciation` | string; explicitly target or sentence scope | Required for sound, script, stress-pattern, reduction, assimilation, phrasing or intonation objectives. Start `Target:` or `Sentence:`; state the exact contrast, stressed/reduced vowel, hard/soft consonant, cluster or contour. IPA may be used only when confidently accurate; concise English with quoted Cyrillic is sufficient. Script/keyboard/handwriting recognition belongs here with its limits. Omit unrelated general pronunciation advice. |
| `usage` | string; actual target in the sentence | Required for governed lexical frames beyond transparent morphology, lexicalized derivation, register/social choice, marked focus, idiom, regional/generational/historical recognition or professional scope. Name the governor, relationship, scope or discourse cue. Explicitly label recognition when productive imitation is not intended. Omit when no extra distinction is needed. |

No additional keys; omit inapplicable optional keys instead of empty/null values. `reading` makes the region nonempty. English learner explanations; Russian forms in Cyrillic. Normal sentence, cloze, answer and lemma never acquire pedagogical acute marks. Distinguish stress movement of a form from its lemma. Common `register` labels a register; `usage` explains its contextual choice without supplying missing front context.

Filled format example (illustrative, not a production card):
```json
{
  "common": {
    "schema_version": 2,
    "id": "ru-01-0001",
    "locale": "ru-RU",
    "sentence": "После работы я читаю газету.",
    "cloze": "газету",
    "answer": "газету",
    "accepted_answers": [],
    "lemma": "газета",
    "meaning": "a newspaper",
    "part_of_speech": "noun"
  },
  "language_specific": {
    "reading": "газе́ту",
    "morphology": "Accusative singular feminine; direct object of читаю."
  }
}
```
