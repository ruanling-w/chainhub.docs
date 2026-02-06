# Chat completion target

| Parameters         | Type    | Description                                                                             |
| ------------------ | ------- | --------------------------------------------------------------------------------------- |
| id                 | string  | A unique identifier for chat completion                                                 |
| choices            | array   | A list of chat completion options. Multiple options are possible if n is greater than 1 |
| created            | integer | A Unix timestamp (in seconds) at which the chat completion was created                  |
| model              | string  | The model used for chat completion                                                      |
| system_fingerprint | string  | This fingerprint represents the backend configuration on which the model is running     |
| object             | string  | Object type, always chat.completion                                                     |
| usage              | object  | Usage statistics for completion requests                                                |
| completion_tokens  | integer | The number of tokens generated in the completion                                        |
| prompt_tokens      | integer | The number of tokens in the prompt                                                      |
| total_tokens       | integer | The total number of tokens used in the request (prompt + completion)                    |

```JSON
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0613",
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```
