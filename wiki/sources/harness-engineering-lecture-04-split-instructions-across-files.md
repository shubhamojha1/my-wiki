---
title: "Lecture 04. Split Instructions Across Files"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/"]
---

# Lecture 04. Split Instructions Across Files

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Fourth in the series, following [[Lecture 03. Making the Repository the Single Source of Truth]].

## Thesis

Instruction files naturally grow from ~50 lines to 600+ over time because "add a rule" is the easiest response every time an agent fails at something. That growth is a vicious cycle, not harmless accumulation: it wastes context budget, buries the constraints that matter most, and erases the distinction between hard rules and soft preferences. The fix is architectural — split one giant file into a short [[Entry File]] plus focused topic documents — not just "write better instructions."

## The Vicious Cycle: Four Cascading Problems

1. **Context Budget Depletion**: a 600-line instruction file can cost 10,000-20,000 tokens — 8-15% of the available context window — before the agent has read a line of actual code. See [[Instruction Bloat]].
2. **[[Lost in the Middle]]**: citing Liu et al. (2023), LLMs use information in the middle of long texts markedly worse than information at the start or end. A security constraint sitting at line 300 of a 600-line file has a real chance of being ignored — not because the model is careless, but because of where it sits.
3. **Priority Conflicts**: every rule is formatted identically, so the agent has no way to tell "never use eval()" (hard constraint) from "prefer functional style" (guideline) apart from reading intent into prose. See [[Priority Clarity]] below.
4. **Maintenance Decay**: instruction files only grow, never shrink — outdated rules stick around because nobody is confident removing them is safe, so [[Instruction Signal-to-Noise Ratio|signal-to-noise ratio]] declines monotonically.

## Core Concepts

- **[[Instruction Bloat]]**: an instruction file occupying 10-15% of the context window, crowding out room for actual task reasoning.
- **[[Lost in the Middle]]**: the underlying attention-positioning effect (Liu et al. 2023) that makes mid-file content unreliable regardless of how important it is.
- **[[Instruction Signal-to-Noise Ratio]]**: the proportion of a file's instructions that are actually relevant to the current task; audits should track this, not just line count.
- **[[Entry File]]**: a short (50-200 line) document whose job is to route to detail, not contain it.
- **Reveal on Demand**: progressive disclosure — deeper documentation exists but is only pulled in when actually needed, rather than front-loaded into every session.
- **Priority Clarity**: the instruction file format itself should make non-negotiable constraints visually and structurally distinct from suggestions, rather than relying on prose tone.

## Recommended Architecture

**Entry file** contains only:
- A one- or two-sentence project overview.
- First-run commands (e.g. `make setup && make test`).
- A maximum of 15 global hard constraints.
- One-line links to topic documents, each with an applicability condition (when does this doc matter?).

**Topic documents** (50-150 lines each, in `docs/`) cover specific areas — API patterns, database rules, testing standards — pulled in only when relevant. Information that belongs in code (type definitions, interface comments) should live there, not be duplicated into prose instructions.

Every instruction, wherever it lives, should carry three things: its source, its applicability condition, and its expiry condition — so a regular audit can tell what's safe to delete. Critical constraints that must stay in the entry file should sit at the top or bottom, never buried in the middle, exploiting rather than fighting the Lost in the Middle effect.

## Case Study

A SaaS team cut a bloated 600-line instruction file down to an 80-line entry file plus topic documents. Task success rate rose from 45% to 72%, and security-constraint compliance rose from 60% to 95% — the first capability-gap data point in this series with a security-specific compliance metric, alongside Lecture 01's Anthropic/OpenAI examples, Lecture 02's staged 20%→~100% rollout, and Lecture 03's 30-microservice platform. See [[Capability Gap]].

## Related Pages

- [[Harness Engineering]]
- [[Instruction Bloat]]
- [[Lost in the Middle]]
- [[Instruction Signal-to-Noise Ratio]]
- [[Entry File]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 03. Making the Repository the Single Source of Truth]]
