# Python llama\_index configuration

```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo",
    api_key="sk-xxxxx",
    api_base="https://api.chainhub.tech/v1")
ret=llm.complete("Paul Graham is ")
print(ret)



```
