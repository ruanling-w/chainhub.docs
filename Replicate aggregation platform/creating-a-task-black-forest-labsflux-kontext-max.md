# Create task black-forest-labs/flux-kontext-max

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/black-forest-labs/flux-kontext-max/predictions:
    post:
      summary: Create task black-forest-labs/flux-kontext-max
      deprecated: false
      description: 'Official documentation: https://replicate.com/black-forest-labs/flux-kontext-max'
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
                      description: A text description of what you want to generate, or instructions on how to edit a given image.
                    input_image:
                      type: string
                      description: Image used for reference. Must be in JPEG, PNG, GIF, or WebP format.
                    aspect_ratio:
                      type: string
                      description: >-
                        Generates the aspect ratio of the image. Uses "match_input_image" to match the aspect ratio of the input image. Default: "match_input_image".
                    output_format:
                      type: string
                      description: The output format for the generated image. Default: "png".
                    safety_tolerance:
                      type: integer
                      description: Safety tolerance: 0 is the strictest, 6 is the most lenient. 2 is the maximum allowed value when using the input image. Default: 2. Minimum: 0, Maximum: 6.
                    prompt_upsampling:
                      type: boolean
                      description: Improved auto-suggestion. Default: false.
                  required:
                    - prompt
                  x-apifox-orders:
                    - prompt
                    - input_image
                    - aspect_ratio
                    - output_format
                    - safety_tolerance
                    - prompt_upsampling
              x-apifox-orders:
                - input
            example:
              input:
                prompt: Make the letters 3D, floating in space on a city street
                input_image: >-
                  https://replicate.delivery/xezq/XfwWjHJ7HfrmXE6ukuLVEpXWfeQ3PQeRI5mApuLXRxST7XMmC/tmpc91tlq20.png
                aspect_ratio: match_input_image
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
                id: 5pcmjq6sfnrmc0cram79p95eg4
                model: black-forest-labs/flux-kontext-max
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
                created_at: '2025-07-29T07:21:33.309Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/5pcmjq6sfnrmc0cram79p95eg4/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/5pcmjq6sfnrmc0cram79p95eg4
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-o4bl6hrud4sg7ceoi45imkh7lq32nbyqvnsyg736v7ghpxwqxheq
                  web: https://replicate.com/p/5pcmjq6sfnrmc0cram79p95eg4
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326937190-run
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
