# Access Tutorial

# Supported models

> If you find any more interesting models on the official website, please contact the administrator to add them.

| Model                                     | Illustrate       |
| ----------------------------------------- | ---------------- |
| fal-ai/flux-1/dev                         | Image generation |
| fal-ai/flux-1/dev/image-to-image          | Image generation |
| fal-ai/flux-1/dev/redux                   | Image generation |
| fal-ai/flux-1/schnell                     | Image generation |
| fal-ai/flux-1/schnell/redux               | Image generation |
| fal-ai/flux-pro/kontext                   | Image generation |
| fal-ai/flux-pro/kontext/max               | Image generation |
| fal-ai/flux-pro/kontext/max/multi         | Image generation |
| fal-ai/flux-pro/kontext/max/text-to-image | Image generation |
| fal-ai/flux-pro/kontext/multi             | Image generation |
| fal-ai/flux-pro/kontext/text-to-image     | Image generation |

---

# Fal-ai API Interface Documentation

> **Agreement**  
> Add header `Authorization: Bearer your-key`  
> The official website uses `Authorization: key your-key`  
> Replace the official `https://queue.fal.run` with your own request domain
> Input, output, and request method are consistent with the official website

## 1. Generate task

### Interface

```
POST {{BASE_URL}}/fal-ai/{{model}}
```

### Example

```shell
curl --request POST \
  --url {{BASE_URL}}/fal-ai/flux-1/dev \
  --header 'Authorization: Bearer your-key' \
  --header 'Content-Type: application/json' \
  --data '{
     "prompt": "Extreme close-up of a single cat eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"openai-hk\" is painted over it in big, white brush strokes with visible texture."
}'
```

Please refer to the documentation for each model for specific request methods. Please note that **request parameters may not function correctly during transit**. You can start testing from the prompt. If you find that a parameter in the documentation is not working properly, you can contact customer service for maintenance.

### Return body

```json
{
  "status": "IN_QUEUE",
  "request_id": "551a32da-52b2-4be8-bf2f-bfb7cce2b324",
  "response_url": "https://queue.fal.run/fal-ai/flux-1/requests/551a32da-52b2-4be8-bf2f-bfb7cce2b324",
  "status_url": "https://queue.fal.run/fal-ai/flux-1/requests/551a32da-52b2-4be8-bf2f-bfb7cce2b324/status",
  "cancel_url": "https://queue.fal.run/fal-ai/flux-1/requests/551a32da-52b2-4be8-bf2f-bfb7cce2b324/cancel",
  "queue_position": 0
}
```

> **Notes**
> The `response_url` in the response body is the link for the next request. You need to replace `https://queue.fal.run` with your intermediary address.

---

## 2. Retrieving Task Results

> Results have an expiration period; please be sure to save them.

### Interface

```
GET {BASE_URL}/fal-ai/{modelname}/requests/{request_id}
```

### Example

```shell
curl --request GET \
  --url {{BASE_URL}}/fal-ai/flux-1/requests/551a32da-52b2-4be8-bf2f-bfb7cce2b324 \
  --header 'Authorization: Bearer hk-your-key' \
  --header 'Content-Type: application/json'
```

---

### Return body.image

Results are in `images`

```json
{
  "images": [
    {
      "url": "https://v3.fal.media/files/rabbit/aQEmU4lEKKIIr9cDOChUB.png",
      "width": 1024,
      "height": 768,
      "content_type": "image/png"
    }
  ],
  "timings": {
    "inference": 1.2249955059960485
  },
  "seed": 920212137,
  "has_nsfw_concepts": [false],
  "prompt": "Extreme close-up of a single cat eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"openai-hk\" is painted over it in big, white brush strokes with visible texture."
}
```

### Return to body.video

Result in `video`

```json
{
  "video": {
    "url": "https://v3.fal.media/files/lion/eSsTNfWQRXfWGim1B8ZL5_output.mp4",
    "content_type": "video/mp4",
    "file_name": "output.mp4",
    "file_size": 946834
  }
}
```

---

> The results may expire; please be sure to save them.

---
