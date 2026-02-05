# Create a video (with a character)

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
      summary: Create a video (with a character)
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
                model:
                  type: string
                orientation:
                  type: string
                  enum:
                    - portrait
                    - landscape
                  x-apifox-enum:
                    - value: portrait
                      name: ''
                      description: Vertical screen
                    - value: landscape
                      name: ''
                      description: Landscape
                prompt:
                  type: string
                duration:
                  type: integer
                  description: Duration
                  enum:
                    - 10
                    - 15
                    - 25
                  x-apifox-enum:
                    - value: 10
                      name: ''
                      description: Sora-2 and Sora-2-Pro are available.
                    - value: 15
                      name: ''
                      description: Sora-2 and Sora-2-Pro are available.
                    - value: 25
                      name: ''
                      description: Sora-2-Pro is available.
                character_url:
                  type: string
                  description: The video link required to create the character. Note that the video must not contain any real people, otherwise the process will fail.
                character_timestamps:
                  type: string
                  description: The duration of a character's appearance in the video, formatted as `{start},{end}`, note that the range of end-start is 1-3 seconds.
                size:
                  type: string
                  enum:
                    - large
                    - small
                  x-apifox-enum:
                    - value: large
                      name: HD
                      description: ''
                    - value: small
                      name: generally
                      description: ''
              required:
                - model
                - prompt
                - size
              x-apifox-orders:
                - images
                - model
                - orientation
                - prompt
                - duration
                - character_url
                - character_timestamps
                - size
                - 01K8ZASVCXKDRDADSJ1KHETZGN
            example:
              images: []
              model: sora-2
              orientation: portrait
              prompt: make animate
              duration: 15
              character_url: >-
                https://filesystem.site/cdn/20251030/javYrU4etHVFDqg8by7mViTWHlMOZy.mp4
              character_timestamps: 1,3
              size: large
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                id: sora-2:task_01k900ag82ecgbewj2xa3758z0
                status: pending
                status_update_time: 1762010677921
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/Unified video format
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-369666077-run
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
