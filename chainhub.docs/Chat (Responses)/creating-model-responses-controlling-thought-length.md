# Create a model response (controlling the length of thought)

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
      summary: Create a model response (controlling the length of thought)
      deprecated: false
      description: |-
        https://platform.openai.com/docs/api-reference/responses/create
        Some OpenAI models only support the Response format, such as o3-pro and codex-mini-latest.
      tags:
        - 聊天(Responses)
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
                  type: string
                reasoning:
                  type: object
                  properties:
                    effort:
                      type: string
                      description: >-
                        The currently supported values are minimal, low, medium, and high. Reducing the reasoning effort can speed up the response and reduce the number of tokens used for reasoning in the response. The default value is medium.
                  x-apifox-orders:
                    - effort
                  description: The description of the chain of thought used by the reasoning model when generating a response.
              x-apifox-orders:
                - model
                - input
                - reasoning
            example:
              model: gpt-5.1
              input:
                - role: user
                  content: Write a one-sentence bedtime story about a unicorn.
              reasoning:
                effort: high
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
          headers: {}
          x-apifox-name: OK
      security:
        - bearer: []
      x-apifox-folder: Chat (Responses)
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326879727-run
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
