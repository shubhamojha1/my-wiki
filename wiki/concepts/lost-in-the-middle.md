---
title: "Lost in the Middle"
type: concept
tags: [ai-agents, context-window, llm-behavior, research]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/"]
---

# Lost in the Middle

Lost in the Middle is a research finding (Liu et al., 2023) that LLMs use information positioned in the middle of long text significantly less effectively than information at the beginning or end. Attention/utilization follows a U-shape over document position, not a flat distribution.

[[Lecture 04. Split Instructions Across Files]] applies this directly to instruction files: a critical security constraint sitting at line 300 of a 600-line `AGENTS.md` has a real, measured chance of being effectively ignored — independent of how clearly it's written — purely because of where it sits in the document. This is the mechanism behind why [[Instruction Bloat]] is actively harmful rather than just wasteful: growth doesn't only cost tokens, it also demotes older content into the position where the model is least likely to use it.

The recommended countermeasure isn't to shorten prose but to exploit the effect: keep only the highest-priority constraints in the entry file, and place them at the very top or very bottom, never buried in a middle section.

## Related

- [[Instruction Bloat]]
- [[Entry File]]
- [[Instruction Signal-to-Noise Ratio]]
- [[Harness Engineering]]
