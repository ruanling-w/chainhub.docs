# /fal-ai/veo3

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/veo3:
    post:
      summary: /fal-ai/veo3
      deprecated: false
      description: Official documentation address：https://fal.ai/models/fal-ai/veo3
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
                aspect_ratio:
                  type: string
                  description: The aspect ratio of the generated video. If set to 1:1, the video will be drawn outside the aspect ratio. Default: "16:9", range [16:9, 9:16, 1:1]
                duration:
                  type: string
                  description: The default value for the generated video duration (in seconds) is "8s".
                enhance_prompt:
                  type: boolean
                  description: Enhance video generation (default: true)
                auto_fix:
                  type: boolean
                  description: Whether to automatically attempt to fix hints that fail content policy or other validation checks by rewriting (default: true)
                resolution:
                  type: string
                  description: The default resolution for generated videos is "720p". The range is [720p, 1080p].
                generate_audio:
                  type: boolean
                  description: Whether to generate audio for the video. If false, 33% of the points will be deducted. Default: true
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - aspect_ratio
                - duration
                - enhance_prompt
                - auto_fix
                - resolution
                - generate_audio
            example:
              prompt: >-
                A casual street interview on a busy New York City sidewalk in
                the afternoon. The interviewer holds a plain, unbranded
                microphone and asks: Have you seen Google's new Veo3 model It is
                a super good model. Person replies: Yeah I saw it, it's already
                available on fal. It's crazy good.
              aspect_ratio: '16:9'
              duration: 8s
              enhance_prompt: true
              auto_fix: true
              resolution: 720p
              generate_audio: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                status: IN_QUEUE
                request_id: 57b19308-8d3e-4196-b8bf-5ca80fa90827
                response_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/57b19308-8d3e-4196-b8bf-5ca80fa90827
                status_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/57b19308-8d3e-4196-b8bf-5ca80fa90827/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/57b19308-8d3e-4196-b8bf-5ca80fa90827/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform/falai-veo3 video generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-352567449-run
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
