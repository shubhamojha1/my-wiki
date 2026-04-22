---
title: "Positional Encoding"
type: concept
tags: [deep-learning, nlp, transformer]
created: 2026-04-23
---

# Positional Encoding

**Positional encoding** adds position information to token embeddings since self-attention is permutation-invariant.

## Methods

### Sinusoidal (Original Transformer)
- Different frequencies for different positions
- Formula: sin(pos/10000^(2i/d_model))

### Learned
- Learnable position embeddings

### RoPE (Rotary Position Embedding)
- Rotate query/key vectors
- Used in LLaMA, Mistral

### ALiBi
- Bias based on distance
- Better extrapolation

## Related

- [[Transformer]] — Uses positional encoding
- [[Self-Attention]] — Where it's added
- [[Embedding]] — Combined with token embeddings