# Main body

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/general/custom-elements:
    post:
      summary: main body
      deprecated: false
      description: ""
      tags:
        - Kling platform/main body
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
                element_name:
                  type: string
                  description: |-
                    The main name
                    Cannot exceed 20 characters
                element_description:
                  type: string
                  description: |-
                    Body description
                    Cannot exceed 100 characters
                element_frontal_image:
                  type: string
                  description: |-
                    Front view reference image
                    Supports inputting Base64 encoded images or image URLs (ensure accessibility)
                    Supported image formats: .jpg / .jpeg / .png
                    Image file size cannot exceed 10MB, image dimensions must be at least 300px, and aspect ratio must be between 1:2.5 and 2.5:1.
                element_refer_list:
                  type: array
                  items:
                    type: object
                    properties:
                      image_url:
                        type: string
                    required:
                      - image_url
                    x-apifox-orders:
                      - image_url
                  description: |-
                    Other References for the Main Subject
                    You can define the main subject's appearance by uploading multiple reference images from different angles.
                    Upload at least one reference image and a maximum of three reference images.
                    Use key:value pairs, as follows:
                    1
                    2
                    3
                    4
                    5
                    "element_refer_list":[
                      {"image_url":"image_url_1"{"image_url":"image_url_2"},
                      {"image_url":"image_url_3"}
                    ]
              required:
                - element_name
                - element_description
                - element_frontal_image
                - element_refer_list
              x-apifox-orders:
                - element_name
                - element_description
                - element_frontal_image
                - element_refer_list
            example:
              element_name: ""
              element_description: ""
              element_frontal_image: ""
              element_refer_list: ""
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
      x-apifox-folder: Kling platform/main body
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-398950420-run
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
