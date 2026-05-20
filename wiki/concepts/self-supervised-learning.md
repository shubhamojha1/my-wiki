---
title: "Self-Supervised Learning"
type: concept
tags: [deep-learning, training, pretraining]
created: 2026-04-23
updated: 2026-05-20
---

# Self-Supervised Learning (SSL)

**Self-supervised learning** is a training paradigm where the model creates its own supervision signal from unlabeled data — no human labels required. A **pretext task** is constructed by hiding or transforming part of the data; the model must recover what was hidden, forcing it to learn useful representations.

## Key Insight

Labels are expensive; raw data is abundant. SSL exploits structure already present in data (word order, image patches, temporal continuity) to generate free supervision at internet scale.

## Two-Phase Training

```
Phase 1: Pretrain (self-supervised, unlabeled)
  → Massive corpus  →  [Pretext task]  →  Model learns representations

Phase 2: Fine-tune or probe (supervised, labeled)
  → Small labeled dataset  →  Freeze/adapt representations  →  Task-specific model
```

## Pretext Tasks by Modality

### Language (NLP)

| Task | Description | Example |
|------|-------------|---------|
| **Masked Language Modeling (MLM)** | Mask 15% of tokens; predict them | BERT, RoBERTa |
| **Causal Language Modeling (CLM)** | Predict next token given all prior | GPT, LLaMA |
| **Span corruption** | Mask and predict spans | T5 |
| **Sentence order prediction** | Is sentence B the next after A? | BERT (auxiliary task) |

### Vision

| Task | Description | Example |
|------|-------------|---------|
| **Contrastive learning** | Different views of same image → same embedding; different images → different | SimCLR, MoCo |
| **Masked image modeling** | Mask 75% of patches; reconstruct | MAE, BEiT |
| **Image–text matching** | Match images to their captions | CLIP, ALIGN |
| **Rotation prediction** | Predict image rotation angle | RotNet |

## Why Representations Transfer

Pretraining forces the model to encode structural properties of the data:
- Language models learn syntax, semantics, world knowledge — all useful for downstream NLP.
- Vision models learn edges, textures, objects — all useful for downstream vision tasks.

The learned representations generalize because the pretext tasks require the same features needed for most downstream tasks.

## Scaling Laws

Self-supervised pretraining obeys power-law scaling: performance on downstream tasks improves predictably with more parameters, more data, and more compute. This drove the development of LLMs (GPT-3, 4, LLaMA) and large vision models (ViT-22B).

## SSL vs Supervised vs Unsupervised

| Paradigm | Labels | Supervision signal | Typical use |
|----------|--------|-------------------|-------------|
| Supervised | Required (expensive) | Human labels | Fine-tuning, small datasets |
| Self-supervised | Not required | Data itself (pretext task) | Pretraining at scale |
| Unsupervised | None | Density / reconstruction | Clustering, anomaly detection |

## Related Concepts

- [[Transformer]] — the architecture most SSL pretraining uses
- [[BERT]] — MLM-based language pretraining
- [[GPT]] — CLM-based language pretraining
- [[Vision Transformer (ViT)]] — vision model often pretrained with SSL
- [[In-Context Learning]] — downstream capability enabled by SSL pretraining
