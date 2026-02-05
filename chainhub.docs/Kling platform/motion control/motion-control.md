# Motion control

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /kling/v1/videos/motion-control:
    post:
      summary: motion control
      deprecated: false
      description: ""
      tags:
        - Kling Platform/Motion Control
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: false
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
                  description: |-
                    Text prompts can include positive and negative descriptions.
                    Prompts can be used to add elements to the screen, achieve camera movement effects, etc. See the Keling "Motion Control" User Guide for details.
                    No more than 2500 characters.
                image_url:
                  type: string
                  description: |-
                    The characters, backgrounds, and other elements in the generated video will be based on the reference image.
                    The video content must meet the following requirements:
                    Characters can be realistic or cartoon-style characters with proportions similar to natural people, avoiding occlusion; realistic characters are preferred.
                    The area of ​​the character in the image must exceed 5% of the image area.
                    Includes support for inputting Base64 encoded images or image URLs (ensure accessibility).
                    Supported image formats: .jpg / .jpeg / .png
                    Image file size cannot exceed 10MB, image dimensions must be at least 300px, and aspect ratio must be between 1:2.5 and 2.5:1.
                keep_original_sound:
                  type: string
                  description: |-
                    Option to keep the original audio of the video
                    Enum values: yes, no
                    yes: Keep the original audio
                    no: Do not keep the original audio
                character_orientation:
                  type: string
                  description: |-
                    Generates the orientation of people in a video, which can be either the same as the image or the same as the video.
                    Enumeration values: image, video, where:
                    image: the orientation of people in the image is the same; in this case, the reference video length must not exceed 10 seconds;
                    video: the orientation of people in the video is the same; in this case, the reference video length must not exceed 30 seconds;
                mode:
                  type: string
                  description: |-
                    Video generation mode
                    Enum values: std, pro
                    std: Standard mode (basic), cost-effective
                    pro: Expert mode (high quality), better video quality
                callback_url:
                  type: string
                external_task_id:
                  type: string
                video_url:
                  type: string
                  description: >-
                    The video content must meet the following requirements:

                    There must be only one realistic-style person, either full-body or upper-body including the head, with no occlusion.

                    The person's body movements and facial expressions must be clear and must not include complex actions such as somersaults or handstands.

                    The action video should be shot in one continuous take, with the person always appearing in the frame; avoid scene cuts or camera movements.

                    Supported video file formats are .mp4 and .mov, with a file size not exceeding 100MB. The length and width of the video must each be between 340px and 3850px. If these checks fail, an error code will be returned.

                    The minimum video duration is 3 seconds. The maximum duration depends on the character orientation (character_orientation):

                      If the orientation matches the person in the video, the maximum duration is 30 seconds.

                      If the orientation matches the person in the image, the maximum duration is 10 seconds.

                    The system will validate the video content and return an error code if there are any issues.
              required:
                - image_url
                - video_url
                - character_orientation
                - mode
              x-apifox-orders:
                - prompt
                - image_url
                - video_url
                - keep_original_sound
                - character_orientation
                - mode
                - callback_url
                - external_task_id
            example:
              prompt: Make the people in the picture look like they are in the video.
              image_url: >-
                https://p4-fdl.klingai.com/ksc2/nNAclQB2ZuqDEm6MuN_yy7WBwX-VSJ7DW9BzEq8AkSf2xBrbVVc9NS3viTiOht2ZEAtnU4f1PzqCQXnbt9smNKHN5hFuxmFfnLJvxQSoaKr3d8vZFp_JXOZcvL8f0W4-5FUtQlu-PFIvxwsn8X2IROKghKCLqQ0PYX3TTXwhwKJo7NSqCKuxwJ7sgTA11Mflkq87--ArN1PdxLGee5rD8Q.png?cacheKey=ChtzZWN1cml0eS5rbGluZy5tZXRhX2VuY3J5cHQSsAG-oRROZ9QX15Z136vy0U9XHk81HfVTfutTifK00RSAJkOox6WfOhljFJYGmpGu7T-pSjkrc_jglivtThAq9w3maStP4AVnvsU6EPV4k11h96vHnPr6ncT_07t-LV7oB0Pnqe0NAWTihVWvffzo1zwRKu-pBBVHD5fFUeofm38uHCJ2AWCiZXlovy-uswtyMu_peSMPM9ZW86ua5VeOkcCgxUGIXM-wJoP1Ratuf4elGBoSbgFFnrpiqTZzapT733K7iU3CIiDpcbQXOnQEs1YkUZvWhgfnDOlog1MrqRmXk3KyN-YA7igFMAE&x-kcdn-pid=112757&pkey=AAX4LOOHvIOIhksHRujlp02vvKT9cVyrKSKpi4zbGommETuT4G-aRzmXzf_canc9UMFYghw1t8FCfEc4TuhzxFOpVxb9-fxtocDBi87kZ6AZx6UXcHr99mq-Eql-V6szHYE
              video_url: >-
                https://v2-fdl.kechuangai.com/bs2/upload-ylab-stunt/ai_portal/1765888564/iruVi3xLEK/%E6%AF%94%E5%BF%83%E8%88%9E.mp4?x-kcdn-pid=112344&pkey=AAV4qWDBpdlkaoPLTTibRcE45eU-vvFFLSfJ39G1-dNBsyDL-EjgGQkJH5kfTPSBRlhyHURv15jluiHTfSDctyD-maauTUuZdcoxgiEUpRNKfwq4td2_MKfg2i-K4bR9djo&cacheKey=CiJzaW5nbGUuc2VjdXJpdHkua2xpbmcubWV0YV9lbmNyeXB0ElCo5bcLqm5hc4LTbnmm1AmjOr6OYQsjXuU6/RsYhpAClCPVu6SzBDoPn9P4Z9MsRhOJRm1o1gofTQyuZ8he5zIdjqH57E33Bfr52J2f++pe7BoSM3fb7wMl2Fj3O+srsempz23IIiDAFsw1NAobuaeyIDF2sRlg9gt4F/VLTu5CeSYyIHkxdSgFMAE=
              keep_original_sound: "yes"
              character_orientation: image
              mode: std
              callback_url: ""
              external_task_id: ""
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
      x-apifox-folder: Kling Platform/Motion Control
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-398754751-run
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
