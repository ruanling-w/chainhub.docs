# Generate video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /alibailian/api/v1/services/aigc/video-generation/video-synthesis:
    post:
      summary: Generate video
      deprecated: false
      description: ''
      tags:
        - Video Model / Universal Meaning Video Generation
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  description: Model Name (Required): Specifies the model used for this video generation. Example value: wan2.5-i2v-preview.
                  type: string
                input:
                  type: object
                  properties:
                    prompt:
                      description: Cue words (optional) are used to describe the elements and visual features that are expected to be included in the generated image.
                      type: string
                    negative_prompt:
                      description: Reverse prompts (optional) are used to describe content that you do not want to see in the video.
                      type: string
                    img_url:
                      description: First frame image, (required) The URL of the first frame image or Base64 encoded data.
                      type: string
                    audio_url:
                      description: The URL of the audio file (optional, only supported by wan2.5-i2v-preview). The model will use this audio to generate the video.
                      type: string
                    template:
                      description: Video effects template, (optional) The name of the video effects template. If left blank, it means no video effects will be used.
                      type: string
                  required:
                    - prompt
                    - negative_prompt
                    - img_url
                    - audio_url
                    - template
                  description: Input information (required) Basic information to input, such as prompts, images, etc.
                  x-apifox-orders:
                    - prompt
                    - negative_prompt
                    - img_url
                    - audio_url
                    - template
                parameters:
                  type: object
                  properties:
                    resolution:
                      description: Video resolution (optional): Specifies the resolution level of the generated video without changing the aspect ratio.
                      type: string
                    duration:
                      description: Video duration, (optional) The duration of the generated video, in seconds. The value of this parameter depends on the model parameter.
                      type: integer
                    prompt_extend:
                      description: Smart Prompt Rewriting (Optional): Whether to enable smart prompt rewriting. The default value is true.
                      type: boolean
                    watermark:
                      description: Watermark identifier, (optional) Whether to add an "AI-generated" watermark identifier. The default value is false.
                      type: boolean
                    audio:
                      description: >-
                        Automatically add audio (optional, only supported by wan2.5-i2v-preview)

                        Controls whether to automatically add audio to the video; only effective when audio_url is empty.
                      type: boolean
                    seed:
                      description: Random number seed, (optional) A fixed seed value helps improve the reproducibility of the generated results.
                      type: integer
                  required:
                    - resolution
                    - duration
                    - prompt_extend
                    - watermark
                    - audio
                    - seed
                  description: Video processing parameters, (optional) Advanced video processing parameters, such as setting resolution, duration, watermark, etc.
                  x-apifox-orders:
                    - resolution
                    - duration
                    - prompt_extend
                    - watermark
                    - audio
                    - seed
              required:
                - model
                - input
                - parameters
              x-apifox-orders:
                - model
                - input
                - parameters
            example: "{\r\n    \"model\": \"wan2.5-i2v-preview\",\r\n    \"input\": {\r\n        \"prompt\": \"Change the lighting\",\r\n        \"img_url\": \"https://brainrot-yt-shorts.oss-cn-beijing.aliyuncs.com/images/cached/55a955b7e41723417281051d7bebdb45.png\"\r\n    },\r\n    \"parameters\": {\r\n        \"resolution\": \"480P\",\r\n        \"prompt_extend\": true,\r\n        // \"duration\": 5,\r\n        \"audio\": true\r\n    }\r\n}"
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  request_id:
                    type: string
                  output:
                    type: object
                    properties:
                      task_id:
                        type: string
                      task_status:
                        type: string
                    required:
                      - task_id
                      - task_status
                required:
                  - request_id
                  - output
              example:
                request_id: ccffb21f-c21e-4eba-861a-6c80e6db6e4d
                output:
                  task_id: a55bfe14-6e78-4b9d-b97d-128420399ed1
                  task_status: PENDING
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model / Universal Meaning Video Generation
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-359496147-run
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
