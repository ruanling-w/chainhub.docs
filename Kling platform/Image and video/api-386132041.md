# Image and video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/videos/image2video:
    post:
      summary: Image and video
      deprecated: false
      description: ''
      tags:
        - Kling Platform / Image/Video
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
                  type: string
                  description: >-
                    模型名称 枚举值:kling-v1, kling-v1-5, kling-v1-6, kling-v2-master,
                    kling-v2-1, kling-v2-1-master, kling-v2-5-turbo,kling-v2-6
                image:
                  type: string
                  description: Reference Image: Supports passing in Base64 encoded images or image URLs (ensure accessibility).
                image_tail:
                  type: string
                  description: Reference Image - Tail Frame Control: Supports passing in Base64 encoded images or image URLs (ensure accessibility).
                prompt:
                  type: string
                  description: |-
                    Positive text prompts cannot exceed 2500 characters.
                    Use `<<<voice_1>>>` to specify the timbre, with the sequence number matching the order of timbres referenced in the `voice_list` parameter.
                    A single video generation task can reference a maximum of two timbres; when specifying a timbre, the `sound` parameter value must be `on`, and the syntax should be as simple as possible.
                    For example: a man saying "Hello" using `<<<voice_1>>>`.
                    When the `voice_list` parameter is not empty and the `prompt` parameter references a timbre ID, the video generation task is billed based on "with specified timbre".
                negative_prompt:
                  type: string
                  description: Negative text prompts
                cfg_scale:
                  type: number
                  description: The Kling-v2.x model does not support the degree of freedom in generating videos with the current parameters; the larger the value, the smaller the model's degree of freedom, and the stronger the correlation with the prompts input by the user.
                mode:
                  type: string
                  description: |-
                    Video generation mode
                    Enum values: std, pro
                    std: Standard mode (basic), cost-effective
                    pro: Expert mode (high quality), better video quality
                static_mask:
                  type: string
                  description: Static brush stroke area (mask image painted by the user using a motion brush)
                dynamic_masks:
                  type: array
                  items:
                    type: object
                    properties:
                      mask:
                        type: string
                      trajectories:
                        type: array
                        items:
                          type: object
                          properties:
                            x:
                              type: integer
                            'y':
                              type: integer
                          required:
                            - x
                            - 'y'
                          x-apifox-orders:
                            - x
                            - 'y'
                    x-apifox-orders:
                      - mask
                      - trajectories
                  description: Dynamic brush configuration list
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
                duration:
                  type: string
                  description: |-
                    Video duration (in seconds)
                    Enumerated values: 5, 10
                callback_url:
                  type: string
                external_task_id:
                  type: string
                voice_list:
                  type: array
                  items:
                    type: object
                    properties:
                      voice_id:
                        type: string
                    x-apifox-orders:
                      - voice_id
                  description: |-
                    Only versions V2.6 and later support the list of timbres referenced when generating video with the current parameters.
                    A single video generation task can reference a maximum of two timbres.
                    When the `voice_list` parameter is not empty and the `prompt` parameter references a timbre ID, the video generation task is billed based on "with specified timbres".
                sound:
                  type: string
                  description: |-
                    Only versions V2.6 and later support whether to generate audio simultaneously when generating video with the current parameters.
                    Enumeration values: on, off
              required:
                - model_name
                - duration
                - mode
                - image
              x-apifox-orders:
                - model_name
                - image
                - image_tail
                - prompt
                - voice_list
                - sound
                - negative_prompt
                - cfg_scale
                - mode
                - static_mask
                - dynamic_masks
                - camera_control
                - duration
                - callback_url
                - external_task_id
            example: "{\r\n    \"model_name\": \"kling-v1\",\r\n    \"image\": \"https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg\",\r\n    \"image_tail\": \"\",\r\n    \"prompt\": \"\",\r\n    \"negative_prompt\": \"\",\r\n    // \"voice_list\": [\r\n    //     {\r\n    //         \"voiceId\": \"\"\r\n    //     }\r\n    // ],\r\n    // \"sound\": \"\",\r\n    \"cfg_scale\": 0.5,\r\n    \"mode\": \"std\",\r\n    \"static_mask\": \"\",\r\n    \"dynamic_masks\": [\r\n        {\r\n            \"mask\": \"https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg\",\r\n            \"trajectories\": [\r\n                {\r\n                    \"x\": 0,\r\n                    \"y\": 0\r\n                },\r\n                {\r\n                    \"x\": 1,\r\n                    \"y\": 1\r\n                }\r\n            ],\r\n        }\r\n    ],\r\n    // \"camera_control\": {\r\n    //     \"type\": \"simple\",\r\n    //     \"config\": {\r\n    //         \"horizontal\": 1.0,\r\n    //         \"vertical\": 0,\r\n    //         \"pan\": 0,\r\n    //         \"tilt\": 0,\r\n    //         \"roll\": 0,\r\n    //         \"zoom\": 0\r\n    //     }\r\n    // },\r\n    \"duration\": 5,\r\n    \"callback_url\": \"\",\r\n    \"external_task_id\": \"\"\r\n}"
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
      security: []
      x-apifox-folder: Kling Platform / Image/Video
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386132041-run
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
