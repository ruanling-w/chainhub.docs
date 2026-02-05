# /fal-ai/flux-pro/kontext/max/multi

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-pro/kontext/max/multi:
    post:
      summary: /fal-ai/flux-pro/kontext/max/multi
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-pro/kontext/max/multi'
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
                guidance_scale:
                  type: number
                  description: Range value: 1-20
                num_images:
                  type: integer
                  description: Number of generated images, range: 1-4
                output_format:
                  type: string
                  description: Image output format: "jpeg", "png"
                safety_tolerance:
                  type: string
                  description: Safety tolerance
                image_urls:
                  type: array
                  items:
                    type: string
                  description: Image URL
              required:
                - prompt
                - image_urls
              x-apifox-orders:
                - prompt
                - guidance_scale
                - num_images
                - output_format
                - safety_tolerance
                - image_urls
            example:
              prompt: Put the little duckling on top of the woman's t-shirt.
              guidance_scale: 3.5
              num_images: 1
              output_format: jpeg
              safety_tolerance: '2'
              image_urls:
                - >-
                  https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp
                - >-
                  https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp
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
                request_id: 30bc4aeb-0543-4198-929c-da97da4d14c9
                response_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/30bc4aeb-0543-4198-929c-da97da4d14c9
                status_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/30bc4aeb-0543-4198-929c-da97da4d14c9/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/30bc4aeb-0543-4198-929c-da97da4d14c9/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-321180443-run
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
