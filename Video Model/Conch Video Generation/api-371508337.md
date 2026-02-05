# First and last frame video

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
      summary: First and last frame video
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
              model: MiniMax-Hailuo-02
              prompt: A little pig is running happily on the highway.
              duration: 10
              first_frame_image: >-
                https://wx4.sinaimg.cn/mw690/8545bf24ly1hq626p2k5aj20j60j7t9t.jpg
              last_frame_image: >-
                https://inews.gtimg.com/om_bt/OBcldFgmIx8oKc7VlrEnHqso_pEEeyfa9Va0gHrQR7NBcAA/641
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
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Seashell Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-371508337-run
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
