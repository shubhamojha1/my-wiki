---
title: "REST API"
type: concept
tags: [api, rest, http, architecture]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-api", "rest-api-design-best-practices"]
---

# REST API

**REST** (Representational State Transfer) is an architectural style for distributed hypermedia systems, defined by Roy Fielding in his 2000 dissertation. It describes six constraints that, when applied, make a system scalable, stateless, and independently evolvable.

## Six Constraints

1. **Client-Server** — UI and data storage concerns are separated; client and server evolve independently
2. **Stateless** — each request contains all information needed; server holds no client session state
3. **Cacheable** — responses declare cacheability; clients and proxies can reuse them
4. **Uniform Interface** — consistent resource identification, manipulation through representations, self-descriptive messages
5. **Layered System** — client cannot tell if it talks directly to the server or an intermediary (load balancer, CDN)
6. **Code on Demand** *(optional)* — server can send executable code to client (e.g., JavaScript)

## HTTP Methods

| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| `GET` | Retrieve resource | Yes | Yes |
| `POST` | Create resource | No | No |
| `PUT` | Replace resource | Yes | No |
| `PATCH` | Partial update | No | No |
| `DELETE` | Remove resource | Yes | No |
| `HEAD` | Get headers only | Yes | Yes |

**Idempotent** = calling N times has same effect as calling once. **Safe** = no side effects.

## Resource-Oriented URLs

Resources are nouns; actions come from HTTP methods:

```
GET    /users          → list users
GET    /users/42       → get user 42
POST   /users          → create user
PUT    /users/42       → replace user 42
PATCH  /users/42       → update user 42 partially
DELETE /users/42       → delete user 42

GET    /users/42/posts → posts belonging to user 42
```

## Status Codes

| Range | Meaning | Examples |
|-------|---------|---------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301 Moved Permanently, 304 Not Modified |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 404 Not Found, 409 Conflict, 429 Too Many Requests |
| 5xx | Server error | 500 Internal Server Error, 503 Service Unavailable |

## Strengths

- Leverages existing HTTP infrastructure (caching, proxies, CDNs)
- Wide tooling and client support
- Simple mental model for CRUD operations
- Statelessness enables horizontal scaling

## Weaknesses

- [[Over-fetching]] — endpoints return fixed structures regardless of what client needs
- [[Under-fetching]] — related data requires multiple round trips (N+1 problem)
- No standard for real-time; requires WebSockets or SSE alongside REST
- Versioning is ad-hoc (`/v1/`, headers, query params)

## Related Concepts

- [[HTTP]] — the protocol REST is built on
- [[GraphQL]] — alternative that eliminates over/under-fetching
- [[gRPC]] — binary alternative for internal service communication
- [[Over-fetching]] — structural weakness of REST
- [[Under-fetching]] — structural weakness of REST
- [[Idempotency]] — critical property for safe retries
- [[Rate Limiting]] — common REST API protection mechanism
- [[REST API Design Best Practices]] — conventions for clean REST design
