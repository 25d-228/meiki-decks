# meiki-decks

Japanese Foundation 1 contains 150 beginner Japanese audio-cloze cards and one
full-sentence MP3 for each card.

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

Generate missing audio files:

```bash
python meiki_decks.py generate-audio
```

Check the card data and generated files:

```bash
python meiki_decks.py check
```

While editing card content, the audio requirement can be skipped:

```bash
python meiki_decks.py check --allow-missing-audio
```

Build and verify the import archive:

```bash
python meiki_decks.py build
```

The completed outputs are:

```text
audio/ja-001.mp3 through audio/ja-150.mp3
dist/meiki-ja-jp-foundation-1-v0.1.0.meiki
dist/README.txt
```
