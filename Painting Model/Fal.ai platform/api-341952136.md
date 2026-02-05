# /fal-ai/nano-banana/edit Image editing

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/nano-banana/edit:
    post:
      summary: /fal-ai/nano-banana/edit Image editing
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/nano-banana/edit'
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
                  description: Image editing prompts.
                image_urls:
                  type: array
                  items:
                    type: string
                  description: The URL of the image that needs to be edited.
                num_images:
                  type: integer
                  description: Number of images to generate. Range: 1-4. Default: 1
              required:
                - prompt
                - image_urls
              x-apifox-orders:
                - prompt
                - image_urls
                - num_images
            example:
              prompt: >-
                make a photo of the man driving the car down the california
                coastline
              image_urls:
                - >-
                  https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png
                - >-
                  https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-341952136-run
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
