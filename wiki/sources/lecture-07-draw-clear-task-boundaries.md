---
title: "Lecture 07. Draw Clear Task Boundaries for Agents"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/"]
---

# Lecture 07. Draw Clear Task Boundaries for Agents

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Seventh in the series, following [[Lecture 06. Make the Agent Initialize Before Every Work Session]].

## Thesis

Agents given one feature to build tend to overreach: asked for "add user authentication," they simultaneously touch database schemas, routes, components, and middleware — 12 files modified, 800 new lines, and zero working end-to-end features. See [[Overreach and Under-finish]].

## Attention Is a Finite Resource

The lecture frames this mathematically: if an agent's context capacity is C and it activates k tasks at once, each task gets only C/k of the available resource. Once C/k drops below the minimum a single task needs, nothing finishes — not "everything finishes a bit slower." Anthropic research is cited again here (see [[Anthropic]]): agents using a "small next step" strategy show a 37% higher task completion rate than agents given broad prompts.

## Overreach and Under-finish

These two failure modes amplify each other cyclically, and the lecture grounds this in two outside references: Little's Law (L = λ × W — more work-in-progress increases lead time, which increases the odds any given piece fails before finishing) and Steve McConnell's *Rapid Development*, which names scope creep as the single leading cause of project failure. See [[Overreach and Under-finish]] for the full mechanism.

## The Four-Step Fix

1. **Enforce [[WIP Limit|WIP=1]]**: only one active task at a time; the next feature starts only after the current one passes end-to-end verification.
2. **Define explicit [[Completion Evidence]]**: every feature needs an executable check (e.g. `curl -X POST /api/register ... | jq .status == 201`), not a subjective read of the diff.
3. **Externalize the [[Scope Surface]]**: a machine-readable file (JSON/Markdown) recording every task's state as a DAG, so a fresh session immediately sees what's done, in progress, or blocked.
4. **Monitor Verified Completion Rate**: VCR = verified tasks / activated tasks; block new task starts while VCR < 1.0. See [[Completion Evidence]].

## Case Study

Same REST API project, 8 planned features, two modes:

| Mode | Simultaneous features | Lines written | End-to-end pass rate | Final completion |
|---|---|---|---|---|
| Unconstrained | 5 at once | ~800 | 20% (1 of 5 working) | 37.5% |
| WIP=1 | Sequential | ~1200 total | Higher quality | 87.5% |

More total code was written under WIP=1, and it finished more than twice as much work — a direct rebuttal to "more parallel activity means more progress." A seventh capability-gap data point in this series, and the first that compares two *policies* on the same project rather than a before/after harness addition. See [[Capability Gap]].

## Related Pages

- [[Harness Engineering]]
- [[Overreach and Under-finish]]
- [[WIP Limit]]
- [[Completion Evidence]]
- [[Scope Surface]]
- [[Definition of Done]]
- [[Context Anxiety]]
- [[Anthropic]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 06. Make the Agent Initialize Before Every Work Session]]
