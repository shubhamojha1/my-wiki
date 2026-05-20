---
title: "Message Passing"
type: concept
tags: [deep-learning, graph, gnn]
created: 2026-04-23
updated: 2026-05-20
---

# Message Passing (Graph Neural Networks)

**Message passing** is the computational primitive underlying nearly all [[Graph Neural Network]] (GNN) architectures. At each layer, every node collects information from its neighbors, aggregates it, and updates its own representation.

## Framework

The **Message Passing Neural Network (MPNN)** framework (Gilmer et al., 2017) unifies most GNN variants into three steps per layer:

```
For each node v, at layer k:

1. MESSAGE:    m_{u→v}^(k) = MSG^(k)( h_u^(k-1), h_v^(k-1), e_{uv} )
                              ↑ function of source, target, and edge features

2. AGGREGATE:  a_v^(k)     = AGG^(k)( { m_{u→v}^(k) : u ∈ N(v) } )
                              ↑ permutation-invariant (sum, mean, max)

3. UPDATE:     h_v^(k)     = UPDATE^(k)( h_v^(k-1), a_v^(k) )
                              ↑ typically an MLP
```

After `k` layers, `h_v^(k)` encodes the structure and features of all nodes within `k` hops of `v`.

## Receptive Field

```
k=1: v's immediate neighbors
k=2: v's 2-hop neighborhood (neighbors of neighbors)
k=k: all nodes within k hops
```

More layers = larger receptive field, but risk of **over-smoothing** (all node representations converge) if `k` is too large.

## Aggregation Functions

| Function | Formula | Properties |
|----------|---------|-----------|
| **Sum** | `Σ m_{u→v}` | Captures structural information (node degree affects output) |
| **Mean** | `(1/|N(v)|) Σ m` | Normalizes by degree; ignores structure |
| **Max** | `max(m_{u→v})` | Captures most prominent feature |
| **Attention** | `Σ α_{uv} m` | Learned weights per neighbor → [[Graph Attention]] |

GIN (Graph Isomorphism Network) proves that **sum** aggregation is the most expressive (equivalent to Weisfeiler-Leman graph isomorphism test).

## How Popular GNNs Instantiate MPNN

| Model | MSG | AGG | UPDATE |
|-------|-----|-----|--------|
| **GCN** | `W · h_u` | Degree-normalized sum | — (merged with AGG) |
| **GraphSAGE** | `h_u` | Mean or LSTM | MLP on concat(h_v, agg) |
| **GAT** | `W · h_u` | Attention-weighted sum | Activation |
| **GIN** | `h_u` | Sum | MLP |

## Over-Smoothing Problem

After many layers all node embeddings become indistinguishable — similar to the vanishing gradient problem in depth. Mitigations: residual connections, PairNorm, limiting to 2–4 layers.

## Related Concepts

- [[Graph Neural Network]] — the full model built on message passing
- [[Graph Attention]] — uses learned attention weights in the AGG step
- [[Graph Convolution]] — spectral-domain view of message passing
- [[Skip Connection]] — used in GNNs to combat over-smoothing
