---
title: "Lecture 05. Keeping Context Alive Across Sessions"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Lecture 05. Keeping Context Alive Across Sessions

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Fifth in the series, following [[Lecture 04. Split Instructions Across Files]].

## Thesis

Long-running tasks that span multiple sessions lose continuity when the context window exhausts mid-project — a new session loses decision history, design rationale, and understanding of project state. Critically, this isn't fixable by bigger context windows: "context windows are finite. This isn't a problem that model upgrades can solve — even if window sizes grow to 1M tokens, complex tasks will still exhaust them." The fix has to be structural persistence, not a bigger buffer.

## The What/Why Loss

The deeper failure mode is an information-hierarchy problem: agents generate intermediate reasoning explaining *why* a decision was made, but compaction typically preserves only the *what* (the resulting code), discarding the *why*. A fresh session sees an implemented decision with no justification attached, and may quietly undo something the team deliberately chose. This is the direct motivation for the [[Decision Log]] artifact below.

The lecture also cites Anthropic's [[Context Anxiety]] research here: as an agent senses it's running low on tokens, it rushes toward closure, skips verification, and picks the first plausible fix over the best one.

## Core Concepts

- **[[Rebuild Cost]]**: the time a new session needs to reach an executable, oriented state. The lecture targets compressing this from ~15 minutes down to ~3.
- **[[Drift]]**: the growing gap between what an agent believes about the repo and what's actually true, which compounds across session boundaries if nothing corrects it.
- **[[Compaction vs. Reset]]**: two different continuity strategies. Compaction summarizes context within a session (cheap, but risks losing reasoning); reset starts a fresh session that reconstructs understanding from persisted artifacts (cleaner, but only as good as those artifacts).

## State Persistence Artifacts

- **`PROGRESS.md`** (extends Lecture 03's recommendation): latest commit hash, test status, completed tasks, in-progress work, known issues, next steps.
- **[[Decision Log]]** (`DECISIONS.md`): what was chosen, why alternatives were rejected, and the constraints that shaped the choice — the artifact that actually preserves the "why."
- **Git commits as checkpoints**: each atomic unit of work gets a descriptive commit, producing automatically-versioned state snapshots for free.
- **[[Harness Initialization Flow]]**: `AGENTS.md` should specify an explicit clock-in routine (read state files, verify consistency with actual repo state) and clock-out routine (update progress, confirm state, commit) bookending every session.

## Case Study

Structured state persistence (progress file + decision log + verification records) versus a baseline lacking these mechanisms: rebuild time down 78%, feature completion up from 58% to 100%, defect rate down from 43% to 8% — a fifth capability-gap data point in this series. See [[Capability Gap]].

## Strategy

Mixed approach: short tasks complete within a single session and don't need this machinery. Long tasks spanning sessions need progress files, decision logs, and verification records, or [[Drift]] accumulates unchecked.

## Related Pages

- [[Harness Engineering]]
- [[Agent State Management]]
- [[Agent State ACID Principles]]
- [[Context Anxiety]]
- [[Rebuild Cost]]
- [[Drift]]
- [[Compaction vs. Reset]]
- [[Decision Log]]
- [[Harness Initialization Flow]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 04. Split Instructions Across Files]]
