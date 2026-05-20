---
title: "Multi-Head Attention"
type: concept
tags: [deep-learning, nlp, attention, transformer]
created: 2026-04-23
updated: 2026-05-20
sources: ["deep-learning-survey-2023"]
---

# Multi-Head Attention

**Multi-head attention** (MHA) runs multiple independent [[Self-Attention]] operations in parallel, each with its own learned projections. The outputs are concatenated and projected back to the model dimension. It allows the model to simultaneously attend to information from different representation subspaces at different positions.

## How It Works

For each of the H heads:
```
head_i = Attention(Q·W_i^Q, K·W_i^K, V·W_i^V)

MultiHead(Q, K, V) = Concat(head_1, ..., head_H) · W^O
```

Where:
- `W_i^Q ∈ ℝ^(d_model × d_k)` — query projection for head i
- `W_i^K ∈ ℝ^(d_model × d_k)` — key projection for head i
- `W_i^V ∈ ℝ^(d_model × d_v)` — value projection for head i
- `W^O ∈ ℝ^(H·d_v × d_model)` — output projection

Typically `d_k = d_v = d_model / H`, so total computation is similar to single-head attention.

## Why Multiple Heads?

Each head attends to different aspects of the sequence:
- One head might capture syntactic relationships (subject-verb agreement)
- Another might capture semantic similarity
- Another might focus on co-reference

Empirically, different heads specialize in different linguistic patterns, increasing the model's representational capacity without proportionally increasing cost.

## Variants

| Variant | Key Change | Use Case |
|---------|-----------|---------|
| **Multi-Head Attention (MHA)** | Separate K, V per head | Original Transformer; encoder |
| **Multi-Query Attention (MQA)** | Shared single K, V across all heads | Faster inference; used in PaLM, Falcon |
| **Grouped Query Attention (GQA)** | Shared K, V per group of heads | Balance between MHA and MQA; LLaMA 2 (70B), Mistral |
| **Cross-Attention** | Q from decoder, K/V from encoder | Encoder-decoder models (T5, BART) |

## Typical Configurations

| Model | Heads | Hidden dim | Layers |
|-------|-------|-----------|--------|
| BERT-base | 12 | 768 | 12 |
| GPT-2 | 12 | 768 | 12 |
| GPT-3 (175B) | 96 | 12,288 | 96 |
| LLaMA 3 (70B) | 64 (GQA: 8 KV groups) | 8,192 | 80 |

## Related Concepts

- [[Self-Attention]] — the single-head building block
- [[Transformer]] — the architecture that uses MHA
- [[Flash Attention]] — memory-efficient algorithm for computing MHA
- [[Positional Encoding]] — combined with input before MHA
