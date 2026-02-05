# Upscale (high-definition zoom)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /ideogram/upscale:
    post:
      summary: Upscale (high-definition zoom)
      deprecated: false
      description: Official documentation：https://developer.ideogram.ai/api-reference/api-reference/upscale
      tags:
        - Painting Models / Ideogram
      parameters:
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
          required: true
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
          required: false
          example: multipart/form-data
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                image_request:
                  description: |>-
                       "prompt": "a beautiful sunset over     mountains", // Prompt word to guide zooming in (optional)
                        "resemblance": 50, // Similarity (optional) Range: 1-100, default 50
                        "detail": 50, // Detail level (optional) Range: 1-100, default 50
                        "magic_prompt_option": "AUTO", // Whether to use MagicPrompt (optional) Possible values: AUTO/ON/OFF
                        "num_images": 1, // Number of images generated (optional) Range: 1-8, default 1
                        "seed": 123456 // Random seed (optional) Range: 0-2147483647
                  example: "{\r\n    \"resemblance\": 50,\r\n    \"magic_prompt_option\": \"AUTO\",\r\n    \"prompt\": \"A%20serene%20tropical%20beach%20\",\r\n    \"seed\": 12345,\r\n    \"detail\": 50\r\n}"
                  type: string
                image_file:
                  description: ' Image file (required): The source image file that needs to be enlarged.'
                  example: file://C:\Users\Administrator\Desktop\example.png
                  type: string
                  format: binary
            example: ''
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                  message:
                    type: string
                  request_id:
                    type: string
                  data:
                    type: object
                    properties:
                      task_id:
                        type: string
                      task_status:
                        type: string
                      created_at:
                        type: integer
                      updated_at:
                        type: integer
                    required:
                      - task_id
                      - task_status
                      - created_at
                      - updated_at
                required:
                  - code
                  - message
                  - request_id
                  - data
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model/Ideogram
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-244685729-run
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
