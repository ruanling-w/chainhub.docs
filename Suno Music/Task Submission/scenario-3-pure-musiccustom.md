# Scene 3: Pure Music. Custom

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/generate:
    post:
      summary: "Scene 3: Pure Music. Custom"
      deprecated: false
      description: ""
      tags:
        - Music Suno / Task Submission
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
            example:
              prompt: ""
              tags: heavy metal
              mv: chirp-v3-5
              title: 北京
              continue_clip_id: null
              continue_at: null
              infill_start_s: null
              infill_end_s: null
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
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-408850611-run
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
