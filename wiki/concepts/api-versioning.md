---
title: "API Versioning"
type: concept
tags: [api, rest, versioning]
created: 2026-07-10
sources: ["hellointerview-api-design"]
---

# API Versioning

Strategies for evolving an API's contract without breaking existing clients, by giving a request an explicit version identifier.

## Strategies

**URL versioning** — the version is part of the path: `/v1/events`, `/v2/events`. Explicit and immediately visible in logs, docs, and browser address bars; the most common default choice.

**Header versioning** — the version travels in a request header: `Accept-Version: v2`. Keeps URLs stable across versions (useful if the URL itself is treated as a durable resource identifier), but is less discoverable — a version isn't visible just from looking at the endpoint being called.

Other approaches exist in practice but weren't covered in the source for this page — query-parameter versioning (`?version=2`) and content negotiation via `Accept` media types are common variants of header-style versioning.

## Interview Guidance

URL versioning is the safer default to state in an interview: it's unambiguous and requires no follow-up explanation. Notably, many system design breakdowns skip versioning entirely, which suggests interviewers generally don't weight it heavily relative to resource modeling, protocol choice, and auth — worth mentioning briefly rather than dwelling on.

## Related Concepts

- [[REST API]] — the primary context where versioning strategy matters
- [[URI Naming Conventions]] — versioning is one convention among several for URL structure
