# Create chat autocomplete qwen-mt-turbo

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
      summary: Create chat autocomplete qwen-mt-turbo
      deprecated: false
      description: >+
        Given a hint, the model will return one or more complete predictions, and may also return the probability of an alternative label at each location.

        Complete with the provided hint and parameters

        Official documentation: https://help.aliyun.com/zh/model-studio/machine-translation#d8aee140d1ows

      tags:
        - Chat/ChatGpt Interface/ChatGPT Chat
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
        - name: X-Forwarded-Host
          in: header
          description: ""
          required: false
          example: localhost:5173
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
                    The ID of the model to use. For details on which models can be used with the chat API, see the Model Endpoint Compatibility Table.

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
                  description: A list of messages contained in the conversation so far. Python code example.
                temperature:
                  type: integer
                  description: >-
                    The sampling temperature to use is between 0 and 2. Higher values ​​(such as 0.8) will make the output more random, while lower values ​​(such as 0.2) will make the output more focused and deterministic. We generally recommend changing this or `top_p`, but not both.
                top_p:
                  type: integer
                  description: >-
                    An alternative to temperature sampling is called kernel sampling, where the model considers the results of labels with a top_p probability quality. So 0.1 means only labels constituting the top 10% probability quality are considered. We generally recommend changing this or `temperature`, but not both.
                "n":
                  type: integer
                  description: |-
                    The default value is 1.
                    This determines how many chat completion options to generate for each input message.
                stream:
                  type: boolean
                  description: >-
                    The default value is false. If set, partial message increments will be sent, similar to ChatGPT. The flag will be sent as data-only server-sent events, which will occur when available and in the data: [DONE] message stream termination event. Python code example.
                stop:
                  type: string
                  description: The default value is null. A maximum of 4 sequences will be generated before the API stops generating further tags.
                max_tokens:
                  type: integer
                  description: |-
                    Defaults to inf
                    Maximum number of tags generated in chat completion.

                    The total length of input and generated tags is limited by the model's context length. Example Python code for calculating tags.
                presence_penalty:
                  type: number
                  description: >-
                    A number between -2.0 and 2.0. Positive values ​​penalize new tokens based on whether they have appeared in the text so far, thus increasing the likelihood that the model will discuss new topics.

                    [See more information on frequency and presence penalties.](https://platform.openai.com/docs/api-reference/parameter-details)
                frequency_penalty:
                  type: number
                  description: >-
                    The default value is a number between 0 and 2.0, with a positive value between 2.0 and 2.0. Positive values ​​penalize new tags based on the current frequency of the text's presence, reducing the likelihood of the model repeating the same lines.

                    More information on frequency and presence penalties.
                logit_bias:
                  type: "null"
                  description: >-
                    Modifies the likelihood of a specified tag appearing in the completion.

                    Accepts a JSON object that maps tags (tag IDs specified by the tagger) to associated bias values ​​(-100 to 100). Mathematically, the bias is added to the logit generated by the model before sampling. The exact effect varies by model, but values ​​between -1 and 1 should decrease or increase the likelihood of the associated tag being selected; values ​​like -100 or 100 should result in the associated tag being disabled or exclusively selected.
                user:
                  type: string
                  description: >-
                    A unique identifier representing your end users can help OpenAI monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
                response_format:
                  type: object
                  properties: {}
                  x-apifox-orders: []
                  description: >-
                    Specifies the format of the object that the model must output. Setting `{ "type": "json_object" }` enables JSON mode, which ensures that the messages generated by the model are valid JSON. Important: When using JSON mode, you must also instruct the model to generate JSON via a system or user message. Failure to do so may result in the model generating an endless stream of empty tokens until the token limit is reached, leading to increased latency and a "stuck" appearance for requests. Also note that if `finish_reason="length"`, the message content may be partially truncated, indicating that more than `max_tokens` has been generated or the conversation has exceeded the maximum context length. Display Attributes
                seen:
                  type: integer
                  description: >-
                    This feature is in the testing phase. If specified, our system will make a best effort to sample deterministically so that repeated requests using the same seed and parameters should return the same result. Determinism cannot be guaranteed; you should refer to the `system_fingerprint` response parameter to monitor backend changes.
                tools:
                  type: array
                  items:
                    type: string
                  description: A list of tools that the model can invoke. Currently, only functions as tools are supported. Use this feature to provide a list of functions that the model can use to generate JSON input.
                tool_choice:
                  type: object
                  properties: {}
                  description: >-
                    Controls which function the model calls (if any). `none` means the model will not call the function but will generate a message. `auto` means the model can choose between generating a message and calling the function. Force the model to call the function using `{"type": "function", "function":
                    {"name": "my_function"}}`. If no function exists, the default is `none`. If a function exists, the default is `auto`. Displays possible types.
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
              model: qwen-mt-turbo
              messages:
                - role: user
                  content: I didn't laugh after watching this video.
              translation_options:
                source_lang: auto
                target_lang: English
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
      x-apifox-folder: Chat/ChatGpt Interface/ChatGPT Chat
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327199929-run
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
