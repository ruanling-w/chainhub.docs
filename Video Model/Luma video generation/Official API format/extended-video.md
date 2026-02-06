# Extended video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /luma/generations/{task_id}/extend:
    post:
      summary: Extended video
      deprecated: false
      description: Official documentation: https://docs.lumalabs.ai/docs/video-generation
      tags:
        - Video Model/Luma Video Generation/Official API Format
      parameters:
        - name: task_id
          in: path
          description: The task ID is the ID of the video task that needs to be extended.
          required: true
          example: 4665a07c-7641-4809-a133-10786201bb56
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                user_prompt:
                  description: Required, user input prompt/problem description, used to generate the main input of the content
                  type: string
                expand_prompt:
                  description: Optional, whether to enable prompt optimization function
                  type: boolean
                image_url:
                  description: Optional, reference image URL or Base64 encoding
                  type: string
                image_end_url:
                  description: Optional, target keyframe image URL or Base64 encoding
                  type: string
                notify_hook:
                  description: Optional, callback notification address
                  type: string
              required:
                - user_prompt
                - expand_prompt
                - image_url
                - image_end_url
                - notify_hook
              x-apifox-orders:
                - user_prompt
                - expand_prompt
                - image_url
                - image_end_url
                - notify_hook
            example:
              user_prompt: add cat
              expand_prompt: true
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
                id: 749d328e-4fd0-43a8-8c89-32394d60da69
                prompt: ''
                state: pending
                queue_state: null
                created_at: '2024-12-22T14:48:39.947851Z'
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
      x-apifox-folder: Video Model/Luma Video Generation/Official API Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-247123616-run
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
