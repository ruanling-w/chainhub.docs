# Audio to text conversion gpt-4o-transcribe

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /v1/audio/transcriptions:
    post:
      summary: Audio to text conversion gpt-4o-transcribe
      deprecated: false
      description: Official documentation：https://platform.openai.com/docs/guides/speech-to-text
      tags:
        - Chat/ChatGPT Interface/ChatGPT Audio
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: false
          example: multipart/form-data
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  description: >+
                    The audio file object to be transcribed (not the filename) must be in the following format: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

                  example: file://C:\Users\Administrator\Desktop\test.m4a
                  type: string
                  format: binary
                model:
                  description: |+
                    The model ID to use. Currently, only whisper-1 and gpt-4o-mini-transcribe are available.

                  example: gpt-4o-transcribe
                  type: string
                language:
                  description: |+
                    The language of the input audio. Providing the input language in ISO-639-1 format can improve accuracy and reduce latency.

                  example: ""
                  type: string
                prompt:
                  description: |+
                    An optional text prompt to guide the model's style or continue from the previous audio segment. The prompt should match the audio language.

                  example: ""
                  type: string
                response_format:
                  description: |-
                    The default is JSON.
                    The format of the transcription output can be selected as: JSON or Text.
                  example: json
                  type: string
                temperature:
                  description: >-
                    The default value is 0, and the sampling temperature is between 0 and 1. Higher values ​​like 0.8 will make the output more random, while lower values ​​like 0.2 will make it more focused and deterministic. If set to 0, the model will automatically increase the temperature using log probability until a specific threshold is reached.
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
              examples:
                "1":
                  summary: Successful examples
                  value:
                    text: >-
                      Imagine the wildest idea that you've ever had, and you're
                      curious about how it might scale to something that's a
                      100, a 1,000 times bigger. This is a place where you can
                      get to do that.
                "2":
                  summary: Successful examples
                  value:
                    text: One two three four five six seven eight nine ten
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Chat/ChatGPT Interface/ChatGPT Audio
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421914-run
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
