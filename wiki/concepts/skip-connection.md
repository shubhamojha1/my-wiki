---
title: "Skip Connection"
type: concept
tags: [deep-learning, architecture]
created: 2026-04-23
---

# Skip Connection

A **skip connection** (or **residual connection**) adds the input of a layer directly to its output, forming a "residual block."

## How It Works

```
output = F(x) + x
```

Where F(x) is the learned transformation.

## Benefits

- **Enables deeper networks**: Mitigates vanishing gradient
- **Easier optimization**: Learns identity mapping first
- **Gradient flow**: Direct path for gradients back

## Origin

- **ResNet** (He et al., 2015): Won ImageNet with 152 layers
- Now ubiquitous in deep learning

## Related

- [[Residual Network]] — Uses skip connections
- [[Transformer]] — Has layer normalization + skip
- [[Training Dynamics]] — What skip connections affect