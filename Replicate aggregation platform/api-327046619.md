# Create task google/imagen-4-ultra

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/google/imagen-4-ultra/predictions:
    post:
      summary: Create task google/imagen-4-ultra
      deprecated: false
      description: Official documentation:https://replicate.com/google/imagen-4-ultra
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
                      description: The format for the output image. Default: "jpg"
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
                  capturing the nostalgic warmth of a mid-2000s indie film. The
                  focus is a young woman with a sleek, straight bob haircut in
                  cool platinum white with freckled skin, looking directly and
                  intently into the camera lens with a knowing smirk, her head
                  is looking up slightly. She wears an oversized band t-shirt
                  that says "Imagen 4 Ultra on Replicate" in huge stylized text
                  over a long-sleeved striped top and simple silver stud
                  earrings. The lighting is soft, golden hour sunlight creating
                  lens flare and illuminating dust motes in the air. The
                  background shows a blurred outdoor urban setting with
                  graffiti-covered walls (the graffiti says "ultra" in stylized
                  graffiti lettering), rendered with a shallow depth of field.
                  Natural film grain, a warm, slightly muted color palette, and
                  sharp focus on her expressive eyes enhance the intimate,
                  authentic feel
                aspect_ratio: '16:9'
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
                id: het8zf0rtnrm80crb5gaw4ecdw
                model: google/imagen-4-ultra
                version: hidden
                input:
                  aspect_ratio: '16:9'
                  output_format: jpg
                  prompt: >-
                    The photo: Create a cinematic, photorealistic medium shot
                    capturing the nostalgic warmth of a mid-2000s indie film.
                    The focus is a young woman with a sleek, straight bob
                    haircut in cool platinum white with freckled skin, looking
                    directly and intently into the camera lens with a knowing
                    smirk, her head is looking up slightly. She wears an
                    oversized band t-shirt that says "Imagen 4 Ultra on
                    Replicate" in huge stylized text over a long-sleeved striped
                    top and simple silver stud earrings. The lighting is soft,
                    golden hour sunlight creating lens flare and illuminating
                    dust motes in the air. The background shows a blurred
                    outdoor urban setting with graffiti-covered walls (the
                    graffiti says "ultra" in stylized graffiti lettering),
                    rendered with a shallow depth of field. Natural film grain,
                    a warm, slightly muted color palette, and sharp focus on her
                    expressive eyes enhance the intimate, authentic feel
                  safety_filter_level: block_only_high
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T03:28:46.805Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/het8zf0rtnrm80crb5gaw4ecdw/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/het8zf0rtnrm80crb5gaw4ecdw
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-l5a4j53wjt36wq6hvdr5vt5zu2fuzpe3gfvygtciezllg7og3lpq
                  web: https://replicate.com/p/het8zf0rtnrm80crb5gaw4ecdw
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327046619-run
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
