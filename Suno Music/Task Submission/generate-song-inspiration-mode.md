# Generate a song (Inspiration Mode)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /suno/submit/music:
    post:
      summary: Generate a song (Inspiration Mode)
      deprecated: false
      description: ''
      tags:
        - Music Suno / Task Submission
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
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
                prompt:
                  description: Lyrics content, used only in custom mode
                  type: string
                mv:
                  description: Model selection: options include chirp-v3-0 and chirp-v3-5; the default is chirp-v3-0.
                  type: string
                title:
                  description: Song title, used only in custom mode
                  type: string
                tags:
                  description: Style tags, used only in custom mode; multiple tags are separated by commas.
                  type: string
                make_instrumental:
                  description: Whether to generate an instrumental version; true indicates that an instrumental version will be generated.
                  type: boolean
                task_id:
                  description: Task ID, used to perform operations on an existing task (such as continuing the task).
                  type: string
                continue_at:
                  description: Continue writing the starting time point, a floating-point number, in seconds.
                  type: number
                continue_clip_id:
                  description: Song IDs that need to be continued
                  type: string
                gpt_description_prompt:
                  description: Creative description prompts, used only in Inspiration Mode.
                  type: string
                notify_hook:
                  description: Callback notification address after task completion
                  type: string
              required:
                - prompt
                - mv
                - gpt_description_prompt
              x-apifox-orders:
                - prompt
                - mv
                - title
                - tags
                - make_instrumental
                - task_id
                - continue_at
                - continue_clip_id
                - gpt_description_prompt
                - notify_hook
            example:
              gpt_description_prompt: A beautiful love song
              make_instrumental: false
              mv: chirp-v4
              prompt: Cat Dance
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                  data:
                    type: string
                  message:
                    type: string
                required:
                  - code
                  - data
                  - message
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-248983692-run
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
