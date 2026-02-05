# Create video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/video/create:
    post:
      summary: 'Create video '
      deprecated: false
      description: ''
      tags:
        - Video Model/GROOK Video Generation/Video Unified Format
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
                  description: Model name: grok-video-3
                prompt:
                  type: string
                  description: ' Prompt '
                aspect_ratio:
                  type: string
                  description: Optional: 2:3, 3:2, 1:1
                size:
                  type: string
                  description: 720P or 1080P (currently only 720P is supported)
                images:
                  type: array
                  items:
                    type: string
                  description: Image link
              required:
                - model
                - prompt
                - aspect_ratio
                - size
                - images
              x-apifox-orders:
                - model
                - prompt
                - aspect_ratio
                - size
                - images
            example:
              model: grok-video-3
              prompt: The kitten is eating fish --mode=custom
              aspect_ratio: '3:2'
              size: 720P
              images:
                - >-
                  https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_5_imageToimage.png
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  status:
                    type: string
                  status_update_time:
                    type: integer
                required:
                  - id
                  - status
                  - status_update_time
              examples:
                '1':
                  summary: Successful examples
                  value:
                    id: veo3.1-components:1762241017-xTL0P9HvGF
                    status: pending
                    status_update_time: 1762241017286
                '2':
                  summary: Successful examples
                  value:
                    id: grok:299604b7-c5ea-47b5-bc64-c06f300f0d27
                    status: processing
                    status_update_time: 1764522528
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Frequency model/grok video generation/video unified format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-385288046-run
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
