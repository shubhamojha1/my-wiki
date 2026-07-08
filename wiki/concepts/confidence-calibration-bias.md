---
title: "Confidence Calibration Bias"
type: concept
tags: [ai-agents, llm-behavior, research, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Confidence Calibration Bias

Confidence calibration bias is the systematic gap between an agent's self-reported confidence that a task is complete and the task's actual quality. [[Lecture 09. Preventing Agents from Declaring Victory Too Early]] grounds this in real outside research rather than treating it as an anecdotal quirk: Guo et al.'s 2017 ICML paper proved that modern neural networks are systematically overconfident — their predicted probabilities don't match their actual accuracy. The lecture argues coding agents inherit this same bias, and that for complex multi-file tasks the miscalibration is significantly positive (i.e. agents overstate completion, not understate it).

Anthropic's 2026 research sharpens this specifically for self-evaluation: agents asked to grade their own work give systematically inflated assessments — worse for subjective tasks — even in cases where a human observer would call the result substandard.

This is why the harness, not the agent, has to hold the bar: see [[Premature Completion Declaration]] for the failure mode this bias produces, [[Three-Layer Termination Validation]] for the structural fix, and [[Worker/Checker Separation]] for the specific fix to the self-evaluation version of the problem.

## Related

- [[Premature Completion Declaration]]
- [[Worker/Checker Separation]]
- [[Three-Layer Termination Validation]]
- [[Verification Gap]]
- [[Context Anxiety]]
