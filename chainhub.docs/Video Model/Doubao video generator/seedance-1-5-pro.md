# seedance-1-5-pro

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
      summary: seedance-1-5-pro
      deprecated: false
      description: ''
      tags:
        - Video Model/Bean Bun Video Generation
      parameters: []
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
                        description: Type of input content
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
                      role:
                        type: string
                        description: Location or purpose of the image.
                    required:
                      - type
                      - image_url
                      - role
                    x-apifox-orders:
                      - type
                      - text
                      - image_url
                      - role
                  description: Input the data into the model to generate video information, supporting both text and image information.
              required:
                - model
                - content
              x-apifox-orders:
                - model
                - content
            example:
              model: doubao-seedance-1-5-pro-251215
              content:
                - type: text
                  text: The girl hugs the fox, opens her eyes, and looks gently at the camera. The fox holds her affectionately. The camera slowly pulls back, revealing the girl's hair blowing in the wind, and the sound of the wind can be heard.
                - type: image_url
                  image_url:
                    url: >-
                      https://ark-project.tos-cn-beijing.volces.com/doc_image/i2v_foxrgirl.png
              ratio: adaptive
              duration: 4
              watermark: false
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
                  status:
                    type: string
                required:
                  - id
                  - status
              examples:
                '1':
                  summary: Success example
                  value:
                    id: cgt-20250918170228-dw9rb
                    status: submitted
                '2':
                  summary: Success example
                  value:
                    id: cgt-20260108111352-gwv4p
                    status: submitted
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-410229637-run
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
