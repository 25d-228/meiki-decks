# meiki-decks

The Japanese series contains staged audio-cloze decks and one full-sentence
MP3 for every card.

## Requirements

- macOS on Apple silicon
- Python 3.9 or newer
- [FFmpeg](https://ffmpeg.org/)
- [MLX-Audio](https://github.com/Blaizzy/mlx-audio)
- the Qwen3-TTS model cached locally

Install the runtime and explicitly download the model:

```bash
brew install ffmpeg
uv tool install mlx-audio --prerelease=allow
uvx --from huggingface-hub hf download \
  mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit
```

The script runs the following command once per missing card, with the complete
sentence as `--text`:

```bash
HF_HUB_OFFLINE=1 mlx_audio.tts.generate \
  --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit \
  --text '<complete sentence>' \
  --voice Ono_Anna \
  --lang_code Japanese \
  --temperature 0.7 \
  --output_path '<temporary directory>' \
  --file_prefix '<card id>' \
  --audio_format mp3 \
  --join_audio
```

`HF_HUB_OFFLINE=1` prevents generation from silently downloading model
weights.

Commands default to `ja-JP-foundation-1`. Select another deck with `--deck`:

```bash
python meiki_decks.py generate-audio --deck ja-JP-foundation-2
```

Check the card data and generated files:

```bash
python meiki_decks.py check --deck ja-JP-foundation-2
```

While editing card content, the audio requirement can be skipped:

```bash
python meiki_decks.py check --deck ja-JP-foundation-2 --allow-missing-audio
```

Build and verify the import archive:

```bash
python meiki_decks.py build --deck ja-JP-foundation-2
```

Build and verify a combined initial-installation archive:

```bash
python meiki_decks.py build-bundle --bundle ja-JP-complete
python meiki_decks.py build-bundle --bundle all-current
```

Importing these combined archives uses full-collection replacement semantics:

> Importing this archive replaces the current Meiki collection. It is intended for initial installation, not for updating an existing studied collection.

The completed outputs are:

```text
audio/ja-001.mp3 through audio/ja-150.mp3
dist/meiki-ja-jp-foundation-1-v0.1.0.meiki
dist/README.txt

audio/ja-JP-foundation-2/ja-f2-001.mp3 through ja-f2-150.mp3
dist/meiki-ja-jp-foundation-2-v0.1.0.meiki
dist/README-ja-JP-foundation-2.txt

audio/ja-JP-elementary-1/ja-e1-001.mp3 through ja-e1-200.mp3
dist/meiki-ja-jp-elementary-1-v0.1.0.meiki
dist/README-ja-JP-elementary-1.txt

audio/ja-JP-intermediate-1/ja-i1-001.mp3 through ja-i1-250.mp3
dist/meiki-ja-jp-intermediate-1-v0.1.0.meiki
dist/README-ja-JP-intermediate-1.txt

audio/ja-JP-upper-intermediate-1/ja-u1-001.mp3 through ja-u1-250.mp3
dist/meiki-ja-jp-upper-intermediate-1-v0.1.0.meiki
dist/README-ja-JP-upper-intermediate-1.txt

audio/ja-JP-advanced-1/ja-a1-001.mp3 through ja-a1-300.mp3
dist/meiki-ja-jp-advanced-1-v0.1.0.meiki
dist/README-ja-JP-advanced-1.txt

audio/ko-KR-foundation-1/ko-f1-001.mp3 through ko-f1-150.mp3
dist/meiki-ko-kr-foundation-1-v0.1.0.meiki
dist/README-ko-KR-foundation-1.txt

audio/ko-KR-foundation-2/ko-f2-001.mp3 through ko-f2-200.mp3
dist/meiki-ko-kr-foundation-2-v0.1.0.meiki
dist/README-ko-KR-foundation-2.txt

audio/ko-KR-intermediate-1/ko-i1-001.mp3 through ko-i1-250.mp3
dist/meiki-ko-kr-intermediate-1-v0.1.0.meiki
dist/README-ko-KR-intermediate-1.txt

audio/ko-KR-upper-intermediate-1/ko-u1-001.mp3 through ko-u1-250.mp3
dist/meiki-ko-kr-upper-intermediate-1-v0.1.0.meiki
dist/README-ko-KR-upper-intermediate-1.txt

audio/ko-KR-advanced-1/ko-a1-001.mp3 through ko-a1-300.mp3
dist/meiki-ko-kr-advanced-1-v0.1.0.meiki
dist/README-ko-KR-advanced-1.txt

audio/zh-Hans-CN-foundation-1/zh-f1-001.mp3 through zh-f1-150.mp3
dist/meiki-zh-hans-cn-foundation-1-v0.1.0.meiki
dist/README-zh-Hans-CN-foundation-1.txt

audio/fr-FR-foundation-1/fr-f1-001.mp3 through fr-f1-150.mp3
dist/meiki-fr-fr-foundation-1-v0.1.0.meiki
dist/README-fr-FR-foundation-1.txt

audio/es-MX-foundation-1/es-f1-001.mp3 through es-f1-150.mp3
dist/meiki-es-mx-foundation-1-v0.1.0.meiki
dist/README-es-MX-foundation-1.txt

dist/meiki-ja-jp-complete-v0.1.0.meiki
dist/README-ja-JP-complete.txt

dist/meiki-all-current-v0.1.0.meiki
dist/README-all-current.txt
```
