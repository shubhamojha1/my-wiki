---
title: "Lecture 02. What a Harness Actually Is"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# Lecture 02. What a Harness Actually Is

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Follow-up to [[Lecture 01. Strong Models Don't Mean Reliable Execution]].

## Thesis

Most people conflate "a harness" with "a prompt file." The lecture argues a harness is precise and structural: everything in the engineering infrastructure outside the model weights. It gives a concrete, checkable five-subsystem definition rather than a vague notion of "good instructions."

Core framing: "the repo IS the spec" — and its sharper corollary, "anything the agent cannot see, for all practical purposes, does not exist." All necessary context must live in the repository itself, not in a developer's head or an old chat thread.

## Tool Survey

The lecture characterizes four existing tools by which harness subsystem they get right or wrong:

- **Claude Code**: reads `CLAUDE.md`, runs shell commands, maintains session history, and executes tests — but without explicit test-running instructions, verification is impossible.
- **[[Cursor]]**: uses `.cursorrules` files, can read project structure and lint config — but its state management is weak; closing the IDE loses context.
- **[[Codex]]**: uses git worktrees for environment isolation and has local observability (logs, metrics, traces); performs much better in repos with `AGENTS.md`-style documentation and clear verification commands.
- **[[AutoGPT]]**: a cautionary example — without structured state management, context accumulates indefinitely on long tasks, producing loops and failures. The lecture is explicit that the problem is the harness architecture, not the model.

## The Five-Subsystem Harness Model

A complete harness needs all five; missing any one produces an incomplete harness:

1. **Instruction Subsystem** — a doc (`AGENTS.md`/`CLAUDE.md`) with project overview, tech stack + versions, first-run commands, hard constraints, and links to deeper docs.
2. **Tool Subsystem** — least-privilege tool access. Too little (e.g. no shell) blocks the agent from installing dependencies and doing the work at all.
3. **Environment Subsystem** — self-describing environment state: `pyproject.toml`/`package.json`, `.nvmrc`/`.python-version`, Docker/devcontainers for reproducibility.
4. **State Subsystem** — a `PROGRESS.md` tracking completed work, in-progress items, and blockers; updated before a session ends, reviewed when the next one begins.
5. **Feedback Subsystem** — explicit verification commands (tests, type check, lint, a combined `make check`). The lecture calls this the subsystem with typically the highest ROI.

## Guiding Principles

- **Provide maps, not manuals**: `AGENTS.md` should be a directory (~100 lines), not an encyclopedia — push detail into a `docs/` folder.
- **Constrain through rules, not micromanagement**: enforce invariants with executable rules rather than enumerating every instruction.
- **Remove one component at a time**: ablate subsystems sequentially, holding the model fixed, to measure each one's marginal contribution — see [[Controlled Variable Exclusion Test]].

## Case Study: Staged Harness Rollout

A ~20,000-line TypeScript + React frontend project, same model throughout:

| Stage | Harness addition | Success rate |
|---|---|---|
| 1 | Basic README only | 20% |
| 2 | `AGENTS.md` with stack versions, naming conventions, architecture decisions | 60% |
| 3 | Explicit verification commands listed | 80% |
| 4 | Progress-file templates introduced | 80-100% |

The model never changed. The entire 20% → ~100% improvement came from harness changes — a second concrete data point (alongside lecture 01's Anthropic/OpenAI examples) for [[Capability Gap]].

## Exercises

- **Five-tuple harness audit**: score a project 1-5 on each subsystem, improve the weakest for 30 minutes, observe the change.
- **Controlled variable exclusion test**: pick one model and task, remove instructions/feedback/state one at a time, measure drops, combine with failure-log analysis to rank marginal value.
- **Affordance analysis**: find cases where the agent "wants to do something but can't," and classify the gap as execution-based (doesn't know how) vs. evaluation-based (can't verify success).

## Related Pages

- [[Harness Engineering]]
- [[Controlled Variable Exclusion Test]]
- [[Capability Gap]]
- [[Codex]]
- [[Cursor]]
- [[AutoGPT]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
