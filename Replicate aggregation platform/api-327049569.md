# Create task prunaai/vace-14b

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/prunaai/vace-14b/predictions:
    post:
      summary: Create task prunaai/vace-14b
      deprecated: false
      description: Official documentation:https://replicate.com/prunaai/vace-14b
      tags:
        - Replicate aggregation platform
      parameters:
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
                version:
                  type: string
                input:
                  type: object
                  properties:
                    seed:
                      type: integer
                      description: Random seed (-1 indicates random)
                    size:
                      type: string
                      description: Output resolution. Default: "832*480"
                    prompt:
                      type: string
                      description: Textual description.
                    src_mask:
                      type: string
                      description: Enter the mask video or image you want to edit.
                    frame_num:
                      type: integer
                      description: Number of frames to generate. Default: 81.
                    src_video:
                      type: string
                      description: Enter the video you want to edit.
                    speed_mode:
                      type: string
                      description: Speed ​​optimization level. Default: "Lightly Juiced 🍊 (more consistent)"
                    sample_shift:
                      type: integer
                      description: Sample offset. Default: 16
                    sample_steps:
                      type: integer
                      description: Example steps. Default: 50
                    sample_solver:
                      type: string
                      description: Sample solver. Default: "unipc"
                    src_ref_images:
                      type: array
                      items:
                        type: string
                      description: Input a reference image for editing.
                    sample_guide_scale:
                      type: integer
                      description: Sample guidance scale. Default: 5
                  required:
                    - prompt
                  x-apifox-orders:
                    - seed
                    - size
                    - prompt
                    - src_mask
                    - frame_num
                    - src_video
                    - speed_mode
                    - sample_shift
                    - sample_steps
                    - sample_solver
                    - src_ref_images
                    - sample_guide_scale
              x-apifox-orders:
                - version
                - input
            example:
              version: 51299232dc3d0946d5f5ed74935d85243e172698f747d291460db1e6ef3669fb
              input:
                seed: -1
                size: 1280*720
                prompt: >-
                  The video shows a man riding a horse on a vast grassland. He
                  has long lavender hair and wears a traditional dress of a
                  white top and black pants. The animation style makes him look
                  like he is doing some kind of outdoor activity or performing.
                  The background is a spectacular mountain range and cloud sky,
                  giving a sense of tranquility and vastness. The entire video
                  is shot from a fixed angle, focusing on the rider and his
                  horse.
                src_mask: >-
                  https://replicate.delivery/pbxt/N323tegI7AuoZmg0U5CuTKa7VBFC4gymhe0kT8Jk3o2sjUUj/src_mask.mp4
                frame_num: 81
                src_video: >-
                  https://replicate.delivery/pbxt/N323u1ljtNYyyaLrgw0ZLmXgepvWlBvxbJWi3sAa2VDPuNus/src_video.mp4
                speed_mode: Extra Juiced 🚀 (even more speed)
                sample_shift: 16
                sample_steps: 50
                sample_solver: unipc
                src_ref_images:
                  - >-
                    https://replicate.delivery/pbxt/N323t5X69JB1MPD4w4cDIxK4rm0BG0W2JOWBrDrR4O9HTcyp/src_ref_image_1.png
                sample_guide_scale: 5
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
                  model:
                    type: string
                  version:
                    type: string
                  input:
                    type: object
                    properties:
                      aspect_ratio:
                        type: string
                      input_image:
                        type: string
                      output_format:
                        type: string
                      prompt:
                        type: string
                      prompt_upsampling:
                        type: boolean
                      safety_tolerance:
                        type: integer
                    required:
                      - aspect_ratio
                      - input_image
                      - output_format
                      - prompt
                      - prompt_upsampling
                      - safety_tolerance
                  logs:
                    type: string
                  output:
                    type: 'null'
                  data_removed:
                    type: boolean
                  error:
                    type: 'null'
                  status:
                    type: string
                  created_at:
                    type: string
                  urls:
                    type: object
                    properties:
                      cancel:
                        type: string
                      get:
                        type: string
                      stream:
                        type: string
                      web:
                        type: string
                    required:
                      - cancel
                      - get
                      - stream
                      - web
                required:
                  - id
                  - model
                  - version
                  - input
                  - logs
                  - output
                  - data_removed
                  - error
                  - status
                  - created_at
                  - urls
              examples:
                '1':
                  summary: Create image
                  value:
                    created: 1589478378
                    data:
                      - url: https://...
                      - url: https://...
                '2':
                  summary: Successful examples
                  value:
                    id: w44zs9cet5rmc0cqzp49gpkhf8
                    model: black-forest-labs/flux-kontext-dev
                    version: hidden
                    input:
                      aspect_ratio: match_input_image
                      input_image: >-
                        https://replicate.delivery/xezq/XfwWjHJ7HfrmXE6ukuLVEpXWfeQ3PQeRI5mApuLXRxST7XMmC/tmpc91tlq20.png
                      output_format: jpg
                      prompt: Make the letters 3D, floating in space on a city street
                      prompt_upsampling: false
                      safety_tolerance: 2
                    logs: ''
                    output: null
                    data_removed: false
                    error: null
                    status: starting
                    created_at: '2025-07-12T07:27:54.577Z'
                    urls:
                      cancel: >-
                        https://api.replicate.com/v1/predictions/w44zs9cet5rmc0cqzp49gpkhf8/cancel
                      get: >-
                        https://api.replicate.com/v1/predictions/w44zs9cet5rmc0cqzp49gpkhf8
                      stream: >-
                        https://stream.replicate.com/v1/files/bcwr-h7bu76ujftxzwih5u35puoysogps56mqvpvjz4nrxskhfe7ks42a
                      web: https://replicate.com/p/w44zs9cet5rmc0cqzp49gpkhf8
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327049569-run
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
