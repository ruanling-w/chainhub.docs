# Create task lucataco/animate-diff

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/predictions:
    post:
      summary: Create task lucataco/animate-diff
      deprecated: false
      description: Official documentation:https://replicate.com/lucataco/animate-diff
      tags:
        - Replicate aggregation platform
      parameters:
        - name: Authorization
          in: header
          description: ''
          required: false
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                version:
                  type: string
                input:
                  type: object
                  properties:
                    path:
                      type: string
                      description: Select a module. Default value: "toonyou_beta3.safetensors".
                    seed:
                      type: integer
                      description: 0 = Random, maximum value: 2147483647.
                    steps:
                      type: integer
                      description: Number of inference steps. Default: 25. Minimum: 1, Maximum: 100.
                    prompt:
                      type: string
                      description: Enter the prompt word.
                    n_prompt:
                      type: string
                      description: Negative message. Default: "".
                    motion_module:
                      type: string
                      description: Select the motion model. Default value: "mm_sd_v14".
                    guidance_scale:
                      type: number
                      description: Guide strength. Default: 7.5. Minimum: 1, Maximum: 10.
                  x-apifox-orders:
                    - path
                    - seed
                    - steps
                    - prompt
                    - n_prompt
                    - motion_module
                    - guidance_scale
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                lucataco/animate-diff:beecf59c4aee8d81bf04f0381033dfa10dc16e845b4ae00d281e2fa377e48a9f
              input:
                path: toonyou_beta3.safetensors
                seed: 255224557
                steps: 25
                prompt: >-
                  masterpiece, best quality, 1girl, solo, cherry blossoms,
                  hanami, pink flower, white flower, spring season, wisteria,
                  petals, flower, plum blossoms, outdoors, falling petals, white
                  hair, black eyes
                n_prompt: >-
                  badhandv4, easynegative, ng_deepnegative_v1_75t,
                  verybadimagenegative_v1.3, bad-artist,
                  bad_prompt_version2-neg, teeth
                motion_module: mm_sd_v14
                guidance_scale: 7.5
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  created:
                    type: integer
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                      required:
                        - url
                      x-apifox-orders:
                        - url
                required:
                  - created
                  - data
                x-apifox-orders:
                  - created
                  - data
              example:
                id: jywwf9nkfnrj20crap0as52zeg
                model: lucataco/animate-diff
                version: >-
                  beecf59c4aee8d81bf04f0381033dfa10dc16e845b4ae00d281e2fa377e48a9f
                input:
                  guidance_scale: 7.5
                  motion_module: mm_sd_v14
                  n_prompt: >-
                    badhandv4, easynegative, ng_deepnegative_v1_75t,
                    verybadimagenegative_v1.3, bad-artist,
                    bad_prompt_version2-neg, teeth
                  path: toonyou_beta3.safetensors
                  prompt: >-
                    masterpiece, best quality, 1girl, solo, cherry blossoms,
                    hanami, pink flower, white flower, spring season, wisteria,
                    petals, flower, plum blossoms, outdoors, falling petals,
                    white hair, black eyes
                  seed: 255224557
                  steps: 25
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-29T09:25:54.685Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/jywwf9nkfnrj20crap0as52zeg/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/jywwf9nkfnrj20crap0as52zeg
                  stream: >-
                    https://stream.replicate.com/v1/files/qoxq-rtwpkbal3tte26cwukk5qz4jari7vrzuxx747qitukq6pqukjhxq
                  web: https://replicate.com/p/jywwf9nkfnrj20crap0as52zeg
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-326482871-run
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
