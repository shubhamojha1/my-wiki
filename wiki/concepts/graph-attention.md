---
title: "Graph Attention"
type: concept
tags: [deep-learning, graph, gnn, attention]
created: 2026-04-23
updated: 2026-05-20
---

# Graph Attention

**Graph attention** is a [[Graph Neural Network]] aggregation strategy that assigns learned importance weights to each neighbor during message passing, rather than treating all neighbors equally (as in [[Graph Convolution]]).

## Motivation

A node's neighbors are not equally relevant. In a social network, close friends matter more than distant acquaintances. In a molecular graph, strongly bonded atoms drive chemical properties more than weakly bonded ones. Standard graph convolution (GCN) uses degree-normalized uniform averaging, missing this structure.

## GAT Algorithm (Graph Attention Network)

For node `v` aggregating neighbor `u`:

**1. Compute raw attention score:**
```
e(v,u) = LeakyReLU( a^T · [W·h_v ‖ W·h_u] )
```
where `W` is a shared weight matrix, `h_v`/`h_u` are node features, `a` is a learnable attention vector, and `‖` denotes concatenation.

**2. Normalize with softmax across all neighbors N(v):**
```
α(v,u) = softmax_u( e(v,u) ) = exp(e(v,u)) / Σ_{k∈N(v)} exp(e(v,k))
```

**3. Weighted aggregation:**
```
h'_v = σ( Σ_{u∈N(v)} α(v,u) · W·h_u )
```

**Multi-head attention** runs K independent attention heads and concatenates (or averages) their outputs — same motivation as in Transformers.

## Expressiveness Hierarchy

Per Bronstein et al. (2021):
```
message-passing ⊇ attention ⊇ convolution
```
Graph attention is a special case of message passing; GCN convolution is a special case of attention (with fixed uniform weights).

## GAT vs GCN

| Aspect | GCN | GAT |
|--------|-----|-----|
| Neighbor weights | Fixed (degree normalization) | Learned (attention) |
| Inductive | No (fixed graph structure) | Yes (weights computed from features) |
| Computational cost | O(E) | O(E · K) with K heads |
| Interpretability | Low | Medium (attention weights can be visualized) |
| When better | Homogeneous graphs | Heterogeneous importance among neighbors |

## Variants

| Model | Key Difference |
|-------|---------------|
| **GAT** (Veličković et al., 2018) | Additive attention, multi-head |
| **GATv2** (Brody et al., 2022) | Fixes static-vs-dynamic attention flaw in GAT |
| **Transformer on graphs** | Full self-attention across all nodes (not just neighbors) |
| **Graph Transformer** | Combines positional encoding with graph attention |

## Related Concepts

- [[Graph Neural Network]] — the parent framework
- [[Graph Convolution]] — fixed-weight alternative
- [[Message Passing]] — the general mechanism GAT instantiates
- [[Multi-Head Attention]] — the attention mechanism adapted for graphs
- [[Self-Attention]] — the underlying operation
