# Generate 3.0 (Text-based Image Generator)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /ideogram/v1/ideogram-v3/generate:
    post:
      summary: "Generate 3.0 (Text-based Image Generator) "
      deprecated: false
      description: >-
        Using the Ideogram 3.0 model, synchronously generate images based on given prompts and optional parameters.

        For specific parameters, please refer to the official documentation: https://developer.ideogram.ai/api-reference/api-reference/generate-v3

        The returned image URL is valid for 24 hours; after that time, the image will be inaccessible.

        Image already de-promoted.
      tags:
        - Painting Model/Ideogram
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
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
                prompt:
                  type: string
                  description: Prompt text required to generate the image
                seed:
                  type: integer
                  minimum: 0
                  maximum: 2147483647
                  description: Random seed. Setting this value will result in repeatable generation results.
                resolution:
                  type: string
                  enum:
                    - 512x1536
                    - 576x1408
                    - 576x1472
                    - 576x1536
                    - 640x1344
                    - 640x1408
                    - 640x1472
                    - 640x1536
                    - 704x1152
                    - 704x1216
                    - 704x1280
                    - 704x1344
                    - 704x1408
                    - 704x1472
                    - 736x1312
                    - 768x1088
                    - 768x1216
                    - 768x1280
                    - 768x1344
                    - 800x1280
                    - 832x960
                    - 832x1024
                    - 832x1088
                    - 832x1152
                    - 832x1216
                    - 832x1248
                    - 864x1152
                    - 896x960
                    - 896x1024
                    - 896x1088
                    - 896x1120
                    - 896x1152
                    - 960x832
                    - 960x896
                    - 960x1024
                    - 960x1088
                    - 1024x832
                    - 1024x896
                    - 1024x960
                    - 1024x1024
                    - 1088x768
                    - 1088x832
                    - 1088x896
                    - 1088x960
                    - 1120x896
                    - 1152x704
                    - 1152x832
                    - 1152x864
                    - 1152x896
                    - 1216x704
                    - 1216x768
                    - 1216x832
                    - 1248x832
                    - 1280x704
                    - 1280x768
                    - 1280x800
                    - 1312x736
                    - 1344x640
                    - 1344x704
                    - 1344x768
                    - 1408x576
                    - 1408x640
                    - 1408x704
                    - 1472x576
                    - 1472x640
                    - 1472x704
                    - 1536x512
                    - 1536x576
                    - 1536x640
                  description: Supported resolution options
                aspect_ratio:
                  type: string
                  enum:
                    - 1x3
                    - 3x1
                    - 1x2
                    - 2x1
                    - 9x16
                    - 16x9
                    - 10x16
                    - 16x10
                    - 2x3
                    - 3x2
                    - 3x4
                    - 4x3
                    - 4x5
                    - 5x4
                    - 1x1
                  description: The aspect ratio used for image generation determines the image resolution. It cannot be used simultaneously with the `resolution` parameter. The default value is 1x1.
                rendering_speed:
                  type: string
                  enum:
                    - TURBO
                    - DEFAULT
                    - QUALITY
                  default: DEFAULT
                  description: Rendering speed options
                magic_prompt:
                  type: string
                  enum:
                    - AUTO
                    - "ON"
                    - "OFF"
                  description: Decide whether to use Magic Prompt when generating requests.
                negative_prompt:
                  type: string
                  description: Describe what needs to be excluded from the image. The description in the prompt takes precedence over the description in the negative prompt.
                num_images:
                  type: integer
                  minimum: 1
                  maximum: 8
                  default: 1
                  description: Number of images to be generated
                color_palette:
                  type: object
                  description: The generated color palette must be explicitly specified either by one of the presets (name) or by the hexadecimal representation of the colors with optional weights (members).
                  oneOf:
                    - type: object
                      properties:
                        name:
                          type: string
                          description: Preset palette names
                      required:
                        - name
                      additionalProperties: false
                      x-apifox-orders:
                        - name
                    - type: object
                      properties:
                        members:
                          type: array
                          items:
                            type: object
                            properties:
                              color:
                                type: string
                                pattern: ^#[0-9A-Fa-f]{6}$
                                description: Hexadecimal representation of color
                              weight:
                                type: number
                                description: Color weight
                            required:
                              - color
                            additionalProperties: false
                            x-apifox-orders:
                              - color
                              - weight
                      required:
                        - members
                      additionalProperties: false
                      x-apifox-orders:
                        - members
                  x-apifox-orders: []
                  properties: {}
                style_codes:
                  type: array
                  items:
                    type: string
                    pattern: ^[0-9A-Fa-f]{8}$
                  description: A list of 8-character hexadecimal codes representing the image style. Cannot be used with style_reference_images or style_type.
                style_type:
                  type: string
                  enum:
                    - AUTO
                    - GENERAL
                    - REALISTIC
                    - DESIGN
                  default: GENERAL
                  description: Style type to generate
              required:
                - prompt
              dependencies:
                resolution:
                  not:
                    required:
                      - aspect_ratio
                aspect_ratio:
                  not:
                    required:
                      - resolution
                style_codes:
                  not:
                    required:
                      - style_reference_images
                      - style_type
              x-apifox-orders:
                - prompt
                - seed
                - resolution
                - aspect_ratio
                - rendering_speed
                - magic_prompt
                - negative_prompt
                - num_images
                - color_palette
                - style_codes
                - style_type
            example:
              prompt: voluptate reprehenderit
              seed: 511526458
              rendering_speed: DEFAULT
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                  message:
                    type: string
                  request_id:
                    type: string
                  data:
                    type: object
                    properties:
                      task_id:
                        type: string
                      task_status:
                        type: string
                      created_at:
                        type: integer
                      updated_at:
                        type: integer
                    required:
                      - task_id
                      - task_status
                      - created_at
                      - updated_at
                required:
                  - code
                  - message
                  - request_id
                  - data
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model/Ideogram
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-295835676-run
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
