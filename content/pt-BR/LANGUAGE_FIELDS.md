## Language-specific fields
Each record has exactly `common` and `language_specific`. Preserve all required common properties from workflow §5: `schema_version: 2`, `id`, `locale: "pt-BR"`, `sentence`, `cloze`, identical `answer`, `accepted_answers` (normally `[]`), `lemma`, `meaning`, `part_of_speech`. Optional nonempty `register` and `note`; no other common fields. English explanatory prose, Portuguese sentence/target/lemma, NFC ordinary spelling. Accepted alternatives require a concrete orthographic/grammatical justification, retain the assigned sense/register, and obey cloze caps; do not enumerate plausible synonyms.

| language_specific key | Type | Scope, meaning and applicability |
|---|---|---|
| variety | nonempty string | Required. Variety of the hidden use: `pt-BR` for production; for recognition use the actual national/region label, e.g. `pt-PT`, `pt-AO`, `pt-MZ`, `pt-CV`, `pt-GW`, `pt-ST`, `pt-TL`, or an explicit diaspora/regional label. No universal hybrid variety. |
| mode | string | Required; exactly `production` or `recognition`. Describes the hidden target's learning role. |
| pronunciation | nonempty string | Required when sound, stress, accent, reduction, linking or prosody is the learning point; otherwise omit unless essential. Explicitly begins `Target:` or `Sentence:` to declare scope. Use IPA between slashes for phonemes and brackets for a stated regional realization, with stress as needed; concise English explains the actual target/form/region. Do not claim an exhaustive transcription from a partial aid. |
| grammar | nonempty string | Required for targeted inflection, gender/number, verb government, contraction, clitic, mood, infinitive or syntax where the common label/lemma does not supply the distinction. Begins `Target:`; describes the actual hidden form/use, its agreement/subject/complement and contrast when relevant. Omit for straightforward lexical targets needing no added grammatical support. |
| usage | nonempty string | Required for recognition or socially/register-sensitive targets. Begins `Target:` or `Sentence:`; explains region, relationship, audience, register, pragmatic force or contextual lexical sense when needed. Omit redundant ordinary-use notes. |

These five keys are the complete local field definition. Omit unused optional keys; no nulls, empty strings, process fields, extra front context, audio, or arbitrary dictionary data. Sound notes describe the chosen São Paulo model, including final unstressed e/o commonly [i]/[u], t/d before [i] commonly [tʃ]/[dʒ], final l commonly [w]; do not universalize across Brazil. Variable r/s realizations are described with a specific region/context and checked before publication.

Filled format example only; do not copy this sentence into production:
```json
{
  "common": {
    "schema_version": 2,
    "id": "pt-00-0001",
    "locale": "pt-BR",
    "sentence": "Meu avô mora perto daqui.",
    "cloze": "avô",
    "answer": "avô",
    "accepted_answers": [],
    "lemma": "avô",
    "meaning": "grandfather",
    "part_of_speech": "noun"
  },
  "language_specific": {
    "variety": "pt-BR",
    "mode": "production",
    "pronunciation": "Target: avô has final stress and closed /o/; avó has open /ɔ/.",
    "grammar": "Target: masculine singular noun."
  }
}
```
