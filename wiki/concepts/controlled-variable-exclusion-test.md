---
title: "Controlled Variable Exclusion Test"
type: concept
tags: [ai-agents, evaluation, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# Controlled Variable Exclusion Test

A controlled variable exclusion test measures which [[Harness Engineering]] subsystem matters most for a given task by holding the model fixed and removing subsystems one at a time — instructions, then feedback, then state, etc. — and observing which removal causes the largest performance drop.

The subsystem whose removal hurts most has the highest marginal contribution for that specific task. This is a diagnostic tool, not a final verdict: ablation results alone can't identify *why* something matters, so the lecture pairs this test with failure-log analysis and root-cause attribution (see [[Diagnostic Loop]]). A subsystem that shows near-zero impact under ablation shouldn't be dismissed outright either — it may be poorly designed, redundant with another subsystem, or simply unused by the task at hand rather than genuinely unnecessary.

## How It Differs From Just Reading the Harness

Inspecting an `AGENTS.md` file tells you what's *present*. This test tells you what's *load-bearing* — which piece the agent actually depends on to succeed, for this task, right now.

## Related

- [[Harness Engineering]]
- [[Capability Gap]]
- [[Diagnostic Loop]]
