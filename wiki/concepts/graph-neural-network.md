---
title: "Graph Neural Network (GNN)"
type: concept
tags: [deep-learning, graph, neural-network]
created: 2026-04-23
---

# Graph Neural Network (GNN)

A **Graph Neural Network** is a deep learning model that operates on graph-structured data, learning representations for nodes, edges, or entire graphs.

## Key Idea

- **Input**: Node features + graph structure (adjacency)
- **Output**: Node/edge/graph embeddings for downstream tasks
- **Key insight**: Combine entity information with relationships

## Tasks

- **Node classification**: Predict label for each node
- **Link prediction**: Predict edges (e.g., recommendation)
- **Graph classification**: Classify entire graphs

## Related

- [[Message Passing]] — Core GNN mechanism
- [[Graph Convolution]] — Spatial/spectral convolution
- [[Graph Attention]] — Attention on graphs