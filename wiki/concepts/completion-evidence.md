---
title: "Completion Evidence"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/"]
---

# Completion Evidence

Completion evidence is a verifiable, executable condition proving a specific task is done — e.g. `curl -X POST /api/register ... | jq .status == 201` — rather than a subjective read of the diff. [[Lecture 07. Draw Clear Task Boundaries for Agents]] applies this at per-task granularity, extending [[Definition of Done]] down from "the feature is done" to "this specific atomic unit of work is done, and here's the command that proves it."

This is what makes a [[WIP Limit]] enforceable rather than just a stated intention: "finish before starting the next" only works if "finish" has an executable check, not a vibe.

**Verified Completion Rate (VCR)** is the aggregate metric built on top of completion evidence: verified tasks divided by activated tasks. The lecture recommends blocking new task activations whenever VCR < 1.0 — i.e. don't start task N+1 while any earlier task lacks passing completion evidence, which is the concrete monitoring mechanism behind enforcing WIP=1 across a whole project rather than task-by-task.

## The Triple Structure (Lecture 08)

[[Lecture 08. Use Feature Lists to Constrain What the Agent Does|Lecture 08]] gives completion evidence a concrete schema as part of each entry in a [[Scope Surface]]: every feature carries a *behavior* description, a *verification* command, and its current *state*, plus an *evidence* field (commit reference, test logs) recording what actually proved the pass. This is the field-level version of "executable, not subjective" — a reviewer or a scheduler can check the evidence field directly rather than trusting an agent's self-report.

## Related

- [[Definition of Done]]
- [[WIP Limit]]
- [[Overreach and Under-finish]]
- [[Verification Gap]]
- [[Scope Surface]]
- [[Harness Primitive]]
