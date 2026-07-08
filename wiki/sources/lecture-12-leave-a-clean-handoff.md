---
title: "Lecture 12. Leave a Clean Handoff at the End of Every Session"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/"]
---

# Lecture 12. Leave a Clean Handoff at the End of Every Session

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Twelfth in the series, following [[Lecture 11. Making the Agent's Runtime Observable]].

## Thesis

A session that ends with unresolved issues — a broken build, failed tests, scattered debug files, an unupdated progress file — costs the next session 30+ minutes just diagnosing what actually happened. OpenAI and Anthropic are cited together here: "long-term reliability depends on operational discipline, not just single-run success."

## Entropy Growth Is the Default State

Lehman's laws of software evolution are cited directly: systems under continuous change inevitably grow more complex without active management — this isn't a special agent failure mode, it's the default behavior of any evolving system. A genuine fourth external research citation in this series, alongside Guo et al. (2017, [[Confidence Calibration Bias]]), Liu et al. (2023, [[Lost in the Middle]]), and Dapper ([[Task Trace]]).

OpenAI's Codex experiments found agents copy whatever pattern already exists in a repository, even when that pattern is inconsistent or suboptimal — the same lesson already in this wiki from [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification|Lecture 10]]'s [[Layered Domain Architecture]] citation, applied here to entropy specifically rather than architectural boundaries. Their response: encode "golden rules" into the repo (prefer shared utilities, validate data structures), establish periodic cleanup workflows, and capture human taste once, then enforce it continuously rather than re-litigating it every session. The framing principle: "Technical debt is a high-interest loan. Continuously paying it off in small increments is almost always better than letting it accumulate."

## Clean State: Five Conditions

Clean state is more than "the code compiles." It requires all five:

1. Build passes (CI-verified).
2. All tests pass, including pre-existing ones.
3. Progress recorded in machine-readable artifacts.
4. No stale artifacts (debug logs, commented-out code, TODO markers).
5. Startup path functional for whoever runs the next session.

This is the concrete definition this wiki's existing [[Harness Initialization Flow]] (Lecture 05) was missing for its clock-out half — that page said "update progress, confirm state, commit" without specifying what "confirmed" actually requires. Folded directly into that page rather than treated as a separate concept.

**Session integrity** — the requirement that a session either leaves all five conditions true or is treated as incomplete, no partial credit — is the same all-or-nothing framing as **Atomicity** in [[Agent State ACID Principles]] (Lecture 03), described again from the session-boundary angle. Folded into that page as a cross-reference.

## "Clean Up Later" Means Never Clean Up

A 12-week agent-developed Electron project, run two ways:

| | Week 1 | Week 12 (no cleanup) | Week 12 (with cleanup) |
|---|---|---|---|
| Build pass rate | 100% | 68% | 97% |
| Test pass rate | 100% | 61% | 95% |
| Startup time | 5 min | 60+ min | 9 min |
| Stale artifacts | — | 103 | 11 |

The cleanup strategy cost roughly 5 extra minutes per session but saved dozens of hours across the 12 weeks — a twelfth capability-gap data point, and notably the first *longitudinal* one in this series (12 weeks of accumulating drift) rather than a single before/after comparison. See [[Capability Gap]].

## How to Do It

1. **Clean state as a completion requirement**, defined explicitly in harness documentation, not left implicit.
2. **Dual-mode cleanup strategy**: immediate cleanup (per-session — remove session-specific temp artifacts, update progress) plus periodic cleanup (weekly full-system scans for structural issues). See [[Cleanup Loop]].
3. **Maintain a [[Quality Document]]**: a living artifact scoring each module A/B/C across verification status, agent understandability, test stability, architecture compliance, and convention adherence.
4. **Periodically simplify the harness** as model capability improves — see [[Harness Simplification]]. Anthropic's cited example: Opus 4.6's capability eliminated the need for Sonnet 4.5's sprint-splitting mechanism, enabling 2+ hours of continuous work.
5. **Cleanup operations must be idempotent** — safe to run repeatedly with no side effects (e.g. `rm -f` rather than `rm`, which errors on a missing file).
6. **High agent throughput changes merge philosophy**: when agent output volume exceeds human review capacity, minimize blocking merge gates — a fast fix often costs less than waiting on review when volume is high.

## Related Pages

- [[Harness Engineering]]
- [[Harness Initialization Flow]]
- [[Agent State ACID Principles]]
- [[Quality Document]]
- [[Cleanup Loop]]
- [[Harness Simplification]]
- [[Layered Domain Architecture]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 11. Making the Agent's Runtime Observable]]
