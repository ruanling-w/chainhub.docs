# Create a video with images using sora-2

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
      summary: Create a video with images using sora-2
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation/Unified video format
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
                images:
                  type: array
                  items:
                    type: string
                  description: Image link
                model:
                  type: string
                  description: Model Name
                orientation:
                  type: string
                  description: |
                    portrait (vertical screen)
                    landscape (horizontal screen)
                prompt:
                  type: string
                  description: Prompt words
                size:
                  type: string
                  description: ' Small, generally 720p'
                duration:
                  type: integer
                  description: 'Enumeration value: 10'
                watermark:
                  type: string
                  description: |
                    The default setting is `true`, which prioritizes removing the watermark. If an error occurs, it will be used as a fallback option if the video still has a watermark.

                    Passing `false` will force the video to be watermark-free, and it will automatically retry if a watermark removal error occurs.
              required:
                - images
                - model
                - orientation
                - prompt
                - size
                - duration
                - watermark
              x-apifox-orders:
                - images
                - model
                - orientation
                - prompt
                - size
                - duration
                - watermark
            example:
              images:
                - >-
                  https://filesystem.site/cdn/20250612/998IGmUiM2koBGZM3UnZeImbPBNIUL.png
              model: sora-2-all
              orientation: portrait
              prompt: make animate
              size: large
              duration: 15
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
                  status_update_time:
                    type: integer
                required:
                  - id
                  - status
                  - status_update_time
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/Unified video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-358068907-run
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
