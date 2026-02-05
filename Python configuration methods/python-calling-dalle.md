# Python calls DALL·E

# Image Generation API Guide

## Function Overview

The API provides three main functions:

1. 🎨 Text to Image Generation (DALL·E 3 and DALL·E 2)
2. ✏️ Image Editing (DALL·E 2 only)
3. 🔄 Image Variation Generation (DALL·E 2 only)

## 1. Image Generation

### Basic Usage

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
```

### Parameter Description

* **Size Options**: 1024x1024, 1024x1792, 1792x1024
* **Quality Options**: standard (default), hd (DALL·E 3 exclusive)
* **Quantity Limits**:
* DALL·E 3: 1 image per batch
* DALL·E 2: Maximum 10 images per batch

## 2. Image Editing (DALL·E 2)

### Usage Examples

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

response = client.images.edit((
  model="dall-e-2",
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url
```

### Requirements

* 📝 Image and mask must be in PNG format
* 📏 Must be a square image
* 💾 File size < 4MB
* ⚖️ Image and mask must be the same size

## 3. Image Variant Generation (DALL·E 2)

### Usage Example

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

response = client.images.create_variation(
  model="dall-e-2",
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
```

### Technical Requirements

* 📝 PNG format
* 📏 Square image
* 💾 File size < 4MB

## Tips and Tricks

### DALL·E 3 Features

* Automatic suggestion optimization
* Suggestion optimization can be controlled via special commands:

```
I NEED to test how the tool works with extremely simple prompts.
DO NOT add any detail, just use it AS-IS:
```

## Notes

### Content Review

* Strictly adhere to content policies
* Violating content will return an error.

### Image URL

* Valid for 1 hour
* Base64 format can be selected for return.
