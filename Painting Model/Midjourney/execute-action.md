# Execute Action

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /mj/submit/action:
    post:
      summary: Execute Action
      deprecated: false
      description: >-
        Official documentation：https://docs.midjourney.com/hc/en-us/articles/32804058614669-Upscalers
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
                chooseSameChannel:
                  type: boolean
                  description: |+
                    Whether to select accounts under the same channel, the default is to only use accounts associated with the task.

                customId:
                  type: string
                  description: Action Icons
                  examples:
                    - MJ::JOB::upsample::2::3dbbd469-36af-4a0f-8f02-df6c579e7011
                taskId:
                  type: string
                  description: Task ID
                  examples:
                    - "14001934816969359"
                notifyHook:
                  type: string
                  description: |+
                    Callback address, use global notifyHook if it is empty.

                state:
                  type: string
                  description: |
                    Custom parameters
              required:
                - chooseSameChannel
              x-apifox-orders:
                - chooseSameChannel
                - customId
                - taskId
                - notifyHook
                - state
            example:
              chooseSameChannel: true
              customId: MJ::JOB::upsample::2::3dbbd469-36af-4a0f-8f02-df6c579e7011
              taskId: "14001934816969359"
              notifyHook: ""
              state: ""
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421942-run
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
