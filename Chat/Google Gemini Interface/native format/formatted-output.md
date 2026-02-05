# Structured Output

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
      summary: Structured Output
      deprecated: false
      description: >-
       Official Documentation: https://ai.google.dev/gemini-api/docs/structured-output?hl=en
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
                        List a few popular cookie recipes, and include the
                        amounts of ingredients.
              generationConfig:
                responseMimeType: application/json
                responseSchema:
                  type: ARRAY
                  items:
                    type: OBJECT
                    properties:
                      recipeName:
                        type: STRING
                      ingredients:
                        type: ARRAY
                        items:
                          type: STRING
                    propertyOrdering:
                      - recipeName
                      - ingredients
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-309478321-run
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
