# Initialize the video to be edited

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/multi-elements/init-selection:
    post:
      summary: Initialize the video to be edited
      deprecated: false
      description: ""
      tags:
        - Kling Platform / Multimodal Video Editing
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
                video_id:
                  type: string
                  description: >-
                    Video ID: Selects the video to be edited from historical works. Only supports videos generated within the last 30 days.
                    Only supports videos with a duration of ≥2 seconds and ≤5 seconds, or ≥7 seconds and ≤10 seconds. Related to the `video_url` parameter; it cannot be empty or have values ​​simultaneously.
                video_url:
                  type: string
                  description: >-
                    Retrieves the video URL, uploads the video download link during upload, and retrieves the video URL returned by the upload interface during area selection editing. Only MP4 and MOV formats are supported.
                    Only videos with a duration ≥2 seconds and ≤5 seconds, or ≥7 seconds and ≤10 seconds are supported.
              x-apifox-orders:
                - video_id
                - video_url
            example:
              video_id: "828013548709777428"
              video_url: ""
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
      x-apifox-folder: Kling Platform / Multimodal Video Editing
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386191600-run
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
