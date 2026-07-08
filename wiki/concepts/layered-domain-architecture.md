---
title: "Layered Domain Architecture"
type: concept
tags: [ai-agents, architecture, openai, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# Layered Domain Architecture

Layered Domain Architecture is [[OpenAI]]'s concrete example of an [[Architectural Boundary Enforcement Rules|architectural boundary]] established up front, cited in [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]]: a fixed sequence of layers — Types → Config → Repo → Service → Runtime → UI — with dependencies allowed to run strictly forward and never backward.

OpenAI's stated reason for establishing this "on day one" rather than letting it emerge: agents copy whatever pattern already exists in a repository, so whatever boundary (or absence of one) is present early gets replicated at scale as the codebase grows. Once established, the boundary should be enforced executably (see [[Architectural Boundary Enforcement Rules]]) rather than left as a diagram or a paragraph in a doc — the same "enforce invariants, don't micromanage implementation" principle from Lecture 02's [[Harness Engineering]].

## Related

- [[Architectural Boundary Enforcement Rules]]
- [[OpenAI]]
- [[Codex]]
- [[Harness Engineering]]
