# Create task minimax/video-01

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/minimax/video-01/predictions:
    post:
      summary: Create task minimax/video-01
      deprecated: false
      description: Official documentation:https://replicate.com/minimax/video-01
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
                  required:
                    - prompt
                  x-apifox-orders:
                    - prompt
                    - prompt_optimizer
              x-apifox-orders:
                - input
            example:
              input:
                prompt: >-
                  a woman is walking through a busy Tokyo street at night, she
                  is wearing dark sunglasses
                prompt_optimizer: true
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
                      prompt:
                        type: string
                      prompt_optimizer:
                        type: boolean
                    required:
                      - prompt
                      - prompt_optimizer
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
                id: ree8dymk95rmc0crb3yt2pqhr4
                model: minimax/video-01
                version: hidden
                input:
                  prompt: >-
                    a woman is walking through a busy Tokyo street at night, she
                    is wearing dark sunglasses
                  prompt_optimizer: true
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T01:41:10.089Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/ree8dymk95rmc0crb3yt2pqhr4/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/ree8dymk95rmc0crb3yt2pqhr4
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-wykptlq2o5ws5ukylao2u654xfxv6aaaekgxijlr7aibzkftt7bq
                  web: https://replicate.com/p/ree8dymk95rmc0crb3yt2pqhr4
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326487974-run
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
