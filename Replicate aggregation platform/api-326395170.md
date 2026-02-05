# Create a task black-forest-labs/flux-kontext-dev

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/black-forest-labs/flux-kontext-dev/predictions:
    post:
      summary: Create task black-forest-labs/flux-kontext-dev
      deprecated: false
      description: 'Official documentation: https://replicate.com/black-forest-labs/flux-kontext-dev'
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
                    go_fast:
                      type: boolean
                      description: Makes the model run faster; output quality may decrease slightly for more difficult hints. Default: true.
                    guidance:
                      type: number
                      description: 'Intensity of prompt words. Default: 2.5. Minimum: 0, Maximum: 10'
                    input_image:
                      type: string
                      description: Image used for reference. Must be in JPEG, PNG, GIF, or WebP format.
                    aspect_ratio:
                      type: string
                      description: >-
                        Generates the aspect ratio of the image. Uses "match_input_image" to match the aspect ratio of the input image. Default value: "match_input_image".
                    output_format:
                      type: string
                      description: Output image format. Default value: "webp".
                    output_quality:
                      type: integer
                      description: >-
                        The quality when saving the output image, ranging from 0 to 100. 100 is the best quality, 0 is the lowest quality. Not applicable to .png output. Default: 80. Minimum: 0, Maximum: 100.
                    num_inference_steps:
                      type: integer
                      description: Number of inference steps, default value: 28. Minimum value: 4, maximum value: 50.
                  required:
                    - prompt
                    - input_image
                  x-apifox-orders:
                    - prompt
                    - go_fast
                    - guidance
                    - input_image
                    - aspect_ratio
                    - output_format
                    - output_quality
                    - num_inference_steps
              x-apifox-orders:
                - input
            example:
              input:
                prompt: Change the car color to red, turn the headlights on
                go_fast: true
                guidance: 2.5
                input_image: >-
                  https://replicate.delivery/pbxt/N5YURZv4ifaW2bMwU7hmrwzgtxf99DTQXpBeobLt1O7dEc3h/pexels-jmark-253096.jpg
                aspect_ratio: match_input_image
                output_format: jpg
                output_quality: 80
                num_inference_steps: 30
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
                      - input_image
                      - prompt
                    x-apifox-orders:
                      - aspect_ratio
                      - input_image
                      - output_format
                      - prompt
                      - prompt_upsampling
                      - safety_tolerance
                x-apifox-orders:
                  - id
                  - model
                  - version
                  - input
              example:
                id: tpdf40dypdrma0cram394vvzkg
                model: black-forest-labs/flux-kontext-dev
                version: hidden
                input:
                  aspect_ratio: match_input_image
                  go_fast: true
                  guidance: 2.5
                  input_image: >-
                    https://replicate.delivery/pbxt/N5YURZv4ifaW2bMwU7hmrwzgtxf99DTQXpBeobLt1O7dEc3h/pexels-jmark-253096.jpg
                  num_inference_steps: 30
                  output_format: jpg
                  output_quality: 80
                  prompt: Change the car color to red, turn the headlights on
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-29T07:12:42.163Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/tpdf40dypdrma0cram394vvzkg/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/tpdf40dypdrma0cram394vvzkg
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-6rywfvqq3376h7243k7xrgtnkaqpwiogzgh7kcehtx7kz3nre6fq
                  web: https://replicate.com/p/tpdf40dypdrma0cram394vvzkg
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326395170-run
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
