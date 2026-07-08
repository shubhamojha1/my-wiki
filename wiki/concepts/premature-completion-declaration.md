---
title: "Premature Completion Declaration"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Premature Completion Declaration

A premature completion declaration is when an agent asserts a task is done despite unmet specifications, because it judged completion from local code-level confidence — syntax looks right, logic seems reasonable, tests it chose to run passed — rather than from global, system-level verification. [[Lecture 09. Preventing Agents from Declaring Victory Too Early]] frames this as the concrete, everyday form of the wiki's existing [[Verification Gap]]: the same gap, but named at the moment it produces a false "done" claim rather than described abstractly.

It follows a predictable pattern the lecture calls **the slippery slope**: syntax appears correct, logic seems reasonable, static analysis shows nothing — and the harness stops there because it lacks execution verification. Unit tests get run but integration tests get skipped; tests get checked but not coverage. "The code looks fine" quietly substitutes for "the feature is complete."

The underlying cause is [[Confidence Calibration Bias]]; the concrete fix is [[Three-Layer Termination Validation]] enforced by the harness rather than judged by the agent.

## Related

- [[Verification Gap]]
- [[Confidence Calibration Bias]]
- [[Three-Layer Termination Validation]]
- [[Definition of Done]]
- [[Completion Evidence]]
