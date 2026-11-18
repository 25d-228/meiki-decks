## Language-specific fields
Every card retains exactly the shared common and language_specific objects. The ten required common fields, optional register/note, schema_version 2, exact locale, one contiguous cloze occurring once, answer equality, NFC, and ordered zh-NN-NNNN IDs remain unchanged. Meanings and explanations are English; Chinese forms and readings retain their appropriate notation.

| Field | Type | Scope / learner label | Applicability and convention |
|---|---|---|---|
| target_pinyin | nonempty string | Target / Pinyin | Required on every card; exact cloze reading, tone diacritics, lexical citation tones for third tones and productive grammatical 一/不; established dictionary-neutral syllables in lexicalized words remain unmarked; normal word-based spacing, apostrophe where required, ü retained except regular j/q/x/y spelling. No tone numbers or English sound approximations. |
| pronunciation_note | nonempty English string | Explicit target or sentence / Connected speech | Required when the objective depends on a sound contrast, sandhi, partial third tone, neutral/weak syllable, prominence, phrasing, or a context-sensitive reading. State its scope and actual realization; keep lexical Pinyin distinct from surface tone changes. Omit when unnecessary. |
| usage_note | nonempty English string | Target in sentence / Use | Required for contrastive grammar, nontransparent compounds, idioms, and social/register/recognition distinctions needing explanation beyond common.meaning. State the actual sense, construction, or social force. Omit when unnecessary; no extra front context. |
| idiom_support | object of five nonempty English strings: literal, contemporary, collocations, register, avoid | Complete targeted idiom / Expression | Required for targeted chengyu and culturally opaque conventional four-character expressions, including literal versus contemporary sense, Chinese collocation examples inside English prose, register and inappropriate/pretentious contexts. The card sentence is its original natural example. Do not invent historical origins; verified historical associations may be stated in usage_note only when needed. Omit for ordinary transparent four-character sequences. |
| recognition | object with nonempty English strings variety, explanation and a nonempty Chinese string form | Target / Recognition | Only for explicitly mapped passive Traditional or regional recognition. Attribute form/variety and explain its correspondence or pragmatic distinction; sentence gives the recognition cue, canonical answer and lemma stay Simplified standard Chinese. It is not an alternative active-script series. |

No other specific keys. language_specific is never empty because target_pinyin is always required. Do not duplicate meaning, add full sentence translations, store process fields, or put essential visible context in notes. Optional objects are omitted, not null or empty.

Filled format example (illustrative only, not a production slot):
```json
{"common":{"schema_version":2,"id":"zh-03-0001","locale":"zh-Hans-CN","sentence":"我把钥匙放在桌上了。","cloze":"钥匙","answer":"钥匙","accepted_answers":[],"lemma":"钥匙","meaning":"key; keys","part_of_speech":"noun"},"language_specific":{"target_pinyin":"yàoshi","pronunciation_note":"Target: 匙 is a neutral-tone syllable in 钥匙."}}
```
