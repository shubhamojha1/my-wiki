---
title: "Lecture 09. Preventing Agents from Declaring Victory Too Early"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Lecture 09. Preventing Agents from Declaring Victory Too Early

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Ninth in the series, following [[Lecture 08. Use Feature Lists to Constrain What the Agent Does]].

## Thesis

An agent implements password reset — modifies the database, writes the endpoint, adds an email template, runs unit tests, all pass — and declares completion. The actual system is broken: the email service config is missing, the DB migration left the schema inconsistent, and the end-to-end flow was never actually run. Modern neural networks are systematically overconfident (Guo et al., ICML 2017), and coding agents inherit the same bias — feeling "done" while remaining far from it. See [[Premature Completion Declaration]].

This sharpens the wiki's existing [[Verification Gap]]: the agent isn't lying or being lazy, it's judging completion from local code-level confidence (syntax looks right, logic seems reasonable) when system-level correctness requires global, executed verification.

## The Slippery Slope

Premature completion follows a predictable pattern: syntax looks correct, logic seems reasonable, static analysis is clean — and the harness stops there because it lacks comprehensive execution verification. Unit tests run but integration tests get skipped; tests get checked but not coverage. "The code looks fine" quietly substitutes for "the feature is complete."

## Passing Unit Tests ≠ Task Complete

Unit tests isolate units and mock dependencies, which makes them structurally unable to catch cross-component problems:

1. **Interface mismatch**: a renderer passes a relative file path; a preload script expects an absolute one. Mocked unit tests pass; the mismatch only surfaces end-to-end.
2. **State propagation errors**: a DB migration changes a table schema, but an ORM caching layer still holds old schema entries. Fresh mock environments in unit tests never see this cross-layer inconsistency.
3. **Environment dependency**: code behaves correctly in the test environment but fails in the real one — config differences, network latency, service unavailability.

## Refactoring While We're at It

Agents frequently start refactoring, optimizing, or polishing style before core functionality has actually passed verification. This moves the boundary between verified and unverified code and risks breaking paths that were previously working — premature optimization becomes a new source of risk rather than an improvement. See [[Completion Priority Constraint]].

## Confidence Calibration Bias and Worker/Checker Separation

Guo et al. (ICML 2017) proved neural networks are systematically miscalibrated — confident beyond their actual accuracy. Anthropic's 2026 research found the same pattern in self-evaluation specifically: agents asked to grade their own work give systematically inflated assessments, worse for subjective tasks, even where a human observer would call the result substandard. See [[Confidence Calibration Bias]].

The fix is [[Worker/Checker Separation]]: an independent evaluator agent, tuned to be critical, catches what self-evaluation misses. This reuses the same experiment already in this wiki from [[Lecture 01. Strong Models Don't Mean Reliable Execution|Lecture 01]] — same model (Opus 4.5), same 2D retro game editor task — but this lecture supplies the concrete numbers for the first time: a single bare-run agent took 20 minutes and $9, with core features not working; three agents (planner + generator + evaluator) took 6 hours and $200, with core features working. See [[Harness-Induced Failure]] and [[Anthropic]], both updated with these figures.

## Three-Layer Termination Validation

The concrete fix for premature completion is a layered check, none of which can be skipped:

- **Layer 1 — Syntax and Static Analysis**: cheapest, least informative, but mandatory. Get the spelling right before reading further.
- **Layer 2 — Runtime Behavior Verification**: the app actually starts, critical paths execute. Core evidence that the feature is *runnable*, not just written.
- **Layer 3 — System-Level Confirmation**: end-to-end testing, integration validation, real user-scenario simulation. The last line of defense — proof the feature is *correct*, not just runnable.

See [[Three-Layer Termination Validation]]. This also encompasses the **Verification-Validation Dual Gate** (spec-correctness layer, then end-to-end-requirements layer, both must pass — see [[Verification-Validation Dual Gate]]) and OpenAI's pattern of actionable error feedback: instead of "Test failed," give the agent something like "Test failed: POST /api/reset-password returned 500. Check that the email service config exists in environment variables. The template file should be at templates/reset-email.html" — specific enough to self-correct from.

## Runtime Feedback Signals

Objective signals for judging real completion: the application started and reached a ready state, critical feature paths executed successfully at runtime, database writes/file operations/side effects are correct, and temporary resources got cleaned up. These are what feed Layer 2 and Layer 3 of the termination validation above.

## Case Study

The password-reset scenario itself: unit tests all passed, agent declared done, but the end-to-end flow was never run, the DB migration left an inconsistent schema, and email config was missing from the target environment. Enforcing three-layer termination validation — start the full app, run the complete reset flow, verify DB state — caught all three defects within the session, saving an estimated 5-10x the cost of fixing them post-hoc. A ninth capability-gap data point. See [[Capability Gap]].

## Related Pages

- [[Harness Engineering]]
- [[Verification Gap]]
- [[Premature Completion Declaration]]
- [[Confidence Calibration Bias]]
- [[Worker/Checker Separation]]
- [[Three-Layer Termination Validation]]
- [[Verification-Validation Dual Gate]]
- [[Completion Priority Constraint]]
- [[Harness-Induced Failure]]
- [[Anthropic]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 08. Use Feature Lists to Constrain What the Agent Does]]
