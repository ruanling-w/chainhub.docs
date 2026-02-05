# Create task andreasjansson/stable-diffusion-animation

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/predictions:
    post:
      summary: Create task andreasjansson/stable-diffusion-animation
      deprecated: false
      description: Official documentation:https://replicate.com/andreasjansson/stable-diffusion-animation
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
                    width:
                      type: integer
                      description: Output image width. Default value: 512.
                    height:
                      type: integer
                      description: Output image height. Default value: 512.
                    prompt_end:
                      type: string
                      description: A prompt that appears when the animation ends. You can use | (vertical bar symbol) to separate multiple prompts, thus including multiple prompts.
                    prompt_start:
                      type: string
                      description: The animation begins.
                    gif_ping_pong:
                      type: boolean
                      description: Whether to reverse the animation and return to the beginning before the loop. Default: false
                    output_format:
                      type: string
                      description: Output file format. Default: "gif".
                    guidance_scale:
                      type: number
                      description: Guide strength. Default: 7.5. Minimum: 1, Maximum: 20.
                    prompt_strength:
                      type: number
                      description: Lower cue strength generates more coherent GIFs, while higher cue strength generates more but may result in jumps. Default: 0.8.
                    film_interpolation:
                      type: boolean
                      description: Whether to use FILM for inter-frame interpolation (film-net.github.io) Default: true
                    intermediate_output:
                      type: boolean
                      description: Whether to display intermediate output during the generation process. Default: false
                    num_inference_steps:
                      type: integer
                      description: Number of denoising steps. Default: 50. Minimum: 1, Maximum: 500.
                    num_animation_frames:
                      type: integer
                      description: Animation frame rate. Default: 10. Minimum: 2, Maximum: 50.
                    gif_frames_per_second:
                      type: integer
                      description: Outputs GIF frames per second. Default: 20. Minimum: 1, Maximum: 50.
                    num_interpolation_steps:
                      type: integer
                      description: The number of steps inserted between animation frames. Default: 5. Minimum: 1, Maximum: 50.
                  required:
                    - prompt_end
                    - prompt_start
                  x-apifox-orders:
                    - width
                    - height
                    - prompt_end
                    - prompt_start
                    - gif_ping_pong
                    - output_format
                    - guidance_scale
                    - prompt_strength
                    - film_interpolation
                    - intermediate_output
                    - num_inference_steps
                    - num_animation_frames
                    - gif_frames_per_second
                    - num_interpolation_steps
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                andreasjansson/stable-diffusion-animation:ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5
              input:
                width: 512
                height: 512
                prompt_end: >-
                  tall rectangular black monolith, a white room in the future
                  with a bed, victorian details and a tall black monolith, a
                  detailed matte painting by Wes Anderson, behance, light and
                  space, reimagined by industrial light and magic, matte
                  painting, criterion collection
                prompt_start: >-
                  tall rectangular black monolith, monkeys in the desert looking
                  at a large tall monolith, a detailed matte painting by Wes
                  Anderson, behance, light and space, reimagined by industrial
                  light and magic, matte painting, criterion collection
                gif_ping_pong: true
                output_format: mp4
                guidance_scale: 7.5
                prompt_strength: 0.9
                film_interpolation: true
                intermediate_output: false
                num_inference_steps: 50
                num_animation_frames: 25
                gif_frames_per_second: 20
                num_interpolation_steps: 5
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
              example:
                id: 8qnr2j4kynrj00crapbtfewwdg
                model: andreasjansson/stable-diffusion-animation
                version: >-
                  ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5
                input:
                  film_interpolation: true
                  gif_frames_per_second: 20
                  gif_ping_pong: true
                  guidance_scale: 7.5
                  height: 512
                  intermediate_output: false
                  num_animation_frames: 25
                  num_inference_steps: 50
                  num_interpolation_steps: 5
                  output_format: mp4
                  prompt_end: >-
                    tall rectangular black monolith, a white room in the future
                    with a bed, victorian details and a tall black monolith, a
                    detailed matte painting by Wes Anderson, behance, light and
                    space, reimagined by industrial light and magic, matte
                    painting, criterion collection
                  prompt_start: >-
                    tall rectangular black monolith, monkeys in the desert
                    looking at a large tall monolith, a detailed matte painting
                    by Wes Anderson, behance, light and space, reimagined by
                    industrial light and magic, matte painting, criterion
                    collection
                  prompt_strength: 0.9
                  width: 512
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-29T09:50:53.941Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/8qnr2j4kynrj00crapbtfewwdg/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/8qnr2j4kynrj00crapbtfewwdg
                  stream: >-
                    https://stream.replicate.com/v1/files/qoxq-lpghpenswbt2fqhz7xaggbmesoqxvt4h3ralq47fkfdcsgf2jmuq
                  web: https://replicate.com/p/8qnr2j4kynrj00crapbtfewwdg
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326479811-run
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
