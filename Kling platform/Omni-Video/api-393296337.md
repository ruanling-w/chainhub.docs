# Omni-Video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/videos/omni-video:
    post:
      summary: Omni-Video
      deprecated: false
      description: ''
      tags:
        - Kling platform/Omni-Video
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
                model_name:
                  type: string
                  description: Model name Enumeration value: kling-video-o1
                prompt:
                  type: string
                  description: |-
                    Text prompts, which can include positive and negative descriptions.
                    Prompts can be templated to meet different video generation needs.
                    Cannot exceed 2500 characters.
                image_list:
                  type: array
                  items:
                    type: object
                    properties:
                      image_url:
                        type: string
                      type:
                        type: string
                    x-apifox-orders:
                      - image_url
                      - type
                  description: |-
                    Reference Figure List

                    Reference images, including those for the main subject, scene, and style, can be used as the first or last frame in video generation. When used as the first or last frame:
                    The `type` parameter defines whether an image is the first or last frame: `first_frame` for the first frame and `end_frame` for the last frame.
                    Currently, last frame-only generation is not supported; that is, a first frame is required if a last frame image is present.
                    Video editing functions cannot be used when generating video from the first frame or from both the first and last frames.
                video_list:
                  type: array
                  items:
                    type: object
                    properties:
                      video_url:
                        type: string
                      refer_type:
                        type: string
                      keep_original_sound:
                        type: string
                    x-apifox-orders:
                      - video_url
                      - refer_type
                      - keep_original_sound
                  description: >-
                    Reference video, obtained via URL

                    It can be used as a feature reference video or as a video to be edited; the default is the video to be edited. The original audio can be selectively preserved.

                    The `refer_type` parameter distinguishes the reference video type: `feature` is the feature reference video, and `base` is the video to be edited.

                    When the reference video is a video to be edited, the first and last frames cannot be defined.

                    The `keep_original_sound` parameter selects whether to preserve the original audio: `yes` preserves it, `no` does not preserve it; this parameter also applies to the feature reference video.
                mode:
                  type: string
                  description: |-
                    Video generation mode
                    Enum values: std, pro
                    std: Standard mode (basic), cost-effective
                    pro: Expert mode (high quality), better video quality
                aspect_ratio:
                  type: string
                  description: |-
                    Aspect ratio (width:height) of the generated video
                    Enumerated values: 16:9, 9:16, 1:1
                    Required when first frame reference or video editing functions are not used.
                duration:
                  type: string
                  description: >-
                    Video duration (in seconds)

                    Enumerated values: 3, 4, 5, 6, 7, 8, 9, 10, where:

                    When using text-based video or first-frame image-based video, only 5 and 10 seconds are supported.

                    When using the video editing function ("refer_type":"base"), the output result is the same as the input video duration, and the current parameter is invalid; in this case, the billing is based on the input video duration rounded to the nearest integer.
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - model_name
                - prompt
                - mode
                - duration
              x-apifox-orders:
                - model_name
                - prompt
                - image_list
                - video_list
                - mode
                - aspect_ratio
                - duration
                - callback_url
                - external_task_id
            example:
              model_name: kling-video-o1
              prompt: Put a crown on <<<image_1>>>
              image_list:
                - image_url: >-
                    https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
              mode: pro
              aspect_ratio: '16:9'
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
      x-apifox-folder: Kling platform/Omni-Video
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-393296337-run
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
