# Generate a song (upload a song for secondary creation).

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/submit/music:
    post:
      summary: Generate a song (upload a song for secondary creation).
      deprecated: false
      description: ""
      tags:
        - Music Suno / Task Submission
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
                prompt:
                  type: string
                  description: The lyrics to be sung next
                tags:
                  type: string
                  description: Style tags
                negative_tags:
                  type: string
                  description: Negative labels, unwanted elements
                mv:
                  type: string
                  description: Model version number
                title:
                  type: string
                  description: Title
                continue_clip_id:
                  type: string
                  description: Continue writing audio ID
                continue_at:
                  type: integer
                  description: Continue writing the starting time point
                task:
                  type: string
                  description: Task type, defaults to "Extended".
              required:
                - prompt
                - mv
                - title
                - continue_clip_id
                - continue_at
                - task
              x-apifox-orders:
                - prompt
                - tags
                - negative_tags
                - mv
                - title
                - continue_clip_id
                - continue_at
                - task
            example:
              prompt: lyrics
              tags: ""
              negative_tags: ""
              mv: chirp-v4
              title: title
              continue_clip_id: ca94a97d-d3f2-4a63-aeee-ba3a43384bcd
              continue_at: 10
              task: upload_extend
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
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-305049403-run
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
