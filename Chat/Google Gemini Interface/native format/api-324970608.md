# Function calling

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-2.5-pro:generateContent:
    post:
      summary: Function calling
      deprecated: false
      description: >-
        Official Documentation: https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn&example=meeting
      tags:
        - Chat/Google Gemini API/Native Format
      parameters:
        - name: key
          in: query
          description: ''
          required: true
          example: '{{YOUR_API_KEY}}'
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                contents:
                  type: array
                  items:
                    type: object
                    properties:
                      parts:
                        type: array
                        items:
                          type: object
                          properties:
                            text:
                              type: string
                            inline_data:
                              type: object
                              properties:
                                mime_type:
                                  type: string
                                data:
                                  type: string
                              required:
                                - mime_type
                                - data
                generationConfig:
                  type: object
                  properties:
                    responseModalities:
                      type: array
                      items:
                        type: string
                  required:
                    - responseModalities
              required:
                - contents
                - generationConfig
            example:
              contents:
                - role: user
                  parts:
                    - text: >-
                        Schedule a meeting with Bob and Alice for 03/27/2025 at
                        10:00 AM about the Q3 planning.
              tools:
                - functionDeclarations:
                    - name: schedule_meeting
                      description: >-
                        Schedules a meeting with specified attendees at a given
                        time and date.
                      parameters:
                        type: object
                        properties:
                          attendees:
                            type: array
                            items:
                              type: string
                            description: List of people attending the meeting.
                          date:
                            type: string
                            description: Date of the meeting (e.g., '2024-07-29')
                          time:
                            type: string
                            description: Time of the meeting (e.g., '15:00')
                          topic:
                            type: string
                            description: The subject or topic of the meeting.
                        required:
                          - attendees
                          - date
                          - time
                          - topic
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Chat/Google Gemini API/Native Format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-324970608-run
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
