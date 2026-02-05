# Submit video generation task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /luma/generations:
    post:
      summary: Submit video generation task
      deprecated: false
      description: Official documentation: https://docs.lumalabs.ai/docs/video-generation
      tags:
        - Video Model/Luma Video Generation/Official API Format
      parameters:
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
                  description: Required, user input prompt/problem description
                  type: string
                expand_prompt:
                  description: Optional, prompt optimization switch
                  type: boolean
                loop:
                  description: Optional, whether to loop reference images
                  type: boolean
                image_url:
                  description: Optional, reference image source
                  type: string
                image_end_url:
                  description: Optional, target keyframe image
                  type: string
                notify_hook:
                  description: Optional, callback notification address after processing is completed
                  type: string
                resolution:
                  type: string
                  description: |
                    720p or 1080p, default 720p
                duration:
                  type: string
                  description: |
                    Duration only supports 5s
                model_name:
                  type: string
                  description: |
                    ray-v1, ray-v2, official display is ray1.6 ray2
              required:
                - user_prompt
                - expand_prompt
                - loop
                - image_url
                - image_end_url
                - notify_hook
                - resolution
                - duration
                - model_name
              x-apifox-orders:
                - user_prompt
                - expand_prompt
                - loop
                - image_url
                - image_end_url
                - notify_hook
                - resolution
                - duration
                - model_name
            example:
              user_prompt: A gust of wind blew through the forest, causing the woman's veil to flutter slightly.
              model_name: ray-v2
              duration: 5s
              resolution: 720p
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
          x-apifox-name: 成功
      security:
        - bearer: []
      x-apifox-folder: Video Model/Luma Video Generation/Official API Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-247110323-run
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
