# /fal-ai/flux-lora

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-lora:
    post:
      summary: /fal-ai/flux-lora
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-lora'
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
                image_size:
                  type: string
                  description: >-
                    Image dimensions, enumerated values: square, square pro, landscape_4_3, landscape_16_9, portrait_3_4
                num_inference_steps:
                  type: integer
                  description: Range value: 1-50
                guidance_scale:
                  type: number
                  description: Range value: 0-35
                num_images:
                  type: integer
                  description: Number of images, range: 1-4
                enable_safety_checker:
                  type: boolean
                  description: Enable security checks. Default value: true
                output_format:
                  type: string
                  description: Supported output image formats: jpeg, png
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - image_size
                - num_inference_steps
                - guidance_scale
                - num_images
                - enable_safety_checker
                - output_format
            example:
              prompt: >-
                Extreme close-up of a single tiger eye, direct frontal view.
                Detailed iris and pupil. Sharp focus on eye texture and color.
                Natural lighting to capture authentic eye shine and depth. The
                word "FLUX" is painted over it in big, white brush strokes with
                visible texture.
              image_size: landscape_4_3
              num_inference_steps: 28
              guidance_scale: 3.5
              num_images: 1
              enable_safety_checker: true
              output_format: jpeg
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
                request_id: 07e0be22-3380-4699-a377-48729443435c
                response_url: >-
                  https://queue.fal.run/fal-ai/flux-lora/requests/07e0be22-3380-4699-a377-48729443435c
                status_url: >-
                  https://queue.fal.run/fal-ai/flux-lora/requests/07e0be22-3380-4699-a377-48729443435c/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/flux-lora/requests/07e0be22-3380-4699-a377-48729443435c/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-355348632-run
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
