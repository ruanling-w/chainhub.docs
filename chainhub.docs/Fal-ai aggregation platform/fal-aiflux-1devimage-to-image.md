# /fal-ai/flux-1/dev/image-to-image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-1/dev/image-to-image:
    post:
      summary: /fal-ai/flux-1/dev/image-to-image
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-1/dev/image-to-image'
      tags:
        - Fal-ai aggregation platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                image_url:
                  type: string
                  description: >-
                    Drag and drop files here, or provide base64 encoded data.
                    The URL accepts the following file types: jpg, jpeg, png, webp, gif, avif
                strength:
                  type: number
                  description: The intensity of the initial image. Higher intensity values ​​result in better model performance. Default value: 0.95. Range: 0.01-1
                num_inference_steps:
                  type: integer
                  description: Number of inference steps to be performed. Default: 40. Range: 10-50.
                prompt:
                  type: string
                  description: Hints for generating an image
                guidance_scale:
                  type: number
                  description: The CFG (Classifier-Free Guided) scale measures how close you want your model to be to the prompts when searching for relevant images. Default: 3.5. Range: 1-20.
                num_images:
                  type: integer
                  description: Number of images generated. Default: 1. Range: 1-4
                enable_safety_checker:
                  type: boolean
                output_format:
                  type: string
                  description: The format for generating the image. Default: "jpeg" Supported formats: default, png, jpeg
                acceleration:
                  type: string
                  description: Generation speed. Higher speed means faster generation. Default: "regular". Supported options: default, none, regular, high.
              required:
                - image_url
                - prompt
              x-apifox-orders:
                - image_url
                - strength
                - num_inference_steps
                - prompt
                - guidance_scale
                - num_images
                - enable_safety_checker
                - output_format
                - acceleration
            example:
              image_url: https://fal.media/files/koala/Chls9L2ZnvuipUTEwlnJC.png
              strength: 0.95
              num_inference_steps: 40
              prompt: A cat dressed as a wizard with a background of a mystic forest.
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326476432-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https:/api.chainhub.tech
    description: Production Environment
security:
  - bearer: []

```
