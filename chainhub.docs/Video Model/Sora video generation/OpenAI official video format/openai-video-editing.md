# OpenAI video editing

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/videos/{id}/remix:
    post:
      summary: OpenAI video editing
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation/OpenAI official video format
      parameters:
        - name: id
          in: path
          description: ''
          required: true
          example: video_099c5197-abfd-4e16-88ff-1e162f2a5c77
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
              required:
                - prompt
            example:
              prompt: The picture is more detailed
              size: 1280x720
      responses:
        '401':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      message:
                        type: string
                      message_zh:
                        type: string
                      type:
                        type: string
                    required:
                      - message
                      - message_zh
                      - type
                required:
                  - error
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/OpenAI official video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-363040669-run
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
