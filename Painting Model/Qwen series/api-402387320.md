# z-image-turbo

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/images/generations:
    post:
      summary: z-image-turbo
      deprecated: false
      description: ""
      tags:
        - Painting Models / Qwen Series
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                  description: Model Name
                prompt:
                  type: string
                  description: Image description
                size:
                  type: string
                  description: Image size
                "n":
                  type: integer
                  description: Only one image can be generated.
                watermark:
                  type: boolean
                  description: Is it watermarked?
                prompt_extend:
                  type: boolean
                  description: AI-optimized suggestion words
              required:
                - model
                - prompt
                - size
                - "n"
                - watermark
                - prompt_extend
              x-apifox-orders:
                - model
                - prompt
                - size
                - "n"
                - watermark
                - prompt_extend
            example:
              model: z-image-turbo
              prompt: An elegant and dignified couplet hangs in the hall, and the room is decorated in a quiet, classic Chinese style.
              size: 1280x720
              "n": 1
              watermark: false
              prompt_extend: true
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  created:
                    type: integer
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                        b64_json:
                          type: string
                      x-apifox-orders:
                        - url
                        - b64_json
                required:
                  - created
                  - data
                x-apifox-orders:
                  - created
                  - data
              example:
                created: 1767842675
                data:
                  - url: >-
                      https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/...
                    b64_json: ""
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Painting Models / Qwen Series
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-402387320-run
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
