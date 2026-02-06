# Access Tutorial

### Replicate Official Format Call

If you need any models, please contact customer service to add them.

Replace https://api.replicate.com on the official website with {{BASE_URL}}/replicate. The input, output, and request methods should be consistent with the official website.

Integration Process

1. Create a Task
   After submitting the task, obtain the task ID.

2. Get Task Progress
   Query the task progress using the task ID and obtain the result.

PS：The returned resource link is only valid for 1 hour.

Return body Key field descriptions

Project Type Description
input object enter
output string or []string Output URL
status string Status: starting, processing, succeeded, failed

1.Task generation by path
Taking black-forest-labs/flux-schnell as an example

```
curl --request POST \
  --url {{BASE_URL}}/replicate/v1/models/black-forest-labs/flux-schnell/predictions \
  --header 'Authorization: Bearer hk-you-key' \
  --header 'Content-Type: application/json' \
  --data '{
    "input": {
      "prompt": "Japanese cartoon anime style, (1 person) (Gender: Male, Age: 30, Hair: Short black hair, Outfit: Dark blue hunting attire, includes a fitted jacket and trousers.) (A dimly lit room filled with tension,  is questioning Female, 27 years old, long black hair, pink tulle dress., who stands nervously in her pink dress, the sound of rain pattering against the window.)",
      "go_fast": true,
      "megapixels": "1",
      "num_outputs": 1,
      "aspect_ratio": "1:1",
      "output_format": "jpg",
      "output_quality": 80,
      "num_inference_steps": 4
    }
  }'
```

The returned data type ID is the ID of the next query task.

```
{
  "id": "qpt5jq1fssrmc0cmd5hvy31mdg",
  "model": "black-forest-labs/flux-schnell",
  "version": "dp-4d0bcc010b3049749a251855f12800be",
  "input": {
    "aspect_ratio": "1:1",
    "go_fast": true,
    "megapixels": "1",
    "num_inference_steps": 4,
    "num_outputs": 1,
    "output_format": "jpg",
    "output_quality": 80,
    "prompt": "Japanese cartoon anime style, (1 person) (Gender: Male, Age: 30, Hair: Short black hair, Outfit: Dark blue hunting attire, includes a fitted jacket and trousers.) (A dimly lit room filled with tension,  is questioning Female, 27 years old, long black hair, pink tulle dress., who stands nervously in her pink dress, the sound of rain pattering against the window.)"
  },
  "logs": "",
  "output": null,
  "data_removed": false,
  "error": null,
  "status": "starting",
  "created_at": "2025-01-15T09:54:55.566Z",
  "urls": {
    "cancel": "https://api.replicate.com/v1/predictions/qpt5jq1fssrmc0cmd5hvy31mdg/cancel",
    "get": "https://api.replicate.com/v1/predictions/qpt5jq1fssrmc0cmd5hvy31mdg",
    "stream": "https://stream.replicate.com/v1/files/bcwr-gvuc2rokjozhlaxh6dcvk6tvhh2ymt4egnnpxvmtqql57angyfsq"
  }
}
```

2.Generate task.version method
Using lucataco/flux-schnell-lora as an example: refer to the documentation: https://replicate.com/lucataco/flux-schnell-lora?input=http the version obtained from the documentation is 2a6b576af31790b470f0a8442e1e9791213fa13799cbb65a9fc1436e96389574

```
curl --request POST \
  --url {{BASE_URL}}/replicate/v1/predictions \
  --header 'Authorization: Bearer hk-your-key' \
  --header 'Content-Type: application/json' \
  --data '{
    "version": "2a6b576af31790b470f0a8442e1e9791213fa13799cbb65a9fc1436e96389574",
    "input": {
      "prompt": "Japanese cartoon anime style, (1 person) (Gender: Male, Age: 30, Hair: Short black hair, Outfit: Dark blue hunting attire, includes a fitted jacket and trousers.) (A dimly lit room filled with tension,  is questioning Female, 27 years old, long black hair, pink tulle dress., who stands nervously in her pink dress, the sound of rain pattering against the window.)",
      "hf_lora": "alvdansen/frosting_lane_flux",
      "lora_scale": 0.8,
      "num_outputs": 1,
      "aspect_ratio": "1:1",
      "output_format": "webp",
      "output_quality": 80,
      "prompt_strength": 0.8,
      "num_inference_steps": 4
    }
  }'
```

The return body format is consistent with the above format.
Get Task
Obtain the task ID through the above production process.
The results are in the key field `output`.
Note that the returned results and their linked files have time limits.
get {{BASE_URL}}/replicate/v1/predictions/{id}

```
curl --request GET \
  --url {{BASE_URL}}/replicate/v1/predictions/ctdwaehfz1rm80cmd5nsjd8114 \
  --header 'Authorization: Bearer hk-you-key' \
  --header 'Content-Type: application/json'
```

Return body

```json
{
  "id": "ctdwaehfz1rm80cmd5nsjd8114",
  "model": "black-forest-labs/flux-schnell",
  "version": "dp-4d0bcc010b3049749a251855f12800be",
  "input": {
    "aspect_ratio": "1:1",
    "go_fast": true,
    "megapixels": "1",
    "num_inference_steps": 4,
    "num_outputs": 1,
    "output_format": "jpg",
    "output_quality": 80,
    "prompt": "Japanese cartoon anime style, (1 person) (Gender: Male, Age: 30, Hair: Short black hair, Outfit: Dark blue hunting attire, includes a fitted jacket and trousers.) (A dimly lit room filled with tension,  is questioning Female, 27 years old, long black hair, pink tulle dress., who stands nervously in her pink dress, the sound of rain pattering against the window.)"
  },
  "logs": "Using seed: 62182\nrunning quantized prediction\nUsing seed: 62182\n  0%|          | 0/4 [00:00<?, ?it/s]\n 75%|███████▌  | 3/4 [00:00<00:00, 15.38it/s]\n100%|██████████| 4/4 [00:00<00:00, 13.43it/s]\nTotal safe images: 1 out of 1\n",
  "output": [
    "https://replicate.delivery/xezq/RoEhEdyl8PoIGFFPg46TU4Svj24i1NDVYmzehJfqLuX9nTFUA/out-0.jpg"
  ],
  "data_removed": false,
  "error": null,
  "status": "succeeded",
  "created_at": "2025-01-15T10:03:39.896Z",
  "started_at": "2025-01-15T10:03:40.584470194Z",
  "completed_at": "2025-01-15T10:03:41.142386377Z",
  "urls": {
    "cancel": "https://api.replicate.com/v1/predictions/ctdwaehfz1rm80cmd5nsjd8114/cancel",
    "get": "https://api.replicate.com/v1/predictions/ctdwaehfz1rm80cmd5nsjd8114",
    "stream": "https://stream.replicate.com/v1/files/bcwr-q57vie7wuzg3wxv2hvpajgmzqzmxe67kqddednevutmrpdcft6xq"
  },
  "metrics": {
    "image_count": 1,
    "predict_time": 0.557916184
  }
}
```
