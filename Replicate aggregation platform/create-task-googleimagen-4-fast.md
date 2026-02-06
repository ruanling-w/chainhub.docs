# Create task google/imagen-4-fast

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/google/imagen-4-fast/predictions:
    post:
      summary: Create task google/imagen-4-fast
      deprecated: false
      description: Official documentation:https://replicate.com/google/imagen-4-fast
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
                input:
                  type: object
                  properties:
                    prompt:
                      type: string
                      description: Text prompts generated from images.
                    aspect_ratio:
                      type: string
                      description: Aspect ratio of the generated image. Default: "1:1".
                    output_format:
                      type: string
                      description: The format of the output image. Default: "jpg".
                    safety_filter_level:
                      type: string
                      description: >-
                        block_low_and_above is the strictest; block_medium_and_above will block some prompts; block_only_high is the most permissive, but some prompts may still be blocked. Default: "block_only_high".
                  required:
                    - prompt
                  x-apifox-orders:
                    - prompt
                    - aspect_ratio
                    - output_format
                    - safety_filter_level
              x-apifox-orders:
                - input
            example:
              input:
                prompt: >-
                  The photo: Create a cinematic, photorealistic medium shot
                  capturing the dynamic energy of a high-octane action film. The
                  focus is a young woman with wind-swept dark hair streaked with
                  pink highlights and determined features, looking directly and
                  intently into the camera lens, she is slightly off-center. She
                  wears a fitted pink and gold racing jacket over a black tank
                  top with "Imagen 4 Fast" in motion-stylized lettering and on
                  the next line "on Replicate" emblazoned across the chest and
                  aviator sunglasses pushed up on her head. The lighting is
                  dramatic with motion blur streaks and neon reflections from
                  passing city lights, creating dynamic lens flares and light
                  trails (they do not cover her face). The background shows a
                  blurred urban nightscape with streaking car headlights and
                  illuminated skyscrapers rushing past, rendered with heavy
                  motion blur and shallow depth of field. High contrast
                  lighting, vibrant neon color palette with deep blues and
                  electric yellows, and razor-sharp focus on her intense eyes
                  enhance the fast-paced, electrifying atmosphere. She is
                  illuminated while the background is darker.
                aspect_ratio: '4:3'
                output_format: jpg
                safety_filter_level: block_only_high
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
                id: 20z778rke5rm80crb5982z0m1g
                model: google/imagen-4-fast
                version: hidden
                input:
                  aspect_ratio: '4:3'
                  output_format: jpg
                  prompt: >-
                    The photo: Create a cinematic, photorealistic medium shot
                    capturing the dynamic energy of a high-octane action film.
                    The focus is a young woman with wind-swept dark hair
                    streaked with pink highlights and determined features,
                    looking directly and intently into the camera lens, she is
                    slightly off-center. She wears a fitted pink and gold racing
                    jacket over a black tank top with "Imagen 4 Fast" in
                    motion-stylized lettering and on the next line "on
                    Replicate" emblazoned across the chest and aviator
                    sunglasses pushed up on her head. The lighting is dramatic
                    with motion blur streaks and neon reflections from passing
                    city lights, creating dynamic lens flares and light trails
                    (they do not cover her face). The background shows a blurred
                    urban nightscape with streaking car headlights and
                    illuminated skyscrapers rushing past, rendered with heavy
                    motion blur and shallow depth of field. High contrast
                    lighting, vibrant neon color palette with deep blues and
                    electric yellows, and razor-sharp focus on her intense eyes
                    enhance the fast-paced, electrifying atmosphere. She is
                    illuminated while the background is darker.
                  safety_filter_level: block_only_high
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T03:13:27.921Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/20z778rke5rm80crb5982z0m1g/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/20z778rke5rm80crb5982z0m1g
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-blsi6mnoqvfndurpci2t2i77xl2s3k3xb5r5hru3xwyrev6v7uca
                  web: https://replicate.com/p/20z778rke5rm80crb5982z0m1g
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327045600-run
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
