# Remix (mixing graph)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ""
  description: ""
  version: 1.0.0
paths:
  /ideogram/remix:
    post:
      summary: Remix (mixing graph)
      deprecated: false
      description: 官方文档：https://developer.ideogram.ai/api-reference/api-reference/remix
      tags:
        - Painting Model/Ideogram
      parameters:
        - name: Content-Type
          in: header
          description: ""
          required: true
          example: multipart/form-data
          schema:
            type: string
        - name: Accept
          in: header
          description: ""
          required: true
          example: application/json
          schema:
            type: string
        - name: Authorization
          in: header
          description: ""
          required: true
          example: Bearer {{YOUR_API_KEY}}
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                image_request:
                  description: >-
                    "prompt": "a beautiful sunset over mountains",  
                    //Prompt words for generating the image (required)
                       "aspect_ratio": "ASPECT_16_9", 
                       // Image aspect ratio (optional) Possible values: ASPECT_10_16/ASPECT_16_10/ASPECT_9_16/ASPECT_16_9/ASPECT_3_2/ASPECT_2_3/ASPECT_4_3/ASPECT_3_4/ASPECT_1_1/ASPECT_1_3/ASPECT_3_1
                       "color_palette": { 
                       // Color palette (optional)
                       "name": "FRESH" 
                       // Preset palette name (choose one from members) Possible values: EMBER/FRESH/JUNGLE/MAGIC/MELON/MOSAIC/PASTEL/ULTRAMARINE
                       // Or use a custom color:
                          /*"members": [
                            {
                              "color_hex": "#FF0000", // Color hexadecimal value (required)
                              "color_weight": 1.0 // Color weight (optional) Range: 0.05-1.0
                            }
                          ]*/
                        },
                        "image_weight": 50, 
                        // Image weight (optional) Range: 1-100, default 50
                        "magic_prompt_option": "AUTO", 
                        // Whether to use MagicPrompt (optional) Possible values: AUTO/ON/OFF
                        "model": "V_2", 
                        // Model to use (optional) Default V_2, possible values: V_1/V_1_TURBO/V_2/V_2_TURBO
                        "negative_prompt": "clouds,blur", 
                        // Negative prompt (optional) Describes content you don't want to appear in the image
                        "num_images": 1, 
                        // Number of images generated (optional) Range: 1-8, default 1
                        "resolution": "RESOLUTION_1024_1024",
                         // Resolution (optional) Possible values ​​include various resolution combinations from 512x1536 to 1536x640
                        "seed": 123456, 
                        // Random seed (optional) Range: 0-2147483647
                        "style_type": "REALISTIC" 
                        // Style type (optional) Optional values: AUTO/GENERAL/REALISTIC/DESIGN/RENDER_3D/ANIME
                  example: >-
                    {    "image_weight": 50,    "model": "V_1",   
                    "magic_prompt_option": "AUTO",    "prompt":
                    "A%20serene%20tropical%20beach%20",    "aspect_ratio":
                    "ASPECT_10_16",    "seed": 12345,    "negative_prompt":
                    "brush%20strokes%2C%20painting"}
                  type: string
                image_file:
                  description: " Image file (required): The source image file used to generate the new image."
                  example: file://C:\Users\Administrator\Desktop\example.png
                  type: string
                  format: binary
            example: ""
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: integer
                  message:
                    type: string
                  request_id:
                    type: string
                  data:
                    type: object
                    properties:
                      task_id:
                        type: string
                      task_status:
                        type: string
                      created_at:
                        type: integer
                      updated_at:
                        type: integer
                    required:
                      - task_id
                      - task_status
                      - created_at
                      - updated_at
                required:
                  - code
                  - message
                  - request_id
                  - data
          headers: {}
          x-apifox-name: success
      security: []
      x-apifox-folder: Painting Model/Ideogram
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-244685410-run
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
