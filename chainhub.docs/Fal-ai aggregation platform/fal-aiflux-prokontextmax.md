# /fal-ai/flux-pro/kontext/max

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-pro/kontext/max:
    post:
      summary: /fal-ai/flux-pro/kontext/max
      deprecated: false
      description: 'Official documentation:  https://fal.ai/models/fal-ai/flux-pro/kontext/max'
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
                seed:
                  type: integer
                guidance_scale:
                  type: number
                  description: Range value: 1-20
                sync_mode:
                  type: boolean
                  description: Synchronous mode
                num_images:
                  type: integer
                  description: Output image count, range: 1-4
                safety_tolerance:
                  type: string
                  description: Safety tolerance
                output_format:
                  type: string
                  description: Image output formats: "jpeg", "png"
                aspect_ratio:
                  type: string
                  description: Image aspect ratios, enumerated values: 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21
                image_url:
                  type: string
                  description: Image URL
              required:
                - prompt
                - output_format
                - image_url
              x-apifox-orders:
                - prompt
                - seed
                - guidance_scale
                - sync_mode
                - num_images
                - safety_tolerance
                - output_format
                - aspect_ratio
                - image_url
            example:
              prompt: Put a donut next to the flour.
              seed: 0
              guidance_scale: 3.5
              sync_mode: false
              num_images: 1
              safety_tolerance: 2
              output_format: jpeg
              aspect_ratio: string
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
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326492402-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://api.chainhub.tech
    description: Production  Environment
security:
  - bearer: []

```
