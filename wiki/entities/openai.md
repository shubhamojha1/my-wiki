---
title: "OpenAI"
type: entity
tags: [organization, ai-research, machine-learning]
created: 2026-04-05
sources: ["Language Models are Few-Shot Learners.pdf", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# OpenAI

An AI research and deployment company, co-founded in 2015 by Elon Musk, Sam Altman, and others. Known for GPT-3, GPT-4, Codex, and the ChatGPT product.

## History

Founded as a nonprofit, later pivoted to a "capped profit" structure to attract investment. Built GPT-3 in 2020, followed by GPT-3.5, GPT-4, and various other AI systems.

## Key Contributions

- GPT family of language models
- DALL-E image generation
- Whisper speech recognition
- Codex code generation
- ChatGPT consumer product

## GPT-3 Development

OpenAI trained GPT-3 on Azure supercomputers, using large-scale compute to scale transformer models to unprecedented sizes. Released via API in 2021.

## Harness Engineering

Lecture 01 uses OpenAI's 2025 harness engineering article as evidence that agent reliability depends on more than model weights. In the million-line repo experiment, the important change was the harness around [[Codex]]: smaller tasks, clearer repository conventions, and stronger verification loops.

[[Lecture 10. Only a Full Pipeline Run Counts as Real Verification|Lecture 10]] cites OpenAI's experience again for a specific architectural lesson: establish boundaries "on day one," since agents copy whatever pattern already exists in a repository. Their concrete example is a [[Layered Domain Architecture]] (Types → Config → Repo → Service → Runtime → UI, strictly forward dependencies), enforced executably rather than left as documentation — see [[Architectural Boundary Enforcement Rules]].

## Related

- [[GPT-3]] - Their landmark language model
- [[GPT-3 Paper]] - The original research paper
- [[Codex]]
- [[Harness Engineering]]
- [[Layered Domain Architecture]]
- [[Architectural Boundary Enforcement Rules]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]]
