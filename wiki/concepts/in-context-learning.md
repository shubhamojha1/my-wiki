---
title: "In-Context Learning"
type: concept
tags: [machine-learning, nlp, learning-paradigm]
created: 2026-04-05
sources: [Language Models are Few-Shot Learners.pdf]
---

# In-Context Learning

The ability of large language models to learn tasks from examples provided in their input context, without explicit training or parameter updates.

## Mechanism

When examples are included in the prompt, the model:
1. Processes the examples as part of its input
2. Uses attention to relate new inputs to example patterns
3. Generates outputs that match the demonstrated pattern

## Theoretical Perspective

Still debated — whether this is genuine "learning" or pattern matching. Two views:
- **Learning**: Model updates internal representations from context
- **Pattern matching**: Model selects from pre-trained knowledge

## Relation to Few-Shot

In-context learning is the mechanism that enables few-shot prompting. The examples guide the model's output without changing its parameters.

## Scaling Effects

Studies show that larger models exhibit stronger in-context learning, with capabilities emerging at certain scale thresholds.

## Related

- [[Few-Shot Learning]] — The prompting paradigm
- [[GPT-3]] — Demonstrated this at scale
- [[Prompt Engineering]] — Optimizing context for ICL