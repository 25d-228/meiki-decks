## Language-specific fields
Each card has exactly `common` and `language_specific`. Preserve the shared ten required common fields: integer `schema_version: 2`; nonempty strings `id`, `locale`, `sentence`, `cloze`, `answer`, `lemma`, `meaning`, `part_of_speech`; array `accepted_answers` (normally empty). Only nonempty `register` and `note` are optional common keys. English meanings and explanations; ordinary Spanish spelling in sentence, target and lemma. No front-side context outside the complete sentence.

| Specific field | Type and scope | Applicability and notation |
|---|---|---|
| `morphology` | Nonempty English string describing the actual target form | Required for inflected verbs, nouns, adjectives, pronouns and grammatical constructions. Give relevant gender/number, person/tense/mood, clitic function or construction role. Do not list unrelated paradigm forms. Omit for an uninflected lexical item needing no morphological distinction. |
| `pronunciation` | Nonempty string, explicitly prefixed `Target:` or `Sentence:` | Required for all foundation sound–spelling objectives and any later objective involving stress, linking, intonation, emphasis or regional realization. Use syllables separated by hyphens and capitalized stressed syllable when helpful, clearly as an aid; IPA only if accurate and necessary. Explain stable vowels, articulation, phrasing or intonation in English. Ordinary answer spelling stays separate. Omit when it adds no useful information. |
| `usage` | Nonempty English string about the target's frame or contextual use | Required when complement government, false-friend meaning, idiomatic interpretation, pragmatic force or a domain/social convention needs explanation. For every stage 07 card state `Domain: …; relationship: …;` and the specific convention or sense. Relationships and pragmatic cues must already be recoverable in the Spanish sentence; this field cannot invent them. Omit redundant glosses. |
| `variety` | Nonempty English string labeling recognition scope | Required for attributed non-Mexican or nonstandard recognition, e.g. `Recognition: Spain; not the default Mexican production form.` For shared wording do not claim exclusive nationality. Ordinary Mexican production omits this key. |

`language_specific` may be `{}` only where no support above applies. Do not invent other keys or duplicate process evidence. Pronunciation support is textual and is not a claim about actual listening or speaking ability.

For a freely negated verb, use the lexical infinitive as `common.lemma` without `no`. Retain negation in a lemma only for a lexicalized idiom, such as `no acabar de` in its distinct incomplete-achievement sense. When negation belongs to the hidden span, describe it in the contextual meaning and support. A focused inflection may leave negation visible as essential context; do not require every negated verb target to include no.

Filled illustrative example (format only; do not copy its sentence into production):
```json
{
  "common": {
    "schema_version": 2,
    "id": "es-01-0001",
    "locale": "es-MX",
    "sentence": "Mi perro duerme junto a la puerta.",
    "cloze": "perro",
    "answer": "perro",
    "accepted_answers": [],
    "lemma": "perro",
    "meaning": "dog",
    "part_of_speech": "noun"
  },
  "language_specific": {
    "morphology": "Masculine singular noun; masculine possessive phrase.",
    "pronunciation": "Target: PE-rro; intervocalic rr is trilled; both vowels remain full."
  }
}
```
