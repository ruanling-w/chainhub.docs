# Report uploaded

## OpenAPI Specification

````yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/uploads/audio/{id}/upload-finish:
    post:
      summary: Report uploaded
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
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                upload_type:
                  type: string
                upload_filename:
                  type: string
                  description: Uploaded file name
              required:
                - upload_type
                - upload_filename
              x-apifox-orders:
                - upload_type
                - upload_filename
            example:
              upload_type: file_upload
              upload_filename: my_audio.mp3
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apifox-orders: []
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-402408952-run
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
