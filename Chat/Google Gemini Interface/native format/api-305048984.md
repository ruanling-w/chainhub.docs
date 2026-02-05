# Text Generation

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-2.5-pro:generateContent:
    post:
      summary: Text Generation
      deprecated: false
      description: >-
        Official Documentation: https://ai.google.dev/gemini-api/docs/text-generation?hl=en#multi-turn-conversations
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
                  - text: You are a piglet. You will add 'Oink' at the beginning of your reply.
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
          x-apifox-name: Success
      security: []
      x-apifox-folder: Chat/Google Gemini API/Native Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-305048984-run
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
