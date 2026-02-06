# 创建任务 stability-ai/stable-diffusion

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
      summary: Create task stability-ai/stable-diffusion
      deprecated: false
      description: 'Official documentation: https://replicate.com/stability-ai/stable-diffusion'
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
                    width:
                      type: integer
                      description: Width of the generated image (in pixels). Must be a multiple of 64. Default: 768.
                    height:
                      type: integer
                      description: The height of the generated image (in pixels). Must be a multiple of 64. Default: 768.
                    prompt:
                      type: string
                      description: Input prompt.
                    scheduler:
                      type: string
                      description: Select a scheduler. Default: "DPMSolverMultistep".
                    num_outputs:
                      type: integer
                      description: Number of images to generate. Default: 1. Minimum: 1, Maximum: 4.
                    guidance_scale:
                      type: number
                      description: No classifier-guided scale. Default: 7.5. Minimum: 1, Maximum: 20.
                    num_inference_steps:
                      type: integer
                      description: Number of denoising steps. Default: 50. Minimum: 1, Maximum: 500.
                  required:
                    - guidance_scale
                    - num_inference_steps
                  x-apifox-orders:
                    - width
                    - height
                    - prompt
                    - scheduler
                    - num_outputs
                    - guidance_scale
                    - num_inference_steps
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4
              input:
                width: 768
                height: 768
                prompt: an astronaut riding a horse on mars, hd, dramatic lighting
                scheduler: K_EULER
                num_outputs: 1
                guidance_scale: 7.5
                num_inference_steps: 50
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
                created: 1589478378
                data:
                  - url: https://...
                  - url: https://...
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326398523-run
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
