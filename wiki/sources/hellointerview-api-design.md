---
title: "API Design for System Design Interviews"
type: source
tags: [system-design, api, rest, graphql, grpc, interview]
created: 2026-07-10
sources: ["https://www.hellointerview.com/learn/system-design/core-concepts/api-design"]
---

# API Design for System Design Interviews

Source: [[Hello Interview]] core-concepts guide.

## Framing

The article treats API design as one phase of a system design interview's delivery framework — roughly a 5-minute step where a candidate shows engineering judgment rather than produces a perfect specification. It repeatedly warns against over-investing here: candidates more often spend too long on API design than too little, at the expense of bigger architectural questions later in the interview.

## Protocol Choice

Three protocols cover most interview scenarios:

- **[[REST API]]** — the default. Standard HTTP methods over resource URLs; maps naturally onto database operations and HTTP semantics.
- **[[GraphQL]]** — a single endpoint with a client-specified query shape, chosen specifically when different clients ([[Over-fetching|over]]-/[[Under-fetching|under]]-fetching) need different data shapes, or when an interviewer raises that problem directly. The article names the N+1 problem as GraphQL's biggest gotcha, solved via Dataloader-style batching.
- **[[gRPC]]** — action/procedure-oriented, Protocol-Buffer-typed, used for internal service-to-service calls where performance and type safety matter. The article's interview guidance: outline the user-facing API (usually REST) and only mention gRPC for internal communication if time allows.

## REST Details Beyond What's Already Covered

Two resource-modeling rules not previously captured in [[REST API]]:

- Nest resources when the parent-child relationship is required: `GET /events/{id}/tickets`.
- Keep resources flat with query parameters when the relationship is optional: `GET /tickets?event_id=123&section=VIP`.

Three ways data reaches an API, given as a single worked example (`POST /events/123/bookings?notify=true`): **path parameters** identify a specific resource, **query parameters** filter/sort/modify retrieval, **request body** carries the actual payload for creates/updates.

## New Ground: Pagination Strategies

The article contrasts two pagination approaches in more depth than this wiki had:

- Offset-based (`?offset=20&limit=10`): intuitive, but unstable under concurrent writes — new records can shift results, causing duplicates or skips.
- [[Cursor-Based Pagination]] (`?cursor=<token>&limit=10`, response includes a `next_cursor`): stable under real-time data, but harder to support "jump to page N" navigation.

Interview guidance: offset-based is fine by default; reach for cursor-based specifically under high-volume or real-time scenarios.

## New Ground: API Versioning

Two strategies, neither previously documented in this wiki:

- **URL versioning** (`/v1/events`, `/v2/events`) — explicit, easy to understand, the article's recommended default for interviews.
- **Header versioning** (`Accept-Version: v2`) — keeps URLs clean but is less discoverable.

The article notes many system design breakdowns skip versioning entirely, suggesting interviewers don't weight it heavily — a useful interview-triage signal alongside the "don't over-invest" framing above.

## New Ground: Authentication, Authorization, and Rate Limiting

- **[[Authentication vs. Authorization]]** — the article's core distinction: authentication verifies identity, authorization verifies permission. Both checks are required together (valid token *and* ownership/role).
- **[[API Key]]** vs **[[JWT]]** as the two credential mechanisms it names: API keys for server-to-server and third-party developer access; JWTs for stateless user sessions, since any service holding the verification key can validate a JWT independently — a natural fit for distributed systems.
- **[[RBAC]]** — roles (customer / venue manager / admin in the article's ticketing example) map to permission sets, checked alongside authentication on every request.
- Rate limiting is covered at a level this wiki's existing [[Rate Limiting]] page already exceeds — the article's guidance (per-user/per-IP/per-endpoint limits, `429` on exceedance) adds nothing new here.

## Related Pages

- [[REST API]]
- [[GraphQL]]
- [[gRPC]]
- [[Over-fetching]]
- [[Under-fetching]]
- [[Page Pagination]]
- [[Cursor-Based Pagination]]
- [[API Versioning]]
- [[Authentication vs. Authorization]]
- [[API Key]]
- [[JWT]]
- [[RBAC]]
- [[Rate Limiting]]
- [[Hello Interview]]
