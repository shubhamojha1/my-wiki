---
title: "Transformer"
type: concept
tags: [deep-learning, nlp, architecture]
created: 2026-04-23
---

# Transformer

The **Transformer** is a deep learning architecture based entirely on self-attention, without recurrence or convolution. It revolutionized NLP and now vision.

## Architecture

- **Encoder**: Processes input sequence (BERT-style)
- **Decoder**: Generates output autoregressively (GPT-style)
- **Attention**: Self-attention computes relationships between all positions

## Key Components

- **Multi-head attention**: Multiple attention functions in parallel
- **Feed-forward networks**: Position-wise MLPs
- **Positional encoding**: Adds position information
- **Layer normalization**: Stabilizes training

## Variants

- **BERT**: Encoder-only, masked language modeling
- **GPT**: Decoder-only, autoregressive generation
- **T5**: Encoder-decoder, text-to-text

## Impact

- State-of-the-art in NLP, vision, speech
- Enabled large language models (GPT, PaLM)
- Foundation for multimodal models

## Related

- [[Self-Attention]] — Core mechanism
- [[GPT]] — Generative transformer
- [[BERT]] — Bidirectional encoder
- [[Vision Transformer]] — Vision application