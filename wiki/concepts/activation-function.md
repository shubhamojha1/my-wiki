---
title: "Activation Function"
type: concept
tags: [deep-learning, neural-network, ml]
created: 2026-04-23
updated: 2026-05-20
sources: ["deep-learning-survey-2023"]
---

# Activation Function

An **activation function** introduces non-linearity into a neural network. Without it, stacking multiple linear layers would collapse into a single linear transformation — the network could only learn linear relationships. Activation functions let networks approximate arbitrarily complex functions.

## Common Activation Functions

### ReLU (Rectified Linear Unit)
- **Formula**: `max(0, x)`
- **Properties**: Simple, fast to compute, sparse activations (many zeros)
- **Default choice** for hidden layers in deep networks
- **Dying ReLU problem**: neurons that consistently receive negative inputs permanently output 0 and stop learning

### Leaky ReLU
- **Formula**: `max(αx, x)` where α is small (e.g., 0.01)
- Fixes dying ReLU by allowing small negative outputs
- α is a hyperparameter

### GELU (Gaussian Error Linear Unit)
- **Formula**: `x · Φ(x)` where Φ is the CDF of the standard normal distribution
- Approximated as `0.5x(1 + tanh(√(2/π)(x + 0.044715x³)))`
- **Used in**: BERT, GPT-2, GPT-3, most modern Transformers
- Smoother than ReLU; slightly more expensive to compute

### SwiGLU (Swish-Gated Linear Unit)
- **Formula**: `x · sigmoid(βx)` combined with a gating mechanism
- **Used in**: LLaMA, PaLM, Gemini
- Empirically outperforms GELU on language model benchmarks
- Requires a parameter-free gate that increases compute slightly

### Sigmoid
- **Formula**: `1 / (1 + e^(-x))`
- Output range: (0, 1) — naturally interpreted as probability
- **Use case**: Output layer for binary classification
- **Problem**: Vanishing gradients for large |x|; slow training

### Tanh
- **Formula**: `tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))`
- Output range: (-1, 1) — zero-centered, unlike sigmoid
- **Use case**: Recurrent networks (LSTMs, GRUs) for gate activations
- Still suffers from vanishing gradients

### Softmax
- **Formula**: `e^(x_i) / Σ e^(x_j)` for each class j
- **Use case**: Output layer for multi-class classification; attention score normalization
- Produces a probability distribution (outputs sum to 1)

## Comparison

| Function | Range | Zero-centered | Vanishing Gradient | Modern Usage |
|----------|-------|--------------|-------------------|-------------|
| Sigmoid | (0,1) | No | Severe | Output (binary) |
| Tanh | (-1,1) | Yes | Moderate | RNNs |
| ReLU | [0,∞) | No | No | Default hidden |
| GELU | ~(-0.17,∞) | Roughly | No | Transformers |
| SwiGLU | ~(-0.28,∞) | Roughly | No | LLMs |

## Related Concepts

- [[Transformer]] — uses GELU and SwiGLU
- [[Self-Attention]] — uses Softmax for attention weights
- [[Skip Connection]] — helps with gradient flow independent of activation choice
- [[Multi-Head Attention]] — Softmax inside each attention head
