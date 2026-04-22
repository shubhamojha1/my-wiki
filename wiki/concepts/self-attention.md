---
title: "Self-Attention"
type: concept
tags: [deep-learning, nlp, attention]
created: 2026-04-23
---

# Self-Attention

**Self-attention** (or **scaled dot-product attention**) is the core mechanism in Transformers that computes relationships between all positions in a sequence.

## How It Works

For each position in the sequence:
1. **Query (Q)**: What I'm looking for
2. **Key (K)**: What I contain
3. **Value (V)**: What I would provide

Attention score: `softmax(QK^T / sqrt(d_k)) * V`

## Multi-Head Attention

- Run multiple attention functions (heads) in parallel
- Each head learns different relationship types
- Concatenate outputs, linear project

## Properties

- **Parallel**: All positions computed simultaneously
- **Long-range**: Direct connections between any positions
- **Quadratic**: O(n²) complexity with sequence length

## Variants

- **Causal**: Mask future positions (for generation)
- **Sparse**: Reduce to O(n√n) or O(n)
- **FlashAttention**: Memory-efficient exact attention

## Related

- [[Transformer]] — Uses self-attention
- [[Multi-Head Attention]] — Parallel attention heads
- [[FlashAttention]] — Efficient implementation