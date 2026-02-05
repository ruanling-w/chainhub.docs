# Submit Blend task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /mj/submit/blend:
    post:
      summary: Submit Blend task
      deprecated: false
      description: >-
        Official documentation：https://docs.midjourney.com/hc/en-us/articles/32635189884557-Blend-Images-on-Discord
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
                quality:
                  type: string
                  description: This affects the quality of the generated image. `hd` creates an image with finer details and higher consistency. This parameter is only supported for `dall-e-3`.
                botType:
                  type: string
                  description: |+
                    bot type, mj (default) or niji

                  enum:
                    - NIJI_JOURNEY
                    - MID_JOURNEY
                  x-apifox-enum:
                    - value: NIJI_JOURNEY
                      name: ""
                      description: ""
                    - value: MID_JOURNEY
                      name: ""
                      description: ""
                  examples:
                    - MID_JOURNEY
                base64Array:
                  type: string
                  description: |+
                    Image base64 array

                dimensions:
                  type: string
                  description: |+
                    Proportion: PORTRAIT(2:3); SQUARE(1:1); LANDSCAPE(3:2)

                  enum:
                    - PORTRAIT
                    - SQUARE
                    - LANDSCAPE
                  x-apifox-enum:
                    - value: PORTRAIT
                      name: ""
                      description: ""
                    - value: SQUARE
                      name: ""
                      description: ""
                    - value: LANDSCAPE
                      name: ""
                      description: ""
                  examples:
                    - SQUARE
                notifyHook:
                  type: string
                  description: |+
                    Callback address, use global notifyHook if it is empty.

                state:
                  type: string
                  description: |
                    Custom parameters
              required:
                - botType
              x-apifox-orders:
                - botType
                - base64Array
                - dimensions
                - quality
                - notifyHook
                - state
            example:
              botType: MID_JOURNEY
              base64Array:
                - data:image/png;base64,xxx1
                - data:image/png;base64,xxx2
              dimensions: SQUARE
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421943-run
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
