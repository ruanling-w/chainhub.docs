# Generate 3.0 (Image Editing)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /ideogram/v1/ideogram-v3/edit:
    post:
      summary: Generate 3.0 (Image Editing)
      deprecated: false
      description: >-
        Using the Ideogram 3.0 model, synchronously generate images based on given prompts and optional parameters.

        For specific parameters, please refer to the official documentation: https://developer.ideogram.ai/api-reference/api-reference/edit-v3

        The returned image URL is valid for 24 hours; after that time, the image will be inaccessible.

        Image already de-promoted.
      tags:
        - Painting Model/Ideogram
      parameters:
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
          required: true
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            encoding:
              seed:
                contentType: multipart/form-data
            schema:
              type: object
              properties:
                image:
                  format: binary
                  type: string
                  description: |
                    The image is being reprocessed (maximum size 10 megabytes); currently only JPEG, WebP, and PNG formats are supported.
                  example: file://C:\Users\Administrator\Desktop\example.png
                mask:
                  format: binary
                  type: string
                  example: file://C:\Users\Administrator\Desktop\example.png
                seed:
                  description: Random seed, range 0-2147483647, setting this value will yield repeatable results.
                  example: 12345
                  type: integer
                prompt:
                  example: A photo of a cat wearing a hat.
                  type: string
              required:
                - image
            example: ""
      responses:
        "200":
          description: ""
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-295871433-run
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
