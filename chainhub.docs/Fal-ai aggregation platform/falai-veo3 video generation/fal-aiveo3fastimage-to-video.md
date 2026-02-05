# /fal-ai/veo3/fast/image-to-video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/veo3/fast/image-to-video:
    post:
      summary: /fal-ai/veo3/fast/image-to-video
      deprecated: false
      description: Official documentation address：https://fal.ai/models/fal-ai/veo3/fast/image-to-video
      tags:
        - Fal-ai aggregation platform/falai-veo3 video generation
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: Text prompts describing how to animate the image
                image_url:
                  type: string
                  description: >-
                    The URL of the input image to be used to create the animation. The aspect ratio should be 720p or higher, with a 16:9 aspect ratio. If the image's aspect ratio is not 16:9, it will be cropped to fit.
                aspect_ratio:
                  type: string
                  description: The default aspect ratio for the generated video is "auto".
                duration:
                  type: string
                  description: The default value for the generated video duration (in seconds) is "8s".
                generate_audio:
                  type: boolean
                  description: Whether to generate audio for the video. If false, 33% of the points will be deducted. Default: true
                resolution:
                  type: string
                  description: The default resolution for generated videos is "720p". The range is [720p, 1080p].
              required:
                - prompt
                - image_url
              x-apifox-orders:
                - prompt
                - image_url
                - aspect_ratio
                - duration
                - generate_audio
                - resolution
            example:
              prompt: >-
                A woman looks into the camera, breathes in, then exclaims
                energetically, "have you guys checked out Veo3 Image-to-Video on
                Fal? It's incredible!"
              image_url: >-
                https://storage.googleapis.com/falserverless/example_inputs/veo3-i2v-input.png
              aspect_ratio: '16:9'
              duration: 8s
              generate_audio: true
              resolution: 720p
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                status: IN_QUEUE
                request_id: 1b24b3ae-16a2-4d19-b10d-1e323ebff061
                response_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/1b24b3ae-16a2-4d19-b10d-1e323ebff061
                status_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/1b24b3ae-16a2-4d19-b10d-1e323ebff061/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/veo3/requests/1b24b3ae-16a2-4d19-b10d-1e323ebff061/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform/falai-veo3 video generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-352888771-run
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
