# Add video selection area

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/multi-elements/add-selection:
    post:
      summary: Add video selection area
      deprecated: false
      description: ""
      tags:
        - Kling Platform / Multimodal Video Editing
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
                session_id:
                  type: string
                  description: The session ID is generated based on the video initialization task and will not change with the editing selection.
                frame_index:
                  type: integer
                  description: A maximum of 10 marker frames can be added, meaning a maximum of 10 frames can be used to mark a video selection area. Only one frame can be marked at a time.
                points:
                  type: array
                  items:
                    type: object
                    properties:
                      x:
                        type: integer
                      "y":
                        type: integer
                    x-apifox-orders:
                      - x
                      - "y"
                  description: >-
                    Select coordinates, represented by x and y. Value range: [0,1], expressed as a percentage; [0,1] represents the top left corner of the screen.
                    Supports adding multiple marker points simultaneously; a maximum of 10 points can be marked in a single frame.
              required:
                - session_id
                - frame_index
                - points
              x-apifox-orders:
                - session_id
                - frame_index
                - points
            example:
              session_id: "828033558945619987"
              frame_index: 1
              points:
                - x: 0
                  "y": 1
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
      x-apifox-folder: Kling Platform / Multimodal Video Editing
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386198862-run
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
