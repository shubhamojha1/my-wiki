---
title: "What is In-Context Learning?"
type: query
tags: [llm, learning, gpt]
created: 2026-04-16
sources: [in-context-learning.md]
---

# What is In-Context Learning?

In-context learning (ICL) is the ability of large language models to learn tasks from examples in the prompt, without explicit training or parameter updates.

## How It Works

1. Examples included in input context
2. Attention mechanism relates new inputs to example patterns
3. Model generates outputs matching demonstrated pattern

## Key Insight

ICL is the mechanism that enables [[Few-Shot Learning]]. The examples guide output without changing model weights.

## Open Question

Is it genuine "learning" or sophisticated pattern matching?
- **Learning view**: Model updates internal representations from context
- **Pattern matching view**: Model selects from pre-trained knowledge

## Scaling Behavior

Larger models show stronger ICL; capabilities emerge at scale thresholds (related to [[Emergent Abilities]]).

## Related

- [[Few-Shot Learning]] — The prompting paradigm ICL enables
- [[In-Context Learning]] — Full concept page
- [[GPT-3]] — Demonstrated ICL at scale
