---
title: "Quality Document"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/"]
---

# Quality Document

A quality document is a living artifact scoring each module in a codebase (e.g. Quality: A/B/C) across five dimensions: verification status, agent understandability, test stability, architecture compliance, and code convention adherence. [[Lecture 12. Leave a Clean Handoff at the End of Every Session]] recommends maintaining this alongside `PROGRESS.md`/[[Decision Log]] as part of [[Agent State Management]].

Its purpose is proactive rather than reactive: instead of discovering a module has decayed only when something breaks, a quality document makes decay visible ahead of time, so [[Cleanup Loop|periodic cleanup]] can be targeted at the modules that actually need it rather than sweeping the whole codebase uniformly.

## Related

- [[Cleanup Loop]]
- [[Agent State Management]]
- [[System of Record]]
- [[Harness Engineering]]
