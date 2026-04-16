---
title: "Few-Shot Learning"
type: concept
tags: [machine-learning, nlp, learning-paradigm]
created: 2026-04-05
sources: [Language Models are Few-Shot Learners.pdf]
---

# Few-Shot Learning

A learning paradigm where a model can perform a new task given only a small number of examples in the prompt, without gradient-based fine-tuning.

## Variations

- **Zero-shot**: Task description only, no examples
- **One-shot**: Task description + 1 example
- **Few-shot**: Task description + few (typically 10-100) examples

## How It Works

The examples are provided as part of the model's context window. The model learns to infer the task pattern from these examples without updating its weights.

## Key Insight

The GPT-3 paper showed that larger language models become better at few-shot learning, suggesting that scale improves the model's ability to infer tasks from limited examples.

## Comparison with Traditional ML

| Aspect | Fine-tuning | Few-Shot |
|--------|------------|----------|
| Examples needed | Many (thousands) | Few (1-100) |
| Training time | Minutes to days | None |
| Per-task storage | Model weights | Prompt tokens |
| Adaptation | Updates weights | In-context |

## Limitations

- Less reliable than fine-tuning for complex tasks
- Context length limits number of examples
- Performance varies by task type

## Related

- [[GPT-3]] — First demonstrated few-shot at scale
- [[GPT-3 Paper]] — The original paper
- [[In-Context Learning]] — The mechanism