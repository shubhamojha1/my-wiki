---
title: "Vector Database"
type: concept
tags: [database, vector, ml, embeddings]
created: 2026-04-22
sources: [cmu_15-445_lec01]
---

# Vector Database

A database specialized for storing and searching vector embeddings - numerical representations of data (text, images, audio) from ML models.

## Purpose

Enable **similarity search** (nearest neighbor) on high-dimensional vectors:
- Semantic search on text embeddings
- Image/audio similarity
- Recommendation systems

## How It Works

1. **Embed**: Convert data to vectors using ML models
2. **Index**: Build specialized index for fast search
3. **Query**: Find nearest vectors to query vector

## Key Algorithms

- **HNSW**: Hierarchical Navigable Small World - graph-based
- **IVF**: Inverted File Index - clustering-based
- **PQ**: Product Quantization - compression for large scales

## Exact vs Approximate

- **Exact (KNN)**: Perfect results, slower
- **Approximate (ANN)**: Faster, some accuracy tradeoff

## Examples

```sql
-- pgvector example
SELECT * FROM documents 
ORDER BY embedding <-> query_embedding
LIMIT 10;
```

## Integration

Often paired with:
- **LLMs**: Store knowledge base as embeddings
- **LangChain**: Semantic search over documents
- **OpenAI**: Generate embeddings for storage/querying

## Popular Systems

- **Pinecone**: Managed vector DB
- **Weaviate**: Open-source with GraphQL
- **Milvus**: Open-source, Apache
- **pgvector**: PostgreSQL extension

## Related Concepts

- [[Relational Model]]
- [[Embedding]]
- [[Nearest Neighbor Search]]