# Create task

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /tencent-vod/v1/aigc-video:
    post:
      summary: Create task
      deprecated: false
      description: Official documentation:https://cloud.tencent.com/document/product/266/126240
      tags:
        - Video Model/Tencent AIGC Video Generation
      parameters:
        - name: Authorization
          in: header
          description: ''
          required: false
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
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
                  description: |-
                    To prevent the model from generating video prompts.
                    Example value: red
                enhance_prompt:
                  type: string
                  description: |-
                    Whether to automatically optimize prompt words. When enabled, the input Prompt will be automatically optimized to improve generation quality. Values include:
                    Enabled: Enabled;
                    Disabled: Disabled;

                    Example value: Enabled
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
                        Specifies the aspect ratio of the generated video.
                        When ModelName is Kling, for text-to-video generation, the available values ​​are 16:9, 9:16, and 1:1, with 16:9 as the default.
                        When ModelName is Vidu, for text-to-video generation and when using reference images, the available values ​​are:
                        16:9, 9:16, 4:3, 3:4, and 1:1, with 4:3 and 3:4 supported only in version q2.
                        When ModelName is Hailuo, this is not currently supported.
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
                        Whether to enable input content compliance check. Possible values:
                        Enabled: Enabled;
                        Disabled: Disabled;
                        Example value: Enabled
                    output_compliance_check:
                      type: string
                      description: |-
                        Whether to enable output content compliance check. Possible values:
                        Enabled: Enabled;
                        Disabled: Disabled;
                        Example value: Enabled
                    audio_generation:
                      type: string
                      description: |-
                        Whether to generate audio. Supported models include GV and OS. Values include:
                        Enabled: Enabled;
                        Disabled: Disabled;
                        Default value: Enabled
                        Example value: Enabled
                    duration:
                      type: string
                      description: |-
                        The duration of the generated video, in seconds.
                        When ModelName is Kling, the possible values ​​are 5 and 10, with a default of 5;
                        When ModelName is Hailuo, the possible values ​​are 6 and 10, with a default of 6;
                        When ModelName is Vidu, values ​​from 1 to 10 can be specified;
                        Example value: 8.0
                    resolution:
                      type: string
                      description: |-
                        The resolution of the generated video.

                        When ModelName is Kling, the options are 720P and 1080P, with 720P as the default.
                        When ModelName is Hailuo, the options are 768P and 1080P, with 768P as the default.
                        When ModelName is Vidu, the options are 720P and 1080P, with 720P as the default.
                        Example value: 720P
                  x-apifox-orders:
                    - storage_mode
                    - resolution
                    - aspect_ratio
                    - audio_generation
                    - duration
                    - person_generation
                    - input_compliance_check
                    - output_compliance_check
                  description: Configure the output media files for the live video task.
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
                  description: >-
                    This list contains a maximum of three source images, describing the resource images the model will use when generating the video.

                    Models supporting multiple image inputs:

                    1. GV: When using multiple image inputs, LastFrameFileId and LastFrameUrl cannot be used.

                    2. Vidu: Supports multi-image reference for video generation. For the q2 model, images 1-7 can be passed in using the ObjectId from FileInfos as the subject ID.

                    Note:
                    1. Image size cannot exceed 10MB.
                    2. Supported image formats: jpeg, png.
                last_frame_url:
                  type: string
                  description: >-
                    The URL of the media file used to generate the video as the last frame. Notes:
                    1. Only GV, Kling, and Vidu models are supported. Other models are not currently supported. When ModelName is GV, if this parameter is specified, FileInfos must also be specified as the first frame of the video to be generated. This parameter can only be specified when ModelName is Kling, ModelVersion is 2.1, and the output resolution is 1080P. This parameter can only be specified when ModelName is Vidu, ModelVersion is q2-pro, or q2-turbo.
                    2. The image size must be less than 5MB.
                    3. Image format options are: jpeg, jpg, png, webp.
                    Example value: https://test.com/1.png
                model_name:
                  type: string
                  description: |-
                    Model name. Values:
                    Hailuo: Sea snail;
                    Kling: Kling;
                    Vidu;
                    Example value: GV
                model_version:
                  type: string
                  description: |-
                    Model version. Possible values:
                    When ModelName is Hailuo, possible values ​​are 02, 2.3, 2.3-fast;
                    When ModelName is Kling, possible values ​​are 1.6, 2.0, 2.1, 2.5, O1;
                    When ModelName is Vidu, possible values ​​are q2, q2-pro, q2-turbo;
                    Example value: 2.3
              required:
                - model_name
                - prompt
                - model_version
              x-apifox-orders:
                - model_name
                - model_version
                - prompt
                - negative_prompt
                - enhance_prompt
                - file_infos
                - last_frame_url
                - output_config
                - session_id
                - session_context
                - tasks_priority
                - ext_info
            example:
              model_name: Kling
              model_version: '1.6'
              prompt: A car was driving on the highway, under the bright sunshine.
              negative_prompt: Blurry, jittery
              enhance_prompt: Enabled
              output_config:
                storage_mode: Temporary
                media_name: car-video
                duration: 8
                resolution: 1080P
                aspect_ratio: '16:9'
                audio_generation: Enabled
                person_generation: AllowAdult
                input_compliance_check: Enabled
                output_compliance_check: Enabled
                enhance_switch: Enabled
      responses:
        '200':
          description: ''
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
                    type: 'null'
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
          x-apifox-name: Success
      security: []
      x-apifox-folder: Video Model/Tencent AIGC Video Generation
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-399032083-run
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
