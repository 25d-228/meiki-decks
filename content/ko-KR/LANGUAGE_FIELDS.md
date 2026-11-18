## Language-specific fields
Every card has exactly common and language_specific. Preserve all shared common fields unchanged: schema_version=2, id, locale, sentence, cloze, answer, accepted_answers, lemma, meaning, part_of_speech; optional nonempty register and note. Answer equals cloze; accepted_answers normally []. No third region or uncounted front context.

| Field in language_specific | Type | Scope, applicability and notation |
|---|---|---|
| target_unit | string | Required: word, attached morpheme, phrase, or fixed utterance. Describes the entire cloze. |
| morphology | string | Required for attached morphemes, irregular targets, contractions and multiword grammatical targets; English explanation with Hangul segmentation identifying exact surface form, dictionary pattern and attachment boundary. No placeholder in the answer itself. |
| pronunciation | string | Required for sound-target cards and wherever a nontransparent reading matters. Begin `Target:` or `Sentence:` to declare scope, quote the exact written form and its standard Hangul pronunciation in square brackets, then concise English explanation. Do not respell the written answer. Omit when unnecessary. |
| prosody | string | Required for rhythm, intonation, timing or emphasis targets. Begin `Sentence:` or `Target:` and describe grouping/intonation in English; no invented lexical stress. |
| speech_level | string | Sentence scope. Required for spoken utterances: informal polite, formal polite, casual, or mixed quotation (explain speakers in social_context). For written prose use plain written when register is a learning point. |
| social_context | string | Sentence scope. Required when honorification, hierarchy, intimacy, indirectness or a marked register matters; concise English explanation of participants already recoverable from the Korean. Never supply missing front context here. |
| lexical_frame | string | Target scope. Required when particles, complements or collocation distinguish the taught sense. English explanation with the actual Hangul frame, not another dictionary entry. |
| root | string | Target/lemma scope. Required for claimed Sino-Korean root instruction. Identify the actual syllable and Hanja root with English meaning; distinguish same-sounding roots. No speculative etymology. |
| script_note | string | Target scope. Required for block construction, symbol distinction, stroke order or keyboard targets. Explain relevant jamo/block position or standard two-set keyboard sequence in English. No romanization; Latin key names are typing instructions only. |
| recognition_only | boolean | Include true only for explicitly attributed regional, generational or marked historical/literary material not offered as the general productive standard. Explain source/register in common.note or social_context. Otherwise omit. |

All optional fields are omitted when unnecessary; never null or empty. Descriptive strings use English, with Hangul, Hanja and key names only when needed. These are learner supports, never process records. A short nontransparent pronunciation claim must concern the actual inflected form. Do not require all support fields on every card.

Filled illustrative example (format only; do not copy into production):
```json
{"common":{"schema_version":2,"id":"ko-01-0001","locale":"ko-KR","sentence":"선생님, 질문이 있어요.","cloze":"질문","answer":"질문","accepted_answers":[],"lemma":"질문","meaning":"a question","part_of_speech":"noun"},"language_specific":{"target_unit":"word","speech_level":"informal polite","social_context":"A learner addresses a teacher politely; the subject is a question, not the teacher.","lexical_frame":"질문이 있다: have a question."}}
```
