# /fal-ai/flux-pro/kontext

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-pro/kontext:
    post:
      summary: /fal-ai/flux-pro/kontext
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-pro/kontext'
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
                  description: Hints for generating an image
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
                image_url:
                  type: string
                  description: >-
                    Drag and drop files here, or provide base64 encoded data.
                    The URL accepts the following file types: jpg, jpeg, png, webp, gif, avif
              required:
                - prompt
                - image_url
              x-apifox-orders:
                - prompt
                - guidance_scale
                - num_images
                - output_format
                - safety_tolerance
                - image_url
            example:
              prompt: Put a donut next to the flour.
              guidance_scale: 3.5
              num_images: 1
              output_format: jpeg
              safety_tolerance: '2'
              image_url: >-
                https://v3.fal.media/files/rabbit/rmgBxhwGYb2d3pl3x9sKf_output.png
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326486293-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://api.chainhub.tech
    description: Production Environment
  - bearer: []

```
