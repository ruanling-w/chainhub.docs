# /fal-ai/imagen4/preview

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /fal-ai/imagen4/preview:
    post:
      summary: /fal-ai/imagen4/preview
      deprecated: false
      description: 'Official documentation: https://fal.ai/models/fal-ai/imagen4/preview'
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
                aspect_ratio:
                  type: string
                  description: Image aspect ratio, enumerated values: 1:1, 16:9, 9:16, 3:4, 4:3
                num_images:
                  type: integer
                  description: Number of images generated, range: 1-4
                resolution:
                  type: string
                  description: Resolution: Enumerated values: "1K", "2K"
              required:
                - prompt
              x-apifox-orders:
                - prompt
                - aspect_ratio
                - num_images
                - resolution
            example:
              prompt: >-
                Capture an intimate close-up bathed in warm, soft,
                late-afternoon sunlight filtering into a quintessential 1960s
                kitchen. The focal point is a charmingly designed vintage
                package of all-purpose flour, resting invitingly on a speckled
                Formica countertop. The packaging itself evokes pure nostalgia:
                perhaps thick, slightly textured paper in a warm cream tone,
                adorned with simple, bold typography (a friendly serif or
                script) in classic red and blue “ALL-PURPOSE FLOUR”, featuring a
                delightful illustration like a stylized sheaf of wheat or a
                cheerful baker character. In smaller bold print at the bottom of
                the package: “NET WT 5 LBS (80 OZ) 2.27kg”. Focus sharply on the
                package details – the slightly soft edges of the paper bag, the
                texture of the vintage printing, the inviting "All-Purpose
                Flour" text. Subtle hints of the 1960s kitchen frame the shot –
                the chrome edge of the counter gleaming softly, a blurred
                glimpse of a pastel yellow ceramic tile backsplash, or the
                corner of a vintage metal canister set just out of focus. The
                shallow depth of field keeps attention locked on the beautifully
                designed package, creating an aesthetic rich in warmth,
                authenticity, and nostalgic appeal.
              aspect_ratio: '1:1'
              num_images: 1
              resolution: 1K
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
                request_id: 484ccb37-5477-44fe-8e75-6d6f6e9160b3
                response_url: >-
                  https://queue.fal.run/fal-ai/imagen4/requests/484ccb37-5477-44fe-8e75-6d6f6e9160b3
                status_url: >-
                  https://queue.fal.run/fal-ai/imagen4/requests/484ccb37-5477-44fe-8e75-6d6f6e9160b3/status
                cancel_url: >-
                  https://queue.fal.run/fal-ai/imagen4/requests/484ccb37-5477-44fe-8e75-6d6f6e9160b3/cancel
                logs: null
                metrics: {}
                queue_position: 0
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Fal-ai aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-349238024-run
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
