# Speech Synthesis

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/audio/tts:
    post:
      summary: Speech Synthesis
      deprecated: false
      description: ''
      tags:
        - Kling platform/speech synthesis
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: false
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
                text:
                  type: string
                  description: The text for synthesized audio; the maximum text length is 1000 characters, exceeding this limit will result in an error code; the system will validate the text content, and will return an error code if any issues are found.
                voice_id:
                  type: string
                  description: >-
                    The timbre ID system offers a variety of timbres to choose from, with specific timbre effects, timbre IDs, and language correspondences. Custom text is not supported for timbre previews.
                    Timbre preview file naming convention: Timbre Name#Timbre ID#Timbre Language
                voice_language:
                  type: string
                  description: The text for synthesized audio; the maximum text length is 1000 characters, exceeding this limit will result in an error code; the system will validate the text content, and will return an error code if any issues are found.
                voice_speed:
                  type: integer
                  description: Effective speech rate range: 0.8~2.0, accurate to one decimal place; any range exceeding this will be automatically rounded.
              required:
                - text
                - voice_id
                - voice_language
              x-apifox-orders:
                - text
                - voice_id
                - voice_language
                - voice_speed
            example:
              text: Describe the scene you see
              voice_id: genshin_vindi2
              voice_language: zh
              voice_speed: '1.0'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Kling platform/speech synthesis
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386347843-run
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
