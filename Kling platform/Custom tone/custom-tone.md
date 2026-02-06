# Custom tone

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/general/custom-voices:
    post:
      summary: Custom tone
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Custom Tones
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
                voice_name:
                  type: string
                  description: Timbre Name
                voice_url:
                  type: string
                  description: |-
                    Audio data file download link
                    Supports .mp3/.wav/.mp4/.mov audio and video files
                    The audio must be clean and free of background noise, containing only one type of vocal, and last for at least 5 seconds and no more than 30 seconds.
                video_id:
                  type: string
                  description: |-
                    Historical work IDs can be used to provide audio materials by referencing historical works.

                    Only videos meeting the following conditions can be used for customized sound:
                    Videos generated using the V2.6 model with the `sound` parameter set to `on`
                    Videos generated via the Digital Human API
                    Videos generated via the Lip-Sync API
                    The audio must contain a clean, noise-free voice, with only one type of voice, and a duration of at least 5 seconds and no more than 30 seconds.
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - voice_name
              x-apifox-orders:
                - voice_name
                - voice_url
                - video_id
                - callback_url
                - external_task_id
            examples: {}
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                voice_name: Test tone
                voice_url: ""
                video_id: "830460928805724256"
                callback_url: ""
                external_task_id: ""
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling Platform/Custom Tones
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-393212449-run
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
