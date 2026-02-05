# /fal-ai/flux-1/schnell/redux

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-1/schnell/redux:
    post:
      summary: /fal-ai/flux-1/schnell/redux
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-1/schnell/redux'
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
                num_inference_steps:
                  type: integer
                  description: Number of inference steps to be performed. Default: 4. Range: 1-12
                image_size:
                  type: string
                  description: Size of the generated image. Default: landscape_4_3 Range (3:4, 4:3, 16:9, 9:16)
                num_images:
                  type: integer
                  description: Number of images generated. Default: 1. Range: 1-4
                enable_safety_checker:
                  type: boolean
                  description: If set to true, the security inspector is enabled. Default: true
                output_format:
                  type: string
                  description: The format for generating the image. Default: "jpeg" Supported formats: default, png, jpeg
                acceleration:
                  type: string
                  description: Generation speed. Higher speed means faster generation. Default: "regular". Supported options: default, none, regular, high.
              required:
                - image_url
              x-apifox-orders:
                - image_url
                - num_inference_steps
                - image_size
                - num_images
                - enable_safety_checker
                - output_format
                - acceleration
            example:
              image_url: https://fal.media/files/kangaroo/acQvq-Kmo2lajkgvcEHdv.png
              num_inference_steps: 4
              image_size: landscape_4_3
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326483575-run
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
