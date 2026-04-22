---
title: "Graph Attention"
type: concept
tags: [deep-learning, graph, gnn, attention]
created: 2026-04-23
---

# Graph Attention

**Graph attention** applies attention mechanisms to graphs, learning which neighbors are most important.

## How It Works

- Compute attention coefficient for each neighbor
- Normalize with softmax
- Weighted sum of neighbor features

## Relationship

Per Bronstein et al.:
`message-passing ⊇ attention ⊇ convolution`

Graph attention is a special case of message passing that uses attention weights.

## Famous Models

- **GAT (Graph Attention Network)**: Uses multi-head attention
- **Transformer** on graphs: Apply transformer to graph structure

## Related

- [[Graph Neural Network]] — Parent concept
- [[Message Passing]] — Base mechanism
- [[Graph Convolution]] — Alternative aggregation
- [[Multi-Head Attention]] — Used in GAT