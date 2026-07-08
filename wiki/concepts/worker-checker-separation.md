---
title: "Worker/Checker Separation"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Worker/Checker Separation

Worker/checker separation is the fix [[Lecture 09. Preventing Agents from Declaring Victory Too Early]] proposes for self-evaluation's [[Confidence Calibration Bias]]: don't let the agent that did the work also be the one that judges whether it's done. An independent evaluator agent, deliberately tuned to be critical, catches problems that self-evaluation systematically misses.

This reuses the same experiment already documented in this wiki from [[Lecture 01. Strong Models Don't Mean Reliable Execution|Lecture 01]] — same model (Opus 4.5), same 2D retro game editor task, comparing a bare single-agent run against a three-agent harness (planner + generator + evaluator) — but Lecture 09 supplies concrete cost/time figures for the first time:

| Configuration | Time | Cost | Result |
|---|---|---|---|
| Single agent (bare) | 20 minutes | $9 | Core features not working |
| Three agents (planner + generator + evaluator) | 6 hours | $200 | Core features working |

The harnessed version cost roughly 22x more and took 18x longer — and was the only one that actually worked. See [[Harness-Induced Failure]] and [[Anthropic]] for where this case study is otherwise documented.

Worker/checker separation on its own only establishes that the checker is *independent* — it doesn't establish that the checker's judgment is *reliable*. [[Lecture 11. Making the Agent's Runtime Observable|Lecture 11]] supplies the missing mechanism: an [[Evaluator Rubric]] with quantifiable dimensions and explicit thresholds, so evaluation becomes evidence-based scoring rather than just a second, differently-biased opinion. Lecture 11's separate Anthropic DAW experiment (a distinct case study from the one above — see [[Anthropic]]) shows this directly: early evaluator versions dismissed real issues until the rubric/prompts were refined against cases where evaluator judgment diverged from human judgment.

## Related

- [[Confidence Calibration Bias]]
- [[Harness-Induced Failure]]
- [[Anthropic]]
- [[Three-Layer Termination Validation]]
- [[Evaluator Rubric]]
- [[Layered Observability]]
