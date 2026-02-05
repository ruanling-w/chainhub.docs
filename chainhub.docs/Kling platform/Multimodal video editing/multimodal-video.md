# Multimodal video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/videos/multi-elements:
    post:
      summary: Multimodal video
      deprecated: false
      description: ''
      tags:
        - Kling Platform / Multimodal Video Editing
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
                  description: Model name enumeration value: kling-v1-6
                session_id:
                  type: string
                  description: The session ID is generated based on the video initialization task and will not change with the editing selection.
                edit_mode:
                  type: string
                  description: >-
                    Operation type enumeration values: addition, swap, removal,
                    where: addition: add element, swap: replace element, removal: delete element
                image_list:
                  type: array
                  items:
                    type: string
                    description: |-
                      Recommended Prompt Template Adding Elements
                        //Chinese: Based on the original content in <<<video_1>>>, seamlessly add [x] from <<<image_1>>> to the [x] in <<<video_1>>> in a natural and vivid way.
                        //English: Using the context of <<<video_1>>>, seamlessly add [x] from <<<image_1>>> Replacing Elements
                        //Chinese: Replace the [x] in <<<video_1>>> with the [x] in <<<image_1>>>.
                        //English: swap [x] from <<<image_1>>> for [x] from <<<video_1>>> Deleting Elements
                        //Chinese: Delete the [x] in <<<video_1>>>
                        //English: Delete [x] from <<<video_1>>> Note: The [x] in Chinese and [x] in English are parts that need to be filled in by the user.
                  description: Cropped reference image
                prompt:
                  type: string
                  description: Positive text prompts
                negative_prompt:
                  type: string
                  description: Negative text prompts
                mode:
                  type: string
                  description: |-
                    Video generation mode
                    Enumeration values: std, pro
                    std: Standard mode (basic), cost-effective
                    pro: Expert mode (high quality), high performance, better video quality
                duration:
                  type: string
                  description: |-
                    Video duration (in seconds)
                    Enumerated values: 5, 10
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - model_name
                - session_id
                - edit_mode
                - prompt
                - mode
                - duration
              x-apifox-orders:
                - model_name
                - session_id
                - edit_mode
                - image_list
                - prompt
                - negative_prompt
                - mode
                - duration
                - callback_url
                - external_task_id
            example:
              model_name: kling-v1-6
              session_id: ''
              edit_mode: ''
              image_list: []
              prompt: ''
              negative_prompt: ''
              mode: std
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
      x-apifox-folder: Kling Platform / Multimodal Video Editing
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-389936303-run
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
