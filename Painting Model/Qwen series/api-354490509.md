# qwen-image-edit-2509

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/images/generations:
    post:
      summary: qwen-image-edit-2509
      deprecated: false
      description: |+
        Given a prompt and/or an input image, the model will generate a new image.

      tags:
        - Painting Models / Qwen Series
      parameters:
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
                prompt:
                  type: string
                  description: Prompt words
                image:
                  type: string
                  description: Image URL
              required:
                - model
                - prompt
                - image
              x-apifox-orders:
                - model
                - prompt
                - image
            example:
              model: qwen-image-edit-2509
              prompt: Put the little duck on the woman's T-shirt
              image: >-
                https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                  created:
                    type: integer
                  usage:
                    type: object
                    properties:
                      prompt_tokens:
                        type: integer
                      completion_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                      prompt_tokens_details:
                        type: object
                        properties:
                          cached_tokens_details:
                            type: object
                            properties: {}
                        required:
                          - cached_tokens_details
                      completion_tokens_details:
                        type: object
                        properties: {}
                      output_tokens:
                        type: integer
                    required:
                      - prompt_tokens
                      - completion_tokens
                      - total_tokens
                      - prompt_tokens_details
                      - completion_tokens_details
                      - output_tokens
                required:
                  - data
                  - created
                  - usage
          headers: {}
          x-apifox-name: x-apifox-name: Success
      security: []
      x-apifox-folder: Painting Models / Qwen Series
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-354490509-run
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
