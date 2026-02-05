# Creation complete

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/completions:
    post:
      summary: Creation complete
      deprecated: false
      description: |
        Given a hint, the model will return one or more complete predictions, and may also return the probability of an alternative label at each location.

        Completion creation for the provided hint and parameters

        https://platform.openai.com/docs/api-reference/completions
      tags:
        - Chat/ChatGpt API/ChatGPT Auto-completion
      parameters:
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
                  title: ""
                  description: >-
                    The ID of the model you want to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all available models, or see our [Model Overview](https://platform.openai.com/docs/models/overview) for their descriptions.
                prompt:
                  type: string
                  title: ""
                  description: >-
                    The generated hint is encoded as a string, an array of strings, an array of tokens, or an array of token arrays. Note that `<|endoftext|>` is the document separator seen by the model during training; therefore, if no hint is specified, the model will generate the beginning of a new document.
                max_tokens:
                  type: integer
                  title: ""
                  description: |-
                    The default value is 16.
                    The maximum number of tokens generated during completion.

                    The token count hinted at plus `max_tokens` cannot exceed the model's context length. Python code example for counting tokens.
                temperature:
                  type: integer
                  title: ""
                  description: >-
                    The default value is 1.
                    The sampling temperature to use, between 0 and 2. Higher values ​​(such as 0.8) will make the output more random, while lower values ​​(such as 0.2) will make it more focused and deterministic.

                    We generally recommend changing this or top_p, rather than both.
                top_p:
                  type: integer
                  description: A unique identifier representing the end user, which can help OpenAI monitor and detect abuse. Learn more.
                "n":
                  type: integer
                  description: >-
                    The default value is 1.

                    This determines the number of completions generated for each prompt.

                    Note: Because this parameter generates many completions, it can quickly deplete your token quota. Use it with caution and ensure that you have reasonable settings for max_tokens and stop.
                stream:
                  type: boolean
                  title: ""
                  description: >-
                    Defaults to false. Whether to rewind partial progress. If set, the token will be sent as an event to the server when available, and the stream will be terminated by a data-only message.

                    Terminated by a data: [DONE] message. Object message terminated. Python code example.
                logprobs:
                  type: "null"
                  title: ""
                  description: >-
                    The default value is null.

                    It includes the logprobs of the 5 most likely tokens, and the selected token. For example, if logprobs is 5, the API will return a list of the 5 most likely tokens.

                    The API will always return the logprobs of the sampled token, so the response may contain at most logprobs+1 elements.

                    The maximum value of logprobs is 5.
                stop:
                  type: string
                  title: ""
                  description: The default value is null. A maximum of four sequences are allowed; the API will stop generating any more tokens from these. The returned text will not include the stopping sequence.
                best_of:
                  type: integer
                  description: >-
                    The default value is 1. It generates `best_of` completenesses on the server side and returns the "best" completeness (the one with the highest log probability for each token). Results cannot be streamed.

                    When used with `n`, `best_of` controls the number of candidate completenesses, and `n` specifies the number to return – `best_of` must be greater than `n`.

                    Note: Because this parameter generates many completenesses, it can quickly deplete your token quota. Use it with caution and ensure you have reasonable settings for `max_tokens` and `stop`.
                echo:
                  type: boolean
                  description: The default value is false. In addition to auto-completion, it also provides feedback.
                frequency_penalty:
                  type: number
                  description: The default value is a number between 0 and 2.0. Positive values ​​penalize new tokens based on the current frequency of the text, reducing the likelihood of the model repeating the same lines word for word.
                logit_bias:
                  type: object
                  properties: {}
                  description: >-
                    The default value is null. This modifies the likelihood of a specified token appearing after modification.

                    It accepts a JSON object that maps tokens (specified by the token ID in the GPT tokenizer) to associated bias values, ranging from -100 to 100. You can use this tokenizer tool (for GPT-2 and GPT-3) to convert text to token IDs. Mathematically, the bias is added to the generated logit before sampling the model. The exact effect varies by model, but values ​​between -1 and 1 should decrease or increase the likelihood of selection; values ​​like -100 or 100 should result in the disabling or exclusive selection of the associated token.

                    For example, you could pass {"50256": -100} to prevent the generation of <|endoftext|> tokens.
                  x-apifox-orders: []
                presence_penalty:
                  type: number
                  description: >-
                    The default value is a number between 0 and 2.0. Positive values ​​penalize new tokens based on whether they appear in the current text, increasing the likelihood of the model discussing new topics. See [link/reference] for more information on frequency and presence penalties.
                seed:
                  type: integer
                  description: >-
                    If specified, our system will make a best-effort deterministic sampling so that repeated requests using the same seed and parameters should return the same results.

                    Determinism is not guaranteed; you should refer to the `system_fingerprint` response parameters to monitor backend changes.
                suffix:
                  type: string
                  description: The default value is null. This is the suffix that appears after the text is completed.
                user:
                  type: string
              required:
                - model
                - prompt
                - user
              x-apifox-orders:
                - model
                - prompt
                - best_of
                - echo
                - frequency_penalty
                - logit_bias
                - logprobs
                - max_tokens
                - "n"
                - presence_penalty
                - seed
                - stop
                - stream
                - suffix
                - temperature
                - user
                - top_p
            example:
              model: gpt-3.5-turbo-instruct
              prompt: Hello,
              max_tokens: 30
              temperature: 0
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
                  model:
                    type: string
                  system_fingerprint:
                    type: string
                  choices:
                    type: array
                    items:
                      type: object
                      properties:
                        text:
                          type: string
                        index:
                          type: integer
                        logprobs:
                          type: "null"
                        finish_reason:
                          type: string
                      x-apifox-orders:
                        - text
                        - index
                        - logprobs
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
                  - model
                  - system_fingerprint
                  - choices
                  - usage
                x-apifox-orders:
                  - id
                  - object
                  - created
                  - model
                  - system_fingerprint
                  - choices
                  - usage
              example:
                id: cmpl-ByvHP6AWeB1L5vWZSPNHsB12sU9db
                object: text_completion
                created: 1753859563
                model: gpt-3.5-turbo-instruct
                choices:
                  - index: 0
                    logprobs: null
                    finish_reason: length
                    text: I'm Xiaoice, nice to meet you. I'm an AI assistant that can reply to...
                usage:
                  prompt_tokens: 3
                  completion_tokens: 30
                  total_tokens: 33
          headers: {}
          x-apifox-name: Ok
      security:
        - bearer: []
      x-apifox-folder: Chat/ChatGpt API/ChatGPT Auto-completion
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421925-run
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
