---
title: "Self-Supervised Learning"
type: concept
tags: [deep-learning, training, pretraining]
created: 2026-04-23
---

# Self-Supervised Learning

**Self-supervised learning** is a pretraining paradigm where the model learns representations from unlabeled data by solving proxy tasks.

## How It Works

1. **Pretrain on unlabeled data**: Create supervision from data itself
2. **Finetune on labeled data**: Transfer to downstream task

## Common Pretraining Tasks

### Language
- **Masked Language Modeling (BERT)**: Predict masked tokens
- **Next Token Prediction (GPT)**: Predict next token

### Vision
- **Contrastive learning**: SimCLR, CLIP
- **Masked image modeling**: MAE, BEiT

## Why It Works

- **Massive unlabeled data**: Internet-scale data available
- **Transferable features**: Pretraining learns general representations
- **Scaling laws**: More data + compute = better

## Related

- [[Transformer]] — Architecture often used
- [[BERT]] — MLM pretraining
- [[GPT]] — Next-token prediction
- [[Contrastive Learning]] — Vision SSL method