---
title: "Normalization"
type: concept
tags: [deep-learning, training]
created: 2026-04-23
---

# Normalization

**Normalization** techniques stabilize neural network training by normalizing layer inputs.

## Types

### Batch Normalization (BatchNorm)
- Normalize over batch dimension
- Learns γ, β parameters
- Requires large batch size
- Problematic for varying batch sizes

### Layer Normalization (LayerNorm)
- Normalize over feature dimension
- Independent of batch size
- Used in Transformers

### RMSNorm
- Root Mean Square Normalization
- Simpler than LayerNorm, faster
- Used in LLaMA, Mistral

### Group Normalization
- Divide features into groups
- Works with small batches

## Why It Works

- Reduces internal covariate shift
- Enables higher learning rates
- Regularization effect

## Related

- [[Transformer]] — Uses LayerNorm/RMSNorm
- [[Training Dynamics]] — What normalization affects