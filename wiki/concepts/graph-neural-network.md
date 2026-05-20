---
title: "Graph Neural Network (GNN)"
type: concept
tags: [deep-learning, graph, neural-network, ml]
created: 2026-04-23
updated: 2026-05-20
sources: ["deep-learning-survey-2023"]
---

# Graph Neural Network (GNN)

A **Graph Neural Network** is a class of deep learning models designed to operate directly on graph-structured data. Where CNNs exploit spatial locality in grids and RNNs exploit temporal sequences, GNNs exploit the relational structure of graphs — learning embeddings that capture both node features and graph topology.

## Key Idea: Message Passing

The dominant GNN paradigm is **message passing**:

1. Each node aggregates feature vectors from its neighbors
2. The aggregated message is combined with the node's own features
3. A learned transformation produces a new node representation
4. Steps 1–3 repeat for K layers; after K layers, each node's embedding reflects its K-hop neighborhood

```
h_v^(k) = UPDATE(h_v^(k-1), AGGREGATE({h_u^(k-1) : u ∈ N(v)}))
```

## Tasks

| Task | Description | Example |
|------|-------------|---------|
| Node classification | Predict a label for each node | Social network user type |
| Link prediction | Predict whether an edge exists | Recommendation, knowledge graph completion |
| Graph classification | Classify entire graphs | Molecule property prediction |
| Node regression | Predict a continuous value per node | Traffic flow estimation |

## GNN Variants

| Model | Key Innovation | Use Case |
|-------|---------------|---------|
| [[Graph Convolution]] (GCN) | Spectral convolution approximation | Node classification |
| GraphSAGE | Inductive; samples fixed-size neighborhoods | Large graphs |
| [[Graph Attention]] (GAT) | Attention weights on edges | Heterogeneous graphs |
| GIN | Provably most expressive MPNN | Graph classification |

## Limitations

- **Over-smoothing**: With many layers, node representations converge and become indistinguishable
- **Scalability**: Full-batch training on large graphs is memory-intensive; mini-batch requires neighbor sampling
- **Expressiveness**: Standard MPNNs cannot distinguish some non-isomorphic graphs (bounded by Weisfeiler-Lehman test)

## Related Concepts

- [[Message Passing]] — the core computational mechanism in GNNs
- [[Graph Convolution]] — spectral and spatial convolution on graphs
- [[Graph Attention]] — attention-based GNN variant
- [[Self-Attention]] — attention mechanism in Transformers (a special case)
- [[Graph Database]] — storage for graph-structured data
