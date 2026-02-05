# Query video generation task list - search multiple task ID

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
      summary: Query video generation task list - search multiple task ID
      deprecated: false
      description: ''
      tags:
        - Video Model/Bean Bun Video Generation
      parameters:
        - name: filter.task_ids
          in: query
          description: ''
          required: false
          example:
            - cgt-20250917121233-f4sg6
            - cgt-20250917131023-lgmhz
          schema:
            type: array
            items:
              type: string
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
      x-apifox-folder: Video Model/Bean Bun Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-351560434-run
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
