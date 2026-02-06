# Query a single task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /luma/generations/{task_id}:
    get:
      summary: Query a single task
      deprecated: false
      description: '"state": "completed" enumeration values: "pending", "processing", "completed", "failed"'
      tags:
        - Video Model/Luma Video Generation/Query Task
      parameters:
        - name: task_id
          in: path
          description: Task ID
          required: true
          example: 4665a07c-7641-4809-a133-10786201bb56
          schema:
            type: string
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
                  state:
                    type: string
                  video:
                    type: object
                    properties:
                      url:
                        type: string
                      width:
                        type: integer
                      height:
                        type: integer
                      download_url:
                        type: string
                    required:
                      - url
                      - width
                      - height
                      - download_url
                  request:
                    type: object
                    properties:
                      prompt:
                        type: string
                      aspect_ratio:
                        type: string
                    required:
                      - prompt
                      - aspect_ratio
                  artifact:
                    type: object
                    properties:
                      video:
                        type: object
                        properties:
                          url:
                            type: string
                          width:
                            type: integer
                          height:
                            type: integer
                          download_url:
                            type: string
                        required:
                          - url
                          - width
                          - height
                          - download_url
                      thumbnail:
                        type: object
                        properties:
                          url:
                            type: string
                          width:
                            type: integer
                          height:
                            type: integer
                          palette:
                            type: object
                            properties:
                              grid:
                                type: string
                            required:
                              - grid
                          media_type:
                            type: string
                        required:
                          - url
                          - width
                          - height
                          - palette
                          - media_type
                      video_raw:
                        type: object
                        properties:
                          url:
                            type: string
                          width:
                            type: integer
                          height:
                            type: integer
                          duration:
                            type: number
                          media_type:
                            type: string
                        required:
                          - url
                          - width
                          - height
                          - duration
                          - media_type
                      created_at:
                        type: string
                      last_frame:
                        type: object
                        properties:
                          url:
                            type: string
                          width:
                            type: integer
                          height:
                            type: integer
                          palette:
                            type: 'null'
                          media_type:
                            type: string
                        required:
                          - url
                          - width
                          - height
                          - palette
                          - media_type
                    required:
                      - video
                      - thumbnail
                      - video_raw
                      - created_at
                      - last_frame
                  thumbnail:
                    type: object
                    properties:
                      url:
                        type: string
                      width:
                        type: integer
                      height:
                        type: integer
                      palette:
                        type: object
                        properties:
                          grid:
                            type: string
                        required:
                          - grid
                      media_type:
                        type: string
                    required:
                      - url
                      - width
                      - height
                      - palette
                      - media_type
                  video_raw:
                    type: object
                    properties:
                      url:
                        type: string
                      width:
                        type: integer
                      height:
                        type: integer
                      duration:
                        type: number
                      media_type:
                        type: string
                    required:
                      - url
                      - width
                      - height
                      - duration
                      - media_type
                  created_at:
                    type: string
                  last_frame:
                    type: object
                    properties:
                      url:
                        type: string
                      width:
                        type: integer
                      height:
                        type: integer
                      palette:
                        type: 'null'
                      media_type:
                        type: string
                    required:
                      - url
                      - width
                      - height
                      - palette
                      - media_type
                required:
                  - id
                  - state
                  - video
                  - request
                  - artifact
                  - thumbnail
                  - video_raw
                  - created_at
                  - last_frame
              example:
                id: 4665a07c-7641-4809-a133-10786201bb56
                state: completed
                video:
                  url: >-
                    https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                  width: 1360
                  height: 752
                  download_url: >-
                    https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                request:
                  prompt: cat dance
                  aspect_ratio: '16:9'
                artifact:
                  video:
                    url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                    width: 1360
                    height: 752
                    download_url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                  thumbnail:
                    url: >-
                      https://imagedelivery.net/1KomXrSWiTojGGip43n0SQ/e4268de5-4a74-45ff-67b8-dc46df12de00/public
                    width: 1360
                    height: 752
                    palette:
                      grid: >-
                        em9csKqXYUgqdHVmmqeZLB8YaFpLjVw2bmFTTElBHhMNTzgodD8eVzUeTDorRSkYYEQymV80e1M0ck0ugWVRwKCApWk0hF1BgmVP
                    media_type: image
                  video_raw:
                    url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                    width: 1360
                    height: 752
                    duration: 5.041667
                    media_type: video
                  created_at: '0001-01-01T00:00:00Z'
                  last_frame:
                    url: >-
                      https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/606108d9-9daf-4265-84fb-595f18240ac5/video_0_last_frame.jpg
                    width: 1360
                    height: 752
                    palette: null
                    media_type: image
                thumbnail:
                  url: >-
                    https://imagedelivery.net/1KomXrSWiTojGGip43n0SQ/e4268de5-4a74-45ff-67b8-dc46df12de00/public
                  width: 1360
                  height: 752
                  palette:
                    grid: >-
                      em9csKqXYUgqdHVmmqeZLB8YaFpLjVw2bmFTTElBHhMNTzgodD8eVzUeTDorRSkYYEQymV80e1M0ck0ugWVRwKCApWk0hF1BgmVP
                  media_type: image
                video_raw:
                  url: >-
                    https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/35049450-c008-4607-b1d0-0b025599f15d/video0b6619468da8e409da860706bbf26bbad.mp4
                  width: 1360
                  height: 752
                  duration: 5.041667
                  media_type: video
                created_at: '2024-12-22T13:38:40.139Z'
                last_frame:
                  url: >-
                    https://storage.cdn-luma.com/dream-machine/b0d67582-c6f0-4973-a89c-3fea9d46d5e9/606108d9-9daf-4265-84fb-595f18240ac5/video_0_last_frame.jpg
                  width: 1360
                  height: 752
                  palette: null
                  media_type: image
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Luma Video Generation/Query Task
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-247123648-run
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
