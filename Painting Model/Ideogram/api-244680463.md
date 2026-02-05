# ideogram (or ideogram)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /ideogram/generate:
    post:
      summary: ideogram (or ideogram)
      deprecated: false
      description: >-
        Generates images synchronously based on a given prompt and optional
        parameters.

        For detailed parameters, please refer to the official documentation: https://developer.ideogram.ai/api-reference/api-reference/describe

        Generates images synchronously based on the given prompts and optional parameters.

        The returned image URL is valid for 24 hours; after that time, the image will be inaccessible.

        Image already reverse-promoted.
      tags:
        - Painting Model/Ideogram
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
                image_request:
                  type: object
                  properties:
                    prompt:
                      description: Prompt words for generating the image (required)
                      type: string
                    aspect_ratio:
                      description: >-
                        Image aspect ratio (optional)
                        Optional values:ASPECT_10_16/ASPECT_16_10/ASPECT_9_16/ASPECT_16_9/ASPECT_3_2/ASPECT_2_3/ASPECT_4_3/ASPECT_3_4/ASPECT_1_1/ASPECT_1_3/ASPECT_3_1
                      type: string
                    model:
                      description: The model used (optional) defaults to V_2, with possible values: V_1/V_1_TURBO/V_2/V_2_TURBO
                      type: string
                    magic_prompt_option:
                      description: Use MagicPrompt (optional) Optional values: AUTO/ON/OFF
                      type: string
                    seed:
                      description: Random seed (optional) Range: 0-2147483647
                      type: integer
                    style_type:
                      description: >-
                        Style Type (Optional)
                        Optional Values: AUTO/GENERAL/REALISTIC/DESIGN/RENDER_3D/ANIME
                      type: string
                    negative_prompt:
                      description: Reverse hints (optional) describe content you don't want to appear in the image.
                      type: string
                    num_images:
                      description: Number of images to generate (optional) Range: 1-8, default 1
                      type: integer
                    resolution:
                      description: Resolution (optional) Available values ​​include a variety of resolution combinations from 512x1536 to 1536x640.
                      type: string
                    color_palette:
                      type: object
                      properties:
                        name:
                          description: >-
                            Preset palette name (choose one from members)
                            Optional values: EMBER/FRESH/JUNGLE/MAGIC/MELON/MOSAIC/PASTEL/ULTRAMARINE
                          type: string
                      required:
                        - name
                      description: Color palette (optional)
                      x-apifox-orders:
                        - name
                  required:
                    - prompt
                    - aspect_ratio
                    - model
                    - magic_prompt_option
                    - seed
                    - style_type
                    - negative_prompt
                    - num_images
                    - resolution
                    - color_palette
                  description: Image request object (required)
                  x-apifox-orders:
                    - prompt
                    - aspect_ratio
                    - model
                    - magic_prompt_option
                    - seed
                    - style_type
                    - negative_prompt
                    - num_images
                    - resolution
                    - color_palette
              required:
                - image_request
              x-apifox-orders:
                - image_request
            example:
              image_request:
                aspect_ratio: ASPECT_10_16
                magic_prompt_option: AUTO
                model: V_1
                prompt: >-
                  A serene tropical beach scene. Dominating the foreground are
                  tall palm trees with lush green leaves, standing tall against
                  a backdrop of a sandy beach. The beach leads to the azure
                  waters of the sea, which gently kisses the shoreline. In the
                  distance, there is an island or landmass with a silhouette of
                  what appears to be a lighthouse or tower. The sky above is
                  painted with fluffy white clouds, some of which are tinged
                  with hues of pink and orange, suggesting either a sunrise or
                  sunset.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  created:
                    type: string
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        is_image_safe:
                          type: boolean
                        prompt:
                          type: string
                        resolution:
                          type: string
                        seed:
                          type: integer
                        style_type:
                          type: 'null'
                        url:
                          type: string
                required:
                  - created
                  - data
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model/Ideogram
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-244680463-run
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
