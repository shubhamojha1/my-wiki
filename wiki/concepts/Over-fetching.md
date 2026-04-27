---
title: "Over-fetching"
type: concept
tags: [api, rest]
created: 2026-04-28
sources: ["algomaster-rest-vs-graphql"]
---

# Over-fetching

**Over-fetching** is when an API returns more data than the client needs.

## Example

- Request user profile
- Get full user object with 20 fields
- Client only needs name and email

## In REST

- Fixed response structure per endpoint
- All fields always returned

## In GraphQL

- Client specifies exact fields needed
- Eliminates over-fetching

## Related Concepts

- [[REST vs GraphQL]] — Parent concept
- [[REST API]] — Prone to over-fetching
- [[GraphQL]] — Solves over-fetching