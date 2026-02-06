# Scenario 2: Custom lyrics and song title

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /suno/generate:
    post:
      summary: "Scenario 2: Custom lyrics and song title"
      deprecated: false
      description: ""
      tags:
        - Music Suno / Task Submission
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
            example:
              prompt: |-
                [Verse]
                Days of non-stop busyness
                Endless piles of documents
                Dreams hidden deep in the drawer
                The coffee cup has gone cold

                [Verse 2]
                Clocking in at 8 AM
                Tired eyes, lifeless
                Even casual conversations with colleagues are meaningless
                Just hoping time will hurry up and pass by

                [Chorus]
                Work, work, the boss's call
                Finish it, finish it, only then can I feel at peace
                Overtime, overtime, only then can I earn some money
                When will my dreams, my dreams, come true?

                [Verse 3]
                Eating a bento box for lunch
                Looking out the window, the sun is shining brightly
                Life is so far from my dreams
                All I see is my desk and chair

                [Bridge]
                The boss's footsteps are like thunder
                My heart races with the rhythm
                A mountain of documents on the desk
                The complaints gradually fade away

                [Chorus]
                Work, work, the boss's call
                Finish it, finish it, only then can I feel at peace
                Overtime, overtime, only then can I earn some money
                When will my dreams, my dreams, come true?
              mv: chirp-v3-5
              title: Work
              tags: " edm"
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Music Suno / Task Submission
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-408842497-run
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
