---
title: "Graph Convolution"
type: concept
tags: [deep-learning, graph, gnn]
created: 2026-04-23
updated: 2026-05-20
---

# Graph Convolution

**Graph convolution** extends the convolution operation (from image CNNs) to irregular graph-structured data. Like a CNN aggregates pixels in a local window, graph convolution aggregates feature vectors from a node's neighborhood.

## Spectral vs Spatial Approaches

### Spectral Graph Convolution

Defines convolution in the graph frequency domain using the **graph Laplacian** `L = D - A` (degree matrix minus adjacency matrix):

- Decompose L into eigenvectors; filter in that basis
- Global operation — computationally expensive (eigendecomposition is O(n³))
- **ChebNet**: Approximates spectral filters with Chebyshev polynomials (avoids full eigendecomp)
- Limitation: tied to a fixed graph structure; cannot generalize to unseen graphs

### Spatial Graph Convolution

Directly aggregates feature vectors from neighboring nodes in the graph domain:

- No eigendecomposition required
- Generalizes across different graph structures
- The dominant approach today

## GCN (Graph Convolutional Network — Kipf & Welling 2017)

The most influential spatial graph convolution simplification:

**Full formula:**
```
H^(k+1) = σ( Ã · H^(k) · W^(k) )

where Ã = D̃^{-1/2} Ã D̃^{-1/2}   (symmetrically normalized adjacency with self-loops)
      Ã = A + I                      (add self-loops)
      D̃_ii = Σ_j Ã_ij               (degree matrix of Ã)
```

**Per-node view:**
```
h_v^(k+1) = σ( Σ_{u ∈ N(v) ∪ {v}}  (1/√(deg(v)·deg(u))) · W · h_u^(k) )
```

Normalization by `√(deg(v)·deg(u))` prevents high-degree nodes from dominating the aggregation.

## GCN vs Graph Attention (GAT)

| Aspect | GCN | GAT |
|--------|-----|-----|
| Neighbor weights | Fixed (degree normalization) | Learned (attention) |
| Inductive | No — fixed Ã requires all nodes at train time | Yes |
| Computation | O(E) | O(E · K heads) |
| Expressiveness | Lower | Higher |

## Limitations of Graph Convolution

- **Over-smoothing**: After many layers, all node features converge to the same value (similar to low-pass filter on the graph).
- **Fixed structure**: Spectral methods cannot generalize to new graphs.
- **Scalability**: Aggregating full neighborhoods is expensive for high-degree nodes (GraphSAGE mitigates via neighborhood sampling).

## Related Concepts

- [[Graph Neural Network]] — the broader class
- [[Message Passing]] — the unified framework GCN instantiates
- [[Graph Attention]] — replaces fixed weights with learned attention coefficients
- [[Skip Connection]] — added in deep GNNs to combat over-smoothing
