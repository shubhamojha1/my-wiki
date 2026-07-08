---
title: "Verification-Validation Dual Gate"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Verification-Validation Dual Gate

The verification-validation dual gate is [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]'s two-part gate that a feature must pass, borrowing the classic software-engineering distinction between the two words:

- **Verification** ("did we build it right?"): does the implementation correctly match the specification.
- **Validation** ("did we build the right thing, and does it actually work end-to-end?"): does the system meet the real, end-to-end requirement in practice.

Both gates must pass — passing verification alone (the code does what the spec said) doesn't guarantee validation (the feature actually works when run for real), which is exactly the gap that produces a [[Premature Completion Declaration]]. In practice this maps onto [[Three-Layer Termination Validation]]: verification corresponds roughly to Layers 1-2 (does the code match intent, does it run), and validation corresponds to Layer 3 (does the full system behave correctly end-to-end).

## Related

- [[Three-Layer Termination Validation]]
- [[Premature Completion Declaration]]
- [[Definition of Done]]
- [[Completion Evidence]]
