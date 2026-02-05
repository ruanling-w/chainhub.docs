# /fal-ai/kling-video/v2.5-turbo/pro/text-to-video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/kling-video/v2.5-turbo/pro/text-to-video:
    post:
      summary: /fal-ai/kling-video/v2.5-turbo/pro/text-to-video
      deprecated: false
      description: >-
        Official documentation:
        https://fal.ai/models//fal-ai/kling-video/v2.5-turbo/pro/text-to-video
      tags:
        - Fal-ai aggregation platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: Video prompts are generated.
                duration:
                  type: string
                  description: The generated video duration has the following enumeration values: 5 and 10.
                aspect_ratio:
                  type: string
                  description: Video aspect ratio, enumerated values: 16:9, 9:16, 1:1
                negative_prompt:
                  type: string
                cfg_scale:
                  type: number
                  description: Range value: 0-1
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - duration
                - aspect_ratio
                - negative_prompt
                - cfg_scale
            example:
              prompt: >-
                A noble lord walks among his people, his presence a comforting
                reassurance. He greets them with a gentle smile, embodying their
                hopes and earning their respect through simple interactions. The
                atmosphere is intimate and sincere, highlighting the bond
                between the leader and community.
              duration: '5'
              aspect_ratio: '16:9'
              negative_prompt: blur, distort, and low quality
              cfg_scale: 0.5
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apifox-orders: []
              example:
                status: IN_QUEUE
                request_id: 6d5fbbbd-411c-4c7a-9249-e297304c87d4
                response_url: >-
                  https://queue.fal.run/fal-ai/kling-video/requests/6d5fbbbd-411c-4c7a-9249-e297304c87d4
                status_url: >-
                  https://queue.fal.run/fal-ai/kling-video/requests/6d5fbbbd-411c-4c7a-9249-e297304c87d4/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/kling-video/requests/6d5fbbbd-411c-4c7a-9249-e297304c87d4/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-355333276-run
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
