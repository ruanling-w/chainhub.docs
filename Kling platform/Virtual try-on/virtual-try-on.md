# Virtual try-on

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/images/kolors-virtual-try-on:
    post:
      summary: Virtual try-on
      deprecated: false
      description: ""
      tags:
        - Kling platform/virtual try-on
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
                    Model Name Enumeration Values: kolors-virtual-try-on-v1,
                    kolors-virtual-try-on-v1-5
                human_image:
                  type: string
                  description: >-
                    Uploaded images of people; Base64 encoded images or image URLs are supported (ensure they are accessible); supported image formats are .jpg / .jpeg / .png; image file size cannot exceed 10MB, and image dimensions must be at least 300px.
                cloth_image:
                  type: string
                  description: Images of clothing for virtual try-on
                callback_url:
                  type: string
              required:
                - human_image
                - cloth_image
                - model_name
              x-apifox-orders:
                - model_name
                - human_image
                - cloth_image
                - callback_url
            example:
              model_name: kolors-virtual-try-on-v1
              human_image: >-
                https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
              cloth_image: >-
                https://imageproxy.zhongzhuan.chat/api/proxy/image/1db2a32c24087cab3405a00ee4454c94.jpg
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
      x-apifox-folder: Kling platform/virtual try-on
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386354700-run
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
