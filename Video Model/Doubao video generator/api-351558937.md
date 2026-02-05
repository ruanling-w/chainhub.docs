# Query video generation task list - default

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /volc/v1/contents/generations/tasks:
    get:
      summary: Query video generation task list - default
      deprecated: false
      description: ''
      tags:
        - Video Model/Bean Bun Video Generation
      parameters:
        - name: page_size
          in: query
          description: ''
          required: false
          example: '3'
          schema:
            type: string
        - name: filter.status
          in: query
          description: ''
          required: false
          example: succeeded
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                  items:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        model:
                          type: string
                        status:
                          type: string
                        content:
                          type: object
                          properties:
                            video_url:
                              type: string
                          required:
                            - video_url
                        usage:
                          type: object
                          properties:
                            completion_tokens:
                              type: integer
                            total_tokens:
                              type: integer
                          required:
                            - completion_tokens
                            - total_tokens
                        created_at:
                          type: integer
                        updated_at:
                          type: integer
                      required:
                        - id
                        - model
                        - status
                        - content
                        - usage
                        - created_at
                        - updated_at
                required:
                  - total
                  - items
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-351558937-run
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
