# Create task flux-kontext-apps/multi-image-kontext-max

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/flux-kontext-apps/multi-image-kontext-max/predictions:
    post:
      summary: Create task flux-kontext-apps/multi-image-kontext-max
      deprecated: false
      description: Official documentation:https://replicate.com/flux-kontext-apps/multi-image-kontext-max
      tags:
        - Replicate 聚合平台
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
                    prompt:
                      type: string
                      description: A textual description of how to combine or transform two input images.
                    aspect_ratio:
                      type: string
                      description: >-
                        Generates the aspect ratio of the input image. Uses "match_input_image" to match the aspect ratio of the input image. Default: "match_input_image"
                    input_image_1:
                      type: string
                      description: The first input image. It must be in jpeg, png, gif, or webp format.
                    input_image_2:
                      type: string
                      description: The second input image. It must be in jpeg, png, gif, or webp format.
                    output_format:
                      type: string
                      description: The output format for the generated image. Default: "png".
                    safety_tolerance:
                      type: integer
                      description: Safety tolerance: 0 indicates the strictest tolerance, and 2 indicates the most lenient tolerance. 2 is the currently allowed maximum. Default: 2.
                  required:
                    - prompt
                    - input_image_1
                    - input_image_2
                  x-apifox-orders:
                    - prompt
                    - aspect_ratio
                    - input_image_1
                    - input_image_2
                    - output_format
                    - safety_tolerance
              x-apifox-orders:
                - input
            example:
              input:
                prompt: Put the woman into a white t-shirt with the text on it
                aspect_ratio: '1:1'
                input_image_1: >-
                  https://replicate.delivery/pbxt/N5rSeJrCafWpmJuLb62moY8pSMEpSBBwSf7N6hxyIn4fNYMa/w8msa88d01rm80cq3hzsqrdehg.png
                input_image_2: >-
                  https://replicate.delivery/pbxt/N5rSdTCgBqIRvbkedcfLfS5xTSEEOqMtX9FsR1hLK9JYryml/0_1.webp
                output_format: png
                safety_tolerance: 2
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
                      input_image_1:
                        type: string
                      input_image_2:
                        type: string
                      output_format:
                        type: string
                      prompt:
                        type: string
                      safety_tolerance:
                        type: integer
                    required:
                      - aspect_ratio
                      - input_image_1
                      - input_image_2
                      - output_format
                      - prompt
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
                id: b6k38vmb01rme0crb4bbr2apw4
                model: flux-kontext-apps/multi-image-kontext-max
                version: hidden
                input:
                  aspect_ratio: '1:1'
                  input_image_1: >-
                    https://replicate.delivery/pbxt/N5rSeJrCafWpmJuLb62moY8pSMEpSBBwSf7N6hxyIn4fNYMa/w8msa88d01rm80cq3hzsqrdehg.png
                  input_image_2: >-
                    https://replicate.delivery/pbxt/N5rSdTCgBqIRvbkedcfLfS5xTSEEOqMtX9FsR1hLK9JYryml/0_1.webp
                  output_format: png
                  prompt: Put the woman into a white t-shirt with the text on it
                  safety_tolerance: 2
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T02:08:26.368Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/b6k38vmb01rme0crb4bbr2apw4/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/b6k38vmb01rme0crb4bbr2apw4
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-4lncowbqyyr5toyxguv6tr47ffpade3muguvemzik5let3hnlryq
                  web: https://replicate.com/p/b6k38vmb01rme0crb4bbr2apw4
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327029322-run
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
