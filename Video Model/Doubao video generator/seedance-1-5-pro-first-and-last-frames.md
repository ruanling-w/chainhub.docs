# seedance-1-5-pro-first and last frames

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
      summary: 'seedance-1-5-pro-first and last frames '
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
                  text: The girl in the picture says "cheese" to the camera, with a 360-degree camera panning --dur 5
                - type: image_url
                  image_url:
                    url: >-
                      https://ark-project.tos-cn-beijing.volces.com/doc_image/seepro_first_frame.jpeg
                  role: first_frame
                - type: image_url
                  image_url:
                    url: >-
                      https://ark-project.tos-cn-beijing.volces.com/doc_image/seepro_last_frame.jpeg
                  role: last_frame
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
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-402333878-run
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
