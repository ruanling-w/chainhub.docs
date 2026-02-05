# Using Python to convert text to speech

# Text-to-Speech (TTS) API Guide

## Overview

The audio API provides a `speech` endpoint, enabling the following functionalities based on a TTS model:

* 📝 Blog post reading
* 🌍 Multilingual audio generation
* 🎵 Real-time audio streaming output

> **Important Note**: Users must be informed that what they hear is AI-generated speech, not a human voice.

## Basic Usage

### Basic Examples

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
```

## Features

### Audio Quality Options

* **TTS-1**: Low latency, suitable for real-time applications
* **TTS-1-HD**: Higher quality, potentially with less static content

### Available Sounds

* Alloy
* Echo
* Fable
* Nova
* Shimmer
* Onyx

### Supported Output Formats

| Format | Features                    | Suitable Scenarios                  |
| ------ | --------------------------- | ----------------------------------- |
| MP3    | Default Format              | General Scenarios                   |
| Opus   | Low Latency                 | Network Streaming and Communication |
| AAC    | High-Efficiency Compression | Mobile Device Playback              |
| FLAC   | Lossless Compression        | Audio Archiving                     |
| WAV    | Uncompressed                | Low-Latency Applications            |
| PCM    | Raw Sampling                | 24kHz, 16-bit Signed                |

### Real-Time Audio Streaming

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")
```

## Supported Languages

Supports multiple languages, including:

* Asian languages: Chinese, Japanese, Korean, etc.
* European languages: English, French, German, etc.
* Other languages: Arabic, Hindi, etc.

> **Note:** The current audio is primarily optimized for English.

## Frequently Asked Questions

### Q: How do I control the emotion in the generated audio?

A: There is currently no direct control mechanism. Capitalization or grammar may affect the output, but the effect is uncertain.

### Q: Can I create custom voices?

A: Creating custom voices is not supported.

### Q: Ownership of the generated audio?

A: It belongs to the creator, but users must be informed that this is AI-generated audio.
