# Using Python to convert speech to text

# Speech-to-Text API Guide

## Overview

The Audio API provides two main endpoints:

* 📝 **transcriptions**: Audio to text
* 🔄 **translations**: Audio to English translation

### Supported Formats

* 📁 File Size: Maximum 25 MB
* 🎵 Supported Formats: mp3, mp4, mpeg, mpg, m4a, wav, webm

## How to use

### 1. Transcription

Convert audio to original language text

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

# Basic transcription
audio_file = open("/path/to/file/audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
print(transcription.text)

# Specify output format
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)
```

### 2. Translation

Convert audio in any language to English text.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

audio_file = open("/path/to/file/german.mp3", "rb")
translation = client.audio.translations.create(
  model="whisper-1",
  file=audio_file
)
print(translation.text)
```

### 3. Timestamp function

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

print(transcript.words)
```

### 4. Processing Large Files

Use PyDub to split files larger than 25MB:

```python
from pydub import AudioSegment

song = AudioSegment.from_mp3("good_morning.mp3")

# 分割为10分钟片段
ten_minutes = 10 * 60 * 1000
first_10_minutes = song[:ten_minutes]
first_10_minutes.export("good_morning_10.mp3", format="mp3")
```

## Optimization Suggestions

### Tips for Using Prompts

1. 🔍 Used to correct specific word recognition
2. 📜 Maintain contextual coherence
3. ✍️ Control punctuation output
4. 🗣️ Retain filler words
5. 📝 Control output text style (e.g., Simplified/Traditional Chinese)

### Supported Languages

Supports 98 languages, including:

* Major Asian languages: Chinese, Japanese, Korean, etc.
* European languages: English, French, German, etc.
* Other regional languages: Arabic, Hindi, etc.

> **Note**: Only languages ​​with a Word Error Rate (WER) below 50% are listed. Other languages ​​are supported, but the quality may be lower.
