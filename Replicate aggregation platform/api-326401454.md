# Create task stability-ai/sdxl

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
      summary: Create task stability-ai/sdxl
      deprecated: false
      description: 'Official documentation: https://replicate.com/stability-ai/sdxl'
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
                input:
                  type: object
                  properties:
                    width:
                      type: integer
                      description: Output image width. Default: 1024.
                    height:
                      type: integer
                      description: Output image height. Default value: 1024.
                    prompt:
                      type: string
                      description: Input prompt.
                    refine:
                      type: string
                      description: Which refining style to use. Default: "no_refiner".
                    scheduler:
                      type: string
                      description: Scheduler. Default value: "K_EULER".
                    lora_scale:
                      type: number
                      description: LoRA additive scaling. Only applies to trained models. Default: 0.6.
                    num_outputs:
                      type: integer
                      description: Number of images to output. Default: 1. Minimum: 1, Maximum: 4.
                    guidance_scale:
                      type: number
                      description: No classifier-guided scale. Default: 7.5. Minimum: 1, Maximum: 50.
                    apply_watermark:
                      type: boolean
                      description: >-
                       Apply a watermark to determine if the image was generated in a downstream application. You can use this method to disable the watermark if you have other regulations regarding the secure generation or deployment of images. Default: true.
                    high_noise_frac:
                      type: number
                      description: For expert_ensemble_refiner, the noise score to use. Default: 0.8. Minimum: 0, Maximum: 1.
                    negative_prompt:
                      type: string
                      description: Enter a negative prompt. Default: "".
                    prompt_strength:
                      type: number
                      description: >-
                        Hint strength when using img2img / inpaint. 1.0

                        Corresponds to completely destroying information in the image. Default: 0.8. Minimum: 0, Maximum: 1.
                    num_inference_steps:
                      type: integer
                      description: Number of denoising steps. Default: 50. Minimum: 1, Maximum: 500.
                  x-apifox-orders:
                    - width
                    - height
                    - prompt
                    - refine
                    - scheduler
                    - lora_scale
                    - num_outputs
                    - guidance_scale
                    - apply_watermark
                    - high_noise_frac
                    - negative_prompt
                    - prompt_strength
                    - num_inference_steps
              x-apifox-orders:
                - input
            example:
              version: >-
                stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc
              input:
                width: 768
                height: 768
                prompt: An astronaut riding a rainbow unicorn, cinematic, dramatic
                refine: expert_ensemble_refiner
                scheduler: K_EULER
                lora_scale: 0.6
                num_outputs: 1
                guidance_scale: 7.5
                apply_watermark: false
                high_noise_frac: 0.8
                negative_prompt: ''
                prompt_strength: 0.8
                num_inference_steps: 25
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
              examples:
                '1':
                  summary: Create image
                  value:
                    created: 1589478378
                    data:
                      - url: https://...
                      - url: https://...
                '2':
                  summary: Successful examples
                  value:
                    id: w44zs9cet5rmc0cqzp49gpkhf8
                    model: black-forest-labs/flux-kontext-dev
                    version: hidden
                    input:
                      aspect_ratio: match_input_image
                      input_image: >-
                        https://replicate.delivery/xezq/XfwWjHJ7HfrmXE6ukuLVEpXWfeQ3PQeRI5mApuLXRxST7XMmC/tmpc91tlq20.png
                      output_format: jpg
                      prompt: Make the letters 3D, floating in space on a city street
                      prompt_upsampling: false
                      safety_tolerance: 2
                    logs: ''
                    output: null
                    data_removed: false
                    error: null
                    status: starting
                    created_at: '2025-07-12T07:27:54.577Z'
                    urls:
                      cancel: >-
                        https://api.replicate.com/v1/predictions/w44zs9cet5rmc0cqzp49gpkhf8/cancel
                      get: >-
                        https://api.replicate.com/v1/predictions/w44zs9cet5rmc0cqzp49gpkhf8
                      stream: >-
                        https://stream.replicate.com/v1/files/bcwr-h7bu76ujftxzwih5u35puoysogps56mqvpvjz4nrxskhfe7ks42a
                      web: https://replicate.com/p/w44zs9cet5rmc0cqzp49gpkhf8
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326401454-run
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
