# Get WAV

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/act/wav/{clip_id}:
    get:
      summary: Get WAV
      deprecated: false
      description: ""
      tags:
        - Music Suno/Query Interface
      parameters:
        - name: clip_id
          in: path
          description: ""
          required: true
          example: 9c4f48f1-c0d2-44eb-bf9c-e34d559b374c
          schema:
            type: string
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-357249347-run
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
