---
title: "Cleanup Loop"
type: concept
tags: [ai-agents, harness-engineering, maintenance]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/"]
---

# Cleanup Loop

A cleanup loop is [[Lecture 12. Leave a Clean Handoff at the End of Every Session]]'s dual-mode maintenance strategy for reversing the entropy that Lehman's laws of software evolution predict as the default state of any continuously-changing system:

- **Immediate cleanup** — done at the end of every session: remove session-specific temporary artifacts, update progress. This is the concrete content of the clock-out half of [[Harness Initialization Flow]].
- **Periodic cleanup** — a recurring (e.g. weekly) full-system scan addressing structural issues that accumulate too slowly for any single session to notice: encoding "golden rules" into the repo (prefer shared utilities, validate data structures), consulting the [[Quality Document]] to target modules that have actually decayed, and applying [[Harness Simplification]] where the harness itself has become unnecessary overhead.

Cleanup operations at either cadence must be **idempotent** — safe to run repeatedly with no side effects from repetition (e.g. `rm -f somefile` rather than `rm somefile`, which errors if the file is already gone). An idempotent cleanup script can be run defensively without an agent needing to reason about whether it's "already been run" — it just runs, and the end state is the same either way.

The lecture frames the underlying economics simply: "technical debt is a high-interest loan. Continuously paying it off in small increments is almost always better than letting it accumulate" — a 12-week case study (see [[Capability Gap]]) found the cleanup strategy cost roughly 5 extra minutes per session but saved dozens of hours over the full period.

A related practice for high agent throughput: when agent output volume exceeds human review capacity, minimize blocking merge gates — a fast fix often costs less than waiting on review when volume is high, which changes what "cleanup" should prioritize under load.

## Related

- [[Quality Document]]
- [[Harness Simplification]]
- [[Harness Initialization Flow]]
- [[Capability Gap]]
