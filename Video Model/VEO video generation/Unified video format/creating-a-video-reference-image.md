# Creating a video (see reference image)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/video/create:
    post:
      summary: Creating a video (see reference image)
      deprecated: false
      description: ''
      tags:
        - Video model/veo video generation/Unified video format
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
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
                  description: |-
                    Enumeration value:
                    veo2
                    veo2-fast
                    veo2-fast-frames
                    veo2-fast-components
                    veo2-pro
                    veo3
                    veo3-fast
                    veo3-pro
                    veo3-pro-frames
                    veo3-fast-frames
                    veo3-frames
                prompt:
                  type: string
                  description: Prompt words
                images:
                  type: array
                  items:
                    type: string
                  description: >
                    When the model uses `veo2-fast-frames`, a maximum of two frames are supported, representing the first and last frames. When the model uses `veo3-pro-frames`, a maximum of one first frame is supported. When the model uses `veo2-fast-components` or `veo3.1-components`, a maximum of three components are supported. In this case, the images represent elements from the video.
                enhance_prompt:
                  type: boolean
                  description: |
                    Since VEO only supports English prompts, you can turn on this switch if you need Chinese prompts to be automatically converted to English.
                enable_upsample:
                  type: string
                  description: Excess
                aspect_ratio:
                  type: string
                  description: |
                    ⚠️Only VEO3 supports "16:9" or "9:16" aspect ratios.
              required:
                - model
                - prompt
                - enhance_prompt
                - enable_upsample
                - aspect_ratio
              x-apifox-orders:
                - model
                - prompt
                - images
                - enhance_prompt
                - enable_upsample
                - aspect_ratio
            example:
              prompt: The cow flew into the sky
              model: veo3.1-components
              images:
                - >-
                  https://filesystem.site/cdn/20250612/VfgB5ubjInVt8sG6rzMppxnu7gEfde.png
                - >-
                  https://filesystem.site/cdn/20250612/998IGmUiM2koBGZM3UnZeImbPBNIUL.png
                - >-
                  https://iknow-pic.cdn.bcebos.com/5882b2b7d0a20cf4ced1ab5f64094b36adaf99e9
              enhance_prompt: true
              enable_upsample: true
              aspect_ratio: '16:9'
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
              example:
                id: veo3.1-components:1762241017-xTL0P9HvGF
                status: pending
                status_update_time: 1762241017286
          headers: {}
          x-apifox-name: OK
      security:
        - bearer: []
      x-apifox-folder: Video model/veo video generation/Unified video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-371329190-run
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
