# /fal-ai/qwen-image-edit-lora

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /fal-ai/qwen-image-edit-lora:
    post:
      summary: /fal-ai/qwen-image-edit-lora
      deprecated: false
      description: ""
      tags:
        - Fal-ai aggregation platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
            example:
              prompt: Change bag to apple macbook
              num_inference_steps: 30
              guidance_scale: 4
              num_images: 1
              enable_safety_checker: true
              output_format: png
              image_url: >-
                http://e.hiphotos.baidu.com/image/pic/item/a1ec08fa513d2697e542494057fbb2fb4316d81e.jpg
              negative_prompt: blurry, ugly
              acceleration: regular
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-355971008-run
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
