---
title: "Lecture 01. Strong Models Don't Mean Reliable Execution"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/"]
---

# Lecture 01. Strong Models Don't Mean Reliable Execution

Source: [[Learn Harness Engineering]] by [[Walking Labs]].

## Thesis

The lecture argues that model capability and agent reliability are different problems. Current coding agents achieve roughly 50-60% pass rates on benchmarks, but real-world performance drops further when the task specification is vague, the repository conventions are implicit, the environment is incomplete, verification is missing, or prior state is not preserved across sessions.

The practical conclusion is simple: "When things fail, don't swap the model first — check the harness." Map each failure to a specific layer instead of assuming insufficient model capability.

## Failure Modes

- Vague requirements: the model has to guess what "add a search feature" means in practice.
- Implicit conventions: rules live in human memory or old chat messages instead of the repo.
- Incomplete environment setup: dependency and toolchain issues consume context and attention.
- No verification path: the agent decides it is done without tests, lint, or type checks.
- Cross-session state loss: each run repeats discovery work and forgets prior decisions.

## Key Terms

- [[Capability Gap]]: benchmark scores can look good while real tasks still fail frequently.
- [[Harness Engineering]]: the surrounding system that makes a model usable for real work.
- [[Harness-Induced Failure]]: a good model fails because the execution environment is weak.
- [[Verification Gap]]: the difference between the agent's claim of completion and actual correctness.
- [[Diagnostic Loop]]: execute, observe, attribute, fix, rerun.
- [[Definition of Done]]: explicit criteria that can be checked by command.
- [[Context Anxiety]]: low-context behavior where the agent rushes to finish and skips validation.
- [[Agent State Management]]: preserving task progress, repo discoveries, and decisions across sessions.

## Case Studies

The lecture uses two examples to show that the same model can behave very differently under different harnesses.

Anthropic's experiment compares the same prompt and model, [[Claude Sonnet|Opus 4.5]], building a 2D game editor with and without a support harness. The bare run fails in about 20 minutes and produces no playable result. The harnessed run adds planner, generator, and evaluator roles, takes about 6 hours, and produces a working game editor. As the lecture puts it: "the same model produces fundamentally different output in a bare environment versus one with a complete harness."

OpenAI's harness engineering story is used as the opposite side of the same point. Three engineers generated roughly one million lines of code with [[Codex]] over five months by systematically developing the harness — not the model — around it: environment, task decomposition, and feedback loops. That turned an unreliable setup into a much more dependable one.

## Operational Guidance

- Attribute every failure to a specific layer instead of saying "the model is not good enough."
- Write the completion criteria before asking the agent to work.
- Put repo conventions, stack versions, and verification commands in the repository root — concretely, an `AGENTS.md` file documenting tech stack, architectural conventions, and verification commands. The lecture argues this single document is often more effective than upgrading to a more expensive model.
- Treat failures as signals that the harness has a defect.
- Keep a simple task log so repeated failures can be traced to the same layer.

## Related Pages

- [[Harness Engineering]]
- [[Capability Gap]]
- [[Harness-Induced Failure]]
- [[Verification Gap]]
- [[Diagnostic Loop]]
- [[Definition of Done]]
- [[Context Anxiety]]
- [[Agent State Management]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Anthropic]]
- [[OpenAI]]
- [[Codex]]
- [[Claude Sonnet]]
- [[SWE-bench]]
