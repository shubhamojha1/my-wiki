---
title: "In-Context Learning"
type: concept
tags: [machine-learning, nlp, learning-paradigm]
created: 2026-04-05
updated: 2026-05-20
sources: [Language Models are Few-Shot Learners.pdf]
---

# In-Context Learning (ICL)

**In-context learning** is the ability of a large language model to adapt its behavior to a new task by conditioning on examples provided in the prompt — without any gradient updates or parameter changes. The "learning" happens entirely in the forward pass through the context window.

## How It Works

```
Prompt:
  Input: "The movie was great"  →  Output: positive
  Input: "Terrible acting"      →  Output: negative
  Input: "Loved every minute"   →  Output: ???

Model output: positive     ← learned from the two examples in-context
```

The model processes all examples using self-attention, allowing each new token to attend to every prior example. The pattern is extracted via attention weights computed at inference time — no weight updates occur.

## Shot Taxonomy

| Mode | Examples in prompt | Description |
|------|--------------------|-------------|
| **Zero-shot** | 0 | Task described in words; no demonstrations |
| **One-shot** | 1 | One example per class or task |
| **Few-shot** | 2–10+ | Several examples; GPT-3's original framing |
| **Many-shot** | 100s–1000s | Modern long-context models; approaches fine-tuning quality |

## Theoretical Debate

Whether ICL is "genuine learning" or "retrieval" is an open research question:

| View | Argument |
|------|---------|
| **Task learning** | Model uses context to infer the latent function and applies it to new inputs; can generalize beyond seen patterns |
| **Pattern retrieval** | Model identifies which pre-trained knowledge to apply; accuracy depends on similarity of demonstrations to training data |

Evidence: Models can learn label-reversed tasks (e.g., positive → negative) from context, suggesting some task induction occurs.

## What Makes Good Demonstrations

- **Format consistency**: All examples follow the same input → output structure.
- **Representative**: Cover the diversity of inputs the model will see.
- **Correct labels** (mostly): Wrong examples degrade performance, but models are somewhat robust to a few errors.
- **Ordering**: Recency matters — later examples have more influence (primacy/recency bias).

## Scaling Effects

ICL emerges at scale and improves sharply at large model sizes (10B+ parameters). Smaller models benefit less from demonstrations. This is one of the **emergent capabilities** observed in GPT-3 and its successors.

## ICL vs Fine-Tuning

| Aspect | ICL | Fine-Tuning |
|--------|-----|-------------|
| Parameter updates | None | Yes |
| Setup cost | None (just write a prompt) | Compute + labeled dataset |
| Generalization | Limited to context length | Persistent in weights |
| Flexibility | Swap tasks by changing prompt | One task per model |
| Performance ceiling | Below fine-tuning for specialized tasks | Higher |

## Related Concepts

- [[Few-Shot Learning]] — the prompting paradigm ICL enables
- [[Transformer]] — the architecture that makes ICL possible (attention over context)
- [[Prompt Engineering]] — designing demonstrations that maximize ICL performance
- [[Self-Supervised Learning]] — how models are pre-trained to be ICL-capable
