---
title: "Lecture 06. Make the Agent Initialize Before Every Work Session"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/"]
---

# Lecture 06. Make the Agent Initialize Before Every Work Session

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Sixth in the series, following [[Lecture 05. Keeping Context Alive Across Sessions]].

## Thesis

Initialization and implementation are two fundamentally different kinds of work with opposing objectives: implementation maximizes feature quantity and quality, initialization maximizes reliability for everything that comes after it. When an agent jumps straight into coding without a dedicated setup step, it wastes time discovering configuration problems mid-feature instead of building — and mixing the two objectives weakens both. See [[Initialization Phase]].

This is a distinct concern from Lecture 05's [[Harness Initialization Flow]]: that lecture's clock-in/clock-out routine is the lightweight bookend around *every* session (read state, verify, work, update state, commit). This lecture is about treating a project's (or a large task's) *initial setup* as its own dedicated phase, separate from feature work entirely — the two compose (a project gets a full initialization once, and every session thereafter still does the lighter clock-in/clock-out).

## What Goes Wrong When You Mix Them

- Infrastructure gets built carelessly — a framework gets configured but never actually verified to work.
- **Unverified Accumulation**: code gets written before the testing infrastructure that should validate it exists, so that code may need redesigning once real verification arrives. See [[Initialization Phase]].
- Context budget spent on ad-hoc setup leaves less room for the features that were actually the point of the session.
- Implicit, undocumented setup decisions (which test framework, how directories are organized) contradict each other across sessions, since nothing forced them to be made once and recorded.

## Research Support

Anthropic's long-running application development research is cited directly: projects using a dedicated initialization phase showed 31% higher feature completion rates in multi-session scenarios compared to mixed approaches — a sixth capability-gap data point in this series. See [[Capability Gap]].

## What Initialization Should Produce

1. A runnable environment.
2. A verifiable test framework.
3. A [[Startup Readiness Checklist]] document.
4. A task breakdown with acceptance criteria.
5. A git checkpoint commit.

**Templates over empty directories**: starting from a project template outperforms starting from scratch, since it eliminates redundant setup work the template already solved.

**Metric**: success is measured by whether subsequent sessions can operate independently, and concretely by "time from start to first passing test" — a companion metric to [[Rebuild Cost]], but measured on first setup rather than on every subsequent session restart.

## Case Study

A comparison found dedicated initialization cost about 20 minutes upfront, but recovered that investment through faster subsequent sessions, cutting total rebuild time by 60% versus mixed approaches that skipped a dedicated init phase.

## Related Pages

- [[Harness Engineering]]
- [[Initialization Phase]]
- [[Startup Readiness Checklist]]
- [[Harness Initialization Flow]]
- [[Rebuild Cost]]
- [[Capability Gap]]
- [[Anthropic]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 05. Keeping Context Alive Across Sessions]]
