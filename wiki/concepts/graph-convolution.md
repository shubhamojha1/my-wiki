---
title: "Graph Convolution"
type: concept
tags: [deep-learning, graph, gnn]
created: 2026-04-23
---

# Graph Convolution

**Graph convolution** applies convolution operations to graphs, aggregating neighbor information.

## Types

### Spectral
- Based on graph Laplacian eigen decomposition
- Smoother filters but limited to fixed structure
- Example: Chebyshev Network (ChebNet)

### Spatial
- Directly operates on graph structure
- Aggregate from neighbor nodes
- More efficient, most common today
- Example: GraphSAGE, GCN

## Graph Convolutional Network (GCN)

```
h_v' = σ(Σ_{u∈N(v)} W h_u)
```

Simple but effective message passing with normalization.

## Related

- [[Graph Neural Network]] — Parent concept
- [[Message Passing]] — Base mechanism
- [[Graph Attention]] — Attention-weighted aggregation