# Flux creation (OpenAI dall-e-3 format)

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
      summary: Flux creation (OpenAI dall-e-3 format)
      deprecated: false
      description: |+
        [picture](https://platform.openai.com/docs/api-reference/images)

        Given a prompt and/or an input image, the model will generate a new image.

        Related guide: [Image Generation](https://platform.openai.com/docs/guides/images)

        Create an image based on the prompts.

      tags:
        - Painting Models / FLUX Series / GPT Compatible Format
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
                  description: Models used for image generation.
                prompt:
                  type: string
                  description: A text description of the required image. Maximum length is 1000 characters.
                "n":
                  type: integer
                  description: The number of images to be generated must be between 1 and 10.
                size:
                  type: string
                  description: The size of the generated image. It must be one of 256x256, 512x512, or 1024x1024.
                quality:
                  type: string
                  description: This affects the quality of the generated image. `hd` creates an image with finer details and higher consistency. This parameter is only supported for `dall-e-3`.
                response_format:
                  type: string
                  description: Returns the format of the generated image. It must be either a .json file or a .json URL.
                style:
                  type: string
                  description: style
                user:
                  type: string
                  description: >-
                    The style of the generated image. Must be either `vivid` or `natural`. `vivid` makes the model tend to generate hyper-realistic and dramatic images. `natural` makes the model generate more natural, less realistic images. This parameter only supports `dall-e-3`.
                aspect_ratio:
                  type: string
                  description: >-
                    Image aspect ratio: Possible enum values: 21:9, 16:9, 4:3, 3:2, 1:1,
                    2:3, 3:4, 9:16, 9:21
                  x-apifox-mock: "1:1"
              required:
                - prompt
                - aspect_ratio
              x-apifox-orders:
                - prompt
                - model
                - "n"
                - quality
                - response_format
                - style
                - user
                - size
                - aspect_ratio
            example: |-
              {
                "model": "flux-kontext-pro",
                "prompt": "a beautiful landscape with a river and mountains",
               // "size": "1024x1524",
                "n": 1,
                "aspect_ratio": "21:9"
              }
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
      x-apifox-folder: Painting Models / FLUX Series / GPT Compatible Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421932-run
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
