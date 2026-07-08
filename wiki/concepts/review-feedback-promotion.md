---
title: "Review Feedback Promotion"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# Review Feedback Promotion

Review feedback promotion is the practice of converting a recurring human code-review comment into a permanent automated check — an [[Architectural Boundary Enforcement Rules|architectural rule]], a new end-to-end test scenario, or a lint rule, depending on what actually catches the class of defect being flagged. [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]] frames this as how a harness gets measurably stronger over time: instead of a reviewer catching the same mistake repeatedly across sessions, the second occurrence gets automated so it can never recur silently.

This closes the loop between human review and machine-enforced verification — it's the mechanism by which lessons learned in review become part of the [[Three-Layer Termination Validation]] the harness runs on every subsequent task, rather than tacit knowledge that lives only in a reviewer's memory (echoing the [[Knowledge Visibility Gap]] from Lecture 03).

## Related

- [[Architectural Boundary Enforcement Rules]]
- [[Three-Layer Termination Validation]]
- [[Knowledge Visibility Gap]]
- [[Harness Engineering]]
