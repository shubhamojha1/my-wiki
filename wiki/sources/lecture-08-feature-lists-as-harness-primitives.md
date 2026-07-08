---
title: "Lecture 08. Use Feature Lists to Constrain What the Agent Does"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/"]
---

# Lecture 08. Use Feature Lists to Constrain What the Agent Does

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Eighth in the series, following [[Lecture 07. Draw Clear Task Boundaries for Agents]].

## Thesis

An agent can claim an e-commerce site is complete while payment processing is still unimplemented — because "you never told it what 'done' means." A feature list isn't a human planning checklist; it's "the foundational structure the entire harness is built on," the thing the scheduler, verifier, and handoff reporter all read from. Per Anthropic and OpenAI guidance cited here, artifacts like this must be externalized into machine-readable repo files, not left in conversation text.

This lecture's Feature State Machine is the same underlying artifact as Lecture 07's [[Scope Surface]] — a DAG of task states externalized to a repo file — described with more precision: it names the four actual states and adds the rule that gates movement between them. Rather than treat it as a separate structure, this ingest folds the added detail directly into [[Scope Surface]].

## Documents vs. Primitives

The lecture's sharpest new distinction: "documents are for humans to read; primitives are for systems to execute." A primitive can't be quietly bypassed the way an application-layer check can — it functions more like a database-level constraint than a linted convention. This reframes why a feature list has to be externalized and machine-enforced rather than left as prose: see [[Harness Primitive]].

## The Feature State Machine (folded into Scope Surface)

- Each feature carries a **triple structure**: behavior description, verification command, current state. See [[Completion Evidence]] for the concrete schema.
- States: `not_started` → `active` → `blocked` → `passing`.
- **Pass-state gating**: only a successful verification command moves a feature to `passing` — the agent cannot set its own state.
- **Single source of truth**: all scope information comes from this one list, not from scattered conversation or comments.
- **Back-pressure**: unresolved features create pressure against starting new ones, which is the same mechanism [[WIP Limit]] relies on from the other direction.

## Four Harness Components That Depend on the Feature List

1. **Scheduler** — selects the next `not_started` feature.
2. **Verifier** — executes verification commands, approves state transitions.
3. **Handoff reporter** — generates session summaries automatically from feature states.
4. **Progress tracker** — measures project health metrics off the same list.

## Implementation

Minimal format (JSON):

```json
{
  "id": "F03",
  "behavior": "POST /cart/items returns 201",
  "verification": "curl command with JSON validation",
  "state": "passing",
  "evidence": "commit reference, test logs"
}
```

Harness control, not agent autonomy, governs state changes — the agent can't directly mark a feature `passing`; only a successful verification run can. Granularity should be calibrated so each feature is "completable in one session": broad enough to avoid micromanagement, narrow enough to actually finish within a single work block.

## Case Study

Unstructured tracking produced 20-minute diagnostic periods at the start of each new session and duplicate implementations of already-built functionality. Structured feature lists cut that resume time to 3 minutes with zero rework, and delivered 45% higher feature completion than free-form tracking — an eighth capability-gap data point in this series. See [[Capability Gap]].

## Related Pages

- [[Harness Engineering]]
- [[Harness Primitive]]
- [[Scope Surface]]
- [[Completion Evidence]]
- [[WIP Limit]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 07. Draw Clear Task Boundaries for Agents]]
