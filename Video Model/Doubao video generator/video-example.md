# Video Example

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /volc/v1/contents/generations/tasks:
    post:
      summary: Video Example
      deprecated: false
      description: Official documentation: https://www.volcengine.com/docs/82379/1520757
      tags:
        - Video Model/Bean Bun Video Generation
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: false
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ''
          required: false
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
                  description: The ID of the model you need to call
                content:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                        description: The input content type should be text here.
                      text:
                        type: string
                        description: >-
                          The text input to the model describes the desired video output, including:
                          Text prompts (required): Supports both Chinese and English. It is recommended to keep the text to no more than 500 characters. Too many characters can scatter information, causing the model to ignore details and focus only on key points, resulting in missing elements in the video.
                    x-apifox-orders:
                      - type
                      - text
                    required:
                      - type
                      - text
                  description: Input the data into the model to generate video information, supporting both text and image information.
              required:
                - model
                - content
              x-apifox-orders:
                - model
                - content
            example: "{\r\n    \"model\": \"doubao-seedance-1-0-pro-fast-251015\",\r\n    \"content\": [\r\n        {\r\n            \"type\": \"text\",\r\n            \"text\": \"Multiple shots. A detective enters a dimly lit room. He examines clues on the table and picks up an item from the table. The camera pans to him as he ponders. --ratio 16:9\"\r\n            // text\": \"Multiple shots. A detective enters a dimly lit room. He examines clues on the table and picks up an item from the table. The camera pans to him as he ponders. --rs 720p --rt 16:9 --dur 5 --fps 24 --wm true --seed 11 --cf false\"\r\n        }\r\n    ]\r\n}"
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                id: cgt-20250918165243-bfpzb
                status: submitted
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-350878596-run
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
