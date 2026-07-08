---
title: "Harness-Induced Failure"
type: concept
tags: [ai-agents, reliability, software-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Harness-Induced Failure

Harness-induced failure is when a model has enough capability to solve a task, but the surrounding system prevents it from doing so reliably.

Lecture 01 uses controlled experiments to make this concrete: the same model can fail in a bare prompt-only setup and succeed when the harness adds planning, generation, evaluation, verification, and state persistence.

[[Lecture 09. Preventing Agents from Declaring Victory Too Early|Lecture 09]] revisits this exact experiment — same model (Opus 4.5), same 2D retro game editor task — and supplies concrete figures: a single bare-run agent took 20 minutes and $9 with core features not working; three agents (planner + generator + evaluator, see [[Worker/Checker Separation]]) took 6 hours and $200 with core features working. The harnessed run cost roughly 22x more and took 18x longer, and was the only one that actually worked.

## Related

- [[Harness Engineering]]
- [[Anthropic]]
- [[Codex]]
- [[Verification Gap]]
- [[Diagnostic Loop]]
- [[Worker/Checker Separation]]
