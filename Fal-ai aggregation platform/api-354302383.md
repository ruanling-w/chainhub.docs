# /fal-ai/qwen-image-edit-plus

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/qwen-image-edit-plus:
    post:
      summary: /fal-ai/qwen-image-edit-plus
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/qwen-image-edit-plus'
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
                  description: Prompt words.
                image_size:
                  type: string
                  description: >-
                    Image dimensions, enumerated values: square, square_hd, landscape_4_3, landscape_16_9, portrait_3_4, portrait_9_16
                num_inference_steps:
                  type: integer
                  description: Range value: 2-100
                guidance_scale:
                  type: integer
                  description: Range value: 0-20
                num_images:
                  type: integer
                  description: Number of images generated, range: 1-4
                enable_safety_checker:
                  type: boolean
                  description: Enable security checks. Default value: true
                output_format:
                  type: string
                  description: Supported output image formats: jpeg, png
                image_urls:
                  type: array
                  items:
                    type: string
                  description: Image URL
                negative_prompt:
                  type: string
              required:
                - prompt
                - image_urls
              x-apifox-orders:
                - prompt
                - image_size
                - num_inference_steps
                - guidance_scale
                - num_images
                - enable_safety_checker
                - output_format
                - image_urls
                - negative_prompt
            example:
              prompt: >-
                Close shot portrait of a woman in front of this car on this
                highway
              image_size: square_hd
              num_inference_steps: 50
              guidance_scale: 4
              num_images: 1
              enable_safety_checker: true
              output_format: png
              image_urls:
                - >-
                  https://v3.fal.media/files/monkey/i3saq4bAPXSIl08nZtq9P_ec535747aefc4e31943136a6d8587075.png
                - >-
                  https://v3.fal.media/files/penguin/BCOZp6teRhSQFuOXpbBOa_da8ef9b4982347a2a62a516b737d4f21.png
                - >-
                  https://v3.fal.media/files/tiger/sCoZhBksx9DvwSR4_U3_C_3d1f581441874005908addeae9c10d0f.png
              negative_prompt: blurry, ugly
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
                request_id: 9c08e7d8-312c-402d-a691-c207a9cb8121
                response_url: >-
                  https://queue.fal.run/fal-ai/qwen-image-edit-plus/requests/9c08e7d8-312c-402d-a691-c207a9cb8121
                status_url: >-
                  https://queue.fal.run/fal-ai/qwen-image-edit-plus/requests/9c08e7d8-312c-402d-a691-c207a9cb8121/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/qwen-image-edit-plus/requests/9c08e7d8-312c-402d-a691-c207a9cb8121/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-354302383-run
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
