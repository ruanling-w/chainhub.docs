# Batch retrieval tasks

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /luma/tasks:
    post:
      summary: Batch retrieval tasks
      deprecated: f'"state": "completed" enumeration values: "pending", "processing", "completed", "failed"'
      tags:
        - Video Model/Luma Video Generation/Query Task
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
          required: true
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
                  description: The model used is optional; the default is kling-image.
                  type: string
                prompt:
                  description: Positive prompt, required, describes the content you want to generate, cannot exceed 500 characters.
                  type: string
                negative_prompt:
                  description: Negative prompt, optional, describes the elements you don't want to appear in the image, cannot exceed 200 characters.
                  type: string
                image:
                  description: >-
                    Reference image, optional, supports Base64 encoding or image URL, supports .jpg/.jpeg/.png format, size cannot exceed 10MB
                  type: string
                image_fidelity:
                  description: The influence intensity of the reference image, optional, the value range is 0-1, the larger the value, the closer the generated image is to the reference image.
                  type: number
                'n':
                  description: The number of images to generate, optional, the value range is 1-9.
                  type: integer
                aspect_ratio:
                  description: The aspect ratio of the generated image, optional, optional values: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3
                  type: string
                callback_url:
                  description: Callback notification address, optional, when the task status changes, the system will send a notification to this address.
                  type: string
              required:
                - model
                - prompt
                - negative_prompt
                - image
                - image_fidelity
                - 'n'
                - aspect_ratio
                - callback_url
              x-apifox-orders:
                - model
                - prompt
                - negative_prompt
                - image
                - image_fidelity
                - 'n'
                - aspect_ratio
                - callback_url
            example:
              ids:
                - 4665a07c-7641-4809-a133-10786201bb56
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    artifact:
                      type: object
                      properties:
                        created_at:
                          type: string
                        last_frame:
                          type: object
                          properties:
                            height:
                              type: integer
                            media_type:
                              type: string
                            palette:
                              type: 'null'
                            url:
                              type: string
                            width:
                              type: integer
                          required:
                            - height
                            - media_type
                            - palette
                            - url
                            - width
                        thumbnail:
                          type: object
                          properties:
                            height:
                              type: integer
                            media_type:
                              type: string
                            palette:
                              type: object
                              properties:
                                grid:
                                  type: string
                              required:
                                - grid
                            url:
                              type: string
                            width:
                              type: integer
                          required:
                            - height
                            - media_type
                            - palette
                            - url
                            - width
                        video:
                          type: object
                          properties:
                            download_url:
                              type: string
                            height:
                              type: integer
                            url:
                              type: string
                            width:
                              type: integer
                          required:
                            - download_url
                            - height
                            - url
                            - width
                        video_raw:
                          type: object
                          properties:
                            duration:
                              type: number
                            height:
                              type: integer
                            media_type:
                              type: string
                            url:
                              type: string
                            width:
                              type: integer
                          required:
                            - duration
                            - height
                            - media_type
                            - url
                            - width
                      required:
                        - created_at
                        - last_frame
                        - thumbnail
                        - video
                        - video_raw
                    created_at:
                      type: string
                    id:
                      type: string
                    last_frame:
                      type: object
                      properties:
                        height:
                          type: integer
                        media_type:
                          type: string
                        palette:
                          type: 'null'
                        url:
                          type: string
                        width:
                          type: integer
                      required:
                        - height
                        - media_type
                        - palette
                        - url
                        - width
                    request:
                      type: object
                      properties:
                        aspect_ratio:
                          type: string
                        prompt:
                          type: string
                      required:
                        - aspect_ratio
                        - prompt
                    state:
                      type: string
                    thumbnail:
                      type: object
                      properties:
                        height:
                          type: integer
                        media_type:
                          type: string
                        palette:
                          type: object
                          properties:
                            grid:
                              type: string
                          required:
                            - grid
                        url:
                          type: string
                        width:
                          type: integer
                      required:
                        - height
                        - media_type
                        - palette
                        - url
                        - width
                    video:
                      type: object
                      properties:
                        download_url:
                          type: string
                        height:
                          type: integer
                        url:
                          type: string
                        width:
                          type: integer
                      required:
                        - download_url
                        - height
                        - url
                        - width
                    video_raw:
                      type: object
                      properties:
                        duration:
                          type: number
                        height:
                          type: integer
                        media_type:
                          type: string
                        url:
                          type: string
                        width:
                          type: integer
                      required:
                        - duration
                        - height
                        - media_type
                        - url
                        - width
              example:
                - artifact:
                    created_at: '0001-01-01T00:00:00Z'
                    last_frame:
                      height: 752
                      media_type: image
                      palette: null
                      url: >-
                        https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/606108d9-9daf-4265-84fb-595f18240ac5/video_0_last_frame.jpg
                      width: 1360
                    thumbnail:
                      height: 752
                      media_type: image
                      palette:
                        grid: >-
                          em9csKqXYUgqdHVmmqeZLB8YaFpLjVw2bmFTTElBHhMNTzgodD8eVzUeTDorRSkYYEQymV80e1M0ck0ugWVRwKCApWk0hF1BgmVP
                      url: >-
                        https://imagedelivery.net/1KomXrSWiTojGGip43n0SQ/e4268de5-4a74-45ff-67b8-dc46df12de00/public
                      width: 1360
                    video:
                      download_url: >-
                        https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                      height: 752
                      url: >-
                        https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                      width: 1360
                    video_raw:
                      duration: 5.041667
                      height: 752
                      media_type: video
                      url: >-
                        https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                      width: 1360
                  created_at: '2024-12-22T13:38:40.139Z'
                  id: 4665a07c-7641-4809-a133-10786201bb56
                  last_frame:
                    height: 752
                    media_type: image
                    palette: null
                    url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/606108d9-9daf-4265-84fb-595f18240ac5/video_0_last_frame.jpg
                    width: 1360
                  request:
                    aspect_ratio: '16:9'
                    prompt: cat dance
                  state: completed
                  thumbnail:
                    height: 752
                    media_type: image
                    palette:
                      grid: >-
                        em9csKqXYUgqdHVmmqeZLB8YaFpLjVw2bmFTTElBHhMNTzgodD8eVzUeTDorRSkYYEQymV80e1M0ck0ugWVRwKCApWk0hF1BgmVP
                    url: >-
                      https://imagedelivery.net/1KomXrSWiTojGGip43n0SQ/e4268de5-4a74-45ff-67b8-dc46df12de00/public
                    width: 1360
                  video:
                    download_url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                    height: 752
                    url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                    width: 1360
                  video_raw:
                    duration: 5.041667
                    height: 752
                    media_type: video
                    url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                    width: 1360
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Luma Video Generation/Query Task
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-247123658-run
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
