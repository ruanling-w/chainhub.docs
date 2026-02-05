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
      summary: 'Query task '
      deprecated: false
      description: |+
        Given a hint, the model will return one or more complete predictions, and may also return the probability of an alternative label at each location.

        Complete creation for the provided hint and parameters

      tags:
        - Video Model/GROOK Video Generation/Video Unified Format
      parameters:
        - name: id
          in: query
          description: |
            Task ID
          required: true
          example: grok:eee6faa8-9dee-455c-aa82-02ac623adf3a
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
              examples:
                '1':
                  summary: Successful examples
                  value:
                    id: 033fa60e-f37c-4ff6-a44d-5585ffea938d
                    status: pending
                    video_url: null
                    enhanced_prompt: >-
                      ```

                      A surreal and whimsical digital painting of a majestic
                      brown cow with large, feathered wings soaring gracefully
                      through a vibrant blue sky. The cow has a joyful
                      expression, its tail streaming behind it as it flies among
                      fluffy white clouds. Below, a patchwork of green farmland
                      stretches into the distance, with tiny farm buildings and
                      a group of astonished farmers looking up in amazement. The
                      scene is bathed in warm golden sunlight, creating a
                      dreamlike and magical atmosphere. Art style inspired by
                      fantasy illustrations with soft brushstrokes and rich,
                      saturated colors.

                      ```
                    status_update_time: 1750323167003
                '2':
                  summary: Successful examples
                  value:
                    id: grok:299604b7-c5ea-47b5-bc64-c06f300f0d27
                    mode: text
                    type: create
                    error: ''
                    model: grok-3
                    ratio: '3:2'
                    prompt: cat fish  --mode=custom
                    status: completed
                    post_id: 393ae1ec-1dc7-4f26-bb53-afe361bc3b3a
                    asset_id: 393ae1ec-1dc7-4f26-bb53-afe361bc3b3a
                    progress: 100
                    trace_id: 4cc3a75aa6d6a0788f86195e0cbad44e
                    upscaled: false
                    video_id: 393ae1ec-1dc7-4f26-bb53-afe361bc3b3a
                    video_url: >-
                      https://soruxgpt-saas-yimeng.soruxgpt.com/file_download/ca10efbb-ae64-426e-99f0-f365bc3cd941.mp4
                    completed_at: 1764522552
                    thumbnail_url: >-
                      https://soruxgpt-saas-yimeng.soruxgpt.com/file_download/f4fd6fe4-8091-4528-be32-335f4fc9af65.jpg
                    video_file_id: ca10efbb-ae64-426e-99f0-f365bc3cd941
                    thumbnail_file_id: f4fd6fe4-8091-4528-be32-335f4fc9af65
                    status_update_time: 1764522552
                    upscale_on_complete: false
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Video Model/GROOK Video Generation/Video Unified Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-385288050-run
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
