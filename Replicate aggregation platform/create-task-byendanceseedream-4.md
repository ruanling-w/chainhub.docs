# Create task bytedance/seedream-4

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /replicate/v1/models/bytedance/seedream-4/predictions:
    post:
      summary: Create task bytedance/seedream-4
      deprecated: false
      description: ""
      tags:
        - Replicate aggregation platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
            example:
              input:
                size: 2K
                width: 2048
                height: 2048
                prompt: >-
                  a photo of a store front called i"sedream 4", it sells books,
                  a poster in the window says i"sedream 4 now on Replicate!"
                max_images: 2
                image_input: []
                aspect_ratio: "4:3"
                sequential_image_generation: auto
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
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-356491310-run
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
