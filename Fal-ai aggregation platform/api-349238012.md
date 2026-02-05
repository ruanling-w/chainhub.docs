# /fal-ai/bytedance/seedream/v4/text-to-image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /fal-ai/bytedance/seedream/v4/text-to-image:
    post:
      summary: /fal-ai/bytedance/seedream/v4/text-to-image
      deprecated: false
      description: "Official documentation: https://fal.ai/models/fal-ai/bytedance/seedream/v4/text-to-image"
      tags:
        - Fal-ai aggregation platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
              x-apifox-orders: []
            example:
              prompt: >-
                Draw a chart showing the typical vegetation distribution in four
                different climate zones: tropical rainforest, temperate forest,
                desert, and tundra.
              image_size:
                height: 1280
                width: 1280
              num_images: 1
              enable_safety_checker: true
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
                status: IN_QUEUE
                request_id: acf05732-7cb3-445b-9f39-fdaeccb1d730
                response_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/acf05732-7cb3-445b-9f39-fdaeccb1d730
                status_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/acf05732-7cb3-445b-9f39-fdaeccb1d730/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/flux-pro/requests/acf05732-7cb3-445b-9f39-fdaeccb1d730/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-349238012-run
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
