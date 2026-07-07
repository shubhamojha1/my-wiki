---
title: "Anthropic"
type: entity
tags: [organization, ai-research, machine-learning]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/"]
---

# Anthropic

Anthropic is an AI company whose models and research are cited repeatedly across the [[Learn Harness Engineering]] series as evidence that harness quality can dominate agent performance.

Lecture 01 cites a controlled experiment where the same model and prompt were run twice. The weak setup failed quickly. The stronger setup added planner, generator, and evaluator roles and produced a working result.

[[Lecture 06. Make the Agent Initialize Before Every Work Session|Lecture 06]] cites Anthropic's long-running application development research directly: projects using a dedicated [[Initialization Phase]] showed 31% higher feature completion rates in multi-session scenarios than projects mixing setup and implementation.

[[Lecture 07. Draw Clear Task Boundaries for Agents|Lecture 07]] cites Anthropic again: agents using a "small next step" strategy show a 37% higher task completion rate than agents given broad prompts — the research basis for [[WIP Limit|WIP=1]]. See [[Overreach and Under-finish]].

## Related

- [[Claude Sonnet]]
- [[Harness-Induced Failure]]
- [[Harness Engineering]]
- [[Initialization Phase]]
- [[Overreach and Under-finish]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 06. Make the Agent Initialize Before Every Work Session]]
- [[Lecture 07. Draw Clear Task Boundaries for Agents]]
