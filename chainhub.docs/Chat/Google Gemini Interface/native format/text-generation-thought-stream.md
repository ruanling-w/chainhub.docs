# Text generation + thinking - stream

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-2.5-pro:streamGenerateContent:
    post:
      summary: 'Text generation + thinking - stream '
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
              contents:
                - parts:
                    - text: 1+2+3+4+5+....+999?
                  role: user
              systemInstruction:
                parts:
                  - text: hi
                role: user
              safetySettings:
                - category: HARM_CATEGORY_HATE_SPEECH
                  threshold: 'OFF'
                - category: HARM_CATEGORY_SEXUALLY_EXPLICIT
                  threshold: 'OFF'
                - category: HARM_CATEGORY_HARASSMENT
                  threshold: 'OFF'
                - category: HARM_CATEGORY_DANGEROUS_CONTENT
                  threshold: 'OFF'
                - category: HARM_CATEGORY_CIVIC_INTEGRITY
                  threshold: BLOCK_NONE
              tools: []
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-338836071-run
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
