# Create translation (not supported)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/audio/translations:
    post:
      summary: Create translation (not supported)
      deprecated: false
      description: ""
      tags:
        - Chat/ChatGPT Interface/ChatGPT Audio
      parameters: []
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  description: >+
                    The audio file object to be translated (not the filename) must be in the following format: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

                  example: file://C:\Users\Administrator\Desktop\test.m4a
                  type: string
                  format: binary
                model:
                  description: |+
                    The model ID to use. Currently, only whisper-1 is available.

                  example: gpt-4o-transcribe
                  type: string
                prompt:
                  description: |+
                    An optional text prompt to guide the model's style or continue from the previous audio segment. The prompt text should be in English.

                  example: ""
                  type: string
                response_format:
                  description: |+
                    The translation result can be formatted as: json, text, srt, verbose_json, or vtt.

                  example: ""
                  type: string
                temperature:
                  description: >-
                    The default value is 0.

                    Sampling temperature, between 0 and 1. Higher values, such as 0.8, will make the output more random, while lower values, such as 0.2, will make it more focused and deterministic. If set to 0, the model will automatically increase the temperature using log probability until a specific threshold is reached.
                  example: 0
                  type: number
              required:
                - file
                - model
            examples: {}
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  text:
                    type: string
                required:
                  - text
                x-apifox-orders:
                  - text
              example:
                text: >-
                  Hello, my name is Wolfgang and I come from Germany. Where are
                  you heading today?
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Chat/ChatGPT Interface/ChatGPT Audio
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421915-run
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
