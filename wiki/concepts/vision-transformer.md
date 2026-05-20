---
title: "Vision Transformer (ViT)"
type: concept
tags: [deep-learning, computer-vision, transformer, ml]
created: 2026-04-23
updated: 2026-05-20
sources: ["deep-learning-survey-2023"]
---

# Vision Transformer (ViT)

The **Vision Transformer (ViT)** applies the standard [[Transformer]] architecture directly to images by treating fixed-size image patches as a sequence of tokens — the same way words are treated in NLP. Introduced by Dosovitskiy et al. (2020), it demonstrated that transformers can match or surpass CNNs on image classification without any convolutions.

## How It Works

```
Image (224×224) → 14×14 grid of 16×16 patches (196 tokens)
    → Flatten each patch → Linear projection → Patch embeddings
    → Prepend [CLS] token → Add positional embeddings
    → Transformer Encoder (L layers of MHA + FFN)
    → [CLS] embedding → MLP head → Class probabilities
```

1. **Patch extraction**: Split image into N = (H·W) / P² non-overlapping patches of size P×P (typically P=16)
2. **Linear projection**: Flatten each patch to a vector; project to embedding dimension d
3. **[CLS] token**: Prepend a learnable class token that aggregates global context
4. **Positional embedding**: Add learnable 1D positional embeddings (patches have no inherent order)
5. **Transformer encoder**: Standard L-layer transformer; attention operates over patch tokens
6. **Classification head**: MLP applied to [CLS] token output

## Key Properties

- **Global attention from layer 1** — unlike CNNs, every patch can attend to every other patch from the very first layer
- **Inductive biases** — ViT has far fewer image-specific inductive biases than CNNs (no convolution, no local connectivity), which makes it more data-hungry but also more flexible
- **Scales with data and compute** — ViT-Huge (632M params) trained on JFT-300M substantially outperforms CNNs

## Variants

| Model | Key Innovation |
|-------|---------------|
| **ViT** (2020) | Original; needs large datasets |
| **DeiT** (2021) | Data-efficient via knowledge distillation; trains on ImageNet-1K |
| **Swin Transformer** (2021) | Hierarchical; shifted windows; more like CNN |
| **BEiT** (2021) | Self-supervised pre-training via masked image modeling |
| **MAE** (2022) | Masked Autoencoder; 75% patch masking for self-supervision |

## Trade-offs vs. CNN

| Aspect | ViT | CNN |
|--------|-----|-----|
| Data requirement | High (pre-training helps) | Low (works from scratch) |
| Global context | Immediate (full attention) | Grows with depth |
| Inductive biases | Minimal | Translation equivariance |
| Scaling behavior | Excellent | Good |
| Interpretability | Attention maps | Feature maps |

## Related Concepts

- [[Transformer]] — the base architecture
- [[Self-Attention]] — the core mechanism
- [[Multi-Head Attention]] — used in each transformer block
- [[Positional Encoding]] — required since patches have no order
