# Create task minimax/video-01-live

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/minimax/video-01-live/predictions:
    post:
      summary: Create task minimax/video-01-live
      deprecated: false
      description: Official documentation:https://replicate.com/minimax/video-01-live
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
                      description: Generate text prompts.
                    prompt_optimizer:
                      type: boolean
                      description: Use the hint optimizer. Default: true
                    first_frame_image:
                      type: string
                      description: The first frame image used to generate the video. The output video will have the same aspect ratio as this image.
                  required:
                    - prompt
                    - first_frame_image
                  x-apifox-orders:
                    - prompt
                    - prompt_optimizer
                    - first_frame_image
              x-apifox-orders:
                - input
            example:
              input:
                prompt: a man is talking angrily
                prompt_optimizer: true
                first_frame_image: >-
                  https://replicate.delivery/pbxt/M9jlcXgeaypBr2yQYGf9JXgxUCJWRt8ODUDvt90UWPUsQBXC/back-to-the-future.png
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
                id: x18c1re8mxrma0crb3x8wbwqmg
                model: minimax/video-01-live
                version: hidden
                input:
                  first_frame_image: >-
                    https://replicate.delivery/pbxt/M9jlcXgeaypBr2yQYGf9JXgxUCJWRt8ODUDvt90UWPUsQBXC/back-to-the-future.png
                  prompt: a man is talking angrily
                  prompt_optimizer: true
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T01:38:07.143Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/x18c1re8mxrma0crb3x8wbwqmg/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/x18c1re8mxrma0crb3x8wbwqmg
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-tfjtzspnxcjigf5eyyqqfkc3rrtv7ruou6yxzspuiy2cdzi7gizq
                  web: https://replicate.com/p/x18c1re8mxrma0crb3x8wbwqmg
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326486964-run
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
