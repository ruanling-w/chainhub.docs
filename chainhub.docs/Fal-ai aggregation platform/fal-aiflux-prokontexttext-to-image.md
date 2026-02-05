# /fal-ai/flux-pro/kontext/text-to-image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-pro/kontext/text-to-image:
    post:
      summary: /fal-ai/flux-pro/kontext/text-to-image
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-pro/kontext/text-to-image'
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
                  description: Prompts for generating an image.
                guidance_scale:
                  type: number
                  description: The CFG (Classifier-Free Guided) scale measures how close you want your model to be to the prompts when searching for relevant images. Default: 3.5. Range: 1-20.
                num_images:
                  type: integer
                  description: Number of images generated. Default: 1. Range: 1-4
                output_format:
                  type: string
                  description: The format for generating the image. Default: "jpeg" Supported formats: default, png, jpeg
                safety_tolerance:
                  type: string
                  description: The safety tolerance level for generated images. 1 indicates the strictest tolerance, and 5 indicates the most lenient. Default value: "2"
                aspect_ratio:
                  type: string
                  description: >-
                    The aspect ratio of the generated image. Default: "1:1"
                    Supported verses: 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - guidance_scale
                - num_images
                - output_format
                - safety_tolerance
                - aspect_ratio
            example:
              prompt: >-
                Extreme close-up of a single tiger eye, direct frontal view.
                Detailed iris and pupil. Sharp focus on eye texture and color.
                Natural lighting to capture authentic eye shine and depth. The
                word "FLUX" is painted over it in big, white brush strokes with
                visible texture.
              guidance_scale: 3.5
              num_images: 1
              output_format: jpeg
              safety_tolerance: '2'
              aspect_ratio: '1:1'
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
                request_id: acf05732-7cb3-445b-9f39-fdaeccb1d730
                response_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/acf05732-7cb3-445b-9f39-fdaeccb1d730
                status_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/acf05732-7cb3-445b-9f39-fdaeccb1d730/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/acf05732-7cb3-445b-9f39-fdaeccb1d730/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326487979-run
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
