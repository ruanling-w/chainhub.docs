# Create an embed

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/embeddings:
    post:
      summary: Create an embed
      deprecated: false
      description: |+
        Obtain a vector representation of a given input, which machine learning models and algorithms can easily use.

        Related guide: [Embeddings](https://platform.openai.com/docs/guides/embeddings)

        Create an embedding vector representing the input text.

      tags:
        - Chat/ChatGPT Interface/ChatGPT Embeddings
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
                  description: >-
                    The ID of the model you want to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all available models, or see our [Model Overview](https://platform.openai.com/docs/models/overview) for their descriptions.
                input:
                  type: string
                  description: >-
                    Enter text to obtain the embedding, encoded as a string or an array of tokens. To obtain the embeddings of multiple inputs in a single request, pass an array of strings or an array of tokens. Each input must not exceed 8192 tokens in length.
              required:
                - model
                - input
              x-apifox-orders:
                - model
                - input
            example:
              model: text-embedding-3-large
              input: Meow meow meow meow meow meow meow meow meow meow
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        object:
                          type: string
                        embedding:
                          type: array
                          items:
                            type: number
                        index:
                          type: integer
                      x-apifox-orders:
                        - object
                        - embedding
                        - index
                  model:
                    type: string
                  usage:
                    type: object
                    properties:
                      prompt_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                    required:
                      - prompt_tokens
                      - total_tokens
                    x-apifox-orders:
                      - prompt_tokens
                      - total_tokens
                required:
                  - object
                  - data
                  - model
                  - usage
                x-apifox-orders:
                  - object
                  - data
                  - model
                  - usage
              example: |-
                {
                  "object": "list",
                  "data": [
                    {
                      "object": "embedding",
                      "embedding": [
                        0.0023064255,
                        -0.009327292,
                        .... (1536 floats total for ada-002)
                        -0.0028842222
                      ],
                      "index": 0
                    }
                  ],
                  "model": "text-embedding-ada-002",
                  "usage": {
                    "prompt_tokens": 8,
                    "total_tokens": 8
                  }
                }
          headers: {}
          x-apifox-name: Create embeddings
      security:
        - bearer: []
      x-apifox-folder: Chat/ChatGPT Interface/ChatGPT Embeddings
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421926-run
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
