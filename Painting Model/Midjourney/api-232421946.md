# Submit Modal

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /mj/submit/modal:
    post:
      summary: Submit Modal
      deprecated: false
      description: ""
      tags:
        - Painting Model/Midjourney
      parameters:
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
              properties:
                maskBase64:
                  type: string
                  description: |+
                    Partially redrawn mask base64

                prompt:
                  type: string
                  description: |
                    Prompt words
                taskId:
                  type: integer
                  description: |
                    Task ID
              required:
                - maskBase64
              x-apifox-orders:
                - maskBase64
                - prompt
                - taskId
            example:
              maskBase64: ""
              prompt: ""
              taskId: "14001934816969359"
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
                      required:
                        - url
                      x-apifox-orders:
                        - url
                required:
                  - created
                  - data
                x-apifox-orders:
                  - created
                  - data
              example:
                created: 1589478378
                data:
                  - url: https://...
                  - url: https://...
          headers: {}
          x-apifox-name: Create image
      security:
        - bearer: []
      x-apifox-folder: Painting Model/Midjourney
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421946-run
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
