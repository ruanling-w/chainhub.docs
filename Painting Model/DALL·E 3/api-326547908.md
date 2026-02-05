# Create DALL·E 3

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
      summary: Create DALL·E 3
      deprecated: false
      description: |+
        [picture](https://platform.openai.com/docs/api-reference/images)

        Given a prompt and/or an input image, the model will generate a new image.

        Related guidelines: [Image generation](https://platform.openai.com/docs/guides/images)

        Create an image based on the prompts.

      tags:
        - Painting model / DALL·E 3
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
                  description: >+
                    The size of the generated image. It must be one of 1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or auto (default) for gpt-image-1; one of 256x256, 512x512, or 1024x1024 for dall-e-2; and one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3.

                quality:
                  type: string
                  description: This affects the quality of the generated image. `hd` creates an image with finer details and higher consistency. This parameter is only supported for `dall-e-3`.
                response_format:
                  type: string
                  description: Returns the format of the generated image. It must be either a .json file or a .json URL.
                style:
                  type: string
                  description: >+
                    The style of the generated image. This parameter only supports dall-e-3. It must be either vivid or natural.
                    Vivid will cause the model to generate surreal and dramatic images. Natural will cause the model to generate more natural-looking, less surreal images.

                user:
                  type: string
                  description: A unique identifier that represents your end user can help OpenAI monitor and detect abuse.
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - model
                - "n"
                - quality
                - response_format
                - style
                - user
                - size
            example:
              model: dall-e-3
              prompt: A cute baby sea otter
              "n": 1
              size: 1024x1024
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
      x-apifox-folder: Painting model / DALL·E 3
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326547908-run
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
