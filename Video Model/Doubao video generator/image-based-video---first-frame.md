# Image-based video - first frame

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
      summary: Image-based video - first frame
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
                  description: 'The ID of the model you need to call '
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
                        description: The text input to the model describes the video to be generated.
                      image_url:
                        type: object
                        properties:
                          url:
                            type: string
                            description: The image object input to the model, the image URL
                        required:
                          - url
                        x-apifox-orders:
                          - url
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
                    Generate kitten video --rs 1080p --rt 16:9 --ratio 16:9 --dur 5 --fps 24
                    --wm false --seed 0 --cf false
                - type: image_url
                  image_url:
                    url: >-
                      https://brainrot-yt-shorts.oss-cn-beijing.aliyuncs.com/images/cached/55a955b7e41723417281051d7bebdb45.png
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                id: cgt-20250918165813-8tz7p
                status: submitted
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-350891452-run
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
