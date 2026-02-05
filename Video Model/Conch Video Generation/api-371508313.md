# Image and video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /minimax/v1/video_generation:
    post:
      summary: Image and video
      deprecated: false
      description: >-
        Official Documentation: https://www.minimax.io/platform/document/Model%3Fkey=684261f14c5738213294faa7?key=66d1439376e52fcee2853049&document=video_generation
      tags:
        - Video Model/Seashell Video Generation
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
                model:
                  type: string
                  description: Model Name: MiniMax-Hailuo-02
                prompt:
                  type: string
                  description: Prompt words
                duration:
                  type: integer
                  description: Video length supports 6 and 10 seconds.
              required:
                - model
                - prompt
                - duration
              x-apifox-orders:
                - model
                - prompt
                - duration
            example:
              model: MiniMax-Hailuo-2.3
              prompt: A little pig is running happily on the highway.
              duration: 10
              first_frame_image: >-
                https://wx4.sinaimg.cn/mw690/8545bf24ly1hq626p2k5aj20j60j7t9t.jpg
              resolution: 768P
              'prompt_optimizer ': true
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
                task_id: '306792606023824'
                base_resp:
                  status_code: 0
                  status_msg: success
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Seashell Video Generation
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-371508313-run
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
