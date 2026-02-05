# Create task black-forest-labs/flux-fill-pro

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/black-forest-labs/flux-fill-pro/predictions:
    post:
      summary: Create task black-forest-labs/flux-fill-pro
      deprecated: false
      description: Official documentation:https://replicate.com/black-forest-labs/flux-fill-pro
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
                      description: >-
                        A black and white image to describe the parts of the image that need repair. Black areas will be preserved, and white areas will be repaired. Must be the same size as the original image. This parameter is optional if you provided an alpha mask in the original image. Must be in jpeg, png, gif, or webp format.
                    image:
                      type: string
                      description: The image to be repaired. It may contain an alpha mask. It must be in jpeg, png, gif, or webp format.
                    steps:
                      type: integer
                      description: Number of diffusion steps. A higher value results in finer detail, but also longer processing time. Default: 50. Minimum: 15, Maximum: 50.
                    prompt:
                      type: string
                      description: Text prompts generated from images.
                    guidance:
                      type: integer
                      description: >-
                        Controls the balance between textual cues adherence and image quality/variety. Higher values ​​result in outputs that more closely resemble the cues, but may reduce overall image quality. Lower values ​​offer greater creative freedom in the output, but may result in lower relevance to the cues. Default: 60. Minimum: 1.5, Maximum: 100.
                    outpaint:
                      type: string
                      description: Options for quick repair of the input image. The mask will be ignored. Default: "None"
                    output_format:
                      type: string
                      description: description: The format of the output image. Default: "jpg".
                    safety_tolerance:
                      type: integer
                      description: Safety tolerance: 1 indicates the strictest tolerance, and 6 indicates the most lenient tolerance. Default: 2.
                    prompt_upsampling:
                      type: boolean
                      description: Automatically modify suggestions to generate more creative ideas. Default: false
                  required:
                    - image
                    - prompt
                  x-apifox-orders:
                    - mask
                    - image
                    - steps
                    - prompt
                    - guidance
                    - outpaint
                    - output_format
                    - safety_tolerance
                    - prompt_upsampling
              x-apifox-orders:
                - input
            example:
              input:
                mask: >-
                  https://replicate.delivery/pbxt/M0gpLCYdCLbnhcz95Poy66q30XW9VSCN65DoDQ8IzdzlQonw/kill-bill-mask.png
                image: >-
                  https://replicate.delivery/pbxt/M0gpKVE9wmEtOQFNDOpwz1uGs0u6nK2NcE85IihwlN0ZEnMF/kill-bill-poster.jpg
                steps: 50
                prompt: movie poster says "FLUX FILL"
                guidance: 60
                outpaint: None
                output_format: jpg
                safety_tolerance: 2
                prompt_upsampling: false
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
                id: w72vtvbb79rmc0crb57tckqt24
                model: black-forest-labs/flux-fill-pro
                version: hidden
                input:
                  guidance: 60
                  image: >-
                    https://replicate.delivery/pbxt/M0gpKVE9wmEtOQFNDOpwz1uGs0u6nK2NcE85IihwlN0ZEnMF/kill-bill-poster.jpg
                  mask: >-
                    https://replicate.delivery/pbxt/M0gpLCYdCLbnhcz95Poy66q30XW9VSCN65DoDQ8IzdzlQonw/kill-bill-mask.png
                  outpaint: None
                  output_format: jpg
                  prompt: movie poster says "FLUX FILL"
                  prompt_upsampling: false
                  safety_tolerance: 2
                  steps: 50
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T03:10:33.786Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/w72vtvbb79rmc0crb57tckqt24/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/w72vtvbb79rmc0crb57tckqt24
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-3y7tn6jo35hzo7xvk5kf2dslvdwmggf5zty5vnbfhq4tsggfhesa
                  web: https://replicate.com/p/w72vtvbb79rmc0crb57tckqt24
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327043723-run
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
