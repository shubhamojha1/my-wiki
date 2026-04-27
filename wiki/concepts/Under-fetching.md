---
title: "Under-fetching"
type: concept
tags: [api, rest]
created: 2026-04-28
sources: ["algomaster-rest-vs-graphql"]
---

# Under-fetching

**Under-fetching** requires multiple API calls to get related data.

## n+1 Problem

- Fetch 1 user → then fetch each of their N posts
- Requires N+1 requests total

## In REST

- Each resource has its own endpoint
- Related data requires chained requests

## In GraphQL

- Single request can fetch nested data
- Solves n+1 problem

## Related Concepts

- [[REST vs GraphQL]] — Parent concept
- [[REST API]] — Prone to under-fetching
- [[GraphQL]] — Solves under-fetching