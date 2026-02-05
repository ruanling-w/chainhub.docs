# Submit video generation task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /runwayml/v1/image_to_video:
    post:
      summary: Submit video generation task
      deprecated: false
      description: >-
        Official documentation：https://docs.dev.runwayml.com/api/#tag/Start-generating/paths/~1v1~1image_to_video/post
      tags:
        - Video Model/Runway Video Generation
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
                promptImage:
                  description: Required, HTTPS URL or data URI, containing the encoded image as the first frame of the generated video.
                  type: string
                model:
                  type: string
                  description: Required. Specifies the model variant to use. Optional values: "gen4_turbo" or "gen3a_turbo".
                ratio:
                  type: string
                  description: ' Required. Output video resolution in "width:height" format. Different models support different resolutions.'
                seed:
                  description: Optional, random seed value (0-4294967295), the same seed will produce similar results for the same request.
                  type: integer
                promptText:
                  description: Optional, string (≤1000 characters), describing in detail the content expected to appear in the video.
                  type: string
                duration:
                  description: Optional, video duration (seconds), selectable values: 5 or 10, default is 10.
                  type: integer
              required:
                - promptImage
                - model
                - ratio
                - seed
                - promptText
                - duration
              x-apifox-orders:
                - promptImage
                - model
                - ratio
                - seed
                - promptText
                - duration
            example:
              promptImage: https://www.bt.cn/bbs/template/qiao/style/image/btlogo.png
              model: gen4_turbo
              promptText: cat dance
              watermark: false
              duration: 5
              ratio: '1280:768'
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-247132317-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://api.chainub.tech
    description: Production Environment
security:
  - bearer: []

```
