# /fal-ai/vidu/reference-to-image

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/vidu/reference-to-image:
    post:
      summary: /fal-ai/vidu/reference-to-image
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/vidu/reference-to-image'
      tags:
        - Fal-ai aggregation platform
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: Prompt words
                reference_image_urls:
                  type: array
                  items:
                    type: string
                  description: Reference image URL
                aspect_ratio:
                  type: string
                  description: Image aspect ratio, enumerated values: 1:1, 16:9, 9:16
              required:
                - prompt
                - reference_image_urls
              x-apifox-orders:
                - prompt
                - reference_image_urls
                - aspect_ratio
            example:
              prompt: >-
                The little devil is looking at the apple on the beach and
                walking around it.
              reference_image_urls:
                - >-
                  https://storage.googleapis.com/falserverless/web-examples/vidu/new-examples/reference1.png
                - >-
                  https://storage.googleapis.com/falserverless/web-examples/vidu/new-examples/reference2.png
                - >-
                  https://storage.googleapis.com/falserverless/web-examples/vidu/new-examples/reference3.png
              aspect_ratio: '16:9'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apifox-orders: []
              example:
                status: IN_QUEUE
                request_id: 405a114e-04bd-463a-a98c-895502cfdce9
                response_url: >-
                  https://queue.fal.run/fal-ai/vidu/requests/405a114e-04bd-463a-a98c-895502cfdce9
                status_url: >-
                  https://queue.fal.run/fal-ai/vidu/requests/405a114e-04bd-463a-a98c-895502cfdce9/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/vidu/requests/405a114e-04bd-463a-a98c-895502cfdce9/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-349238015-run
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
