# Create videos using storyboards

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/videos:
    post:
      summary: Create videos using storyboards
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation/OpenAI official video format
      parameters: []
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                model:
                  example: sora-2
                  type: string
                prompt:
                  description: The format of the prompts is fixed as shown in the example; you can change the time and scene descriptions.
                  example: >-
                    Shot 1:\nduration: 5sec\nScene: The fridge door opens. A
                    cute, chubby purple monster comes out of it.\n\nShot
                    2:\nduration: 5sec\nScene: the color of the monster to
                    purple Shot 3:\nduration: 5sec\nScene: A second monster
                    comes out right after
                  type: string
                seconds:
                  type: string
                  enum:
                    - '10'
                    - '15'
                    - '25'
                  x-apifox-enum:
                    - value: '10'
                      name: ''
                      description: ''
                    - value: '15'
                      name: ''
                      description: ''
                    - value: '25'
                      name: ''
                      description: Only Pro version supported
                  description: Length of generated video
                  example: '15'
                input_reference:
                  format: binary
                  type: string
                  description: Reference image
                  example: >-
                    file://C:\Users\WUKONG\Desktop\989e-633a9d8ce6ef59a78b06bfe2b487c896.jpg
                size:
                  description: >+
                    Output resolution format is width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). The default value is 720x1280.

                  example: 720x1280
                  type: string
                watermark:
                  description: Watermark not required; no watermark is required by default if no watermark is uploaded.
                  example: 'false'
                  type: string
                private:
                  type: boolean
                  description: Hide video (true) - Video will not be published, and it cannot be remixed (secondary edited). Default is false.
                  example: 'false'
                character_url:
                  type: string
                  description: The video link required to create the character. Note that the video must not contain any real people, otherwise the process will fail.
                  example: ''
                character_timestamps:
                  description: The duration of a character's appearance in the video, formatted as {start},{end}, note that the range of end-start is 1 to 3 seconds.
                  example: ''
                  type: string
                metadata:
                  example: ''
                  type: string
                character_from_task:
                  description: Completed task IDs can be used to create roles.
                  example: ''
                  type: string
                character_create:
                  type: boolean
                  description: Once the video is created, a character will be automatically created based on the generated video.
                  example: ''
              required:
                - model
                - prompt
            examples: {}
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  object:
                    type: string
                  model:
                    type: string
                  status:
                    type: string
                  progress:
                    type: integer
                  created_at:
                    type: integer
                  seconds:
                    type: string
                  size:
                    type: string
                required:
                  - id
                  - object
                  - model
                  - status
                  - progress
                  - created_at
                  - seconds
                  - size
              example:
                id: sora-2:task_01kbhfs5yceakr1pa0qrfzfeqk
                object: video
                model: sora-2
                status: queued
                progress: 0
                created_at: 1764744797290
                seconds: '15'
                size: 1280x720
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/OpenAI official video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-385627774-run
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
