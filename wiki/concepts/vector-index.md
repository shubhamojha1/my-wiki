---
title: "Vector Index"
type: concept
tags: [database, index, vector, embeddings]
created: 2026-04-23
updated: 2026-05-20
---

# Vector Index

A **vector index** is a specialized data structure for **approximate nearest neighbor (ANN)** search in high-dimensional spaces. Given a query vector `q`, find the k closest vectors in the index by some distance metric (cosine similarity, L2/Euclidean, dot product).

Standard indexes (B-trees) cannot be used because distance in N-dimensional space has no linear order — sorting on dimension 1 is useless when dimension 2 to N matter equally.

## Why Exact Nearest Neighbor Is Impractical

Exact k-NN requires comparing the query to every indexed vector: O(N × D) where D = dimensions (typically 768–4096 for LLM embeddings). For 100M vectors at D=1536: 153 billion multiplications per query. ANN trades a small accuracy loss (~95–99% recall) for orders-of-magnitude speedup.

## Major ANN Algorithms

### HNSW (Hierarchical Navigable Small World)

Graph-based index with multiple layers. Upper layers contain long-range "express" edges; lower layers have dense local neighborhoods:

```
Layer 2 (sparse):  A ─────────────── E
Layer 1:           A ── B ─────── D ─ E
Layer 0 (dense):   A─B─C─D─E─F─G─H─I
```

Search starts at the top layer, greedily descends toward the query vector. O(log N) search. Highest recall among ANN methods. High memory usage (stores graph edges).

### IVF (Inverted File Index)

Partition vectors into K clusters (Voronoi cells) via k-means. At search time, only probe the `nprobe` closest clusters:

```
nprobe=1: search 1 cluster  → fast, lower recall
nprobe=10: search 10 clusters → slower, higher recall
```

Scales to very large datasets. Often combined with PQ for compression.

### PQ (Product Quantization)

Compress high-dimensional vectors by splitting each into M sub-vectors and quantizing each sub-vector to one of k centroids. Stores a short code (M bytes) instead of the full float vector:

- Reduces memory by 8–64×
- Enables billion-scale search
- Combined with IVF: **IVF-PQ** (Faiss default)

## Algorithm Comparison

| Algorithm | Search speed | Recall | Memory | Build time |
|-----------|-------------|--------|--------|-----------|
| **HNSW** | Fast | Highest (~99%) | High (graph) | Slow |
| **IVF-Flat** | Fast | High (tunable) | Medium | Fast |
| **IVF-PQ** | Very fast | Good (~95%) | Very low | Moderate |
| **ScaNN** | Very fast | High | Low | Moderate |
| **Exact (brute force)** | Slow | 100% | Low | None |

## Where Vector Indexes Are Used

| System | Index Type | Notes |
|--------|-----------|-------|
| **pgvector** (PostgreSQL) | HNSW, IVF-Flat | Native SQL; add-on extension |
| **Faiss** (Meta) | IVF-PQ, HNSW, many more | GPU-accelerated; research library |
| **Milvus** | HNSW, IVF | Dedicated vector DB |
| **Pinecone** | Managed | Serverless vector search |
| **Weaviate, Qdrant** | HNSW | Full vector DB with metadata filtering |
| **Redis VSS** | HNSW, IVF | In-memory vector search |

## Related Concepts

- [[Embeddings]] — the dense vectors that vector indexes search over
- [[Vector Database]] — a database built around vector indexes
- [[Semantic Search]] — the primary use case: find similar meaning, not exact matches
- [[Approximate Nearest Neighbor]] — the search problem vector indexes solve
