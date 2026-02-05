# Using Python to create and edit images with gpt-image-1

```python
# Create image
from openai import OpenAI
import base64
client = OpenAI( base_url="https://api.chainhub.tech/v1",
    api_key="sk-xxx")

prompt = """
An illustration from a children's book depicts a veterinarian using a stethoscope to listen to the heartbeat of a baby otter.
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("otter.png", "wb") as f:
    f.write(image_bytes)
```

```python
# Edit Image
import base64
from openai import OpenAI
client = OpenAI( base_url="https://api.chainhub.tech/v1",
    api_key="sk-xxx")

prompt = """
Generate a hyper-realistic image of a gift basket placed on a white background, labeled "Relax" and tied with a ribbon in a handwritten style. The gift basket contains all the items in the reference image.
"""

result = client.images.edit(
    model="gpt-image-1",
    image=[
        open("body-lotion.png", "rb"),
        open("bath-bomb.png", "rb"),
        open("incense-kit.png", "rb"),
        open("soap.png", "rb"),
    ],
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("gift-basket.png", "wb") as f:
    f.write(image_bytes)
```

First effect:
![image.png](https://api.apifox.com/api/v1/projects/5443236/resources/519764/image-preview)
The second image used:

![image.png](https://api.apifox.com/api/v1/projects/5443236/resources/519766/image-preview)

![image.png](https://api.apifox.com/api/v1/projects/5443236/resources/519767/image-preview)

![image.png](https://api.apifox.com/api/v1/projects/5443236/resources/519768/image-preview)

![image.png](https://api.apifox.com/api/v1/projects/5443236/resources/519769/image-preview)
Second effect:
![image.png](https://api.apifox.com/api/v1/projects/5443236/resources/519765/image-preview)
