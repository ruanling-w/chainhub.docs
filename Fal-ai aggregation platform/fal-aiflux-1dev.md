# /fal-ai/flux-1/dev

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-1/dev:
    post:
      summary: /fal-ai/flux-1/dev
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-1/dev'
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
                image_size:
                  type: string
                  description: Size of the generated image. Default: landscape_4_3 Range (3:4, 4:3, 16:9, 9:16)
                num_inference_steps:
                  type: integer
                  description: Number of inference steps to be performed. Default: 28. Range: 0-50
                guidance_scale:
                  type: number
                  description: The CFG (Classifier-Free Guided) scale measures how close you want your model to be to the prompts when searching for relevant images. Default: 3.5. Range: 1-20
                num_images:
                  type: integer
                  description:
                enable_safety_checker:
                  type: boolean
                  description: If set to true, the security inspector is enabled. Default: true
                output_format:
                  type: string
                  description: The format of the generated image. Default: "jpeg". Supported formats: default, JPEG, png
                acceleration:
                  type: string
                  description: >-
                    Generation speed. The higher the speed, the faster the generation. Default: "regular". Supported: default, none, regular, high.
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
                - acceleration
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
              acceleration: regular
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
                    x-apifox-orders: []
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
                x-apifox-orders:
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
                request_id: 3892f1e8-5fb1-469f-87b0-696d6054c9f2
                response_url: >-
                  https://queue.fal.run/fal-ai/flux-1/requests/3892f1e8-5fb1-469f-87b0-696d6054c9f2
                status_url: >-
                  https://queue.fal.run/fal-ai/flux-1/requests/3892f1e8-5fb1-469f-87b0-696d6054c9f2/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/flux-1/requests/3892f1e8-5fb1-469f-87b0-696d6054c9f2/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326441625-run
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
