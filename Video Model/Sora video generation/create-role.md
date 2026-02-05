# Create a character

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /sora/v1/characters:
    post:
      summary: Create a character
      deprecated: false
      description: ''
      tags:
        - Video model/sora video generation
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: |
                    The video contains the role to be created, and you can choose either the URL or the `from_task` option. 
                timestamps:
                  type: string
                  description: |
                    The unit is seconds. For example, '1,2' refers to characters appearing within 1 to 2 seconds of the video. Note that the range difference is a maximum of 3 seconds and a minimum of 1 second.
                from_task:
                  type: string
                  description: |
                    You can create a role based on the already generated task ID.
              required:
                - timestamps
              x-apifox-orders:
                - url
                - timestamps
                - from_task
            example: "{\r\n  // \"url\": \"https://filesystem.site/cdn/20251030/javYrU4etHVFDqg8by7mViTWHlMOZy.mp4\",\r\n    \"timestamps\": \"1,3\",\r\n    \"from_task\":\"video_e50c76ca-21d4-40e9-8485-e4ead2d37133\"\r\n}"
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
                    description: Character ID
                  username:
                    type: string
                    description: The character name, used to include in the hints @{username}
                  permalink:
                    type: string
                    description: The character's homepage will redirect you to the OpenAI character's homepage.
                  profile_picture_url:
                    type: string
                    description: Character avatar
                required:
                  - id
                  - username
                  - permalink
                  - profile_picture_url
                x-apifox-orders:
                  - id
                  - username
                  - permalink
                  - profile_picture_url
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-376104874-run
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
