# Python continuous dialogue

```python
import openai
import time

# Print the OpenAI version
print(openai.__version__)

client = openai.OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key="sk-xxx"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1
    )

    assistant_response = response.choices[0].message.content
    print(f"Assistant: {assistant_response}")

    messages.append({"role": "assistant", "content": assistant_response})
    time.sleep(1)
```
