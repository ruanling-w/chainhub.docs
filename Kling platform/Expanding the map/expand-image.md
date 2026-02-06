# Expanding the map

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/images/editing/expand:
    post:
      summary: Expanding the map
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Map Expansion
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: false
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
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
                image:
                  type: string
                  description: |-
                    Reference image
                    Supports passing in Base64 encoded images or image URLs (ensure they are accessible).
                up_expansion_ratio:
                  type: number
                  description: |-
                    Expand the area upwards; calculated based on a multiple of the original image height.
                    Value range: [0, 2], the total area of ​​the new image must not exceed 3 times that of the original image.
                    For example, if the original image height is 20 and the current parameter value is 0.1, then:
                    The distance from the top edge of the original image to the top edge of the new image is 20 x 0.1 = 2, and the entire area within this range is the expanded area.
                down_expansion_ratio:
                  type: number
                  description: |-
                    Expand the area downwards; calculated based on a multiple of the original image height.
                    Value range: [0,2], the total area of ​​the new image must not exceed 3 times that of the original image.
                    For example, if the original image height is 20 and the current parameter value is 0.2, then:
                    The distance from the bottom edge of the original image to the bottom edge of the new image is 20 x 0.2 = 4, and the entire area within this range is the expanded area.
                left_expansion_ratio:
                  type: number
                  description: |-
                    Expand the area to the left; calculated based on a multiple of the original image width.
                    Value range: [0,2], the total area of ​​the new image must not exceed 3 times that of the original image.
                    For example, if the original image width is 30 and the current parameter value is 0.3, then:
                    The distance from the left side of the original image to the left side of the new image is 30 x 0.3 = 9, and the entire area within this range is the expanded area.
                right_expansion_ratio:
                  type: number
                  description: |-
                    Expand the area to the right; calculated based on a multiple of the original image width.
                    Value range: [0,2], the total area of ​​the new image must not exceed 3 times that of the original image.
                    For example, if the original image width is 30 and the current parameter value is 0.4, then:
                    The distance from the right side of the original image to the right side of the new image is 30 x 0.4 = 12, and the entire area within this range is the expanded area.
                prompt:
                  type: string
                  description: |-
                    Positive text prompts
                    cannot exceed 2500 characters
                "n":
                  type: integer
                  description: |-
                    Number of images generated
                    Value range: [1, 9]
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - image
                - up_expansion_ratio
                - down_expansion_ratio
                - left_expansion_ratio
                - "n"
                - right_expansion_ratio
              x-apifox-orders:
                - image
                - up_expansion_ratio
                - down_expansion_ratio
                - left_expansion_ratio
                - right_expansion_ratio
                - prompt
                - "n"
                - callback_url
                - external_task_id
            example:
              image: >-
                https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
              up_expansion_ratio: 0.1
              down_expansion_ratio: 0.1
              left_expansion_ratio: 0.1
              right_expansion_ratio: 0.1
              prompt: Focus Center
              "n": 1
              callback_url: ""
              external_task_id: ""
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling Platform/Map Expansion
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386284418-run
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
