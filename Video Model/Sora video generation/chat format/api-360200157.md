# Continuous modification to generate video

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1/chat/completions:
    post:
      summary: Continuous modification to generate video
      deprecated: false
      description: |-
        Given a hint, the model will return the completion of one or more predictions, and may also return the probability of an alternative label at each location.

        Created with the provided hint and parameters

        Official documentation: https://platform.openai.com/docs/api-reference/chat/create
      tags:
        - Video model/sora video generation/chat format
      parameters:
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
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                  enum:
                    - sora-2
                    - sora-2-pro
                  x-apifox-enum:
                    - value: sora-2
                      name: Standard Version
                      description: Only supports 10s standard definition
                    - value: sora-2-pro
                      name: Member Version
                      description: Supports 15s high definition
                messages:
                  type: array
                  items:
                    type: object
                    properties:
                      role:
                        type: string
                      content:
                        type: string
                    required:
                      - role
                      - content
                    x-apifox-orders:
                      - role
                      - content
                stream:
                  type: boolean
              required:
                - model
                - messages
                - stream
              x-apifox-orders:
                - model
                - messages
                - stream
            example:
              model: sora-2
              messages:
                - role: user
                  content: Generate a high-definition video of cows and horses dancing.
                - role: assistant
                  content: >-
                    ```json

                    {
                      "prompt": "Generate a high-definition video of cows and horses dancing.",
                      "orientation": "portrait"
                    }

                    ```


                    > ID: `task_01k7dzptgwf2z87wj2c3t36qk0`

                    [Data Preview](https://asyncdata.net/web/task_01k7dzptgwf2z87wj2c3t36qk0)

                    |
                    [Raw Data](https://asyncdata.net/source/task_01k7dzptgwf2z87wj2c3t36qk0)

                    > Queuing...

                    > Generating.

                    >🏃‍ Progress 76...

                    > Generating Complete ✅

                    > sid: s_68ec8accd80c8191ae1fc957af78caaa


                    ![https://filesystem.site/cdn/20251013/929d094fcd1844c3ee38be9476fd03.webp](https://filesystem.site/cdn/20251013/929d094fcd1844c3ee38be9476fd03.webp)

                    [Online Play▶️](https://filesystem.site/cdn/20251013/5781a601c5ce5e216e914fef119c99.mp4)
                - role: user
                  content: Let the cow's head have a halo, and the horse's feet step on auspicious clouds.
              stream: true
      responses:
        '200':
          description: ''
          content:
            text/event-stream:
              schema:
                type: object
                properties: {}
              example: |-
                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "role": "assistant",
                                "content": ""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "```"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "json"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\n"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "{\n"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " "
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " \""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "prompt"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\":"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " \""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "让"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "牛"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "的"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "头"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "上"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "顶"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "着"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "光"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "圈"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "，"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "马"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "的"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "脚"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "下"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "踩"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "着"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "祥云"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\",\n"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " "
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " \""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "orientation"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\":"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " \""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "portrait"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\",\n"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " "
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " \""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "sid"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\":"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": " \""
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "s"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "_"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "68"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "ec"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "8"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "acc"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "d"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "80"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "c"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "819"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "1"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "ae"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "1"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "fc"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "957"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "af"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "78"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "c"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "aaa"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\"\n"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "}\n"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "```"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {},
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\n\n> ID: `task_01k7e5w9z5f2d91pekrqy59rwc`\n>[数据预览](https://asyncdata.net/web/task_01k7e5w9z5f2d91pekrqy59rwc) | [原始数据](https://asyncdata.net/source/task_01k7e5w9z5f2d91pekrqy59rwc)\n> 排队中"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\n> 生成中"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\n\n>🏃‍ 进度 36.."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "44.."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "61.."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "69.."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "81.."
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {
                                "content": "\n\n> 生成完成 ✅\n> sid: s_68eca3f141808191b1fd30fea1b731bd\n\n![https://filesystem.site/cdn/20251013/38e999994cfa666de5e677d2af347f.webp](https://filesystem.site/cdn/20251013/38e999994cfa666de5e677d2af347f.webp)\n[在线播放▶️](https://filesystem.site/cdn/20251013/a7a7930bd01f7f313bbb6ecb234075.mp4)"
                            },
                            "finish_reason": null
                        }
                    ]
                }

                data: {
                    "id": "chatcmpl-89C77NMqv7oh6ajWBZful0xBNsJN1",
                    "object": "chat.completion.chunk",
                    "created": 1760338775,
                    "model": "sora-2",
                    "choices": [
                        {
                            "index": 0,
                            "delta": {},
                            "finish_reason": "stop"
                        }
                    ]
                }

                data: [DONE
                ]
          headers: {}
          x-apifox-name: Success
      security:
        - bearer: []
      x-apifox-folder: Video model/sora video generation/chat format
      x-apifox-status: released
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-360200157-run
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
