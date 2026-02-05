# Create task black-forest-labs/flux-kontext-pro

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/black-forest-labs/flux-kontext-pro/predictions:
    post:
      summary: Create task black-forest-labs/flux-kontext-pro
      deprecated: false
      description: 'Official documentation: https://replicate.com/black-forest-labs/flux-kontext-pro'
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
                    prompt:
                      type: string
                      description: A text description of what you want to generate, or instructions on how to edit a given image.
                    input_image:
                      type: string
                      description: Image used for reference. Must be in JPEG, PNG, GIF, or WebP format.
                    aspect_ratio:
                      type: string
                      description: >-
                        Generates the aspect ratio of the image. Uses "match_input_image" to match the aspect ratio of the input image. Default: "match_input_image", supports 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 4:5, 5:4, 21:9, 9:21, 2:1, 1:2.
                    output_format:
                      type: string
                      description: The output format for the generated image. Default: "png".
                    safety_tolerance:
                      type: integer
                      description: Safety tolerance: 0 is the strictest, 6 is the most lenient. 2 is the maximum allowed value when using the input image. Default: 2
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
                prompt: Make this a 90s cartoon
                input_image: >-
                  https://replicate.delivery/pbxt/N55l5TWGh8mSlNzW8usReoaNhGbFwvLeZR3TX1NL4pd2Wtfv/replicate-prediction-f2d25rg6gnrma0cq257vdw2n4c.png
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
                      - prompt
                    x-apifox-orders:
                      - aspect_ratio
                      - input_image
                      - output_format
                      - prompt
                      - prompt_upsampling
                      - safety_tolerance
                required:
                  - input
                x-apifox-orders:
                  - input
              examples:
                '1':
                  summary: Successful examples
                  value:
                    id: b1qw7g8h9xrma0crakst3xbj8m
                    model: black-forest-labs/flux-kontext-pro
                    version: hidden
                    input:
                      aspect_ratio: match_input_image
                      input_image: >-
                        https://replicate.delivery/pbxt/N55l5TWGh8mSlNzW8usReoaNhGbFwvLeZR3TX1NL4pd2Wtfv/replicate-prediction-f2d25rg6gnrma0cq257vdw2n4c.png
                      output_format: jpg
                      prompt: Make this a 90s cartoon
                      prompt_upsampling: false
                      safety_tolerance: 2
                    logs: ''
                    output: null
                    data_removed: false
                    error: null
                    status: starting
                    created_at: '2025-07-29T06:51:12.591Z'
                    urls:
                      cancel: >-
                        https://api.replicate.com/v1/predictions/b1qw7g8h9xrma0crakst3xbj8m/cancel
                      get: >-
                        https://api.replicate.com/v1/predictions/b1qw7g8h9xrma0crakst3xbj8m
                      stream: >-
                        https://stream.replicate.com/v1/files/bcwr-3g5lstbmjxzikqt225npeguwi4bu47ndhirdgete5npgzzzogkpq
                      web: https://replicate.com/p/b1qw7g8h9xrma0crakst3xbj8m
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326937091-run
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
