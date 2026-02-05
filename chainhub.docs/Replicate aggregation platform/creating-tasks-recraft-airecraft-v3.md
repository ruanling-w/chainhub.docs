# Create a quest recraft-ai/recraft-v3

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/recraft-ai/recraft-v3/predictions:
    post:
      summary: Create task recraft-ai/recraft-v3
      deprecated: false
      description: Official documentation: https://replicate.com/recraft-ai/recraft-v3
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
                    size:
                      type: string
                      description: The width and height of the generated image. If an aspect ratio is set, the dimensions are ignored. Default: "1024x1024"
                    style:
                      type: string
                      description: The style of the generated image. Default: "any"
                    prompt:
                      type: string
                      description: Text prompts generated from images.
                    aspect_ratio:
                      type: string
                      description: The aspect ratio of the generated image. Default: "Not set"
                  required:
                    - prompt
                  x-apifox-orders:
                    - size
                    - style
                    - prompt
                    - aspect_ratio
              x-apifox-orders:
                - input
            example:
              input:
                size: 1365x1024
                style: any
                prompt: >-
                  a wildlife photography photo of a red panda using a laptop in
                  a snowy forest
                aspect_ratio: Not set
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
                id: w5k77rccg1rma0crb40tssh86g
                model: recraft-ai/recraft-v3
                version: hidden
                input:
                  aspect_ratio: Not set
                  prompt: >-
                    a wildlife photography photo of a red panda using a laptop
                    in a snowy forest
                  size: 1365x1024
                  style: any
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T01:45:30.496Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/w5k77rccg1rma0crb40tssh86g/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/w5k77rccg1rma0crb40tssh86g
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-otkjt5aiey7d63eore5rhoezsvrxwsc5q6ow2x5lpqh3l6x33hgq
                  web: https://replicate.com/p/w5k77rccg1rma0crb40tssh86g
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326489482-run
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
