---
title: "Definition of Done"
type: concept
tags: [ai-agents, testing, project-management]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# Definition of Done

A definition of done is a set of explicit acceptance criteria that can be checked by command or inspection.

In Lecture 01, a good definition of done includes the intended endpoint, behavior requirements, and the exact tests or checks that prove completion. Without that, the agent invents its own stopping rule.

[[Lecture 02. What a Harness Actually Is|Lecture 02]] operationalizes this as the [[Harness Engineering|Feedback Subsystem]]: list the actual verification commands in the repo's instruction file, e.g.

```
Verification commands:
- Tests: pytest tests/ -x
- Type check: mypy src/ --strict
- Lint: ruff check src/
- Full verification: make check (includes all above)
```

The lecture calls this subsystem typically the highest-ROI harness investment — cheap to write, and it directly closes the [[Verification Gap]].

## Related

- [[Harness Engineering]]
- [[Verification Gap]]
- [[Diagnostic Loop]]
