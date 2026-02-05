# Text generation - stream

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-3-pro-preview:streamGenerateContent:
    post:
      summary: 'Text generation - stream '
      deprecated: false
      description: >-
        Official Documentation: https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#multi-turn-conversations
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
        - name: alt
          in: query
          description: ''
          required: false
          example: sse
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
              required:
                - contents
            example:
              systemInstruction:
                parts:
                  - text: You are a cat. Your name is Neko.
              contents:
                - role: user
                  parts:
                    - text: Hello there
              generationConfig:
                temperature: 1
                topP: 1
                thinkingConfig:
                  includeThoughts: true
                  thinkingBudget: 26240
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
      x-apifox-folder: Chat/Google Gemini API/Native Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-318990658-run
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
