## Language-specific fields
Each ordered card has exactly `common` and `language_specific`. Preserve workflow §5 common fields without additions: required `schema_version: 2`, `id`, `locale`, `sentence`, `cloze`, `answer`, `accepted_answers`, `lemma`, `meaning`, `part_of_speech`; optional nonempty English `register` and `note`. Answer equals the single contiguous cloze; alternatives normally `[]`. NFC, readable UTF-8 JSON, two-space indentation. IDs `ja-NN-0001` onward. No rōmaji answer, front-side context field, process fields or uncounted preamble.

| Field | Type / scope | Required / omitted | Meaning and notation |
|---|---|---|---|
| `target_reading` | string; exact inflected hidden span | Required on every card | Hiragana reading of the actual cloze; retain `ー` when transliterating katakana long vowels. Read particle は as わ, へ as え, を as お when the particle is the target. This is reading support, not an alternative typed answer or phonetic transcription. No spaces or accent numbers. |
| `learning_role` | string; target use | Required on every card | Exactly `production` for ordinary usable standard Japanese, or `recognition` for causative-passive introductory recognition, attributed dialect, role speech, historical/specialist recognition and other restricted uses. Production here labels the teaching role, not certified learner performance. |
| `pronunciation` | nonempty English string; target unless explicitly introduced with `Sentence:` | Required when sound/prosody is a primary learning point; otherwise only if useful | Identify mora, length, gemination, moraic ん, context-dependent high-vowel devoicing, or verified Tokyo phrase/accent/focus information. Quote kana as needed. Distinguish phonemic spelling from phonetic realization; do not claim categorical devoicing or infer compound accents. No unsupported pitch values. |
| `usage` | nonempty English string; exact target in this sentence | Required for viewpoint-sensitive, register-sensitive, recognition-only or potentially misleading targets; otherwise omit | Concise actor/beneficiary, selectional frame, social function, orthographic/input, or sense distinction. Recognition entries name the attributed context and limits; this does not replace required visible situational cues. |

No other specific keys. Since the two first fields are always required, the specific region is never empty in this local design. Common note may explain grammar; avoid duplicating the specific support.

Filled illustrative record (format only, not a production card):
```json
{
  "common": {
    "schema_version": 2,
    "id": "ja-01-0001",
    "locale": "ja-JP",
    "sentence": "駅の前で友達を待っています。",
    "cloze": "待っています",
    "answer": "待っています",
    "accepted_answers": [],
    "lemma": "待つ",
    "meaning": "am waiting",
    "part_of_speech": "verb",
    "note": "The ている form presents the waiting as ongoing here."
  },
  "language_specific": {
    "target_reading": "まっています",
    "learning_role": "production",
    "usage": "The を-marked friend is the person being waited for."
  }
}
```
