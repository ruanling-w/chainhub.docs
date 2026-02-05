# Create task google/imagen-4

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/google/imagen-4/predictions:
    post:
      summary: Create task google/imagen-4
      deprecated: false
      description: Official documentation:https://replicate.com/google/imagen-4
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
                      description: The aspect ratio of the generated image. Default: "1:1". Supported aspect ratios: 1:1, 9:16, 16:9, 3:4, 4:3
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
                  capturing the nostalgic warmth of a late 90s indie film. The
                  focus is a young woman with brightly dyed pink-gold hair and
                  freckled skin, looking directly and intently into the camera
                  lens with a hopeful yet slightly uncertain smile, she is
                  slightly off-center. She wears an oversized, vintage band
                  t-shirt that says "Replicate" (slightly worn) over a
                  long-sleeved striped top and simple silver stud earrings. The
                  lighting is soft, golden hour sunlight streaming through a
                  slightly dusty window, creating lens flare and illuminating
                  dust motes in the air. The background shows a blurred,
                  cluttered bedroom with posters on the wall and fairy lights,
                  rendered with a shallow depth of field. Natural film grain, a
                  warm, slightly muted color palette, and sharp focus on her
                  expressive eyes enhance the intimate, authentic feel
                aspect_ratio: '16:9'
                output_format: jpg
                safety_filter_level: block_medium_and_above
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
                      output_format:
                        type: string
                      prompt:
                        type: string
                      safety_filter_level:
                        type: string
                    required:
                      - aspect_ratio
                      - output_format
                      - prompt
                      - safety_filter_level
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
                id: yj1hjjc3c5rme0crb5jtqtxxmw
                model: google/imagen-4
                version: hidden
                input:
                  aspect_ratio: '16:9'
                  output_format: jpg
                  prompt: >-
                    The photo: Create a cinematic, photorealistic medium shot
                    capturing the nostalgic warmth of a late 90s indie film. The
                    focus is a young woman with brightly dyed pink-gold hair and
                    freckled skin, looking directly and intently into the camera
                    lens with a hopeful yet slightly uncertain smile, she is
                    slightly off-center. She wears an oversized, vintage band
                    t-shirt that says "Replicate" (slightly worn) over a
                    long-sleeved striped top and simple silver stud earrings.
                    The lighting is soft, golden hour sunlight streaming through
                    a slightly dusty window, creating lens flare and
                    illuminating dust motes in the air. The background shows a
                    blurred, cluttered bedroom with posters on the wall and
                    fairy lights, rendered with a shallow depth of field.
                    Natural film grain, a warm, slightly muted color palette,
                    and sharp focus on her expressive eyes enhance the intimate,
                    authentic feel
                  safety_filter_level: block_medium_and_above
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T03:34:41.761Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/yj1hjjc3c5rme0crb5jtqtxxmw/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/yj1hjjc3c5rme0crb5jtqtxxmw
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-wzn4sniemyumrzyhr364uivh625z7wk5w2qlbvbzqci3lgvzhwrq
                  web: https://replicate.com/p/yj1hjjc3c5rme0crb5jtqtxxmw
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327048219-run
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
