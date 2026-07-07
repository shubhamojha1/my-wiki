---
title: "Anthropic"
type: entity
tags: [organization, ai-research, machine-learning]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/"]
---

# Anthropic

Anthropic is an AI company whose models and research are cited repeatedly across the [[Learn Harness Engineering]] series as evidence that harness quality can dominate agent performance.

Lecture 01 cites a controlled experiment where the same model and prompt were run twice. The weak setup failed quickly. The stronger setup added planner, generator, and evaluator roles and produced a working result.

[[Lecture 06. Make the Agent Initialize Before Every Work Session|Lecture 06]] cites Anthropic's long-running application development research directly: projects using a dedicated [[Initialization Phase]] showed 31% higher feature completion rates in multi-session scenarios than projects mixing setup and implementation.

## Related

- [[Claude Sonnet]]
- [[Harness-Induced Failure]]
- [[Harness Engineering]]
- [[Initialization Phase]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 06. Make the Agent Initialize Before Every Work Session]]
