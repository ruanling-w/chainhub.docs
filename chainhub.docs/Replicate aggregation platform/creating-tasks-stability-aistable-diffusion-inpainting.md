# Create task stability-ai/stable-diffusion-inpainting

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
      summary: Create task stability-ai/stable-diffusion-inpainting
      deprecated: false
      description: 'Official documentation: https://replicate.com/stability-ai/stable-diffusion-inpainting'
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
                    mask:
                      type: string
                      description: A black and white image is used as a mask to repair the provided image. White pixels will be repaired, while black pixels will be preserved.
                    image:
                      type: string
                      description: The initial image used to generate the variant. It will be resized to height x width.
                    width:
                      type: integer
                      description: Width of the generated image (in pixels). Must be a multiple of 64. Default: 512.
                    height:
                      type: integer
                      description: The height of the generated image (in pixels). Must be a multiple of 64. Default: 512.
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
                    - mask
                    - image
                  x-apifox-orders:
                    - mask
                    - image
                    - width
                    - height
                    - prompt
                    - scheduler
                    - num_outputs
                    - guidance_scale
                    - num_inference_steps
              x-apifox-orders:
                - input
            example:
              version: >-
                stability-ai/stable-diffusion-inpainting:95b7223104132402a9ae91cc677285bc5eb997834bd2349fa486f53910fd68b3
              input:
                mask: >-
                  https://replicate.delivery/pbxt/HtGQBqO9MtVbPm0G0K43nsvvjBB0E0PaWOhuNRrRBBT4ttbf/mask.png
                image: >-
                  https://replicate.delivery/pbxt/HtGQBfA5TrqFYZBf0UL18NTqHrzt8UiSIsAkUuMHtjvFDO6p/overture-creations-5sI6fQgYIuo.png
                width: 512
                height: 512
                prompt: Face of a yellow cat, high resolution, sitting on a park bench
                scheduler: DPMSolverMultistep
                num_outputs: 1
                guidance_scale: 7.5
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326402431-run
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
