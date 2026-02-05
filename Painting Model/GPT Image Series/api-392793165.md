# Create gpt-image-1.5

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/images/generations:
    post:
      summary: Create gpt-image-1.5
      deprecated: false
      description: |-
        Given a hint, the model will return the completion of one or more predictions, and can also return the probability of the alternative label at each location.

        Completed creation based on the provided prompts and parameters

        Official documentation ：https://platform.openai.com/docs/api-reference/images/create
      tags:
        - Painting Models / GPT Image Series
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
                prompt:
                  description: A text description of the required image. Maximum length is 1000 characters.
                  type: string
                "n":
                  description: The number of images to be generated must be between 1 and 10.
                  type: integer
                size:
                  description: >+
                    The size of the generated image. For GPT image models, it must be one of 1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or auto (default). For dall-e-2, it must be one of 256x256, 512x512, or 1024x1024. For dall-e-3, it must be one of 1024x1024, 1792x1024, or 1024x1792.

                  type: string
              required:
                - prompt
                - "n"
                - size
              x-apifox-orders:
                - prompt
                - "n"
                - size
            example:
              size: 1024x1536
              prompt: a man walks
              model: gpt-image-1.5
              "n": 1
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
      security: []
      x-apifox-folder: Painting Models / GPT Image Series
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-392793165-run
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
