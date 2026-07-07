---
title: "Initialization Phase"
type: concept
tags: [ai-agents, project-setup, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/"]
---

# Initialization Phase

The initialization phase is a dedicated stage of work, separate from implementation, whose objective is reliability rather than feature output. Implementation maximizes the quantity and quality of features shipped; initialization maximizes how dependable the environment and process are for every session that follows. [[Lecture 06. Make the Agent Initialize Before Every Work Session]] argues these are opposing objectives — an agent trying to do both at once builds infrastructure carelessly (configured but unverified) and produces fewer, worse features in the process.

This is distinct from Lecture 05's [[Harness Initialization Flow]]: that's the lightweight clock-in/clock-out bookend around *every* session. The initialization phase described here is a one-time (or per-major-task) setup investment that happens *before* any of those sessions start.

## Unverified Accumulation

Unverified accumulation is the specific failure that results from skipping a dedicated initialization phase: code gets written before the testing infrastructure that should validate it actually exists. That code may need to be redesigned once real verification arrives and reveals problems it couldn't previously catch — so skipping initialization doesn't just delay cost, it can multiply it.

## What Initialization Should Produce

1. A runnable environment.
2. A verifiable test framework.
3. A [[Startup Readiness Checklist]] document.
4. A task breakdown with acceptance criteria.
5. A git checkpoint commit.

Starting from a project template outperforms starting from an empty directory, since it skips redundant setup work the template has already solved. Success is measured by whether later sessions can operate independently, and concretely by time-from-start-to-first-passing-test.

## Related

- [[Startup Readiness Checklist]]
- [[Harness Initialization Flow]]
- [[Rebuild Cost]]
- [[Harness Engineering]]
- [[Capability Gap]]
