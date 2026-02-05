# Image recognition

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/image-recognize:
    post:
      summary: Image recognition
      deprecated: false
      description: ""
      tags:
        - Kling Platform / Image Recognition
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
                image:
                  type: string
                  description: >-
                    The image to be identified can be either Base64 encoded or a URL (ensure it is accessible). Supported image formats are .jpg, .jpeg, and .png.
                    The image file size cannot exceed 10MB, the image dimensions must be at least 300px, and the aspect ratio must be between 1:2.5 and 2.5:1.
              required:
                - image
              x-apifox-orders:
                - image
            example:
              image: >-
                https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
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
      x-apifox-folder: Kling Platform / Image Recognition
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386307948-run
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
