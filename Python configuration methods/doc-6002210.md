# Python request request streaming demo

```python
import requests
import json

url = "https://api.chainhub.tech/v1/chat/completions"

payload = json.dumps({
   "model": "o1-preview",
   "messages": [
      {
         "role": "user",
         "content": "Write a short love letter"
      }
   ],
   "stream": True
})
headers = {
   'Accept': 'text/event-stream',
   'Authorization': 'Bearer your key',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, stream=True)

for line in response.iter_lines():
    if line:
        # Skip blank lines
        line = line.decode('utf-8')
        if line.startswith('data: '):
            if line == 'data: [DONE]':
                break
            # Parse JSON data
            data = json.loads(line[6:]) # Remove the "data: " prefix
            if 'choices' in data and len(data['choices']) > 0:
                delta = data['choices'][0].get('delta', {})
                if 'content' in delta:
                    print(delta['content'], end='', flush=True)
```
