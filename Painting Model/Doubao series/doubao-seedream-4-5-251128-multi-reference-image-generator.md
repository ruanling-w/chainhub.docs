# doubao-seedream-4-5-251128 Multi-Reference Image to Multi-Image

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
      summary: doubao-seedream-4-5-251128  Multi-Reference Image to Multi-Image
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
              model: doubao-seedream-4-5-251128
              prompt: Generate 3 images of a girl and a cow plush toy happily riding a roller coaster in an amusement park, covering morning, noon, and night
              image:
                - >-
                  https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_imagesToimages_1.png
                - >-
                  https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_imagesToimages_2.png
              sequential_image_generation: auto
              sequential_image_generation_options:
                max_images: 3
              size: 2K
              watermark: false
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
              example:
                data:
                  - url: >-
                      https://ark-content-generation-v2-cn-beijing.tos-cn-beijing.volces.com/doubao-seedream-4-0/0217574690542070fa6ef8c2347680bd87fd8d357bb16f1e5ca0f_0.jpeg?X-Tos-Algorithm=TOS4-HMAC-SHA256&X-Tos-Credential={{YOUR_ACCESS_KEY_ID}}%2F20250910%2Fcn-beijing%2Ftos%2Frequest&X-Tos-Date=20250910T015107Z&X-Tos-Expires=86400&X-Tos-Signature=fbc5369be594d6e21be983ed1ec32463b5f82cf0c18c4349e477c11e51e55fa0&X-Tos-SignedHeaders=host
                created: 1757469067
                usage:
                  prompt_tokens: 0
                  completion_tokens: 0
                  total_tokens: 15908
                  prompt_tokens_details:
                    cached_tokens_details: {}
                  completion_tokens_details: {}
                  output_tokens: 15908
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model/Doubao Series
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386006898-run
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
