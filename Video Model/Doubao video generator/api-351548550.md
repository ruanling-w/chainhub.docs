# Image-based video - base64 encoded

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
      summary: Image-based video - base64 encoded
      deprecated: false
      description: Official documentation: https://www.volcengine.com/docs/82379/1520757
      tags:
        - Video Model/Bean Bun Video Generation
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
                  description:  The ID of the model you need to call
                content:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                        description: The type of input content.
                      text:
                        type: string
                        description: The text input to the model describes the video to be generated.
                      image_url:
                        type: object
                        properties:
                          url:
                            type: string
                            description: Image information, here is the image Base64 encoded.
                        required:
                          - url
                        x-apifox-orders:
                          - url
                        description: The image object input to the model.
                    required:
                      - type
                    x-apifox-orders:
                      - type
                      - text
                      - image_url
                  description: Input the data into the model to generate video information, supporting both text and image information.
              required:
                - model
                - content
              x-apifox-orders:
                - model
                - content
            example:
              model: doubao-seedance-1-0-lite-i2v-250428
              content:
                - type: text
                  text: >-
                    The girl hugs the fox, opens her eyes, and looks gently at the camera. The fox cuddles her affectionately. The camera slowly pulls back, and the girl's hair is blown by the wind. --ratio
                    adaptive --dur 5
                - type: image_url
                  image_url:
                    url: >-
                      data:image/png;base64,aHR0cHM6Ly9hcmstcHJvamVjdC50b3MtY24tYmVpamluZy52b2xjZXMuY29tL2RvY19pbWFnZS9pMnZfZm94cmdpcmwucG5n
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                id: cgt-20250918170604-vd988
                status: submitted
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-351548550-run
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
