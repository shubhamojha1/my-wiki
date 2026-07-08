---
title: "Anthropic"
type: entity
tags: [organization, ai-research, machine-learning]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Anthropic

Anthropic is an AI company whose models and research are cited repeatedly across the [[Learn Harness Engineering]] series as evidence that harness quality can dominate agent performance.

Lecture 01 cites a controlled experiment where the same model and prompt were run twice. The weak setup failed quickly. The stronger setup added planner, generator, and evaluator roles and produced a working result.

[[Lecture 06. Make the Agent Initialize Before Every Work Session|Lecture 06]] cites Anthropic's long-running application development research directly: projects using a dedicated [[Initialization Phase]] showed 31% higher feature completion rates in multi-session scenarios than projects mixing setup and implementation.

[[Lecture 07. Draw Clear Task Boundaries for Agents|Lecture 07]] cites Anthropic again: agents using a "small next step" strategy show a 37% higher task completion rate than agents given broad prompts — the research basis for [[WIP Limit|WIP=1]]. See [[Overreach and Under-finish]].

[[Lecture 09. Preventing Agents from Declaring Victory Too Early|Lecture 09]] revisits Lecture 01's planner/generator/evaluator experiment with concrete figures for the first time: a bare single agent took 20 minutes and $9 (core features not working); three agents took 6 hours and $200 (core features working). It also cites Anthropic's 2026 research on self-evaluation bias — agents grading their own work give systematically inflated assessments — as the basis for [[Worker/Checker Separation]]. See [[Confidence Calibration Bias]].

[[Lecture 11. Making the Agent's Runtime Observable|Lecture 11]] documents a **separate, distinct** Anthropic experiment (March 2026, not the same one as above): a three-agent (planner/generator/evaluator) build of a browser-based DAW using the Web Audio API. Total cost across three build/QA rounds: 3 hours 50 minutes, $124.70. Anthropic is also cited here for the observation that incomplete work handed to a new session costs 30-50% of that session's time on redundant re-diagnosis — see [[Layered Observability]] and [[Sprint Contract]].

## Related

- [[Claude Sonnet]]
- [[Harness-Induced Failure]]
- [[Harness Engineering]]
- [[Initialization Phase]]
- [[Overreach and Under-finish]]
- [[Worker/Checker Separation]]
- [[Confidence Calibration Bias]]
- [[Layered Observability]]
- [[Sprint Contract]]
- [[Evaluator Rubric]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 06. Make the Agent Initialize Before Every Work Session]]
- [[Lecture 07. Draw Clear Task Boundaries for Agents]]
- [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]
- [[Lecture 11. Making the Agent's Runtime Observable]]
