# /fal-ai/nano-banana (Text by Wen Sheng Tu)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/nano-banana:
    post:
      summary: /fal-ai/nano-banana (Text by Wen Sheng Tu)
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/nano-banana'
      tags:
        - Painting Model / Fal.ai Platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: Prompt text for generating the image.
                num_images:
                  type: integer
                  description: Number of images to generate. Range: 1-4. Default: 1
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - num_images
            example:
              prompt: >-
                An action shot of a black lab swimming in an inground suburban
                swimming pool. The camera is placed meticulously on the water
                line, dividing the image in half, revealing both the dogs head
                above water holding a tennis ball in it's mouth, and it's paws
                paddling underwater.
              num_images: 1
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  request_id:
                    type: string
                  response_url:
                    type: string
                  status_url:
                    type: string
                  cancel_url:
                    type: string
                  logs:
                    type: 'null'
                  metrics:
                    type: object
                    properties: {}
                  queue_position:
                    type: integer
                required:
                  - status
                  - request_id
                  - response_url
                  - status_url
                  - cancel_url
                  - logs
                  - metrics
                  - queue_position
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model / Fal.ai Platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-341948426-run
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
