---
title: "Lecture 03. Making the Repository the Single Source of Truth"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/"]
---

# Lecture 03. Making the Repository the Single Source of Truth

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Third in the series, following [[Lecture 02. What a Harness Actually Is]].

## Thesis

An agent can only access information from three sources: the system prompt, repository file contents, and tool execution output. Anything else — a Slack thread, a Confluence page, a teammate's memory — is invisible to it. As the lecture puts it: "information that doesn't exist in the repo, doesn't exist for the agent." The repo must therefore function as the authoritative specification document, not just a home for code — see [[System of Record]].

## Core Concepts

- **[[Knowledge Visibility Gap]]**: the portion of project knowledge that lives only in people's heads (or chat/wiki tools) instead of the repository. Every undocumented decision the team already knows is invisible to a fresh agent session.
- **[[System of Record]]**: the repo as final authority on decisions, architecture, execution state, and verification standards — not merely where the code happens to sit.
- **[[Fresh Session Test]]**: evaluate map completeness by starting a brand-new agent session and having it answer a small set of baseline questions using only repo contents. If it can't, the map has a hole.
- **Discovery Cost**: the context budget an agent burns searching for information that should have been immediately visible. A high discovery cost on a recurring question is a signal to document that answer once, in the repo.
- **Knowledge Decay Rate**: how quickly documentation drifts out of sync with the code it describes. Undocumented decay is worse than no documentation, because it actively misleads instead of just being silent.

## Recommended Repository Structure

- `AGENTS.md` at the repo root — project overview, commands, constraints.
- `ARCHITECTURE.md` per module directory — local design context near the code it describes.
- `CONSTRAINTS.md` — hard constraints called out on their own, not buried in prose.
- `PROGRESS.md` — status tracking (ties into [[Agent State Management]]).

## Four Principles for Effective Documentation

1. Knowledge should live adjacent to the code it describes.
2. Standardized entry files let a fresh agent orient quickly (echoes Lecture 02's "maps, not manuals").
3. Documentation should be minimal yet complete — a map, not an encyclopedia.
4. Knowledge updates must be synchronized with code changes, or Knowledge Decay Rate quietly rises.

## Managing Agent State with ACID Principles

The lecture borrows the database ACID model (distinct from the database concept — see [[ACID Transactions]] and [[Agent State ACID Principles]] for the mapping) to structure how agent progress/state should be persisted:

- **Atomicity**: one git commit per logical operation.
- **Consistency**: verification predicates that confirm the repo is actually in the state the agent claims.
- **Isolation**: separate progress files or branches so concurrent agent sessions don't race on the same state.
- **Durability**: critical knowledge is persisted in git-tracked files, not ephemeral session memory.

## Case Study

A 30-microservice e-commerce platform reduced agent task failure from 70% down to a much lower rate purely by centralizing scattered architectural knowledge into standardized repository documentation (`AGENTS.md`/`ARCHITECTURE.md`/`CONSTRAINTS.md`/`PROGRESS.md`) — a third concrete harness-improvement data point alongside Lecture 01's Anthropic/OpenAI case studies and Lecture 02's staged 20%→~100% rollout. See [[Capability Gap]].

## Exercises

- Run a fresh session test with a new agent instance against your own repo.
- Quantify your project's knowledge visibility gap.
- Score your current state management against the ACID framework above.

## Related Pages

- [[Harness Engineering]]
- [[Knowledge Visibility Gap]]
- [[System of Record]]
- [[Fresh Session Test]]
- [[Agent State ACID Principles]]
- [[Agent State Management]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 02. What a Harness Actually Is]]
