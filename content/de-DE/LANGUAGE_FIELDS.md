## Language-specific fields
| Field | Type / scope | Required when / omission |
|---|---|---|
| noun | object: article, plural; optional genitive (all strings); lemma scope | For a hidden noun/nominalized lexical head: article is der/die/das; der/die is also allowed for gender-variable nominalized adjectives/participles, and die can denote an explicitly plural head; plural gives ordinary full plural or explicit no-plural label; add unpredictable genitive. Include useful case/collocation in grammar. Omit otherwise. |
| verb | object: present_3sg, preterite_3sg, participle, auxiliary (strings), separable (boolean); lemma/sense scope | For a hidden lexical verb or its separable component: give exact conventional forms, haben/sein or justified alternatives, and separation for actual sense. Common lemma holds full infinitive. Modals/auxiliaries use standalone participle with note when replacement infinitive is relevant. Omit otherwise. |
| grammar | string; target-in-sentence scope | Required for case/government, inflection, bracket/clauses, phrase/construction objectives; state exact target form/function and relevant governor. Omit if no useful grammatical support. |
| pronunciation | string; explicitly target or sentence scope | Required for sound/stress/prosody/reduction objectives and ambiguous prefix/compound senses. Use IPA in square brackets for exact hidden form or clearly declared lemma/sentence, explain length/quality/endings/stress/consonants/boundaries as relevant. Ordinary orthography stays in common. Omit unnecessary/unverified claims. |
| usage | string; target/context scope | Required for social-force/particle/register or regional pragmatic objectives; explain relationship, meaning here, or written/spoken use concisely. Omit ordinary unproblematic use. |
| recognition | string; target/context scope | Required for recognition-only objectives, explicitly stating region (Austria, Switzerland, northern/central/southern Germany or reported-speech recognition), contrast and de-DE production equivalent where needed. Omit productive neutral de-DE cases. |

No other language_specific keys. Explanations use English; forms are German and phonetic support is IPA. Empty language_specific is allowed only when none of these applies. A recognition card remains a de-DE sentence: explicitly identify the regional item as quoted/referred language rather than mixing production standards. Not every repeated answer is redundant: a distinct sense, complement, inflection or social function may justify it.

Filled format example only (do not copy its sentence into production):
```json
{
  "common": {
    "schema_version": 2,
    "id": "de-01-0001",
    "locale": "de-DE",
    "sentence": "Der Nachbar repariert heute unseren Zaun.",
    "cloze": "Nachbar",
    "answer": "Nachbar",
    "accepted_answers": [],
    "lemma": "Nachbar",
    "meaning": "male neighbor",
    "part_of_speech": "noun"
  },
  "language_specific": {
    "noun": {
      "article": "der",
      "plural": "Nachbarn",
      "genitive": "Nachbarn"
    },
    "grammar": "Nominative singular subject; weak noun: den/dem/des Nachbarn. Useful collocation: dem Nachbarn helfen."
  }
}
```
