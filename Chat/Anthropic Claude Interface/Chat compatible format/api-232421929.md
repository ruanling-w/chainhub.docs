# Create Chat Vision (Streaming)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/chat/completions:
    post:
      summary: Create Chat Vision (Streaming)
      deprecated: false
      description: |
        Given a prompt, the model will return one or more predicted completions, and can also return the probability of alternative tokens at each position.

        Create completions for the provided prompt and parameters.

        Official documentation: https://docs.anthropic.com/en/docs/build-with-claude/vision
      tags:
        - Chat/Anthropic Claude API/Chat Compatible Format
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
          required: false
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                  description: |+
                    The ID of the model to use. For details on which models are compatible with the chat API, see the model endpoint compatibility table.

                messages:
                  type: array
                  items:
                    type: object
                    properties:
                      role:
                        type: string
                      content:
                        type: string
                    x-apifox-orders:
                      - role
                      - content
                  description: List of messages included in the conversation so far. Python code example.
                temperature:
                  type: integer
                  description: >-
                    What sampling temperature to use, between 0 and 2. Higher values (like 0.8) make the output more random, while lower values (like 0.2) make it more focused and deterministic. We generally recommend changing this or `top_p` but not both.
                top_p:
                  type: integer
                  description: >-
                    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend changing this or `temperature` but not both.
                "n":
                  type: integer
                  description: |-
                    Default is 1
                    How many chat completion choices to generate for each input message.
                stream:
                  type: boolean
                  description: >-
                    Default is false. If set, partial message deltas will be sent as in ChatGPT. Tokens will be sent as server-sent events with only data as they become available, and the stream will be terminated with a data: [DONE] message. Python code example.
                stop:
                  type: string
                  description: Default is null. Up to 4 sequences, the API will stop generating further tokens.
                max_tokens:
                  type: integer
                  description: |-
                    Default is inf
                    The maximum number of tokens to generate in the chat completion.

                    The total length of input tokens and generated tokens is limited by the model's context length. Python code example for counting tokens.
                presence_penalty:
                  type: number
                  description: >-
                    Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. [See more about frequency and presence penalties.](https://platform.openai.com/docs/api-reference/parameter-details)
                frequency_penalty:
                  type: number
                  description: >-
                    Default is 0. Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, reducing the model's likelihood to repeat the same line. See more about frequency and presence penalties.
                logit_bias:
                  type: "null"
                  description: >-
                    Modifies the likelihood of specified tokens appearing in the completion.


                    Accepts a JSON object that maps tokens (token IDs as specified by the tokenizer) to an associated bias value (-100 to 100). Mathematically, the bias is added to the model-generated logit before sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase the likelihood of selecting the associated token; values like -100 or 100 should result in disabling or exclusively selecting the associated token.
                user:
                  type: string
                  description: >-
                    A unique identifier representing your end user, which can help OpenAI monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
                response_format:
                  type: object
                  properties: {}
                  x-apifox-orders: []
                  description: >-
                    Object specifying the format the model must output. Setting { "type": "json_object" } enables JSON mode, which ensures the model-generated message is valid JSON. Important: When using JSON mode, you must also instruct the model to generate JSON via a system or user message. If not, the model may generate endless blank streams until the token limit is reached, causing increased latency and a "stuck" request. Also note, if finish_reason="length", the message content may be partially cut off, indicating generation exceeded max_tokens or the conversation exceeded the maximum context length. Show properties
                seen:
                  type: integer
                  description: >-
                    This feature is experimental. If specified, our system will make a best effort to sample deterministically so that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed; you should refer to the system_fingerprint response parameter to monitor backend changes.
                tools:
                  type: array
                  items:
                    type: string
                  description: List of tools the model can call. Currently, only functions as tools are supported. Use this to provide a list of functions for which the model can generate JSON input.
                tool_choice:
                  type: object
                  properties: {}
                  description: >-
                    Controls which function the model calls (if any). none means the model will not call a function and will generate a message. auto means the model can choose between generating a message and calling a function. Use {"type": "function", "function": {"name": "my_function"}} to force the model to call that function. If no functions exist, defaults to none. If functions exist, defaults to auto. Show possible types
                  x-apifox-orders: []
              required:
                - model
                - messages
                - tools
                - tool_choice
              x-apifox-orders:
                - model
                - messages
                - temperature
                - top_p
                - "n"
                - stream
                - stop
                - max_tokens
                - presence_penalty
                - frequency_penalty
                - logit_bias
                - user
                - response_format
                - seen
                - tools
                - tool_choice
            example:
              model: claude-sonnet-4-20250514
              messages:
                - role: system
                  content: You are a helpful assistant.
                - role: user
                  content:
                    - type: text
                      text: What is in this picture? Please describe it in detail.
                    - type: image_url
                      image_url:
                        url: >-
                          https://lsky.zhongzhuan.chat/i/2024/10/17/6711068a14527.png
              stream: true
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  object:
                    type: string
                  created:
                    type: integer
                  choices:
                    type: array
                    items:
                      type: object
                      properties:
                        index:
                          type: integer
                        message:
                          type: object
                          properties:
                            role:
                              type: string
                            content:
                              type: string
                          required:
                            - role
                            - content
                          x-apifox-orders:
                            - role
                            - content
                        finish_reason:
                          type: string
                      x-apifox-orders:
                        - index
                        - message
                        - finish_reason
                  usage:
                    type: object
                    properties:
                      prompt_tokens:
                        type: integer
                      completion_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                    required:
                      - prompt_tokens
                      - completion_tokens
                      - total_tokens
                    x-apifox-orders:
                      - prompt_tokens
                      - completion_tokens
                      - total_tokens
                required:
                  - id
                  - object
                  - created
                  - choices
                  - usage
                x-apifox-orders:
                  - id
                  - object
                  - created
                  - choices
                  - usage
              example:
                id: chatcmpl-123
                object: chat.completion
                created: 1677652288
                choices:
                  - index: 0
                    message:
                      role: assistant
                      content: |-


                        Hello there, how may I assist you today?
                    finish_reason: stop
                usage:
                  prompt_tokens: 9
                  completion_tokens: 12
                  total_tokens: 21
          headers: {}
          x-apifox-name: OK
      security:
        - bearer: []
      x-apifox-folder: Chat/Anthropic Claude Interface/Chat Compatible Formats
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421929-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://api.chainhub.tech
    description: Production Environment
security:
  - bearer: []
```
