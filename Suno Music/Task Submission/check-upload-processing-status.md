# Query upload processing status

## OpenAPI Specification

````yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/uploads/audio/{id}:
    get:
      summary: Query upload processing status
      deprecated: false
      description: |-
        ┌─────────────────────────────────────────────────────────────────┐
        │ Step 1: Request upload authorization                            │
        │ POST /suno/uploads/audio                                        │
        │ ↓ Returns: upload_id, upload_url                                │
        └─────────────────────────────────────────────────────────────────┘
                                        ↓
        ┌─────────────────────────────────────────────────────────────────┐
        │ Step 2: Upload file to S3 (client direct, not via API)          │
        │ PUT {upload_url}                                                │
        │ ↓ Upload audio file                                             │
        └─────────────────────────────────────────────────────────────────┘
                                        ↓
        ┌─────────────────────────────────────────────────────────────────┐
        │ Step 3: Report upload completion                                │
        │ POST /suno/uploads/audio/{id}/upload-finish                     │
        │ ↓ Notify server that file has been uploaded                     │
        └─────────────────────────────────────────────────────────────────┘
                                        ↓
        ┌─────────────────────────────────────────────────────────────────┐
        │ Step 4: Poll upload status (until status is completed)          │
        │ GET /suno/uploads/audio/{id}                                    │
        │ ↓ Poll every 2-3 seconds                                        │
        └─────────────────────────────────────────────────────────────────┘
                                        ↓
        ┌─────────────────────────────────────────────────────────────────┐
        │ Step 5: Initialize audio clip                                   │
        │ POST /suno/uploads/audio/{id}/initialize-clip                   │
        │ ↓ Returns: clip_id                                              │
        └─────────────────────────────────────────────────────────────────┘
                                        ↓
        ┌─────────────────────────────────────────────────────────────────┐
        │ Step 6: Use clip_id to create continuation task                 │
        │ POST /suno/submit/music                                         │
        │ ↓ Returns: task_id (billing starts)                             │
        └─────────────────────────────────────────────────────────────────┘
        ```
      tags:
        - Music Suno / Task Submission
      parameters:
        - name: id
          in: path
          description: ""
          required: true
          example: e9451fca-e267-4e7f-b23e-c7419aa79cab
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
              x-apifox-orders: []
            examples: {}
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  status:
                    type: string
                  error_message:
                    type: "null"
                  s3_id:
                    type: string
                  title:
                    type: string
                  image_url:
                    type: string
                required:
                  - id
                  - status
                  - error_message
                  - s3_id
                  - title
                  - image_url
                x-apifox-orders:
                  - id
                  - status
                  - error_message
                  - s3_id
                  - title
                  - image_url
              example:
                id: c25a8c59-000a-481f-ac28-efde2dc9e677
                status: complete
                error_message: null
                s3_id: m_05c9b477-4519-4810-9ffa-00580c082067
                title: S-100096-100096-84069F8B
                image_url: >-
                  https://cdn1.suno.ai/image_05c9b477-4519-4810-9ffa-00580c082067.png
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-402408975-run
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
````
