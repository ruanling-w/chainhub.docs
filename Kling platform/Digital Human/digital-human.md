# Digital Human

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/avatar/image2video:
    post:
      summary: Digital Human
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Digital Human
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: false
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
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
                image:
                  type: string
                  description: >-
                    The digital human reference image supports inputting Base64 encoded images or image URLs (ensure they are accessible). Supported image formats are .jpg, .jpeg, and .png. Image file size cannot exceed 10MB, image dimensions must be at least 300px, and aspect ratio must be between 1:2.5 and 2.5:1.
                audio_id:
                  type: string
                  description: >-
                    The ID of the audio generated through the listening interface can only be an audio file generated within the last 30 days, with a duration of no less than 2 seconds and no more than 300 seconds. Either the `audio_id` or `sound_file` parameter can be selected; both cannot be empty or have values ​​simultaneously.
                sound_file:
                  type: string
                  description: >-
                    Audio file; supports Base64 encoded audio or audio URL (ensure accessibility); supports .mp3/.wav/.m4a/.aac audio files, file size not exceeding 5MB, error codes will be returned for format mismatch or excessively large files; only audio files with a duration of at least 2 seconds and no more than 300 seconds are supported; the audio_id and sound_file parameters are optional and cannot both be empty or both present; the system will verify the audio content, and will return error codes if there are any problems.
                prompt:
                  type: string
                  description: Positive text prompts
                mode:
                  type: string
                  description: Video generation mode
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - image
                - audio_id
                - sound_file
                - prompt
                - mode
                - callback_url
                - external_task_id
              x-apifox-orders:
                - image
                - audio_id
                - sound_file
                - prompt
                - mode
                - callback_url
                - external_task_id
            example:
              image: >-
                https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
              audio_id: "825455158141661278"
              sound_file: ""
              prompt: ""
              mode: std
              callback_url: ""
              external_task_id: ""
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling Platform/Digital Human
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386315766-run
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
