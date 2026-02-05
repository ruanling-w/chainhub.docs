# Embedded Objects

## [Embeddings](https://platform.openai.com/docs/api-reference/embeddings)

Retrieves a vector representation of a given input, which machine learning models and algorithms can easily use.

Related Guide: [Embeddings](https://platform.openai.com/docs/guides/embeddings)

## [Embedded Objects](https://platform.openai.com/docs/api-reference/embeddings/object)

Represents the embedding vector returned by the embedding endpoint.

index/integer

The index of the embedding in the embedding list.

embedding/array

The embedding vector, which is a list of floating-point numbers. The length of the vector depends on the model listed in the [Embedding Guide](https://platform.openai.com/docs/guides/embeddings).

object/string The object type, always "embedding".

```JSON
{
  "object": "embedding",
  "embedding": [
    0.0023064255,
    -0.009327292,
    .... (1536 floats total for ada-002)
    -0.0028842222,
  ],
  "index": 0
}
```
