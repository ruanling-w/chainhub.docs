# Image generation

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/images/generations:
    post:
      summary: Image generation
      deprecated: false
      description: ""
      tags:
        - Kling Platform / Image Generation
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: false
          example: application/json
          schema:
            type: string
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
                model_name:
                  type: string
                  description: >-
                    Model Name Enumeration Values: kling-v1, kling-v1-5, kling-v2, kling-v2-new,
                    kling-v2-1
                prompt:
                  type: string
                  description: Positive text prompts cannot exceed 2500 characters.
                negative_prompt:
                  type: string
                  description: Negative text prompts cannot exceed 2500 characters.
                image:
                  type: string
                  description: The reference image supports passing in a Base64 encoded image or an image URL (ensure it is accessible).
                image_reference:
                  type: string
                  description: |-
                    Image Reference Types
                    Enumeration Values: subject (character feature reference), face (person's facial appearance reference)
                    When using face (person's facial appearance reference), the uploaded image must contain only one face.
                    When using kling-v1-5 and the image parameter is not empty, this parameter is required.
                image_fidelity:
                  type: number
                  description: |-
                    Reference strength of user-uploaded images during the generation process
                    Value range: [0,1], the larger the value, the stronger the reference strength.
                human_fidelity:
                  type: number
                  description: |-
                    Facial reference strength, i.e., the similarity of facial features of a person in a reference image.
                    Only effective when the `image_reference` parameter is `subject`.
                    Value range: [0,1], the larger the value, the stronger the reference strength.
                resolution:
                  type: string
                  description: |-
                    Image resolution:
                    Enumerated values: 1k, 2k
                    1k: 1K standard definition
                    2k: 2K high definition
                "n":
                  type: integer
                  description: |-
                    Number of images generated
                    Value range: [1, 9]
                aspect_ratio:
                  type: string
                  description: |-
                    The aspect ratio (width:height) of the generated image
                    Enumerated values: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9
                callback_url:
                  type: string
              required:
                - model_name
                - prompt
                - "n"
              x-apifox-orders:
                - model_name
                - prompt
                - negative_prompt
                - image
                - image_reference
                - image_fidelity
                - human_fidelity
                - resolution
                - "n"
                - aspect_ratio
                - callback_url
            example:
              model_name: kling-v1
              prompt: Generate a picture of a seaside.
              negative_prompt: ""
              image: ""
              image_reference: ""
              image_fidelity: "0.5"
              human_fidelity: 0.45
              resolution: 1k
              "n": 1
              aspect_ratio: "16:9"
              callback_url: ""
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling Platform / Image Generation
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386036840-run
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
