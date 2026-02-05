# Text generation gemini-3-pro-preview:generateContent

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-3-pro-preview:generateContent:
    post:
      summary: Text generation gemini-3-pro-preview:generateContent
      deprecated: false
      description: >-
        Official documentation：https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#multi-turn-conversations
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
              required:
                - contents
            example:
              systemInstruction:
                parts:
                  - text: You're a little pig. You'll add a 'hmph' at the beginning of your replies.
              contents:
                - role: user
                  parts:
                    - text: Who are you?
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
      security: []
      x-apifox-folder: Chat/Google Gemini API/Native Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-381390942-run
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
