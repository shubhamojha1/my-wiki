---
title: "Authentication vs. Authorization"
type: concept
tags: [api, security, auth]
created: 2026-07-10
sources: ["hellointerview-api-design"]
---

# Authentication vs. Authorization

Two distinct checks that APIs perform on every protected request, frequently confused because both gate access:

- **Authentication** — verifies *identity*: proving a user or service is who it claims to be. Typically done once per session/request via a credential such as an [[API Key]] or [[JWT]].
- **Authorization** — verifies *permission*: given a known identity, checking whether that identity is allowed to perform the specific requested action on the specific requested resource.

## Why Both Are Required

A request can be authenticated (valid token, known user) but still unauthorized (that user doesn't own the resource, or lacks the required role). Checking only authentication would let any logged-in user act on any other user's data. A correct request handler checks both: is the token valid, and does this identity have the rights this action requires.

## How Authorization Is Typically Structured

The common pattern is [[RBAC]] — assign roles to users and permission sets to roles, then check role membership (or specific resource ownership, e.g. "owns this booking") at request time.

## Related Concepts

- [[API Key]] — one authentication mechanism
- [[JWT]] — another authentication mechanism, carrying identity claims directly in the token
- [[RBAC]] — the common structure for authorization decisions
- [[API Gateway]] — often the layer where authentication is enforced before a request reaches backend services
