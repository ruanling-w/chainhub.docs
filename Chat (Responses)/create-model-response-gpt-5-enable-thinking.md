# Creating Model Responses: GPT-5 Enables Thinking

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/responses:
    post:
      summary: "Creating Model Responses: GPT-5 Enables Thinking"
      deprecated: false
      description: |-
        https://platform.openai.com/docs/api-reference/responses/create
        Some OpenAI models only support the Response format, such as o3-pro and codex-mini-latest.
      tags:
        - Chat (Responses)
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ''
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
                  description: The ID of the model to use. For more information about which models can be used with the chat API, see the model endpoint compatibility table.
                input:
                  type: array
                  items:
                    type: object
                    properties:
                      role:
                        type: string
                      content:
                        type: array
                        items:
                          type: object
                          properties:
                            type:
                              type: string
                            text:
                              type: string
                          x-apifox-orders:
                            - type
                            - text
                    x-apifox-orders:
                      - role
                      - content
                    required:
                      - content
                      - role
                  description: The model's text and images are used to generate responses.
                tools:
                  type: array
                  items:
                    type: string
                  description: A list of tools the model can call. Currently, only functions are supported as tools. Use this feature to provide a list of functions for which the model can generate JSON input.
                text:
                  type: object
                  properties:
                    format:
                      type: object
                      properties:
                        type:
                          type: string
                          description: The type of response format defined. Always text.
                      required:
                        - type
                      x-apifox-orders:
                        - type
                      description: Specifies the format the model must output.
                    verbosity:
                      type: string
                      description: >-
                        Limits the verbosity of the model's response. Lower values result in more concise responses, while higher values result in more detailed responses. The currently supported values are low, medium, and high. The default value is medium.
                  x-apifox-orders:
                    - format
                    - verbosity
                  description: Configuration options for the model's text response. Can be plain text or structured JSON data.
                reasoning:
                  type: object
                  properties:
                    effort:
                      type: string
                      description: >-
                        The currently supported values are minimal, low, medium, and high. Reducing the reasoning effort can speed up the response and reduce the number of tokens used for reasoning in the response. The default value is medium.
                    summary:
                      type: string
                      description: A summary of the inference performed by the model. This is useful for debugging and understanding the model's inference process. (Auto, Concise, or one of these is detailed.)
                  x-apifox-orders:
                    - effort
                    - summary
                stream:
                  type: boolean
                  description: >-
                    The default value is false. If set, partial message increments will be sent, similar to ChatGPT. The flag will be sent as data-only server-sent events, which will occur when available and in the data: [DONE] message stream termination event. Python code example.
                store:
                  type: boolean
                  description: Whether to store the generated model response for later retrieval through the API. The default value is true.
              x-apifox-orders:
                - model
                - input
                - tools
                - text
                - reasoning
                - stream
                - store
            example:
              model: gpt-5-2025-08-07
              input:
                - role: user
                  content:
                    - type: input_text
                      text: 1+2+3+4+5....9985
              tools: []
              text:
                format:
                  type: text
                verbosity: medium
              reasoning:
                effort: medium
                summary: auto
              stream: true
              store: true
      responses:
        '200':
          description: ''
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
      x-apifox-folder: Chat (Responses)
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-333400155-run
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
