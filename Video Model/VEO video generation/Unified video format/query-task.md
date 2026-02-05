# Query task

## OpenAPI Specification

````yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/video/query:
    get:
      summary: Query task
      deprecated: false
      description: |+
        Given a hint, the model will return one or more complete predictions, and may also return the probability of an alternative label at each location.

        Complete creation for the provided hint and parameters

      tags:
        - Video model/veo video generation/Unified video format
      parameters:
        - name: id
          in: query
          description: |
            Task ID
          required: true
          example: veo3.1-fast:1760545785-euexscdeL8
          schema:
            type: string
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
        - name: X-Forwarded-Host
          in: header
          description: ''
          required: false
          example: localhost:5173
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties: {}
            examples: {}
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
                  video_url:
                    type: 'null'
                  enhanced_prompt:
                    type: string
                  status_update_time:
                    type: integer
                required:
                  - id
                  - status
                  - video_url
                  - enhanced_prompt
                  - status_update_time
              example:
                id: 033fa60e-f37c-4ff6-a44d-5585ffea938d
                status: pending
                video_url: null
                enhanced_prompt: >-
                  ```

                  A surreal and whimsical digital painting of a majestic brown
                  cow with large, feathered wings soaring gracefully through a
                  vibrant blue sky. The cow has a joyful expression, its tail
                  streaming behind it as it flies among fluffy white clouds.
                  Below, a patchwork of green farmland stretches into the
                  distance, with tiny farm buildings and a group of astonished
                  farmers looking up in amazement. The scene is bathed in warm
                  golden sunlight, creating a dreamlike and magical atmosphere.
                  Art style inspired by fantasy illustrations with soft
                  brushstrokes and rich, saturated colors.

                  ```
                status_update_time: 1750323167003
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Video model/veo video generation/Unified video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-311081757-run
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

````
