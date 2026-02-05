# Create videos with images using OpenAI.

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/videos:
    post:
      summary: Create videos with images using OpenAI.
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation/OpenAI official video format
      parameters: []
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                model:
                  description: The video generation model to use (allowed values: sora-2, sora-2-pro).
                  example: sora-2
                  type: string
                prompt:
                  description: A text prompt describing the video to be generated.
                  example: A calico cat playing a piano on stage
                  type: string
                seconds:
                  description: Clip duration (seconds) (allowed values: 4, 8, 12). Default is 4 seconds.
                  example: '4'
                  type: string
                size:
                  description: >+
                    Output resolution format is width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). The default value is 720x1280.

                  example: 720x1280
                  type: string
                input_reference:
                  format: binary
                  type: string
                  description: Optional image references are used to guide the generation process.
                  example: >-
                    file://C:\Users\Administrator\Desktop\fuji-mountain-kawaguchiko-lake-morning-autumn-seasons-fuji-mountain-yamanachi-japan_copy.jpg
                watermark:
                  description: '-ALL model available parameters'
                  example: 'false'
                  type: string
                private:
                  description: '-ALL model available parameters'
                  example: 'false'
                  type: string
                style:
                  description: >-
                    -ALL model available parameters Style only supports: thanksgiving, comic, news, selfie,
                    nostalgic, anime
                  example: anime
                  type: string
              required:
                - model
                - prompt
            examples: {}
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                id: video_5c6a605a-30c0-4a6a-9dbd-d1d6cfdd9980
                object: video
                model: sora-2
                status: queued
                progress: 0
                created_at: 1761622232
                seconds: '10'
                size: 1280x720
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/OpenAI official video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-363028872-run
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
