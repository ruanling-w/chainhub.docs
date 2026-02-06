# /fal-ai/kling-video/v2.5-turbo/pro/text-to-video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /fal-ai/kling-video/v2.5-turbo/pro/text-to-video:
    post:
      summary: /fal-ai/kling-video/v2.5-turbo/pro/text-to-video
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
              prompt: >-
                A noble lord walks among his people, his presence a comforting
                reassurance. He greets them with a gentle smile, embodying their
                hopes and earning their respect through simple interactions. The
                atmosphere is intimate and sincere, highlighting the bond
                between the leader and community.
              duration: "5"
              aspect_ratio: "16:9"
              negative_prompt: blur, distort, and low quality
              cfg_scale: 0.5
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-355902046-run
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
