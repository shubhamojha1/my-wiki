---
title: "Codex"
type: entity
tags: [ai-agents, openai, coding-assistant]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# Codex

Codex is OpenAI's coding agent used in the lecture series as the reference point for harness engineering.

[[Lecture 01. Strong Models Don't Mean Reliable Execution|Lecture 01]] points to OpenAI's million-line repo experiment: the important change was not the model itself, but the harness around it. Better task decomposition, explicit repo conventions, and stronger verification loops made Codex much more reliable on long-running engineering work.

[[Lecture 02. What a Harness Actually Is|Lecture 02]] adds architectural detail: Codex uses git worktrees for environment isolation and has local observability (logs, metrics, traces). It performs significantly better in repositories with structured documentation like `AGENTS.md` and clear verification commands — i.e. it rewards a strong [[Harness Engineering|Instruction and Feedback Subsystem]].

## Related

- [[OpenAI]]
- [[Harness Engineering]]
- [[Agent State Management]]
- [[Cursor]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 02. What a Harness Actually Is]]
