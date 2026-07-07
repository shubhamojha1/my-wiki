---
title: "Fresh Session Test"
type: concept
tags: [ai-agents, evaluation, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/"]
---

# Fresh Session Test

A fresh session test evaluates whether a repository's documentation map is actually complete: start a brand-new agent session with no prior conversation history, and have it answer a small set of baseline questions using only what's in the repo. If it can't answer correctly, that information is missing from the [[System of Record]] regardless of whether the team believes it's documented.

This is a cheap, repeatable diagnostic — it directly measures the [[Knowledge Visibility Gap]] rather than assuming documentation is good because it exists. It pairs naturally with [[Controlled Variable Exclusion Test]]: the exclusion test tells you which harness subsystem matters most, and the fresh session test tells you whether the Instruction Subsystem you already have is actually sufficient.

## Related

- [[Knowledge Visibility Gap]]
- [[System of Record]]
- [[Controlled Variable Exclusion Test]]
- [[Harness Engineering]]
