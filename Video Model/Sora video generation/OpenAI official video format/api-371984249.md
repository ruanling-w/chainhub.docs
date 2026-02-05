# Create videos with Character using OpenAI.

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
      summary: Create videos with Character using OpenAI.
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation/OpenAI official video format
      parameters: []
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                model:
                  example: sora-2
                  type: string
                prompt:
                  example: The scene comes to life
                  type: string
                seconds:
                  example: '10'
                  type: string
                input_reference:
                  format: binary
                  type: string
                  example: file://C:\Users\Administrator\Desktop\scene 1.png
                size:
                  description: >+
                    Output resolution format is width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). The default value is 720x1280.

                  example: 720x1280
                  type: string
                watermark:
                  example: ture
                  type: string
                private:
                  example: 'false'
                  type: string
                character_url:
                  example: >-
                    https://filesystem.site/cdn/20251030/javYrU4etHVFDqg8by7mViTWHlMOZy.mp4
                  type: string
                character_timestamps:
                  example: 1,3
                  type: string
              required:
                - model
                - prompt
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
                id: video_6048220c-b0d9-4292-b80b-9c6eaf73f112
                object: video
                model: sora_video2
                status: queued
                progress: 0
                created_at: 1762326617
                seconds: '10'
                size: 1280x720
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/OpenAI official video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-371984249-run
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
