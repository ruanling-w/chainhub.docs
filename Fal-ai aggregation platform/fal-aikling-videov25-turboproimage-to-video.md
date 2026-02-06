# /fal-ai/kling-video/v2.5-turbo/pro/image-to-video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/kling-video/v2.5-turbo/pro/image-to-video:
    post:
      summary: /fal-ai/kling-video/v2.5-turbo/pro/image-to-video
      deprecated: false
      description: >-
        Official documentation:
        https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/image-to-video
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
                  description: Prompt words
                image_url:
                  type: string
                  description: Image URL, accepted file types: jpg, jpeg, png, webp, gif, avif
                duration:
                  type: string
                  description: The generated video duration has the following enumeration values: 5, 10.
                negative_prompt:
                  type: string
                cfg_scale:
                  type: number
                  description: Range value: 0-1
              required:
                - prompt
                - image_url
              x-apifox-orders:
                - prompt
                - image_url
                - duration
                - negative_prompt
                - cfg_scale
            example:
              prompt: >-
                A stark starting line divides two powerful cars, engines revving
                for the challenge ahead. They surge forward in the heat of
                competition, a blur of speed and chrome. The finish line looms
                as they vie for victory.
              image_url: >-
                https://v3.fal.media/files/panda/HnY2yf-BbzlrVQxR-qP6m_9912d0932988453aadf3912fc1901f52.jpg
              duration: '5'
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
                request_id: 727028ec-aa98-4073-9bcd-0acb386abcfc
                response_url: >-
                  https://queue.fal.run/fal-ai/kling-video/requests/727028ec-aa98-4073-9bcd-0acb386abcfc
                status_url: >-
                  https://queue.fal.run/fal-ai/kling-video/requests/727028ec-aa98-4073-9bcd-0acb386abcfc/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/kling-video/requests/727028ec-aa98-4073-9bcd-0acb386abcfc/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-355334957-run
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
