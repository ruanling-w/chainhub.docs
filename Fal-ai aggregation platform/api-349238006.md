# /fal-ai/wan/v2.2-a14b/image-to-image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/wan/v2.2-a14b/image-to-image:
    post:
      summary: /fal-ai/wan/v2.2-a14b/image-to-image
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/wan/v2.2-a14b/image-to-image'
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
                  description: Image URL
                prompt:
                  type: string
                  description: Prompt words
                strength:
                  type: number
                  description: Intensity, range: 0-1
                aspect_ratio:
                  type: string
                  description: Image size
                num_inference_steps:
                  type: integer
                  description: Range value: 2-40
                enable_safety_checker:
                  type: boolean
                  description: Enable security checks. Default value: true
                enable_prompt_expansion:
                  type: boolean
                  description: Enable prompt extension
                acceleration:
                  type: string
                  description: Image generation speed, enumeration values: "regular", "none"
                guidance_scale:
                  type: number
                  description: Range value: 1-10
                guidance_scale_2:
                  type: integer
                  description: Range value: 1-10
                shift:
                  type: integer
                  description: Range value: 1-10
                image_format:
                  type: string
                  description: Image output formats: "jpeg", "png"
              required:
                - image_url
                - prompt
              x-apifox-orders:
                - image_url
                - prompt
                - strength
                - aspect_ratio
                - num_inference_steps
                - enable_safety_checker
                - enable_prompt_expansion
                - acceleration
                - guidance_scale
                - guidance_scale_2
                - shift
                - image_format
            example:
              image_url: >-
                https://storage.googleapis.com/falserverless/example_inputs/wan-image-to-image-input.png
              prompt: >-
                A cinematic shot of an ancient city at sunset, intricate stone
                buildings, warm golden light
              strength: 0.5
              aspect_ratio: auto
              num_inference_steps: 27
              enable_safety_checker: true
              enable_prompt_expansion: false
              acceleration: regular
              guidance_scale: 3.5
              guidance_scale_2: 4
              shift: 2
              image_format: jpeg
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
                request_id: f88f1b41-b325-4f23-926b-da51481bf6c6
                response_url: >-
                  https://queue.fal.run/fal-ai/wan/requests/f88f1b41-b325-4f23-926b-da51481bf6c6
                status_url: >-
                  https://queue.fal.run/fal-ai/wan/requests/f88f1b41-b325-4f23-926b-da51481bf6c6/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/wan/requests/f88f1b41-b325-4f23-926b-da51481bf6c6/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-349238006-run
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
