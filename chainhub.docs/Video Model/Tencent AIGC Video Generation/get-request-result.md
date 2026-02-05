# Get the request result

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /tencent-vod/v1/query/{task_id}:
    get:
      summary: 'Get the request result '
      deprecated: false
      description: ''
      tags:
        - Video Model/Tencent AIGC Video Generation
      parameters:
        - name: task_id
          in: path
          description: ''
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: ''
          required: false
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                Response:
                  Status: FINISH
                  TaskType: AigcImageTask
                  RequestId: 12082802-fe37-410e-ae20-0cf14e91e018
                  CreateTime: '2025-12-29T12:03:30Z'
                  FinishTime: '2025-12-29T12:03:43Z'
                  AigcImageTask:
                    Input:
                      Prompt: pig
                      ModelName: GEM
                      ModelVersion: '2.5'
                      OutputConfig:
                        StorageMode: Temporary
                      EnhancePrompt: Enabled
                      NegativePrompt: blur, distorted
                    Output:
                      FileInfos:
                        - FileUrl: >-
                            http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/ef0aa3215145403710877804273/aigcImageGenFile.png
                          ExpireTime: '2026-01-05T12:03:57Z'
                          StorageMode: Temporary
                    Status: FINISH
                    TaskId: 1392336703-AigcImageTask-47965947a83db42af4b1e3a74c243531t
                    Progress: 100
                  BeginProcessTime: '2025-12-29T12:03:30Z'
          headers: {}
          x-apifox-name: Success
      security: []
      x-apifox-folder: Video Model/Tencent AIGC Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-399032082-run
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
