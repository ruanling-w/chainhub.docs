# /fal-ai/veo3/image-to-video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/veo3/image-to-video:
    post:
      summary: /fal-ai/veo3/image-to-video
      deprecated: false
      description: Official documentation：https://fal.ai/models/fal-ai/veo3/image-to-video
      tags:
        - Fal-ai aggregation platform/falai-veo3 video generation
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: Prompt words
                image_url:
                  type: string
                  description: Reference image URL
                aspect_ratio:
                  type: string
                  description: Size, enumerated values: 16:9, 9:16, auto, default value: "auto"
                duration:
                  type: string
                  description: Video duration, default value: "8s"
                generate_audio:
                  type: boolean
                  description: Generate audio, default value: true
                resolution:
                  type: string
                  description: Resolution, enumerated values: "720p", "1080p"
              required:
                - prompt
                - image_url
              x-apifox-orders:
                - prompt
                - image_url
                - aspect_ratio
                - duration
                - generate_audio
                - resolution
            example:
              prompt: >-
                A woman looks into the camera, breathes in, then exclaims
                energetically, "have you guys checked out Veo3 Image-to-Video on
                Fal? It's incredible!"
              image_url: >-
                https://storage.googleapis.com/falserverless/example_inputs/veo3-i2v-input.png
              aspect_ratio: auto
              duration: 8s
              generate_audio: true
              resolution: 720p
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  request_id:
                    type: string
                  response_url:
                    type: string
                  status_url:
                    type: string
                  cancel_url:
                    type: string
                  logs:
                    type: 'null'
                  metrics:
                    type: object
                    properties: {}
                  queue_position:
                    type: integer
                required:
                  - status
                  - request_id
                  - response_url
                  - status_url
                  - cancel_url
                  - logs
                  - metrics
                  - queue_position
              example:
                status: IN_QUEUE
                request_id: bcd3b436-b7af-42f3-8649-204657bfaf10
                response_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/bcd3b436-b7af-42f3-8649-204657bfaf10
                status_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/bcd3b436-b7af-42f3-8649-204657bfaf10/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/bcd3b436-b7af-42f3-8649-204657bfaf10/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform/falai-veo3 video generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-353201765-run
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
