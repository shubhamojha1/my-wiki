---
title: "Vision Transformer (ViT)"
type: concept
tags: [deep-learning, computer-vision, transformer]
created: 2026-04-23
---

# Vision Transformer (ViT)

The **Vision Transformer** applies the transformer architecture to image recognition by treating image patches as tokens.

## How It Works

1. **Patch embedding**: Split image into fixed-size patches
2. **Linear projection**: Flatten patches into vectors
3. **Position embedding**: Add positional information
4. **Transformer encoder**: Process patch sequence with standard transformer
5. **Classification token**: Use [CLS] token for final prediction

## Key Papers

- **ViT** (Dosovitskiy et al., 2020): Showed transformers can outperform CNNs on large datasets
- **DeiT**: Data-efficient image transformers

## Trade-offs

- **Pros**: Scales well with data, attention visualizable
- **Cons**: Needs large datasets, expensive to train from scratch

## Related

- [[Transformer]] — Base architecture
- [[Self-Attention]] — Core mechanism
- [[CNN]] — Traditional vision architecture