# Multiple images and reference videos

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /kling/v1/videos/multi-image2video:
    post:
      summary: Multiple images and reference videos
      deprecated: false
      description: ''
      tags:
        - Kling platform / Multi-image reference video
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
                  description: Model name Enumeration value: kling-v1-6
                image_list:
                  type: array
                  items:
                    type: object
                    properties:
                      image:
                        type: string
                    required:
                      - image
                    x-apifox-orders:
                      - image
                  description: Supports up to 4 images
                prompt:
                  type: string
                  description: |-
                    Positive text prompts
                    cannot exceed 2500 characters
                negative_prompt:
                  type: string
                  description: Negative text prompts
                mode:
                  type: string
                  description: |-
                    Video generation mode
                    Enum values: std, pro
                    std: Standard mode (basic), cost-effective
                    pro: Expert mode (high quality), better video quality
                duration:
                  type: string
                  description: |-
                    Video duration (in seconds)
                    Enumerated values: 5, 10
                aspect_ratio:
                  type: string
                  description: The aspect ratio (width:height) of the generated image.
                callback_url:
                  type: string
                external_task_id:
                  type: string
              required:
                - model_name
                - mode
                - duration
                - image_list
                - prompt
              x-apifox-orders:
                - model_name
                - image_list
                - prompt
                - negative_prompt
                - mode
                - duration
                - aspect_ratio
                - callback_url
                - external_task_id
            example:
              model_name: kling-v1-6
              image_list:
                - image: >-
                    https://h2.inkwai.com/bs2/upload-ylab-stunt/se/ai_portal_queue_mmu_image_upscale_aiweb/3214b798-e1b4-4b00-b7af-72b5b0417420_raw_image_0.jpg
                - image: >-
                    https://p4-fdl.klingai.com/ksc2/VC9RYcz0EFN3IK7HvGJxvyYKZoI2RJoqDr3DIiw7piElFWcqhZkCo1AXSd1KKuRDOgyh-4S32fgf_Y_E2bI12JyhGq8cUh3JBi15-3LhOi6kHXyhsyklf8i7f_z-7H3UwMKOFf3sUyRwme99EGVIVIbfonztB9YHiRUelIN03Kmj4WOJ7alF7z-hAf2VIb0CcmQgkOCO0Xr4cb3aWMmbzQ.png?cacheKey=ChtzZWN1cml0eS5rbGluZy5tZXRhX2VuY3J5cHQSsAHN4HK7XWwUnbU-46Q6VYOkhHxmQ1SXM2l0e-BFYasrb-1uP_EnXqmdvS5QiMNNsNQVp3iPjf6ArMRBsh6ryOIAKZLAUJt8PGdhJR5vNyJ1VKwQnyZ-HY-1ah-nq3zld8Ku5CrjZbwy25qQ-49HwVGRVVW3UduaRfOYN5JlKTzarHKKd4MdlsaLuke_On28RC_ZH9DpqtgdPE2XClDiiob98C_GO_hJGNQxXFZXz6RLQRoSv3Uc89R3_xETrF65D8P8-8MOIiBvVz-WFbQmW09meHOCiSebrXRVetWFZd9xrpTvc8VZyCgFMAE&x-kcdn-pid=112757&pkey=AAWtwrHKmYCgcvnbtFoiaXw1li4FfT_ZtdY7vJ_P4LchpS9PAfe3IAX19TCZn6WNQirjrIFp2kT5OEl5_S_JJ8oyDLKVn6xLODNisUft5SfwEf3J4k95BSmohuROFGZ8amg
              prompt: Two images merged into one video
              negative_prompt: ''
              mode: std
              duration: '5'
              aspect_ratio: '16:9'
              callback_url: ''
              external_task_id: ''
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
      x-apifox-folder: Kling platform / Multi-image reference video
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-386179083-run
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
