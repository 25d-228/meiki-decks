## Language-specific fields
Exactly `common` and `language_specific` per card. Required `common` fields: integer `schema_version: 2`; nonempty strings `id`, `locale`, `sentence`, `cloze`, `answer`, `lemma`, `meaning`, `part_of_speech`; array of strings `accepted_answers`, normally `[]`. Optional nonempty strings `register`, `note`. No other common fields. `answer == cloze`; the contiguous cloze occurs once in the restored sentence. Meanings are easier contextual English paraphrases; labels describe the whole hidden unit. Lemmas use dictionary forms or complete fixed expressions, with morphological targets explained. No unexplained synonym lists in accepted answers.

All language-specific keys below are optional nonempty strings, omitted when inapplicable; no other keys. `{}` is appropriate only when none is needed. Support is answer-side and cannot introduce necessary front-side context.

| Field | Scope and notation | Required use |
|---|---|---|
| `pronunciation` | Actual hidden form, broad rhotic American IPA between slashes; lexical stress marked with IPA stress signs. A narrow bracketed realization may follow with its environment. | Sound/spelling, lexical stress, irregular spoken form, contractions, weak-form or ending targets; omit gratuitous transcription elsewhere. Describe the actual inflected form, not an unrelated lemma. Verify uncertain claims before production. |
| `usage` | Actual target use; concise English with ordinary quoted examples. | Noun targets: contextual count/noncount behavior, useful number information and a collocation. Complement/preposition targets: full governing frame. Multiword verbs: full expression, sense, transitivity/separability and pronoun placement. Irregular inflection or easily confused constructions: relevant form/contrast. Do not assign permanent articles to nouns. |
| `prosody` | Explicitly sentence-scoped English description of prominence, phrase boundary, linking or contextual reduction. | When stress, grouping, weak forms or connected speech is the learning point. Keep conventional written spelling in sentence and answer. Do not claim universal reductions or confuse quality with duration. |
| `social` | Actual sentence situation and target function: relationship, authority, familiarity, urgency and tone. | Where the target depends on a request/refusal/feedback/stance/register choice, irony, humor or a marked recognized variety. Context must already support the interpretation. Attribute recognition rather than declaring other varieties wrong. |

Filled format example, illustrative only (do not copy into production):
```json
{
  "common": {
    "schema_version": 2,
    "id": "en-US-01-0001",
    "locale": "en-US",
    "sentence": "Please put the wet boots by the door.",
    "cloze": "boots",
    "answer": "boots",
    "accepted_answers": [],
    "lemma": "boot",
    "meaning": "shoes that cover the ankles or more",
    "part_of_speech": "plural noun"
  },
  "language_specific": {
    "pronunciation": "/buts/",
    "usage": "Count noun: one boot, two boots; wear boots."
  }
}
```
