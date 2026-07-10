---
title: "API Key"
type: concept
tags: [api, security, auth]
created: 2026-07-10
sources: ["hellointerview-api-design", "hellointerview-distributed-rate-limiter"]
---

# API Key

A randomly generated string used to identify and authenticate a calling application or developer, rather than an individual end user.

## Usage

```
GET /events
Authorization: Bearer sk_live_abc123...
```

Also commonly sent as a dedicated header such as `X-API-Key`.

## When to Use

- Server-to-server communication, where there's no human user session to represent.
- Third-party/external developer access to a public API, where the key identifies the integration or account, not a specific logged-in person.

API keys are opaque — the server must look them up (typically in a database or cache) to know what they grant, unlike a [[JWT]] which carries claims directly in the token itself.

## Related Concepts

- [[JWT]] — the alternative credential mechanism, used for user sessions rather than application identification
- [[Authentication vs. Authorization]] — an API key is an authentication mechanism; it doesn't by itself determine authorization
- [[Rate Limiting]] — API key is a common client-identification key for per-client rate limits
