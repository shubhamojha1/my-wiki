---
title: "Skip Connection"
type: concept
tags: [deep-learning, architecture, residual, gradient]
created: 2026-04-23
updated: 2026-05-20
sources: ["deep-learning-survey-2023"]
---

# Skip Connection

A **skip connection** (residual connection) adds the input of a layer directly to its output, bypassing the layer's transformation:

```
output = F(x) + x
```

Where `F(x)` is the learned transformation (e.g., two weight layers + activation). The network learns a **residual** — the difference from the identity mapping — rather than the full mapping.

## Why It Works

**The Vanishing Gradient Problem**: In deep networks, gradients shrink as they backpropagate through many layers. By the time gradients reach early layers, they are near zero — those layers stop learning.

Skip connections provide a **direct gradient highway**: the gradient flows back through the identity path (`+x`) without passing through weight matrices, keeping early-layer gradients large enough to learn.

**Easy optimization**: If a layer is not useful, it can learn `F(x) ≈ 0` and the layer becomes identity. This makes it easier to add depth without hurting performance.

## Variants

| Type | Formula | Used In |
|------|---------|---------|
| **Residual** | `F(x) + x` | ResNet (same dimensions) |
| **Projection** | `F(x) + Wx` | ResNet (dim change; W is 1×1 conv) |
| **Dense** | Concat outputs of all previous layers | DenseNet |
| **Pre-activation** | `F(LayerNorm(x)) + x` | [[Transformer]] (Post-LN vs Pre-LN) |

## Impact

- **ResNet** (He et al., 2015) — trained 152-layer networks; first to win ImageNet with ultra-deep architecture
- Skip connections are now **ubiquitous**: every Transformer block uses them (`LayerNorm(Attention(x) + x)`)
- Enable training networks with hundreds or thousands of layers

## In Transformers

Each transformer block applies skip connections twice:

```
x = x + Attention(LayerNorm(x))   # after self-attention
x = x + FFN(LayerNorm(x))         # after feed-forward network
```

(Pre-LN form; original paper used Post-LN: `LayerNorm(x + Attention(x))`)

## Related Concepts

- [[Transformer]] — uses skip connections in every block
- [[Activation Function]] — skip connections work with any activation
- [[Multi-Head Attention]] — wrapped with a skip connection
