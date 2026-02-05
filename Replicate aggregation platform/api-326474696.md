# Create task lucataco/flux-dev-lora

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
      summary: Create task lucataco/flux-dev-lora
      deprecated: false
      description: 'Official documentation: https://replicate.com/lucataco/flux-dev-lora'
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
                       A URL for HF, Replicate, CivitAI, or LoRA. For example: alvdansen/frosting_lane_flux
                    lora_scale:
                      type: number
                      description: Scaling of LoRA weights. Default: 0.8.
                    num_outputs:
                      type: integer
                      description: Number of images to output. Default: 1. Minimum: 1, Maximum: 4.
                    aspect_ratio:
                      type: string
                      description: Aspect ratio of the generated image. Default value: "1:1".
                    output_format:
                      type: string
                      description: The format of the output image. Default value: "webp".
                    guidance_scale:
                      type: number
                      description: Guide strength. Default: 3.5. Minimum: 0, Maximum: 10.
                    output_quality:
                      type: integer
                      description: >-
                        The quality of the output image, ranging from 0 to 100. 100 is the best quality, and 0 is the lowest quality. This is unrelated to the .png output. Default value: 80.。
                    prompt_strength:
                      type: number
                      description: The cue strength (or denoising strength) when using an image against an image. 1.0 corresponds to completely destroying information in the image. Default: 0.8.
                    num_inference_steps:
                      type: integer
                      description: Number of inference steps. Default: 28. Minimum: 1, Maximum: 50.
                  required:
                    - prompt
                  x-apifox-orders:
                    - prompt
                    - hf_lora
                    - lora_scale
                    - num_outputs
                    - aspect_ratio
                    - output_format
                    - guidance_scale
                    - output_quality
                    - prompt_strength
                    - num_inference_steps
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                lucataco/flux-dev-lora:091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3
              input:
                prompt: a beautiful castle frstingln illustration
                hf_lora: alvdansen/frosting_lane_flux
                lora_scale: 0.8
                num_outputs: 1
                aspect_ratio: '1:1'
                output_format: webp
                guidance_scale: 3.5
                output_quality: 80
                prompt_strength: 0.8
                num_inference_steps: 28
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  model:
                    type: string
                  version:
                    type: string
                  input:
                    type: object
                    properties:
                      aspect_ratio:
                        type: string
                      input_image:
                        type: string
                      output_format:
                        type: string
                      prompt:
                        type: string
                      prompt_upsampling:
                        type: boolean
                      safety_tolerance:
                        type: integer
                    required:
                      - aspect_ratio
                      - input_image
                      - output_format
                      - prompt
                      - prompt_upsampling
                      - safety_tolerance
                  logs:
                    type: string
                  output:
                    type: 'null'
                  data_removed:
                    type: boolean
                  error:
                    type: 'null'
                  status:
                    type: string
                  created_at:
                    type: string
                  urls:
                    type: object
                    properties:
                      cancel:
                        type: string
                      get:
                        type: string
                      stream:
                        type: string
                      web:
                        type: string
                    required:
                      - cancel
                      - get
                      - stream
                      - web
                required:
                  - id
                  - model
                  - version
                  - input
                  - logs
                  - output
                  - data_removed
                  - error
                  - status
                  - created_at
                  - urls
              example:
                id: c9zn270jk1rj00crans8m6ssjc
                model: lucataco/flux-dev-lora
                version: >-
                  091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3
                input:
                  aspect_ratio: '1:1'
                  guidance_scale: 3.5
                  hf_lora: alvdansen/frosting_lane_flux
                  lora_scale: 0.8
                  num_inference_steps: 28
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
                created_at: '2025-07-29T09:09:55.992Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/c9zn270jk1rj00crans8m6ssjc/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/c9zn270jk1rj00crans8m6ssjc
                  stream: >-
                    https://stream.replicate.com/v1/files/qoxq-37kfnrolbp7l2vy5f2ffduf6vyqye4savtprvsiikqzpcjbuejfa
                  web: https://replicate.com/p/c9zn270jk1rj00crans8m6ssjc
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326474696-run
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
