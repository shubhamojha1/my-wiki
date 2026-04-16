---
title: "GPT-3"
type: entity
tags: [machine-learning, nlp, language-model, openai]
created: 2026-04-05
sources: [Language Models are Few-Shot Learners.pdf]
---

# GPT-3

The third-generation Generative Pre-trained Transformer, introduced by OpenAI in 2020. At 175 billion parameters, it was the largest language model of its time.

## Overview

GPT-3 is a transformer-based autoregressive language model trained on a diverse corpus of internet text. Its key innovation was demonstrating that scale alone — without fine-tuning — could unlock new capabilities.

## Key Metrics

- **Parameters**: 175 billion
- **Layers**: 96
- **Heads**: 96 per layer
- **Context Length**: 2048 tokens
- **Training Data**: ~570GB of text

## Capabilities

- **Text Generation**: Produces human-like text
- **Few-Shot Learning**: Learns from examples in prompt
- **Translation**: Cross-lingual transfer
- **Question Answering**: Reading comprehension
- **Code Generation**: Writes simple programs
- **Emergent Tasks**: Arithmetic, word unscrambling, reasoning

## Architecture

Based on the transformer decoder architecture, similar to GPT-2 but scaled. Uses:
- Dense attention with alternating widths
- SwiGLU activations
- Layer normalization before each block
- Positional embeddings

## Impact

GPT-3 sparked the large language model era, demonstrating that:
- Scale beyond certain thresholds unlocks emergent abilities
- Few-shot prompting can replace fine-tuning for many tasks
- API-based AI services became commercially viable

## Related

- [[GPT-3 Paper]] — The original paper describing it
- [[OpenAI]] — The organization that built GPT-3
- [[Few-Shot Learning]] — The prompting paradigm it popularized
- [[Transformer]] — The underlying architecture