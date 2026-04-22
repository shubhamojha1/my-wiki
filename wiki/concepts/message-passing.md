---
title: "Message Passing"
type: concept
tags: [deep-learning, graph, gnn]
created: 2026-04-23
---

# Message Passing

**Message passing** is the core mechanism in GNNs where nodes aggregate information from their neighbors.

## How It Works

For each node:
1. **Message**: Compute information to send to neighbors
2. **Aggregate**: Combine messages from all neighbors
3. **Update**: Apply neural network to update node representation

## Formula

```
m_u→v = MSG(h_u)
h_v' = UPDATE(h_v, AGG({m_u→v for u in N(v)}))
```

## Layers

- **1 layer**: Direct neighbors
- **k layers**: k-hop neighborhood
- **Receptive field**: All nodes within k hops

## Related

- [[Graph Neural Network]] — Where message passing is used
- [[Graph Attention]] — Weighted message passing
- [[Graph Convolution]] — Convolution-based message passing