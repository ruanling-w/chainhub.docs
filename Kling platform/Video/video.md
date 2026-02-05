# Video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/videos/text2video:
    post:
      summary: Video
      deprecated: false
      description: ''
      tags:
        - Kling Platform / Video
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: false
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ''
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
                model_name:
                  description: ' Model name enumeration values: kling-v1, kling-v1-6, kling-v2-master, kling-v2-1-master, kling-v2-5-turbo'
                  type: string
                prompt:
                  description: Positive text prompts cannot exceed 2500 characters.
                  type: string
                negative_prompt:
                  description: Negative text prompts cannot exceed 2500 characters.
                  type: string
                cfg_scale:
                  type: number
                  description: The degree of freedom in generating the video; the larger the value, the smaller the model's degree of freedom, and the stronger the correlation with the prompts input by the user.
                mode:
                  type: string
                  description: |-
                    Video generation mode
                    Enumeration values: std, pro
                    std: Standard mode (basic), cost-effective
                    pro: Expert mode (high quality), high performance, better video quality
                camera_control:
                  type: object
                  properties:
                    type:
                      type: string
                    config:
                      type: object
                      properties:
                        horizontal:
                          type: integer
                        vertical:
                          type: integer
                        pan:
                          type: integer
                        tilt:
                          type: integer
                        roll:
                          type: integer
                        zoom:
                          type: integer
                      required:
                        - horizontal
                        - vertical
                        - pan
                        - tilt
                        - roll
                        - zoom
                      x-apifox-orders:
                        - horizontal
                        - vertical
                        - pan
                        - tilt
                        - roll
                        - zoom
                  required:
                    - type
                    - config
                  x-apifox-orders:
                    - type
                    - config
                  description: Protocol for controlling camera movement (if not specified, the model will intelligently match based on the input text/image)
                aspect_ratio:
                  type: string
                  description: The aspect ratio (width:height) of the generated video.
                duration:
                  type: string
                  description: The duration of the generated video is in seconds.
                callback_url:
                  type: string
                external_task_id:
                  type: string
                sound:
                  type: string
                  description: Whether to generate audio simultaneously with video generation: on, off. This parameter is only supported in V2.6 and later versions.
              required:
                - model_name
                - prompt
                - mode
                - duration
                - sound
              x-apifox-orders:
                - model_name
                - prompt
                - negative_prompt
                - cfg_scale
                - mode
                - sound
                - camera_control
                - aspect_ratio
                - duration
                - callback_url
                - external_task_id
            example:
              model_name: kling-v1
              prompt: Generate a video of someone dancing on the beach.
              negative_prompt: ''
              cfg_scale: 0.5
              mode: std
              sound: 'off'
              camera_control:
                type: simple
                config:
                  horizontal: 1
                  vertical: 0
                  pan: 0
                  tilt: 0
                  roll: 0
                  zoom: 0
              aspect_ratio: '16:9'
              duration: '5'
              callback_url: ''
              external_task_id: ''
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling Platform / Video
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386060323-run
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
