# Search for video tasks (free)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /runwayml/v1/tasks/{task_id}:
    get:
      summary: Search for video tasks (free)
      deprecated: false
      description: ''
      tags:
        - Video Model/Runway Video Generation
      parameters:
        - name: task_id
          in: path
          description: Task ID
          required: true
          example: 2f19d8a7-3b74-4fc4-af42-d0bcadbaec54
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ''
          required: true
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                  message:
                    type: string
                  request_id:
                    type: string
                  data:
                    type: object
                    properties:
                      task_id:
                        type: string
                      task_status:
                        type: string
                      created_at:
                        type: integer
                      updated_at:
                        type: integer
                    required:
                      - task_id
                      - task_status
                      - created_at
                      - updated_at
                required:
                  - code
                  - message
                  - request_id
                  - data
              example:
                id: 4665a07c-7641-4809-a133-10786201bb56
                prompt: ''
                state: pending
                queue_state: null
                created_at: '2024-12-22T13:38:40.139409Z'
                batch_id: ''
                video: null
                video_raw: null
                liked: null
                estimate_wait_seconds: null
                thumbnail: null
                last_frame: null
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Runway Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-247132320-run
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
