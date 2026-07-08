---
title: "Architectural Boundary Enforcement Rules"
type: concept
tags: [ai-agents, architecture, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# Architectural Boundary Enforcement Rules

Architectural boundary enforcement rules convert an architecture document into an executable check, rather than leaving a boundary as prose a developer or agent could silently violate. [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]] gives a concrete example: checking that a renderer process never directly calls a Node.js API, via a grep pattern that fails the build if a violation exists.

This applies the same logic as [[Harness Primitive]] (Lecture 08's "documents are for humans to read; primitives are for systems to execute") specifically to architecture rules: a boundary that's only documented can decay unnoticed, but a boundary enforced by a failing build cannot.

Boundaries need to be established before implementation begins, per [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification|Lecture 10]]'s citation of OpenAI's experience: agents copy whatever pattern already exists in a repository, so a weak or absent boundary at day one propagates. See [[Layered Domain Architecture]] for OpenAI's own concrete example of such a boundary. The guiding principle is the same one from Lecture 02: enforce invariants, don't micromanage implementation.

## Related

- [[Layered Domain Architecture]]
- [[Harness Primitive]]
- [[Three-Layer Termination Validation]]
- [[Harness Engineering]]
