## Language-specific fields
Every record has exactly `common` and `language_specific`. Preserve the workflow's required common fields: integer `schema_version: 2`; nonempty strings `id`, `locale`, `sentence`, `cloze`, `answer`, `lemma`, `meaning`, `part_of_speech`; array `accepted_answers`, normally empty. Optional nonempty `register` and `note`. Answer equals cloze. English meanings and explanations throughout; advanced French paraphrase is represented inside the French sentence, never by changing the support language.

| Specific key | Type | Scope and notation | Required / omitted |
|---|---|---|---|
| `noun_support` | array of nonempty strings | Each distinct common-noun lemma in the sentence, including visible nouns, with a useful singular article and gender, e.g. `la porte (feminine)`, `l'arbre (masculine)`; use plural article plus gender for plural-only senses. Qualify gender-changing senses. Direct-address titles are labeled for gender without an unnatural article, e.g. `madame (feminine title; no article in direct address)`. For normally articleless temporal nouns such as `minuit`, give gender and the normal no-article use instead of forcing an unnatural citation article. | Required whenever a common noun occurs; omit for sentences without common nouns. Proper names and substantivized pronouns need no artificial entry. |
| `verb_frame` | nonempty string | English explanation quoting the French lemma/construction and its actual complement frame, e.g. `dépendre de quelque chose; de introduces the condition.` Describe the target construction, not unrelated visible verbs. | Required for verb/preposition, pronominal, object-order or mood-selection targets whose use needs that support; omit when no useful frame is needed. |
| `pronunciation` | nonempty string | Begin `Target:` or `Sentence:` to declare scope. Broad IPA between slashes where useful; English explanation of exact sound, silent segment, liaison, enchaînement, reduction, group boundary or intonation. `|` marks a phrase boundary only in the aid. No respelling of ordinary answers. | Required for planned sound/prosody targets and when silent/linked/reduced forms need help. Otherwise omit. Do not infer liaison from spelling alone. |
| `usage` | nonempty string | English contextual usage/contrast or audience information, with quoted French forms if needed; explicitly mark recognition-only regional/reduced features. No new front-side context. | Required when pragmatic force, a regional recognition contrast, false friend or corrective interpretation needs support beyond `common.meaning/register/note`; otherwise omit. |

No other specific keys. Empty `{}` is allowed only when none applies. Support describes the actual hidden form or explicitly declared sentence scope. It must never contain a missing antecedent, timeline, source or social cue needed on the front.

Filled illustrative format example, not a production card:
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
  "language_specific": {
    "noun_support": ["le sac (masculine)", "la porte (feminine)"]
  }
}
```
