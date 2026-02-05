# Web search

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/chat/completions:
    post:
      summary: Web search
      deprecated: false
      description: Reference documentation: https://platform.openai.com/docs/api-reference/chat/create
      tags:
        - Chat/ChatGpt API/Web Search
      parameters:
        - name: Authorization
          in: header
          description: ''
          required: true
          example: Bearer $OPENAI_API_KEY
          schema:
            type: string
        - name: Content-type
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
                model:
                  type: string
                web_search_options:
                  type: object
                  properties: {}
                messages:
                  type: array
                  items:
                    type: object
                    properties:
                      role:
                        type: string
                      content:
                        type: string
              required:
                - model
                - web_search_options
                - messages
            example:
              model: gpt-4o-search-preview
              web_search_options: {}
              messages:
                - role: user
                  content: What was a positive news story from today?
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
      x-apifox-folder: Chat/ChatGpt API/Web Search
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-306423418-run
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
