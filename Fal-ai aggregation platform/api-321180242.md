# 获取请求结果

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /fal-ai/{model_name}/requests/{request_id}:
    get:
      summary: Get the request result
      deprecated: false
      description: ""
      tags:
        - Fal-ai aggregation platform
      parameters:
        - name: model_name
          in: path
          description: Model name, auto. Our system will automatically determine model_name.
          required: true
          example: auto
          schema:
            type: string
        - name: request_id
          in: path
          description: Task ID
          required: true
          example: 5ed6b6bb-eaa3-4006-859b-e2f3fa748d8c
          schema:
            type: string
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apifox-orders: []
              example:
                seed: 2841475369
                images:
                  - url: >-
                      https://fal.media/files/tiger/BwdOcvXOx0UmkCyCMZGmZ_1ee10db761e146a28fdaadafa528d239.jpg
                    width: 1024
                    height: 1024
                    content_type: image/jpeg
                prompt: Put the little duckling on top of the woman's t-shirt.
                request:
                  prompt: Put the little duckling on top of the woman's t-shirt.
                  image_urls:
                    - >-
                      https://v3.fal.media/files/penguin/XoW0qavfF-ahg-jX4BMyL_image.webp
                    - >-
                      https://v3.fal.media/files/tiger/bml6YA7DWJXOigadvxk75_image.webp
                  num_images: 1
                  output_format: jpeg
                  guidance_scale: 3.5
                  safety_tolerance: "2"
                timings: {}
                has_nsfw_concepts:
                  - false
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-321180242-run
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
