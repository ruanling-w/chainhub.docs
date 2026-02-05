# Generate songs (singer style)

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
      summary: Generate songs (singer style)
      deprecated: false
      description: >+
        # Integration Steps

        ## A. Generate Music

        After generating music through the song generation interface, obtain the `clip_id` value of one of the songs:

        54834687-5e79-4f08-8e14-cf188f15b598

        ## B. Create a Persona

        - The `clip_id` must exist within the system, not the uploader.

        - It cannot be used across accounts, so it may not work if the account is offline.

        ## C. Create using persona_id

        Notes:

        - mv is `chirp-v3-5-tau` or `chirp-v4-tau`

        - task is `artist_consistency`

        - persona_id is obtained in step B

        - artist_clip_id is the same as the `clip_id` in step A

        - It can be used across accounts.
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
                  description: Lyrics
                generation_type:
                  type: string
                  description: Generate content, example value "text"
                tags:
                  type: string
                  description: Style tags
                negative_tags:
                  type: string
                  description: negative labels
                mv:
                  type: string
                  description: Model version number
                title:
                  type: string
                  description: Lyrics title
                task:
                  type: string
                persona_id:
                  type: string
                  description: Character ID
                artist_clip_id:
                  type: string
                  description: ID of a reference audio segment
                vocal_gender:
                  type: string
                  description: Human voice gender
              required:
                - prompt
                - generation_type
                - mv
                - title
                - persona_id
                - artist_clip_id
              x-apifox-orders:
                - prompt
                - generation_type
                - tags
                - negative_tags
                - mv
                - title
                - task
                - persona_id
                - artist_clip_id
                - vocal_gender
            example:
              prompt: |-
                [Verse]
                From dawn till dusk
                You've always been by my side, warming me
                I'm not afraid of wind or rain
                Holding hands tightly, we'll never be apart

                [Verse 2]
                With you, I'm not lonely
                Like stars in the night sky
                No matter how long the road, it doesn't feel far
                Because you are my light

                [Chorus]
                My love, my love, I love you
                You are the only one in the world
                No matter where I am in the world
                My heart will always be with you

                [Verse 3]
                You are my safe haven
                Every night I dream of you
                Even if the road ahead is difficult
                With you, everything is beautiful

                [Chorus]
                My love, my love, I love you
                You are the only one in the world
                No matter where I am in the world
                My heart will always be with you

                [Bridge]
                Every moment of my life
                I experience it with you
                Every tomorrow will be better
                Because of you, I am invincible
              generation_type: TEXT
              tags: electronic, pop
              negative_tags: ""
              mv: chirp-v4-tau
              title: 老公
              task: artist_consistency
              persona_id: 0f6e8077-a7ba-4fc8-8f60-de02c66e56ce
              artist_clip_id: a5fa604c-18b8-4e7f-8d25-9412d4ba8163
              vocal_gender: ""
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
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-305049365-run
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
