# Get the request result

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
      summary: "Get the request result "
      deprecated: false
      description: ""
      tags:
        - Painting Model / Fal.ai Platform
      parameters:
        - name: model_name
          in: path
          description: Model Name
          required: true
          example: auto
          schema:
            type: string
        - name: request_id
          in: path
          description: Task ID
          required: true
          example: acf05732-7cb3-445b-9f39-fdaeccb1d730
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
      security: []
      x-apifox-folder: Painting Model / Fal.ai Platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-343816375-run
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
