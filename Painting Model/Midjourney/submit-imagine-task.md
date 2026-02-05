# Submit Imagine task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /mj/submit/imagine:
    post:
      summary: Submit Imagine task
      deprecated: false
      description: >-
        Official documentation：https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics
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
                botType:
                  type: string
                  description: bot type, mj (default) or niji
                  enum:
                    - MID_JOURNEY
                    - NIJI_JOURNEY
                  x-apifox-enum:
                    - value: MID_JOURNEY
                      name: ""
                      description: ""
                    - value: NIJI_JOURNEY
                      name: ""
                      description: ""
                  examples:
                    - MID_JOURNEY
                prompt:
                  type: string
                  description: Prompt words
                  examples:
                    - Cat
                notifyHook:
                  type: string
                  description: |+
                    Callback address, use global notifyHook if it is empty.

                state:
                  type: string
                  description: Custom parameters
                base64Array:
                  type: array
                  items:
                    type: string
                  description: |+
                    Pad image base64 array

              required:
                - botType
                - prompt
              x-apifox-orders:
                - botType
                - prompt
                - base64Array
                - notifyHook
                - state
            example:
              base64Array: []
              notifyHook: ""
              prompt: cat
              state: ""
              botType: MID_JOURNEY
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apifox-orders: []
              example: "{\r\n    \"code\": 1,\r\n    \"description\": \"Submit success\",\r\n    \"result\": \"1730621718151844\",//任务id\r\n    \"properties\": {\r\n        \"discordChannelId\": \"1300842676874379336\",\r\n        \"discordInstanceId\": \"1572398367386955776\"\r\n    }\r\n}"
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Painting Model/Midjourney
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421938-run
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
