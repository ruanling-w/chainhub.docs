# OpenAI query task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/videos/{id}:
    get:
      summary: OpenAI query task
      deprecated: false
      description: |+
        Given a hint, the model will return one or more complete predictions, and may also return the probability of an alternative label at each location.

        Complete creation for the provided hint and parameters

      tags:
        - Video model/sora video generation/OpenAI official video format
      parameters:
        - name: id
          in: path
          description: ''
          required: true
          example: sora-2:task_01k81e7r1mf0qtvp3ett3mr4jm
          schema:
            type: string
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
        - name: X-Forwarded-Host
          in: header
          description: ''
          required: false
          example: localhost:5173
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties: {}
            examples: {}
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  status:
                    type: string
                  video_url:
                    type: 'null'
                  enhanced_prompt:
                    type: string
                  status_update_time:
                    type: integer
                required:
                  - id
                  - status
                  - video_url
                  - enhanced_prompt
                  - status_update_time
              examples:
                '1':
                  summary: pending
                  value:
                    id: sora-2:task_01k6x15vhrff09dkkqjrzwhm60
                    detail:
                      id: task_01k6x15vhrff09dkkqjrzwhm60
                      input:
                        size: small
                        model: sy_ore
                        images:
                          - >-
                            https://filesystem.site/cdn/20250612/VfgB5ubjInVt8sG6rzMppxnu7gEfde.png
                          - >-
                            https://filesystem.site/cdn/20250612/998IGmUiM2koBGZM3UnZeImbPBNIUL.png
                        prompt: make animate
                        orientation: portrait
                      status: pending
                      pending_info:
                        id: task_01k6x15vhrff09dkkqjrzwhm60
                        seed: null
                        type: video_gen
                        user: user-a1sGDUIOXV32hNITe59LEkHa
                        model: sy_8
                        title: New Video
                        width: 352
                        height: 640
                        prompt: make animate
                        sdedit: null
                        status: processing
                        actions: null
                        guidance: null
                        n_frames: 450
                        priority: 2
                        operation: simple_compose
                        preset_id: null
                        created_at: '2025-10-06T15:10:26.875729Z'
                        n_variants: 1
                        project_id: null
                        request_id: null
                        generations: []
                        tracking_id: null
                        progress_pct: 0.9302178175176704
                        remix_config: null
                        inpaint_items:
                          - type: image
                            preset_id: null
                            crop_bounds: null
                            frame_index: 0
                            cameo_file_id: null
                            generation_id: null
                            upload_media_id: media_01k6x15tnzezbst05sth2qgd8r
                            source_end_frame: 0
                            uploaded_file_id: null
                            source_start_frame: 0
                          - type: image
                            preset_id: null
                            crop_bounds: null
                            frame_index: 0
                            cameo_file_id: null
                            generation_id: null
                            upload_media_id: media_01k6x15tzafwztz74t018v3enw
                            source_end_frame: 0
                            uploaded_file_id: null
                            source_start_frame: 0
                        interpolation: null
                        is_storyboard: null
                        failure_reason: null
                        organization_id: null
                        moderation_result:
                          code: null
                          type: passed
                          task_id: task_01k6x15vhrff09dkkqjrzwhm60
                          is_output_rejection: false
                          results_by_frame_index: {}
                        needs_user_review: false
                        queue_status_message: null
                        progress_pos_in_queue: null
                        num_unsafe_generations: 0
                        estimated_queue_wait_time: null
                    status: pending
                    status_update_time: 1759763621142
                '2':
                  summary: Successful examples
                  value:
                    id: video_5c6a605a-30c0-4a6a-9dbd-d1d6cfdd9980
                    size: 1280x720
                    model: sora-2
                    object: video
                    status: completed
                    seconds: '10'
                    progress: 100
                    video_url: >-
                      https://midjourney-plus.oss-us-west-1.aliyuncs.com/sora/cc4fb429-22a5-4747-a6f9-a6badccf8f42.mp4
                    created_at: 1761622232
                    completed_at: 1761622385
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/OpenAI official video format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-363309789-run
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
