---
title: "Activation Function"
type: concept
tags: [deep-learning, neural-network]
created: 2026-04-23
---

# Activation Function

An **activation function** introduces non-linearity into neural networks, enabling them to learn complex patterns.

## Common Activation Functions

### ReLU (Rectified Linear Unit)
- `max(0, x)` 
- Simple, fast, default choice
- Dying ReLU problem

### GELU (Gaussian Error Linear Unit)
- `x * Φ(x)` 
- Used in BERT, GPT
- Smoother than ReLU

### SwiGLU
- SiLU (Sigmoid Linear Unit) variant
- Used in LLaMA, PaLM
- `x * sigmoid(x)`

### Tanh
- `tanh(x)`
- Historical, zero-centered
- Still used in RNNs

## Related

- [[Neural Network]] — Where activations are used
- [[Transformer]] — Uses GELU, SwiGLU