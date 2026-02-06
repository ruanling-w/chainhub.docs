# Batch retrieval tasks

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/fetch:
    post:
      summary: Batch retrieval tasks
      deprecated: false
      description: ""
      tags:
        - Music Suno/Query Interface
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ""
          required: true
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
              properties:
                clip_id:
                  description: |+
                    Song ID after extend
                  type: string
                is_infill:
                  type: string
              required:
                - clip_id
                - is_infill
              x-apifox-orders:
                - clip_id
                - is_infill
            example:
              ids:
                - b4914cbe-f738-4813-8ac9-4194ae362bed
                - ccb61d4a-701d-4ef2-b23c-c3ff950fc3b5
                - 276677a3-bd50-4388-83c9-39ce18f7041f
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                  data:
                    type: string
                  message:
                    type: string
                required:
                  - code
                  - data
                  - message
              example:
                code: success
                data: 47443cc1-4902-42ae-ae7f-72a9900544e9
                message: ""
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno/Query Interface
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-248984125-run
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
