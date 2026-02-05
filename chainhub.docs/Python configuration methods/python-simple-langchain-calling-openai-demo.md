# Simple Python LangChain calling OpenAI demo

## Recognizing Linked Image Formats

```js
pip install langchain_openai
pip install langchain
```

```python
#New version of langchina
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_base="https://api.chainhub.tech/v1",
    openai_api_key="sk-xxxxx"
)

res = llm.invoke("hello")
print(res.content)


#Older versions of langchina set the relay address by configuring environment variables.
$env:OPENAI_BASE_URL="https://api.chainhub.tech/v1"
$env:OPENAI_API_KEY="sk-xxxxx"

```
