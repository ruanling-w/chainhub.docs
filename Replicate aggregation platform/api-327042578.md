# Create task black-forest-labs/flux-fill-dev

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/models/black-forest-labs/flux-fill-dev/predictions:
    post:
      summary: Create task black-forest-labs/flux-fill-dev
      deprecated: false
      description: Official documentation:https://replicate.com/black-forest-labs/flux-fill-dev
      tags:
        - Replicate aggregation platform
      parameters:
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
                input:
                  type: object
                  properties:
                    mask:
                      type: string
                      description: A black and white image is used to describe the portion of the image that needs to be repaired. Black areas will be preserved, and white areas will be repaired.
                    image:
                      type: string
                      description: >-
                        The image to be repaired. It may contain an alpha mask. If the image width or height is not a multiple of 32, it will be scaled to the nearest multiple of 32. If the image size exceeds 1440x1440, it will be shrunk to fit a 1440x1440 size.
                    prompt:
                      type: string
                      description: Prompt to generate an image.
                    guidance:
                      type: integer
                      description: Guidance information for image generation. Default: 30. Minimum: 0, Maximum: 100.
                    lora_scale:
                      type: integer
                      description: >-
                        Determine the appropriate strength for the primary LoRA. For basic inference, a reasonable result is between 0 and 1. For `go_fast`, we apply a 1.5 multiplier to this value; generally, scaling the base value by this factor will result in good performance. You may still need to experiment to find the optimal value for your specific LoRA. Default: 1. Minimum: -1, Maximum: 3.
                    megapixels:
                      type: string
                      description: >-
                        Approximate pixel count for the generated image. Use match_input to match the size of the input (up to 1440x1440 pixels), default: "1".
                    num_outputs:
                      type: integer
                      description: Number of outputs to generate. Default: 1. Minimum: 1, Maximum: 4.
                    output_format:
                      type: string
                      description: The format of the output image. Default: "webp".
                    output_quality:
                      type: integer
                      description: >-
                        The quality of the output image, ranging from 0 to 100. 100 is the best quality, and 0 is the lowest quality. This is unrelated to the .png output. Default: 80
                    num_inference_steps:
                      type: integer
                      description: Noise reduction steps. Recommended range: 28-50. Fewer steps result in lower output quality but faster speed. Default: 28. Minimum: 1, Maximum: 50.
                  required:
                    - image
                    - prompt
                  x-apifox-orders:
                    - mask
                    - image
                    - prompt
                    - guidance
                    - lora_scale
                    - megapixels
                    - num_outputs
                    - output_format
                    - output_quality
                    - num_inference_steps
              x-apifox-orders:
                - input
            example:
              input:
                mask: >-
                  https://replicate.delivery/pbxt/M0hxLu8a1YBcybWuumSsfoEec8ooer6JZ2fR28vuM1U0CN9m/74b40bb1-364a-461a-bec5-200a38c7bc87.png
                image: >-
                  https://replicate.delivery/pbxt/M0hxMJeO7wFCMr7QYNZsjRxzHhz6ntlLllMteRQNsRD7f3Nf/flux-fill-dev.webp
                prompt: a spaceship
                guidance: 30
                lora_scale: 1
                megapixels: '1'
                num_outputs: 2
                output_format: webp
                output_quality: 80
                num_inference_steps: 28
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
                  model:
                    type: string
                  version:
                    type: string
                  input:
                    type: object
                    properties:
                      aspect_ratio:
                        type: string
                      input_image:
                        type: string
                      output_format:
                        type: string
                      prompt:
                        type: string
                      prompt_upsampling:
                        type: boolean
                      safety_tolerance:
                        type: integer
                    required:
                      - aspect_ratio
                      - input_image
                      - output_format
                      - prompt
                      - prompt_upsampling
                      - safety_tolerance
                  logs:
                    type: string
                  output:
                    type: 'null'
                  data_removed:
                    type: boolean
                  error:
                    type: 'null'
                  status:
                    type: string
                  created_at:
                    type: string
                  urls:
                    type: object
                    properties:
                      cancel:
                        type: string
                      get:
                        type: string
                      stream:
                        type: string
                      web:
                        type: string
                    required:
                      - cancel
                      - get
                      - stream
                      - web
                required:
                  - id
                  - model
                  - version
                  - input
                  - logs
                  - output
                  - data_removed
                  - error
                  - status
                  - created_at
                  - urls
              example:
                id: tv3jnp73n1rmc0crb54b3srz94
                model: black-forest-labs/flux-fill-dev
                version: hidden
                input:
                  guidance: 30
                  image: >-
                    https://replicate.delivery/pbxt/M0hxMJeO7wFCMr7QYNZsjRxzHhz6ntlLllMteRQNsRD7f3Nf/flux-fill-dev.webp
                  lora_scale: 1
                  mask: >-
                    https://replicate.delivery/pbxt/M0hxLu8a1YBcybWuumSsfoEec8ooer6JZ2fR28vuM1U0CN9m/74b40bb1-364a-461a-bec5-200a38c7bc87.png
                  megapixels: '1'
                  num_inference_steps: 28
                  num_outputs: 1
                  output_format: webp
                  output_quality: 80
                  prompt: a spaceship
                logs: ''
                output: null
                data_removed: false
                error: null
                status: starting
                created_at: '2025-07-30T03:03:25.864Z'
                urls:
                  cancel: >-
                    https://api.replicate.com/v1/predictions/tv3jnp73n1rmc0crb54b3srz94/cancel
                  get: >-
                    https://api.replicate.com/v1/predictions/tv3jnp73n1rmc0crb54b3srz94
                  stream: >-
                    https://stream.replicate.com/v1/files/bcwr-epcf2nmmvkvxq7trerel6zuoiwzyoji3ifhkuu3lf7rtdzh3i6ca
                  web: https://replicate.com/p/tv3jnp73n1rmc0crb54b3srz94
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-327042578-run
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
