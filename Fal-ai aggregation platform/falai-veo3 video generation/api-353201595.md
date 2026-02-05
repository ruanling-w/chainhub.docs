# /fal-ai/veo3/requests/{request\_id}

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /fal-ai/veo3/requests/{request_id}:
    get:
      summary: /fal-ai/veo3/requests/{request_id}
      deprecated: false
      description: ""
      tags:
        - Fal-ai aggregation platform/falai-veo3 video generation
      parameters:
        - name: request_id
          in: path
          description: ""
          required: true
          example: 46d69eca-9cf3-475b-974d-8e8fc405cd67
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
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform/falai-veo3 video generation
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-353201595-run
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
