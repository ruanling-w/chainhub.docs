# Creating videos with sora-2-pro

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/video/create:
    post:
      summary: Creating videos with sora-2-pro
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation/Unified video format
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ''
          required: true
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
                images:
                  type: array
                  items:
                    type: string
                  description: Image link
                model:
                  type: string
                  description: Model name
                orientation:
                  type: string
                  description: |
                    portrait (vertical screen)
                    landscape (horizontal screen)
                prompt:
                  type: string
                  description: Prompt words
                size:
                  type: string
                  description: Large HD 1080p
                duration:
                  type: integer
                  description: Support 15, 25
                watermark:
                  type: boolean
                  description: |
                    The default setting is `true`, which prioritizes removing the watermark. If an error occurs, it will be used as a fallback option if the video still has a watermark.

                    Passing `false` will force the video to be watermark-free, and it will automatically retry if a watermark removal error occurs.
                private:
                  type: boolean
                  description: |
                    Whether to hide the video. True - the video will not be published, and it cannot be remixed (secondary edited). Default is false.
              required:
                - images
                - model
                - orientation
                - prompt
                - size
                - duration
                - watermark
                - private
              x-apifox-orders:
                - images
                - model
                - orientation
                - prompt
                - size
                - duration
                - watermark
                - private
            example:
              images: []
              model: sora-2-pro
              orientation: portrait
              prompt: make animate
              size: large
              duration: 15
              watermark: false
              private: true
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
                  created:
                    type: integer
                  choices:
                    type: array
                    items:
                      type: object
                      properties:
                        index:
                          type: integer
                        message:
                          type: object
                          properties:
                            role:
                              type: string
                            content:
                              type: string
                          required:
                            - role
                            - content
                          x-apifox-orders:
                            - role
                            - content
                        finish_reason:
                          type: string
                      x-apifox-orders:
                        - index
                        - message
                        - finish_reason
                  usage:
                    type: object
                    properties:
                      prompt_tokens:
                        type: integer
                      completion_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                    required:
                      - prompt_tokens
                      - completion_tokens
                      - total_tokens
                    x-apifox-orders:
                      - prompt_tokens
                      - completion_tokens
                      - total_tokens
                required:
                  - id
                  - object
                  - created
                  - choices
                  - usage
                x-apifox-orders:
                  - id
                  - object
                  - created
                  - choices
                  - usage
              example:
                id: sora-2:task_01k9009g8ef1esae6388chgcpx
                status: pending
                status_update_time: 1762010645686
          headers: {}
          x-apifox-name: OK
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/Unified video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-358742580-run
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
