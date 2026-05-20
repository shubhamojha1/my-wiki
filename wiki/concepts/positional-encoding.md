---
title: "Positional Encoding"
type: concept
tags: [deep-learning, nlp, transformer, attention]
created: 2026-04-23
updated: 2026-05-20
sources: ["deep-learning-survey-2023"]
---

# Positional Encoding

**Positional encoding** adds position information to token embeddings before they enter a [[Transformer]]. [[Self-Attention]] is **permutation-invariant** — it treats the same tokens identically regardless of order. Without positional encoding, "the dog bit the man" and "the man bit the dog" would produce identical attention outputs.

## Why It's Needed

The attention mechanism computes: `Attention(Q, K, V) = softmax(QKᵀ/√d_k)V`

There is no inherent notion of position in this formula. Positional encoding injects position into the input embeddings before attention is computed.

## Methods

### Sinusoidal (Original Transformer, "Attention Is All You Need")

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

- Different dimensions encode different frequencies
- Deterministic; no parameters to learn
- Poor extrapolation beyond training sequence length

### Learned Absolute Position Embeddings

- A learned embedding table indexed by position (0, 1, 2, ..., max_len)
- Used in BERT, GPT-2
- Simple but hard-capped at max_len; poor extrapolation

### RoPE (Rotary Position Embedding)

- Rotates the query and key vectors by an amount proportional to position
- Applied **inside** each attention head, not to input embeddings
- Captures relative position naturally
- **Used in**: LLaMA, Mistral, Falcon, Gemma, most modern open-source LLMs
- Better length extrapolation than absolute methods

### ALiBi (Attention with Linear Biases)

- Subtracts a linear bias proportional to token distance from attention logits
- No positional embeddings at all — bias is added at attention time
- Strong length extrapolation (can extend far beyond training length)
- **Used in**: BLOOM, MPT

### Relative Position Encodings (T5-style, Shaw et al.)

- Embed the distance between tokens as a scalar bias on attention scores
- Allows attending to relative positions rather than absolute ones
- Used in T5, DeBERTa

## Comparison

| Method | Absolute/Relative | Parameters | Extrapolation | Used In |
|--------|-----------------|-----------|--------------|---------|
| Sinusoidal | Absolute | None | Poor | Original Transformer |
| Learned | Absolute | Yes | Poor | BERT, GPT-2 |
| RoPE | Relative (via rotation) | None | Good | LLaMA, Mistral |
| ALiBi | Relative (via bias) | None | Excellent | BLOOM, MPT |
| T5 Relative | Relative | Small | Good | T5, DeBERTa |

## Related Concepts

- [[Transformer]] — the architecture that requires positional encoding
- [[Self-Attention]] — the permutation-invariant operation PE addresses
- [[Multi-Head Attention]] — where RoPE/ALiBi are applied per head
