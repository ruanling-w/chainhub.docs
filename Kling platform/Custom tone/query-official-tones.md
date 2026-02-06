# Search official sound

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/general/presets-voices:
    get:
      summary: Search official sound
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Custom Tones
      parameters:
        - name: pageNum
          in: query
          description: ""
          required: false
          example: 1
          schema:
            type: integer
        - name: pageSize
          in: query
          description: ""
          required: false
          example: 30
          schema:
            type: integer
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
            examples: {}
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
      x-apifox-folder: Kling Platform/Custom Tones
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-405419408-run
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
