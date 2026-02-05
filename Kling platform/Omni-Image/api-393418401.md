# Omni-Image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/images/omni-image:
    post:
      summary: Omni-Image
      deprecated: false
      description: ''
      tags:
        - Kling platform/Omni-Image
      parameters:
        - name: Content-Type
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
                model_name:
                  type: string
                  description: Model name Enumeration value: kling-image-o1
                prompt:
                  type: string
                  description: |-
                    Text prompts, which can include positive and negative descriptions.
                    Prompts can be templated to meet different image generation needs.
                    Cannot exceed 2500 characters.
                image_list:
                  type: array
                  items:
                    type: object
                    properties:
                      image:
                        type: string
                    x-apifox-orders:
                      - image
                  description: Reference Figure List
                resolution:
                  type: string
                  description: |-
                    Image clarity

                    Enumerated values: 1k, 2k
                    1k: 1K standard definition
                    2k: 2K high definition
                'n':
                  type: integer
                  description: |-
                    Number of images generated
                    Value range: [1, 9]
                aspect_ratio:
                  type: string
                  description: |-
                    The aspect ratio (width:height) of the generated image.
                    Enum values: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9, auto
                    Note: "auto" will intelligently generate the video based on the provided content.
                    When generating a new image based on the aspect ratio of the original image, this parameter is not effective.
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - model_name
                - prompt
              x-apifox-orders:
                - model_name
                - prompt
                - image_list
                - resolution
                - 'n'
                - aspect_ratio
                - callback_url
                - external_task_id
            example:
              model_name: kling-image-o1
              prompt: Change the emoji to a laughing emoji.
              image_list:
                - image: >-
                    https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling platform/Omni-Image
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-393418401-run
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
