# Video effects

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/effects:
    post:
      summary: Video effects
      deprecated: false
      description: ""
      tags:
        - Kling Platform / Video Effects
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
                effect_scene:
                  type: string
                  description: Scene Name
                input:
                  type: object
                  properties:
                    model_name:
                      type: string
                      description: Double player kling-v1, kling-v1-5, kling-v1-6
                    mode:
                      type: string
                      description: >-
                        The video generation mode for two users; enumeration values: std, pro; where std: Standard mode (standard), basic mode, high cost-effectiveness; where pro: Expert mode (high quality), high performance mode, generating higher quality videos.
                    duration:
                      type: string
                      description: Video duration (in units)
                    images:
                      type: array
                      items:
                        type: string
                      description: "Double"
                    image:
                      type: string
                      description: "Single"
                  x-apifox-orders:
                    - model_name
                    - mode
                    - duration
                    - images
                    - image
                  description: >-
                    Reference Image: Supports inputting Base64 encoded images or image URLs (ensure accessibility). Supports different task input structures.
                    Depending on the scene, the fields passed in the structure will differ, as shown in the "Scene Request Body".
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - effect_scene
              x-apifox-orders:
                - effect_scene
                - input
                - callback_url
                - external_task_id
            example:
              effect_scene: balloon_parade
              input:
                duration: "5"
                image: >-
                  https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/kling-op/effects_pic/balloon_parade.jpeg
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
      x-apifox-folder: Kling Platform / Video Effects
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386233275-run
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
