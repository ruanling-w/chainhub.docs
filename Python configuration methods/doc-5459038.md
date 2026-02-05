# Vectorization using Embeddings in Python

# Embeddings API Guide

## Overview

### New Model Release

* **text-embedding-3-small**
* **text-embedding-3-large**
  Features: Lower cost, better multilingual performance, controllable dimensionality

### Main Application Scenarios

* 🔍 Search (Relevance Ranking)
* 📊 Clustering (Similarity Grouping)
* 👍 Recommendation Systems
* ⚠️ Anomaly Detection
* 📈 Diversity Analysis
* 🏷️ Text Classification

## Basic Usage

### Obtaining Embedding Vectors

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)
```

### Response Format

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        -0.006929283495992422, -0.005336422007530928
        // ...more values
      ]
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
```

## Model Comparison

| Model                  | Pages per Dollar | MTEB Performance Evaluation | Maximum Input |
| ---------------------- | ---------------- | --------------------------- | ------------- |
| text-embedding-3-small | 62,500           | 62.3%                       | 8191          |
| text-embedding-3-large | 9,615            | 64.6%                       | 8191          |
| text-embedding-ada-002 | 12,500           | 61.0%                       | 8191          |

## Practical Application Examples

### Processing Comment Data

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key=key
)

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

# Processing Data Frames
df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
df.to_csv('output/embedded_1k_reviews.csv', index=False)

# Load saved embeddings
import pandas as pd
import numpy as np

df = pd.read_csv('output/embedded_1k_reviews.csv')
df['ada_embedding'] = df.ada_embedding.apply(eval).apply(np.array)
```

## Technical Details

### Dimension Explanation

* text-embedding-3-small: Default 1536 dimensions
* text-embedding-3-large: Default 3072 dimensions
* Dimensions can be adjusted via the Dimensions parameter

### Notes

* Billing is based on the number of input tokens
* Approximately 800 tokens per page
* The maximum input for all models is 8191 tokens
