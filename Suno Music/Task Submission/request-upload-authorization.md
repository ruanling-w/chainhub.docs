# Request to upload authorization

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/uploads/audio:
    post:
      summary: Request to upload authorization
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
      tags:
        - Music Suno / Task Submission
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                extension:
                  type: string
              required:
                - extension
              x-apifox-orders:
                - extension
            example:
              extension: mp3
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
                  url:
                    type: string
                  fields:
                    type: object
                    properties:
                      Content-Type:
                        type: string
                      key:
                        type: string
                      AWSAccessKeyId:
                        type: string
                      policy:
                        type: string
                      signature:
                        type: string
                    required:
                      - Content-Type
                      - key
                      - AWSAccessKeyId
                      - policy
                      - signature
                    x-apifox-orders:
                      - Content-Type
                      - key
                      - AWSAccessKeyId
                      - policy
                      - signature
                  is_file_uploaded:
                    type: boolean
                required:
                  - id
                  - url
                  - fields
                  - is_file_uploaded
                x-apifox-orders:
                  - id
                  - url
                  - fields
                  - is_file_uploaded
              example:
                id: f208ab1f-e93a-4417-b089-e7fc38b50268
                url: https://suno-uploads.s3.amazonaws.com/
                fields:
                  Content-Type: audio/mpeg
                  key: raw_uploads/f208ab1f-e93a-4417-b089-e7fc38b50268.mp3
                  AWSAccessKeyId: AKIA2V4GXGDKLZ43MUG7
                  policy: >-
                    eyJleHBpcmF0aW9uIjogIjIwMjYtMDEtMDZUMDM6Mjg6MjlaIiwgImNvbmRpdGlvbnMiOiBbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDUyNDI4ODAwMF0sIFsic3RhcnRzLXdpdGgiLCAiJENvbnRlbnQtVHlwZSIsICJhdWRpby9tcGVnIl0sIHsiYnVja2V0IjogInN1bm8tdXBsb2FkcyJ9LCB7ImtleSI6ICJyYXdfdXBsb2Fkcy9mMjA4YWIxZi1lOTNhLTQ0MTctYjA4OS1lN2ZjMzhiNTAyNjgubXAzIn1dfQ==
                  signature: tevxOl3SW28afyLyzObeCYzIvWI=
                is_file_uploaded: false
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-402407540-run
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
