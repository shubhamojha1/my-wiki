---
title: "Vector Index"
type: concept
tags: [database, index, vector, embeddings]
created: 2026-04-23
---

# Vector Index

A **vector index** is a specialized index structure for efficiently searching high-dimensional vector embeddings.

## Use Case

- **Nearest neighbor search**: Find closest vectors to query
- **Semantic search**: Text/images represented as embeddings
- **ML model serving**: Retrieve similar items

## Techniques

### HNSW (Hierarchical Navigable Small World)
- Graph-based, multi-layer structure
- O(log N) search, high recall
- Used by pgvector, Milvus

### IVF (Inverted File)
- Cluster vectors, search clusters first
- Faster search, slight recall loss
- Combined with PQ for compression

### PQ (Product Quantization)
- Compress vectors into codes
- Enable large-scale search in memory

## Related

- [[Vector Database]] — Database using vector indexes
- [[B+Tree]] — Traditional index (not suitable for vectors)
- [[Embeddings]] — Vector representations