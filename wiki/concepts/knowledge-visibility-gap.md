---
title: "Knowledge Visibility Gap"
type: concept
tags: [ai-agents, documentation, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/"]
---

# Knowledge Visibility Gap

The knowledge visibility gap is the portion of project knowledge that exists only in people's heads, chat tools, or wikis outside the repository — rather than in the repository itself. An agent can only see system prompts, repo file contents, and tool output; anything sitting only in a Slack thread or a teammate's memory does not exist for it.

Every undocumented team decision widens this gap and shows up later as an agent guessing wrong or re-deriving something the team already settled. Closing the gap means moving that knowledge into the [[System of Record]] rather than assuming an agent will infer it.

## Related

- [[System of Record]]
- [[Fresh Session Test]]
- [[Harness Engineering]]
- [[Capability Gap]]
