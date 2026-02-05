# Create task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /tencent-vod/v1/aigc-image:
    post:
      summary: Create task
      deprecated: false
      description: Official documentation:https://cloud.tencent.com/document/product/266/126240
      tags:
        - Painting model / Tencent AIGC raw image
      parameters:
        - name: Authorization
          in: header
          description: ""
          required: false
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ""
          required: false
          example: application/json
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
                  description: Prompt words
                negative_prompt:
                  type: string
                  description: A prompt to prevent the model from generating images.
                enhance_prompt:
                  type: string
                  description: |-
                    Whether to automatically optimize prompts. Enabling this setting will automatically optimize the passed-in prompt to improve generation quality. Possible values:
                    Enabled: On;
                    Disabled: Off;
                output_config:
                  type: object
                  properties:
                    storage_mode:
                      type: string
                      description: |-
                        Storage mode. Possible values:
                        Permanent: Permanent storage. The generated image files will be stored on VOD. The FileId can be obtained from the event notification.
                        Temporary: Temporary storage. The generated image files will not be stored on VOD. The URL for temporary access can be obtained from the event notification.

                        Default value: Temporary
                    aspect_ratio:
                      type: string
                      description: >-
                        Specifies the aspect ratio of the generated image.

                        When ModelName is GEM, the possible values ​​are:

                        1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, and 21:9;

                        When ModelName is Qwen or Jimeng, this is not currently supported. For Jimeng, the model will intelligently determine the aspect ratio of the output image based on the Prompt intent and the reference image size.

                        Example value: 16:9
                    person_generation:
                      type: string
                      description: |-
                        Whether to allow the generation of people or faces. Possible values:
                        AllowAdult: Allows the generation of adults;
                        Disallowed: Disallows the inclusion of people or faces in the image;

                        Example value: AllowAdult
                    input_compliance_check:
                      type: string
                      description: |-
                        Enables or disables input content compliance checks. Possible values:
                        Enabled: Enabled;
                        Disabled: Disabled;

                        Example value: Enabled
                    output_compliance_check:
                      type: string
                      description: |-
                        Enables compliance checks for output content. Possible values:
                        Enabled: Enabled;
                        Disabled: Disabled;

                        Example value: Enabled
                    resolution:
                      type: string
                      description: >-
                        The resolution of the generated image. Possible values ​​are:

                        720P, 1080P, 2K, 4K, 1024x1024, 2048x2048, 2304x1728, 2496x1664, 2560x1440, 3024x1296, 4096x4096, 4694x3520, 4992x3328, 5404x3040, 6198x2656. When using the Jimeng model, it is recommended to specify the image resolution and aspect ratio via Prompt.

                        Example value: 1024x1024
                  x-apifox-orders:
                    - storage_mode
                    - resolution
                    - aspect_ratio
                    - person_generation
                    - input_compliance_check
                    - output_compliance_check
                  description: Configure the output media files for the raw image task.
                session_id:
                  type: string
                  description: >-
                    The identifier used for deduplication. If a request with the same identifier has been made within the last three days, the current request will return an error. Maximum 50 characters; omitting the identifier or including an empty string indicates no deduplication.

                    Example value: mysession
                session_context:
                  type: string
                  description: |-
                    Source context, used to pass through user request information. The audio/video quality regeneration completion callback will return this field value, with a maximum length of 1000 characters.

                    Example value: mySessionContext
                tasks_priority:
                  type: string
                  description: |-
                    Task priority; higher values ​​indicate higher priority. Values ​​range from -10 to 10, with 0 representing no value.

                    Example value: 10
                ext_info:
                  type: string
                  description: |-
                    Reserved field, used for special purposes.
                    Example value: myextinfo
                file_infos:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                        description: |-
                          The input video file type. Possible values ​​are:
                          File: On-demand media file;
                          Url: Accessible URL;

                          Example value: File
                      file_id:
                        type: string
                        description: >-
                          The media file ID of the image file, i.e., the globally unique identifier of the file on VOD, is assigned by the VOD backend after successful upload. This field can be obtained from the video upload completion event notification or the VOD console. This parameter is valid when Type is set to File.

                          Notes:
                          1. Images smaller than 7MB are recommended;
                          2. Image format options are: jpeg, jpg, png, webp.

                          Example value: 3704211***509819
                      text:
                        type: string
                        description: |-
                          Input a description of the image to help the model understand it. Only valid for GEM 2.5 and GEM 3.0.
                          Example value: Task context: This is the main building that needs renovation (Figure 1), and its geometry must not be altered.
                      url:
                        type: string
                        description: |-
                          Accessible file URL. This parameter is valid when Type is set to Url.

                          Notes:
                          1. Images smaller than 7MB are recommended;
                          2. Image format options are: jpeg, jpg, png, webp.

                          Example value: https://test.com/1.png
                    x-apifox-orders:
                      - type
                      - file_id
                      - url
                      - text
                model_name:
                  type: string
                  description: |-
                    Model Name. Values:
                    GEM: Gemini;
                    Qwen: 千问;
                    Hunyuan: 混元.

                    Example Value: GEM
                model_version:
                  type: string
                  description: |-
                    Model version. Possible values:

                    When ModelName is GEM, possible values ​​are 2.5 and 3.0;
                    When ModelName is Qwen, possible value is 0925;
                    When ModelName is Hunyuan, possible value is 3.0;

                    Example value: 2.5
              required:
                - model_name
                - prompt
                - model_version
              x-apifox-orders:
                - model_name
                - model_version
                - prompt
                - file_infos
                - negative_prompt
                - enhance_prompt
                - output_config
                - session_id
                - session_context
                - tasks_priority
                - ext_info
            example:
              model_name: GEM
              model_version: "3.0"
              file_infos:
                - type: file
                  file_id: "387702299774574677"
                  url: ""
                  text: Description information of the original image
              prompt: convert this image to anime style
              negative_prompt: blur, distorted
              enhance_prompt: Enabled
              output_config:
                storage_mode: Temporary
                resolution: 1080P
                aspect_ratio: "1:1"
                person_generation: AllowAdult
                input_compliance_check: Enabled
                output_compliance_check: Enabled
              session_id: image-task-67890
              session_context: '{"user_id": "123", "scene": "profile_picture"}'
              tasks_priority: 10
              ext_info: ""
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  request_id:
                    type: string
                  response_url:
                    type: string
                  status_url:
                    type: string
                  cancel_url:
                    type: string
                  logs:
                    type: "null"
                  metrics:
                    type: object
                    properties: {}
                  queue_position:
                    type: integer
                required:
                  - status
                  - request_id
                  - response_url
                  - status_url
                  - cancel_url
                  - logs
                  - metrics
                  - queue_position
              example:
                Response:
                  TaskId: 251007502-AigcImage***2782aff1e896673f1ft
                  RequestId: f50d7667-72d8-46bb-a7e3-0613588971b6
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting model / Tencent AIGC raw image
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-398427541-run
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
