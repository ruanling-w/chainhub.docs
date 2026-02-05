# /fal-ai/flux-lora/inpainting

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/flux-lora/inpainting:
    post:
      summary: /fal-ai/flux-lora/inpainting
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/flux-lora/inpainting'
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
                image_url:
                  type: string
                  description: Image URL, accepted file types: jpg, jpeg, png, webp, gif, avif
                strength:
                  type: number
                  description: Strength, range: 0.01-1
                mask_url:
                  type: string
                  description: The mask URL accepts the following file types: jpg, jpeg, png, webp, gif, avif
              required:
                - prompt
                - image_url
                - mask_url
              x-apifox-orders:
                - prompt
                - num_inference_steps
                - guidance_scale
                - num_images
                - enable_safety_checker
                - output_format
                - image_url
                - strength
                - mask_url
            example:
              prompt: A photo of a lion sitting on a stone bench
              num_inference_steps: 28
              guidance_scale: 3.5
              num_images: 1
              enable_safety_checker: true
              output_format: jpeg
              image_url: >-
                https://storage.googleapis.com/falserverless/example_inputs/dog.png
              strength: 0.85
              mask_url: >-
                https://storage.googleapis.com/falserverless/example_inputs/dog_mask.png
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apifox-orders: []
              examples:
                '1':
                  summary: Successful examples
                  value:
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
                '2':
                  summary: Successful examples
                  value:
                    status: IN_QUEUE
                    request_id: 72a35804-b407-4b09-894b-3a35559c38f9
                    response_url: >-
                      https://queue.fal.run/fal-ai/flux-lora/requests/72a35804-b407-4b09-894b-3a35559c38f9
                    status_url: >-
                      https://queue.fal.run/fal-ai/flux-lora/requests/72a35804-b407-4b09-894b-3a35559c38f9/status
                    cancel_url: >-
                      https://queue.fal.run/fal-ai/flux-lora/requests/72a35804-b407-4b09-894b-3a35559c38f9/cancel
                    logs: null
                    metrics: {}
                    queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-355349527-run
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
