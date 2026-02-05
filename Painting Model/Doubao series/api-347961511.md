# doubao-seedream-4-0-250828-Image-to-Image

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
      summary: doubao-seedream-4-0-250828-Image-to-Image
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
                  description: >-
                    Prompt for image generation, supports Chinese and English.

                    It is recommended not to exceed 300 Chinese characters or 600 English words. Too much text may scatter information, causing the model to ignore details and focus only on the main points, resulting in missing elements in the generated image.
                image:
                  type: string
                  description: >-
                    Input image information, supports URL or Base64 encoding. doubao-seedream-4.0 supports single or multiple image input.

                    Image URL: Please ensure the image URL is accessible.

                    Base64 encoding: Please follow this format data:image/<image_format>;base64,<Base64_encoding>. Note <image_format> should be lowercase, e.g., data:image/png;base64,<base64_image>.
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
                - image
                - size
                - sequential_image_generation
                - stream
                - response_format
                - watermark
            example:
              model: doubao-seedream-4-0-250828
              prompt: Generate a close-up image of a dog lying on the grass
              image: >-
                https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_imageToimage.png
              size: 1728x2304
              sequential_image_generation: disabled
              stream: false
              response_format: url
              watermark: false
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  created:
                    type: integer
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                      required:
                        - url
                      x-apifox-orders:
                        - url
                required:
                  - created
                  - data
                x-apifox-orders:
                  - created
                  - data
          headers: {}
          x-apifox-name: Create image
      security: []
      x-apifox-folder: Painting Model/Doubao Series
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-347961511-run
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
