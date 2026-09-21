# Mexican Spanish complete bundle v0.1.0

- Archive: `meiki-es-mx-complete-v0.1.0.meiki`
- Version: `0.1.0`
- Locale: `es-MX`
- Production model: educated contemporary central Mexican Spanish
- Total cards: 8,610
- Audio/media objects: 8,610
- Audio byte total: 892,087,056
- Archive byte size: 880,376,978
- SHA-256: `4535a20d9feda296daaa116bdb930842d31735759374e6724bcbeceb785c8ddc`
- Collection checksum:
  `sha256:132bdeee3e8b3f7cdb60f012ce7d97f1b41c724d5caf5540021659d461da1e18`

| Stage | Cards |
| --- | ---: |
| Mexican Spanish 01 — A1 foundation | 800 |
| Mexican Spanish 02 — A2 elementary | 1,000 |
| Mexican Spanish 03 — B1 intermediate | 1,400 |
| Mexican Spanish 04 — B2 upper-intermediate | 2,000 |
| Mexican Spanish 05 — C1 advanced | 2,262 |
| Mexican Spanish 06 — C2 and advanced-use bridge | 1,148 |

The format-4 full-collection archive was independently reopened and verified
for its exact six-stage order and names, per-stage counts, accepted text and
metadata, stable identities and relationships, initial scheduler defaults,
8,610 unseen schedules, and zero review events. All 8,612 ZIP entries passed
inventory and CRC checks: the manifest, collection, and 8,610 distinct media
objects. Canonical paths, byte sizes, local/embedded media SHA-256 values, and
the collection checksum passed verification. Compared with the accepted
development collection, only the six deck display names changed.

All 8,610 MP3 files reuse the accepted final denoised audio byte-for-byte.
No speech model, denoiser, re-encoding, normalization, or trimming was run
for this packaging. The recorded pipeline used `openbmb/VoxCPM2` Ultimate
Cloning with the fixed synthetic female Mexican voice, followed by
`MossFormer2_SE_48K` and MP3 encoding.

Retained reference and pipeline provenance:

- Reference WAV SHA-256:
  `5c2f70a0c0a825e46e8c882e0e3288ec1c24571912d61fa8eb462e84749a9748`
- Reference transcript SHA-256:
  `427b67b309dc10b3c1e3bacae9ada07fe10963262d18e7a9040f5aece977d8b5`
- VoxCPM2 offline snapshot:
  `32279effe8c19989596f05d353d1447f51d9e915`
- VoxCPM2 flags: `load_denoiser=false`; `optimize=false`
- MossFormer2 ClearerVoice-Studio code commit:
  `6b3774dc79c46ae8bed2a4fa5f706f0ac8c75c61`
- MossFormer2 model revision:
  `eff8c97925c8bec812af707814b3e5d777fd4503`
- MossFormer2 checkpoint SHA-256:
  `03692b9f773bbd6bb43b9c5a41f96b1e28affd66e13796b7bec66ad3d8b227c6`
- Encoding: `libmp3lame -q:a 2`; final 48 kHz mono MP3

This is the complete Mexican Spanish initial-installation archive, not an
additive update package or a published release. Generated MP3 and `.meiki`
binaries remain local, ignored, and uncommitted.

The fixed-voice audio-cloze bundle supports bounded language practice, not
C2 certification, exhaustive mastery, multi-accent listening assessment, or
proof that every study-guide objective has been fulfilled. The guide-to-source
review and historical evidence limitations remain as recorded in PR #126:
packaging is not a fresh full content audit and does not verify missing logs
or the two unavailable shell-exit results. Human listening acceptance was
sample-based, not an audition of every file; no repeat listening is required.
