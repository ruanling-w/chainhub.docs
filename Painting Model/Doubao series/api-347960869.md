# doubao-seedream-4-0-250828-Text-to-Image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/images/generations:
    post:
      summary: doubao-seedream-4-0-250828-Text-to-Image
      deprecated: false
      description: |+
        Given a prompt and/or input image, the model will generate a new image.

        Related guide: [Image Generation](https://www.volcengine.com/docs/82379/1666946)

        Create an image based on the prompt.

      tags:
        - Painting Model/Doubao Series
      parameters:
        - name: Authorization
          in: header
          description: ""
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
                model:
                  type: string
                  description: Model ID used for this request.
                prompt:
                  type: string
                  description: Prompt for image generation, supports Chinese and English.
                size:
                  type: string
                  description: |-
                    Specify the size information for the generated image. Two methods are supported, not to be mixed.
                    Method 1 | Specify the resolution of the generated image. Optional values: 1K, 2K, 4K
                    Method 2 | Specify the width and height in pixels. Default: 2048x2048
                    Area range: [1024x1024, 4096x4096]
                    Aspect ratio range: [1/16, 16]
                sequential_image_generation:
                  type: string
                  description: |-
                    Control whether to disable the multi-image feature. Default is disabled.
                    Value range:
                    auto: Automatic mode, the model will decide whether to return multiple images and how many based on the prompt.
                    disabled: Disable multi-image feature, the model will generate only one image.
                stream:
                  type: boolean
                  description: Control whether to enable streaming output mode. Default is false.
                response_format:
                  type: string
                  description: |-
                    Specify the return format of the generated image. Default is url.
                    The generated image is in jpeg format, and the following two return methods are supported:
                    url: Return a download link for the image; the link is valid for 24 hours after image generation, please download the image promptly.
                    b64_json: Return the image data as a Base64-encoded JSON string.
                watermark:
                  type: boolean
                  description: |-
                    Whether to add a watermark to the generated image. Default is true.
                    false: Do not add a watermark.
                    true: Add a watermark with the text "AI Generated" in the lower right corner of the image.
              required:
                - model
                - prompt
              x-apifox-orders:
                - model
                - prompt
                - size
                - sequential_image_generation
                - stream
                - response_format
                - watermark
            example:
              model: doubao-seedream-4-0-250828
              prompt: >-
                Interstellar travel, black hole, a nearly shattered vintage train rushing out of the black hole, strong visual impact, cinematic blockbuster, apocalyptic vibe, dynamic, contrasting colors, oc rendering, ray tracing, motion blur, depth of field, surrealism, deep blue, the picture shapes the subject and scene through delicate and rich color layers, realistic texture, light and shadow effects of a dark background create atmosphere, overall artistic fantasy, exaggerated wide-angle perspective, glare, reflection, ultimate light and shadow, strong gravity, devouring
              size: 1728x2304
              sequential_image_generation: disabled
              stream: false
              response_format: url
              watermark: true
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                  created:
                    type: integer
                  usage:
                    type: object
                    properties:
                      prompt_tokens:
                        type: integer
                      completion_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                      prompt_tokens_details:
                        type: object
                        properties:
                          cached_tokens_details:
                            type: object
                            properties: {}
                        required:
                          - cached_tokens_details
                      completion_tokens_details:
                        type: object
                        properties: {}
                      output_tokens:
                        type: integer
                    required:
                      - prompt_tokens
                      - completion_tokens
                      - total_tokens
                      - prompt_tokens_details
                      - completion_tokens_details
                      - output_tokens
                required:
                  - data
                  - created
                  - usage
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model/Doubao Series
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-347960869-run
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
