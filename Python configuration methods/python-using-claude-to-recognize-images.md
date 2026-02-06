# Using Claude in Python to Recognize Images

## Recognizing Linked Images

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key="sk-xxxx"
)

response = client.chat.completions.create(
  model="claude-3-5-sonnet-20240620",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
```

## Identify local images

```python
import base64
import time
from openai import OpenAI
import openai

key = 'sk-xxxx'

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_path = "Image.jpg"

base64_image = encode_image(image_path)

while True:
    response = client.chat.completions.create(
        model="claude-3-5-sonnet-20240620",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is in this picture? Please describe it in detail."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=1
    )
    print(response)
    print(response.choices[0].message.content)
    time.sleep(1)
```
