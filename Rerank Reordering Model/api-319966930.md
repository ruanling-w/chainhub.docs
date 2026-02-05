# Reorder

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/rerank:
    post:
      summary: Reordering
      deprecated: false
      description: |-
        Given a hint, the model will return the completion of one or more predictions, and can also return the probability of the alternative label at each location.

        Completed creation based on the provided prompts and parameters

        Official document: https://docs.siliconflow.cn/cn/api-reference/rerank/create-rerank
      tags:
        - Rerank Reordering Model
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
                documents:
                  type: array
                  items:
                    type: string
                query:
                  type: string
                top_n:
                  type: integer
                instruct:
                  type: string
              required:
                - model
                - documents
                - query
                - top_n
                - instruct
              x-apifox-orders:
                - model
                - documents
                - query
                - top_n
                - instruct
            example:
              model: qwen3-rerank
              documents:
                - Text ranking models are widely used in search engines and recommendation systems, ranking candidate texts based on their relevance.
                - Quantum computing is a cutting-edge field in computational science.
                - The development of pre-trained language models has brought new progress to text ranking models.
              query: What is a text ranking model?
              top_n: 2
              instruct: >-
                Given a web search query, retrieve relevant passages that answer
                the query.
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
          headers: {}
          x-apifox-name: OK
      security:
        - bearer: []
      x-apifox-folder: Rerank Reordering Model
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-319966930-run
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
