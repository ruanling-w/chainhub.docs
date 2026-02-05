# Create a speech gpt-4o-mini-tts

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/audio/speech:
    post:
      summary: Create a speech gpt-4o-mini-tts
      deprecated: false
      description: Official documentation：https://platform.openai.com/docs/guides/text-to-speech
      tags:
        - Chat/ChatGPT Interface/ChatGPT Audio
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                  description: One of the available TTS models: TTS-1 or TTS-1-HD
                input:
                  type: string
                  description: The text to be generated as audio. Maximum length is 4096 characters.
                voice:
                  type: string
                  description: The voice used when generating audio. Supported voices include: alloy, echo, fable, onyx, nova, and shimmer.
                response_format:
                  type: string
                  description: The default audio format is mp3. Supported formats include: mp3, opus, aac, and flac.
                speed:
                  type: number
                  description: The default value is 1 for the generated audio velocity. Choose a value between 0.25 and 4.0. 1.0 is the default value.
              required:
                - model
                - input
                - voice
              x-apifox-orders:
                - model
                - input
                - voice
                - response_format
                - speed
            example:
              model: gpt-4o-mini-tts
              input: The quick brown fox jumped over the lazy dog.
              voice: alloy
      responses:
        '200':
          description: ''
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
      x-apifox-folder: Chat/ChatGPT Interface/ChatGPT Audio
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-232421913-run
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
