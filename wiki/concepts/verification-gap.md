---
title: "Verification Gap"
type: concept
tags: [ai-agents, testing, software-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Verification Gap

The verification gap is the distance between the agent's confidence that a task is done and the task actually being correct.

Lecture 01 treats this as one of the most common failure modes. Agents can write plausible code, inspect it briefly, and then stop without running the checks that would show the work is incomplete.

[[Lecture 09. Preventing Agents from Declaring Victory Too Early|Lecture 09]] names the moment this gap produces a concrete failure: a [[Premature Completion Declaration]]. It also grounds the gap in real research rather than treating it as an anecdotal quirk — Guo et al.'s 2017 finding that neural networks are systematically overconfident, sharpened by Anthropic's 2026 result that self-evaluation specifically inflates further (see [[Confidence Calibration Bias]]) — and gives a structural fix, [[Three-Layer Termination Validation]], rather than leaving verification as a vague aspiration.

## Related

- [[Definition of Done]]
- [[Harness Engineering]]
- [[Diagnostic Loop]]
- [[Context Anxiety]]
- [[Premature Completion Declaration]]
- [[Confidence Calibration Bias]]
- [[Three-Layer Termination Validation]]
