---
title: "Instruction Signal-to-Noise Ratio"
type: concept
tags: [ai-agents, documentation, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/"]
---

# Instruction Signal-to-Noise Ratio

Instruction signal-to-noise ratio (SNR) is the proportion of an instruction file's content that is actually relevant to the task at hand. It's a sharper audit metric than raw line count: a 200-line file where 190 lines apply to the current task has better SNR than an 80-line file where only 20 lines are relevant.

[[Instruction Bloat|Bloat]] drives SNR down over time — every added rule that no longer applies, or applies only to a case the agent isn't handling right now, is noise. [[Lecture 04. Split Instructions Across Files]] recommends regular audits: every instruction should carry its source, its applicability condition, and its expiry condition, so a reviewer can tell what's safe to delete instead of leaving it in "just in case."

The [[Entry File]] / topic-document split is partly an SNR strategy: keeping only universally-relevant content in the entry file, and pushing conditionally-relevant content into topic docs pulled in only when applicable, raises the effective SNR of whatever the agent actually reads in a given session.

## Related

- [[Instruction Bloat]]
- [[Entry File]]
- [[Lost in the Middle]]
- [[Harness Engineering]]
