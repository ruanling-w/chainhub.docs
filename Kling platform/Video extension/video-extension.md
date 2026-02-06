# Video extension

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/video-extend:
    post:
      summary: Video extension
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Video Extension
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
                  description: The video ID supports extending the generated video ID using text, images, and videos (the original video cannot exceed 3 minutes).
                prompt:
                  type: string
                  description: Positive text suggestions cannot exceed 2500 characters.
                negative_prompt:
                  type: string
                  description: Negative text prompts
                cfg_scale:
                  type: number
                  description: The reference strength of the prompt word ranges from [0,1], with larger values ​​indicating greater reference strength.
                callback_url:
                  type: string
              required:
                - video_id
                - prompt
              x-apifox-orders:
                - video_id
                - prompt
                - negative_prompt
                - cfg_scale
                - callback_url
            example:
              video_id: "828006748715380777"
              prompt: Extend animation effect
              negative_prompt: ""
              cfg_scale: 0.5
              callback_url: ""
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
      x-apifox-folder: Kling Platform/Video Extension
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386231144-run
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
