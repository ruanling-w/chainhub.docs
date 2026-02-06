# Timing: Lyrics, Audio Timeline

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /suno/act/timing/{id}:
    get:
      summary: Timing: Lyrics, Audio Timeline
      deprecated: false
      description: ''
      tags:
        - Music Suno/Query Interface
      parameters:
        - name: id
          in: path
          description: ''
          required: true
          example: a624123d-22cc-4d4d-bf28-78d312f61597
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                code: task_not_exist
                message: task_not_exist
                data: null
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno/Query Interface
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-408281974-run
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
