# Query task (single)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/motion-control/{id}:
    get:
      summary: Query task (single)
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Motion Control
      parameters:
        - name: id
          in: path
          description: ""
          required: true
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ""
          required: false
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
          required: false
          example: Bearer {{YOUR_API_KEY}}
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
      x-apifox-folder: Kling Platform/Motion Control
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-398908063-run
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
