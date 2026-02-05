# Video search

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /alibailian/api/v1/tasks/{task_id}:
    get:
      summary: Video search
      deprecated: false
      description: ''
      tags:
        - Video Model / Universal Meaning Video Generation
      parameters:
        - name: task_id
          in: path
          description: ''
          required: true
          example: a55bfe14-6e78-4b9d-b97d-128420399ed1
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
                  usage:
                    type: object
                    properties:
                      SR:
                        type: integer
                      duration:
                        type: integer
                      video_count:
                        type: integer
                    required:
                      - SR
                      - duration
                      - video_count
                  output:
                    type: object
                    properties:
                      task_id:
                        type: string
                      end_time:
                        type: string
                      video_url:
                        type: string
                      orig_prompt:
                        type: string
                      submit_time:
                        type: string
                      task_status:
                        type: string
                      actual_prompt:
                        type: string
                      scheduled_time:
                        type: string
                    required:
                      - task_id
                      - end_time
                      - video_url
                      - orig_prompt
                      - submit_time
                      - task_status
                      - actual_prompt
                      - scheduled_time
                  request_id:
                    type: string
                required:
                  - usage
                  - output
                  - request_id
              example:
                usage:
                  SR: 480
                  duration: 5
                  video_count: 1
                output:
                  task_id: a55bfe14-6e78-4b9d-b97d-128420399ed1
                  end_time: '2025-10-11 19:02:27.297'
                  video_url: >-
                    https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/1d/21/20251011/9b1c82b0/a55bfe14-6e78-4b9d-b97d-128420399ed1.mp4?Expires=1760266939&OSSAccessKeyId=LTAI5tDUB1cEqFCYhEwWry26&Signature=Fjpx1uAlmLmeYGWx0Ye7n%2F%2F9Isw%3D
                  orig_prompt: Change the lighting
                  submit_time: '2025-10-11 18:55:56.952'
                  task_status: SUCCEEDED
                  actual_prompt: >-
                    A man in an orange shirt flies at high speed from right to left on a broomstick, leaning forward, gripping the broom handle tightly, head facing forward, mouth open, shouting, "Hey! Don't stop me!" The broom moves rapidly through the air, the bristles blurring due to the speed. Below, three people stand on the sidewalk, holding wands and pointing them at the figure in the air, their heads slightly turning to follow his flight, watching his movements. In the background, the sounds of traffic, pedestrian conversations, wind, and the whistling of broomsticks cutting through the air can be heard continuously.
                  scheduled_time: '2025-10-11 18:55:57.908'
                request_id: ec8f059e-f2e5-4887-bb43-3306cd38f403
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model / Universal Meaning Video Generation
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-359507346-run
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
