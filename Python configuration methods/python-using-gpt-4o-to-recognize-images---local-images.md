# Using gpt-4o in Python to recognize local images

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key="sk-xxxx"
)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image= encode_image(".\1.png")

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
```
