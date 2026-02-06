# Create task lucataco/flux-schnell-lora

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/predictions:
    post:
      summary: Create task lucataco/flux-schnell-lora
      deprecated: false
      description: 'Official documentation: https://replicate.com/lucataco/flux-schnell-lora'
      tags:
        - Replicate aggregation platform
      parameters:
        - name: Authorization
          in: header
          description: ''
          required: false
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                version:
                  type: string
                input:
                  type: object
                  properties:
                    prompt:
                      type: string
                      description: Prompt to generate an image.
                    hf_lora:
                      type: string
                      description: >-
                        Huggingface path or LoRA weights URL. For example: alvdansen/frosting_lane_flux
                    lora_scale:
                      type: number
                      description: LoRA weight scaling. Default: 0.8
                    num_outputs:
                      type: integer
                      description: Number of images to output. Default: 1. Minimum: 1, Maximum: 4.
                    aspect_ratio:
                      type: string
                      description: Aspect ratio of the generated image. Default value: "1:1".
                    output_format:
                      type: string
                      description: The format of the output image. Default value: "webp".
                    output_quality:
                      type: integer
                      description: >-
                        The quality of the output image, ranging from 0 to 100. 100 is the best quality, and 0 is the lowest quality. This is unrelated to the .png output. Default value: 80
                    prompt_strength:
                      type: number
                      description: >-
                        Cue strength (or denoising strength) when using an image against an image. 1.0
                        Corresponds to completely destroying information in the image. Default: 0.8. Minimum: 0, Maximum: 1.
                    num_inference_steps:
                      type: integer
                      description: Number of inference steps. Default: 4. Minimum: 1, Maximum: 12.
                  required:
                    - prompt
                  x-apifox-orders:
                    - prompt
                    - hf_lora
                    - lora_scale
                    - num_outputs
                    - aspect_ratio
                    - output_format
                    - output_quality
                    - prompt_strength
                    - num_inference_steps
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                lucataco/flux-schnell-lora:2a6b576af31790b470f0a8442e1e9791213fa13799cbb65a9fc1436e96389574
              input:
                prompt: a beautiful castle frstingln illustration
                hf_lora: alvdansen/frosting_lane_flux
                lora_scale: 0.8
                num_outputs: 1
                aspect_ratio: '1:1'
                output_format: webp
                output_quality: 80
                prompt_strength: 0.8
                num_inference_steps: 4
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  created:
                    type: integer
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                      required:
                        - url
                      x-apifox-orders:
                        - url
                required:
                  - created
                  - data
                x-apifox-orders:
                  - created
                  - data
              example:
                id: nfg4nbtgm9rj00crankr6ft6t0
                model: lucataco/flux-schnell-lora
                version: >-
                  2a6b576af31790b470f0a8442e1e9791213fa13799cbb65a9fc1436e96389574
                input:
                  aspect_ratio: '1:1'
                  hf_lora: alvdansen/frosting_lane_flux
                  lora_scale: 0.8
                  num_inference_steps: 4
                  num_outputs: 1
                  output_format: webp
                  output_quality: 80
                  prompt: a beautiful castle frstingln illustration
                  prompt_strength: 0.8
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-29T08:58:10.978Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/nfg4nbtgm9rj00crankr6ft6t0/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/nfg4nbtgm9rj00crankr6ft6t0
                  stream: >-
                    https://stream.replicate.com/v1/files/qoxq-kwulj767tbexpyags2qj6zh6f5k6dmbvfdt6cigg2f4zcuzpnhcq
                  web: https://replicate.com/p/nfg4nbtgm9rj00crankr6ft6t0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326436155-run
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
