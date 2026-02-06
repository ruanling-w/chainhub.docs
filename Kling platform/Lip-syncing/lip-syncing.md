# Lip-syncing

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/videos/advanced-lip-sync:
    post:
      summary: Lip-syncing
      deprecated: false
      description: ''
      tags:
        - Kling platform/lip-syncing
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: false
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
                session_id:
                  type: string
                  description: The session ID will be generated based on the lip-sync face recognition interface.
                face_choose:
                  type: array
                  items:
                    type: object
                    properties:
                      face_id:
                        type: string
                        description: The face ID is returned by the face recognition interface.
                      audio_id:
                        type: string
                        description: >-
                          The ID of the audio generated through the listening interface can only be an audio file generated within the last 30 days, with a duration of no less than 2 seconds and no more than 60 seconds. Either the `audio_id` or `sound_file` parameter can be selected; both cannot be empty or have values ​​simultaneously.
                      sound_file:
                        type: string
                        description: >-
                          Audio files can be passed in either Base64 encoded audio or an audio URL (ensure it is accessible).
                          Audio files supported are .mp3/.wav/.m4a, with a file size not exceeding 5MB. Incompatible formats or excessively large files will return error codes.
                          Only audio files with a duration of at least 2 seconds and no more than 60 seconds are supported.
                          Either the `audio_id` or `sound_file` parameter can be used; both cannot be empty or have values ​​simultaneously.
                          The system will verify the audio content; if problems are found, it will return error codes.
                      sound_start_time:
                        type: integer
                        description: >-
                          Audio trimming start time; based on the original audio start time, the start time is 0 minutes and 0 seconds, in milliseconds; audio before the start time will be trimmed, and the trimmed audio must not be shorter than 2 seconds.
                      sound_end_time:
                        type: integer
                        description: Audio trimming end time: The end time must not be later than the total duration of the original audio.
                      sound_insert_time:
                        type: integer
                        description: >-
                          The timing of the inserted audio after cropping must overlap with the time interval during which the face can lip-sync, for at least 2 seconds.
                          The start time of the inserted audio must not be earlier than the start time of the video, and the end time of the inserted audio must not be later than the end time of the video.
                      sound_volume:
                        type: integer
                        description: Audio volume level; the larger the value, the louder the volume. Value range: [0, 2]
                      original_audio_volume:
                        type: integer
                        description: Original video volume; the larger the value, the louder the volume. Value range: [0, 2]; if the original video has no sound, this parameter has no effect.
                    x-apifox-orders:
                      - face_id
                      - audio_id
                      - sound_file
                      - sound_start_time
                      - sound_end_time
                      - sound_insert_time
                      - sound_volume
                      - original_audio_volume
                    required:
                      - face_id
                      - sound_start_time
                      - sound_end_time
                      - sound_insert_time
                      - sound_volume
                      - original_audio_volume
                  description: Specific face lip-syncing; includes face ID, lip shape reference, etc.; currently only supports specifying a single person for lip-syncing.
                external_task_id:
                  type: string
                callback_url:
                  type: string
              required:
                - session_id
                - face_choose
              x-apifox-orders:
                - session_id
                - face_choose
                - external_task_id
                - callback_url
            example:
              session_id: '825465778199224380'
              face_choose:
                - face_id: '-1'
                  audio_id: '825451760499568680'
                  sound_file: ''
                  sound_start_time: 0
                  sound_end_time: 5000
                  sound_insert_time: 1000
                  sound_volume: 1
                  original_audio_volume: 1
              external_task_id: ''
              callback_url: ''
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
      x-apifox-folder: Kling platform/lip-syncing
      x-apifox-status: testing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386403357-run
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
