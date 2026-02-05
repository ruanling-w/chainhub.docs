# sound effects

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/audio/text-to-audio:
    post:
      summary: sound effects
      deprecated: false
      description: ""
      tags:
        - Kling platform/Audio
      parameters:
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
              properties:
                prompt:
                  type: string
                  description: Text prompts
                duration:
                  type: string
                  description: The duration of the generated audio can range from 3.0 seconds to 10.0 seconds, supporting one decimal place precision.
                external_task_id:
                  type: string
                callback_url:
                  type: string
              required:
                - prompt
                - duration
              x-apifox-orders:
                - prompt
                - duration
                - external_task_id
                - callback_url
            example:
              prompt: Audio describing the scenery
              duration: 5
              external_task_id: ""
              callback_url: ""
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
      x-apifox-folder: Kling platform/Audio
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386322140-run
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
