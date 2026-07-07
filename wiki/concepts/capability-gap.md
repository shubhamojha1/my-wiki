---
title: "Capability Gap"
type: concept
tags: [ai-agents, evaluation, machine-learning]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# Capability Gap

The capability gap is the difference between what a model can do on benchmarks and what it can do on real engineering tasks.

Lecture 01 uses SWE-bench Verified pass rates as an example. A score in the 50-60 percent range may look acceptable on paper, but it still means a large share of tasks are not solved. Real projects are harder because requirements are vague, conventions are implicit, and verification is often missing.

[[Lecture 02. What a Harness Actually Is|Lecture 02]] adds a second, more granular data point: a ~20,000-line TypeScript + React project ran the *same model* through four stages of harness improvement — basic README (20% success) → `AGENTS.md` with conventions (60%) → explicit verification commands (80%) → progress-file templates (80-100%). The entire gap closed through harness changes alone, with zero change to the model. See [[Harness Engineering]] and [[Controlled Variable Exclusion Test]] for how to isolate which subsystem is responsible for a given gap.

## Related

- [[SWE-bench]]
- [[Harness Engineering]]
- [[Verification Gap]]
- [[Harness-Induced Failure]]
- [[Controlled Variable Exclusion Test]]
