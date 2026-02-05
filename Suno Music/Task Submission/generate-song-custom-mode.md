# Generate a song (custom mode)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/submit/music:
    post:
      summary: Generate a song (custom mode)
      deprecated: false
      description: ""
      tags:
        - Music Suno / Task Submission
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Accept
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
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
                  type: string
                  description: Customized full lyrics.
                mv:
                  type: string
                  description: Model version number
                title:
                  type: string
                  description: Lyrics Title
                tags:
                  type: string
                  description: Song style
                continue_at:
                  type: integer
                  description: Continue writing the song ID
                continue_clip_id:
                  type: string
                task:
                  type: string
                  description: Task type, defaults to "generate"
              required:
                - prompt
                - mv
                - title
              x-apifox-orders:
                - prompt
                - mv
                - title
                - tags
                - continue_at
                - continue_clip_id
                - task
            example:
              prompt: |-
                [Verse]
                Move your paws
                Left and right
                Jump around
                Feel the light
                Whiskers twitch
                Tails in the air
                Dancing cats
                Everywhere

                [Chorus]
                Cat dance
                Oh
                Let's go!
                Swing your tails
                Don’t say no (don’t say no!)
                Purr and twirl
                Like a show
                Cat dance
                Let's steal the glow

                [Verse 2]
                Tiptoe steps
                Soft and sweet
                Tiny paws
                Unbeatable beat
                Meow to the rhythm
                Claws precise
                Every move
                Feline paradise

                [Chorus]
                Cat dance
                Oh
                Let's go!
                Swing your tails
                Don’t say no (don’t say no!)
                Purr and twirl
                Like a show
                Cat dance
                Let's steal the glow

                [Bridge]
                Ooh-ooh
                Bounce and sway (ooh-ooh!)
                Moonlit grooves
                Night turns to day
                Lean and stretch
                Strike your pose
                Every kitty steals the show

                [Chorus]
                Cat dance
                Oh
                Let's go!
                Swing your tails
                Don’t say no (don’t say no!)
                Purr and twirl
                Like a show
                Cat dance
                Let's steal the glow
              mv: chirp-v4
              title: Cat Dance
              tags: romantic raga
              continue_at: 120
              continue_clip_id: ""
              task: ""
      responses:
        "200":
          description: ""
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-305049181-run
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
