# Create videos with images using OpenAI.

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/videos:
    post:
      summary: Create videos with images using OpenAI.
      deprecated: false
      description: ''
      tags:
        - 'Video model/veo video generation/OpenAI video format '
      parameters: []
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                model:
                  description: Currently, only veo_3_1 and veo_3_1-fast are supported. Group selection includes limited-time special offers and the default group.
                  example: veo_3_1
                  type: string
                prompt:
                  description: Prompt words
                  example: Let the cow happily take the driving test (Part 3)
                  type: string
                seconds:
                  description: Duration
                  example: '8'
                  type: string
                input_reference:
                  format: binary
                  type: string
                  description: Pad map
                  example: ile://C:\Users\Administrator\Desktop\scene1.png
                size:
                  description: 720x1280 portrait mode 1280x720 landscape mode
                  example: 16x9
                  type: string
                watermark:
                  example: 'false'
                  type: string
              required:
                - model
                - prompt
                - seconds
                - input_reference
                - size
            examples: {}
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
                  model:
                    type: string
                  status:
                    type: string
                  progress:
                    type: integer
                  created_at:
                    type: integer
                  seconds:
                    type: string
                  size:
                    type: string
                required:
                  - id
                  - object
                  - model
                  - status
                  - progress
                  - created_at
                  - seconds
                  - size
              example:
                id: video_55cb73b3-60af-40c8-95fd-eae8fd758ade
                object: video
                model: veo_3_1
                status: queued
                progress: 0
                created_at: 1762336916
                seconds: '8'
                size: 16x9
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: 'Video model/veo video generation/OpenAI video format '
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-370109881-run
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
