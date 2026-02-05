# Create task ideogram-ai/ideogram-v2-turbo

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/ideogram-ai/ideogram-v2-turbo/predictions:
    post:
      summary: Create task ideogram-ai/ideogram-v2-turbo
      deprecated: false
      description: Official documentation:https://replicate.com/ideogram-ai/ideogram-v2-turbo
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
                      description: Text prompts generated from images.
                    resolution:
                      type: string
                      description: Resolution. Aspect ratio of the image to be covered. This parameter is ignored if a retouched image is specified. Default: "None".
                    style_type:
                      type: string
                      description: Styles help define the specific aesthetic you want to create in the image. Default: "None".
                    aspect_ratio:
                      type: string
                      description: Aspect ratio. Ignored if a resolution is specified or the image is retouched. Default: "1:1".
                    magic_prompt_option:
                      type: string
                      description: >-
                        Magic Prompt
                        Interprets and optimizes your prompts to maximize the diversity and quality of the generated images. You can also use it to write prompts in different languages. Default: "Auto".
                  required:
                    - prompt
                  x-apifox-orders:
                    - prompt
                    - resolution
                    - style_type
                    - aspect_ratio
                    - magic_prompt_option
              x-apifox-orders:
                - input
            example:
              input:
                prompt: >-
                  An illustration of a gold running shoe with the text "Run AI
                  with an API" written on the shoe. The shoe is placed on a pink
                  background. The text is white and bold. The overall image has
                  a modern and techy vibe, with elements of speed.
                resolution: None
                style_type: None
                aspect_ratio: '1:1'
                magic_prompt_option: Auto
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
                id: 2jycc2v9nnrmc0crap5tv5zaxr
                model: ideogram-ai/ideogram-v2-turbo
                version: hidden
                input:
                  aspect_ratio: '1:1'
                  magic_prompt_option: Auto
                  prompt: >-
                    An illustration of a gold running shoe with the text "Run AI
                    with an API" written on the shoe. The shoe is placed on a
                    pink background. The text is white and bold. The overall
                    image has a modern and techy vibe, with elements of speed.
                  resolution: None
                  style_type: None
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-29T09:37:36.685Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/2jycc2v9nnrmc0crap5tv5zaxr/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/2jycc2v9nnrmc0crap5tv5zaxr
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-irvir7a5lzv2z6pja5hol5cy36lt5jekok743kcmbfu4gtvpv7vq
                  web: https://replicate.com/p/2jycc2v9nnrmc0crap5tv5zaxr
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326492658-run
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
