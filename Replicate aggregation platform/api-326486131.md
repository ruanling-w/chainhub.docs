# Create task cjwbw/rembg

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /replicate/v1/predictions:
    post:
      summary: Create task cjwbw/rembg
      deprecated: false
      description: Official documentation:https://replicate.com/cjwbw/rembg
      tags:
        - Replicate aggregation platform
      parameters:
        - name: Authorization
          in: header
          description: ""
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
                version:
                  type: string
                input:
                  type: object
                  properties:
                    image:
                      type: string
                  x-apifox-orders:
                    - image
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                cjwbw/rembg:fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003
              input:
                image: >-
                  https://replicate.delivery/pbxt/Ho28olmw8dnOffOz7yjuPK6UGsOPqFUfpCnq1ur8zaAKxiPH/animal-1.jpeg
      responses:
        "200":
          description: ""
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
                    type: "null"
                  data_removed:
                    type: boolean
                  error:
                    type: "null"
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
                "1":
                  summary: Create image
                  value:
                    created: 1589478378
                    data:
                      - url: https://...
                      - url: https://...
                "2":
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
                    logs: ""
                    output: null
                    data_removed: false
                    error: null
                    status: starting
                    created_at: "2025-07-12T07:27:54.577Z"
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326486131-run
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
