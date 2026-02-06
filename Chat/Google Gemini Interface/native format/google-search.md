# Google search

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-2.5-flash:generateContent:
    post:
      summary: Google search
      deprecated: false
      description: >-
        Official Documentation: https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn
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
                            inline_data:
                              type: object
                              properties:
                                mime_type:
                                  type: string
                                data:
                                  type: string
                              required:
                                - mime_type
                                - data
                            text:
                              type: string
              required:
                - contents
            example:
              contents:
                - role: user
                  parts:
                    - text: What is the weather like in Chongqing today?
              tools:
                - googleSearch: {}
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-350446379-run
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
