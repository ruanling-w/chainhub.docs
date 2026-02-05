# Python Basics Discussion

[You can interact with the API via HTTP requests in any language, our official Python bindings, our official Node.js library, or community-maintained libraries](https://platform.openai.com/docs/libraries/community-libraries).

To install the official Python bindings, run the following command:

```bash
pip install openai
```

```python
key='sk-xxxx'


from openai import OpenAI

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": "Hello?"},

  ],
  timeout=100,

)
print(response)
```
