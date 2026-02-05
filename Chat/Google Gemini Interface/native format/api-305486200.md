# Image Generation

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-2.5-flash-image-preview:generateContent:
    post:
      summary: Image Generation
      deprecated: false
      description: >-
        Official Documentation: https://ai.google.dev/gemini-api/docs/image-generation?hl=en
      tags:
        - Chat/Google Gemini API/Native Format
      parameters:
        - name: key
          in: query
          description: ''
          required: true
          example: '{{YOUR_API_KEY}}'
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                contents:
                  type: array
                  items:
                    type: object
                    properties:
                      parts:
                        type: array
                        items:
                          type: object
                          properties:
                            text:
                              type: string
                generationConfig:
                  type: object
                  properties:
                    responseModalities:
                      type: array
                      items:
                        type: string
                  required:
                    - responseModalities
              required:
                - contents
                - generationConfig
            example:
              contents:
                - role: user
                  parts:
                    - text: >-
                        Hi, can you create a 3d rendered image of a pig with
                        wings and a top hat flying over a happy futuristic scifi
                        city with lots of greenery?
              generationConfig:
                responseModalities:
                  - TEXT
                  - IMAGE
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Chat/Google Gemini API/Native Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-305486200-run
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
