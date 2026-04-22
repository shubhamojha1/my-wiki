---
title: "Multi-Head Attention"
type: concept
tags: [deep-learning, nlp, attention]
created: 2026-04-23
---

# Multi-Head Attention

**Multi-head attention** runs multiple self-attention operations in parallel, allowing the model to attend to different types of information simultaneously.

## How It Works

1. **Linear projections**: Project Q, K, V to d_model dimension h times
2. **Parallel attention**: Run self-attention on each head
3. **Concatenation**: Concatenate all head outputs
4. **Final projection**: Linear project back to d_model

## Why Multiple Heads?

- Each head can learn different relationships
- One head may focus on syntax, another semantics
- Increases model capacity without much computation

## Typical Configuration

- **BERT-base**: 12 heads, 768 hidden, 12 layers
- **GPT-3**: 96 heads, 12288 hidden, 96 layers

## Related

- [[Self-Attention]] — Single head mechanism
- [[Transformer]] — Uses multi-head attention
- [[Attention]] — General concept