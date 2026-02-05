# /fal-ai/veo3/fast

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/veo3/fast:
    post:
      summary: /fal-ai/veo3/fast
      deprecated: false
      description: Official documentation address：https://fal.ai/models/fal-ai/veo3/fast
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
                  description: Text prompts describing the video to be generated
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
              duration: 4s
              enhance_prompt: true
              auto_fix: true
              resolution: 720p
              generate_audio: false
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
                request_id: fabda298-3a7c-43f6-ba3a-2bde5b344173
                response_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/fabda298-3a7c-43f6-ba3a-2bde5b344173
                status_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/fabda298-3a7c-43f6-ba3a-2bde5b344173/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/fabda298-3a7c-43f6-ba3a-2bde5b344173/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: 成功
        x-200:成功:
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
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform/falai-veo3 video generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-352888996-run
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
