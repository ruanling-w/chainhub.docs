# Create video

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
      summary: Create video
      deprecated: false
      description: ''
      tags:
        - Video model/veo video generation/Unified video format
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
                model:
                  type: string
                  enum:
                    - veo2
                    - veo2-fast
                    - veo2-fast-frames
                    - veo2-fast-components
                    - veo2-pro
                    - veo2-pro-components
                    - veo3
                    - veo3-fast
                    - veo3-fast-frames
                    - veo3-frames
                    - veo3-pro
                    - veo3-pro-frames
                    - veo3.1
                    - veo3.1-fast
                    - veo3.1-pro
                  x-apifox-enum:
                    - value: veo2
                      name: ''
                      description: Google's latest advanced AI model, veo2 fast mode, is of high quality and fast speed.
                    - value: veo2-fast
                      name: ''
                      description: Google's latest advanced AI model, veo2 fast mode, is of high quality and fast speed.
                    - value: veo2-fast-frames
                      name: ''
                      description: Google's latest advanced AI model, veo2 fast mode, supports both the first and last frames.
                    - value: veo2-fast-components
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO2 Fast mode,

                        supports uploading image assets. The final generated video will merge all images into a single part of the video; for example, image 1 becomes the background, image 2
                        covers the sky, and so on.
                    - value: veo2-pro
                      name: ''
                      description: Google's latest advanced AI model, VEO2 in high-quality mode, is of very high quality but also very expensive; caution is advised when using it.
                    - value: veo2-pro-components
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO2 Pro mode,

                        supports uploading image materials. The final generated video will merge all images into a single part of the video; for example, image 1 becomes the background, image 2
                        covers the sky, etc.
                    - value: veo3
                      name: ''
                      description: veo3 is Google's latest official video generation model, producing videos with sound. It is currently the only video generation model in the world that includes sound.
                    - value: veo3-fast
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO3, in its fast mode, supports automatic audio generation for videos. It offers high quality at a very low price, making it the best value option.
                    - value: veo3-fast-frames
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO3, in fast mode, supports automatic audio generation for videos, supports first-frame delivery, offers high quality at a very low price, and is the most cost-effective option.
                    - value: veo3-frames
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO3, in fast mode, supports automatic audio generation for videos, supports first-frame delivery, offers high quality at a very low price, and is the most cost-effective option.
                    - value: veo3-pro
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO3, in high-quality mode, supports automatic audio generation for videos. The quality is extremely high, but the price is also extremely high; please use with caution.
                    - value: veo3-pro-frames
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO3, in high-quality mode, supports automatic audio generation for video, supports first-frame transmission but not last-frame transmission. It boasts extremely high quality, but is also extremely expensive; users should exercise caution.
                    - value: veo3.1
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO 3.1, in fast mode, supports automatic audio generation for videos. It offers high quality at a very low price, making it the most cost-effective option. It also features adaptive first-frame and text-based video generation.
                    - value: veo3.1-fast
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO 3.1, in fast mode, supports automatic audio generation for videos. It offers high quality at a very low price, making it the most cost-effective option. It also features adaptive first-frame and text-based video generation.
                    - value: veo3.1-pro
                      name: ''
                      description: >-
                        Google's latest advanced AI model, VEO 3.1, in high-quality mode, supports automatic audio generation for videos. The quality is extremely high, but the price is also extremely high; please be aware of this when using it. It features adaptive first frame and text-based video.
                prompt:
                  type: string
                  description: Prompt words
                enhance_prompt:
                  type: boolean
                  description: Since VEO only supports English prompts, you can turn on this switch if you need Chinese prompts to be automatically converted to English.
                enable_upsample:
                  type: boolean
                images:
                  type: array
                  items:
                    type: string
                  description: >-
                    When the model uses veo2-fast-frames, a maximum of two frames are supported, representing the first and last frames. When the model uses veo3-pro-frames, a maximum of one first frame is supported. When the model uses veo2-fast-components, a maximum of three components are supported, in which case the images represent elements from the video.
                aspect_ratio:
                  type: string
                  description: ⚠️Veo 3 only, "16:9" or "9:16" aspect ratio supported.
              required:
                - prompt
                - model
              x-apifox-orders:
                - enable_upsample
                - enhance_prompt
                - images
                - model
                - prompt
                - aspect_ratio
            example:
              enable_upsample: true
              enhance_prompt: true
              images:
                - >-
                  https://filesystem.site/cdn/20250702/w8AauvxxPhYoqqkFWdMippJpb9zBxN.png
              model: veo3.1-fast
              prompt: make animate
              aspect_ratio: '16:9'
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
                  status:
                    type: string
                  status_update_time:
                    type: integer
                  enhanced_prompt:
                    type: string
                required:
                  - id
                  - status
                  - status_update_time
                  - enhanced_prompt
              example:
                id: veo3-fast-frames:1757555257-PORrVn9sa9
                status: pending
                status_update_time: 1757555257582
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Video model/veo video generation/Unified video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-311044999-run
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
