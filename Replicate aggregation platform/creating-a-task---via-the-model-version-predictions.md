# Create a task - via the model version (predictions)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /replicate/v1/predictions:
    post:
      summary: Create a task - via the model version (predictions)
      deprecated: false
      description: >-
        version models support the following

        "ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4":
        "stability-ai/stable-diffusion",

        "7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc":
        "stability-ai/sdxl",

        "95b7223104132402a9ae91cc677285bc5eb997834bd2349fa486f53910fd68b3":
        "stability-ai/stable-diffusion-inpainting",

        "15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d":
        "stability-ai/stable-diffusion-img2img",

        "2a6b576af31790b470f0a8442e1e9791213fa13799cbb65a9fc1436e96389574":
        "lucataco/flux-schnell-lora",

        "091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3":
        "lucataco/flux-dev-lora",

        "ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5":
        "andreasjansson/stable-diffusion-animation",

        "beecf59c4aee8d81bf04f0381033dfa10dc16e845b4ae00d281e2fa377e48a9f":
        "lucataco/animate-diff",

        "153b0087c2576ad30d8cbddb35275b387d1a6bf986bda5499948f843f6460faf":
        "sujaykhandekar/object-removal",

        "fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003":
        "cjwbw/rembg"

        For detailed model parameters, please visit replicate.com to view the model-specific request parameters.
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
                version:
                  type: string
                input:
                  type: object
                  properties:
                    width:
                      type: integer
                      description: Width of the generated image (in pixels). Must be a multiple of 64. Default: 768.
                    height:
                      type: integer
                      description: The height of the generated image (in pixels). Must be a multiple of 64. Default: 768.
                    prompt:
                      type: string
                      description: Input prompt.
                    scheduler:
                      type: string
                      description: Select a scheduler. Default: "DPMSolverMultistep".
                    num_outputs:
                      type: integer
                      description: Number of images to generate. Default: 1. Minimum: 1, Maximum: 4.
                    guidance_scale:
                      type: number
                      description: No classifier-guided scale. Default: 7.5. Minimum: 1, Maximum: 20.
                    num_inference_steps:
                      type: integer
                      description: Number of denoising steps. Default: 50. Minimum: 1, Maximum: 500.
                  required:
                    - guidance_scale
                    - num_inference_steps
                  x-apifox-orders:
                    - width
                    - height
                    - prompt
                    - scheduler
                    - num_outputs
                    - guidance_scale
                    - num_inference_steps
              x-apifox-orders:
                - version
                - input
            example:
              version: >-
                stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4
              input:
                width: 768
                height: 768
                prompt: an astronaut riding a horse on mars, hd, dramatic lighting
                scheduler: K_EULER
                num_outputs: 1
                guidance_scale: 7.5
                num_inference_steps: 50
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
                created: 1589478378
                data:
                  - url: https://...
                  - url: https://...
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Replicate aggregation platform
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-330236623-run
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
