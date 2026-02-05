# Python OpenAI official libraries (using AutoGPT, langchain, etc.)

# API integration example code

## Method 1: Directly configure OpenAI

```python
import openai

# Set API base address and key
openai.api_base = "https://api.chainhub.tech/v1"
openai.api_key = "sk-xxxxxxxxx"
```

## Method Two: Environment Variable Configuration

> If Method One doesn't work, you can try this method

The following environment variables need to be set:

```bash
OPENAI_API_BASE=https://api.chainhub.tech/v1
OPENAI_API_KEY=sk-xxxxx
```

> **Note:** If modifying environment variables does not work, please restart your system.

## Method 3: Using the OpenAI Client

```python
from openai import OpenAI

# Initialize client
client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key='Your API KEY',
    timeout=120
)

# Chat creation complete
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response)

#Response format

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
```
