# /fal-ai/qwen-image-edit-lora

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/qwen-image-edit-lora:
    post:
      summary: /fal-ai/qwen-image-edit-lora
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/qwen-image-edit-lora'
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
                num_inference_steps:
                  type: integer
                  description: Range value: 2-100
                guidance_scale:
                  type: integer
                  description: Range value: 2-100
                num_images:
                  type: integer
                  description: Number of images generated, range: 1-4
                enable_safety_checker:
                  type: boolean
                  description: Enable security checks. Default value: true
                output_format:
                  type: string
                  description: Supported output image formats: jpeg, png
                image_url:
                  type: string
                  description: Image URL
                negative_prompt:
                  type: string
                acceleration:
                  type: string
                  description: The acceleration level for image generation. Enumerated values: 'none', 'regular', 'high'
              required:
                - prompt
                - image_url
              x-apifox-orders:
                - prompt
                - num_inference_steps
                - guidance_scale
                - num_images
                - enable_safety_checker
                - output_format
                - image_url
                - negative_prompt
                - acceleration
            example:
              prompt: Change bag to apple macbook
              num_inference_steps: 30
              guidance_scale: 4
              num_images: 1
              enable_safety_checker: true
              output_format: png
              image_url: >-
                https://v3.fal.media/files/koala/oei_-iPIYFnhdB8SxojND_qwen-edit-res.png
              negative_prompt: blurry, ugly
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
                request_id: 5044e7a4-d38d-4c8a-81de-c9160c9ec005
                response_url: >-
                  https://queue.fal.run/fal-ai/qwen-image-edit-lora/requests/5044e7a4-d38d-4c8a-81de-c9160c9ec005
                status_url: >-
                  https://queue.fal.run/fal-ai/qwen-image-edit-lora/requests/5044e7a4-d38d-4c8a-81de-c9160c9ec005/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/qwen-image-edit-lora/requests/5044e7a4-d38d-4c8a-81de-c9160c9ec005/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-349238066-run
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
