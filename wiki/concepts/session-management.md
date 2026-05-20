---
title: "Session Management"
type: concept
tags: [caching, web, session, state-management]
created: 2026-05-08
updated: 2026-05-20
sources: ["https://aws.amazon.com/caching/"]
---

# Session Management

**Session management** tracks user state (authentication, preferences, shopping cart) across multiple HTTP requests. Because HTTP is stateless, sessions require an external mechanism to persist state between requests.

## The Problem with Server-Side Local Sessions

If each server stores sessions in local memory:
```
Request 1 → Server A → session created in Server A's memory
Request 2 → Server B (load balancer routes differently) → session not found → user logged out
```

Horizontal scaling or server restarts destroy sessions. A centralized store fixes this.

## Session Storage Patterns

### 1. Server-Side Session (Centralized Store)

```
Client → Load Balancer → Any Server
                             │
                             └─ session_id → Redis/DB [{"user_id":1001, "cart":[...]}]
```

Server-side advantages:
- Session data not exposed to client
- Can store large amounts of data
- Easy to invalidate (delete from store)

### 2. Client-Side Session (JWT / Cookie)

```
Client stores the session data (encrypted/signed) in a cookie or JWT:
  { "user_id": 1001, "role": "admin", "exp": 1716400000 }
  → signed with server secret → tamper-evident

Server decodes on every request (no storage needed).
```

Client-side advantages:
- Stateless — no session store needed
- Works well for horizontal scaling
- Disadvantage: cannot invalidate before expiry; size-limited

## Implementation Options

| Store | Best For | Notes |
|-------|----------|-------|
| **Redis** | High throughput, TTL-based expiry | In-memory; optionally persistent; atomic operations |
| **Memcached** | Simple cache; no persistence needed | Faster than Redis for pure caching; no TTL per field |
| **Relational DB** | Durable sessions with complex queries | Slower; good for compliance/audit |
| **JWT (stateless)** | Microservices, API tokens | No server-side storage; cannot revoke |

## Session Lifecycle

```
Login:     server creates session → generates session_id → stores {user_id, ...} in Redis
           → sets cookie: session_id=abc123 (HttpOnly, Secure)

Request:   client sends cookie → server looks up session_id in Redis → finds user state

Logout:    server deletes session_id from Redis → cookie cleared
           (contrast: JWT cannot be "deleted" — must wait for expiry or use a denylist)

Expiry:    Redis TTL auto-expires inactive sessions (e.g., 30 minutes idle)
```

## Security Considerations

| Risk | Mitigation |
|------|-----------|
| Session hijacking | HttpOnly + Secure cookie flags; short TTL |
| CSRF attacks | SameSite=Strict cookie; CSRF tokens |
| Fixation attacks | Rotate session ID after login |
| JWT not revokable | Use short expiry + refresh token rotation |

## Related Concepts

- [[Caching]] — the general caching pattern session stores leverage
- [[Redis]] — most popular session store
- [[Idempotency Key]] — different from session; tracks per-operation state
- [[OSI Layer 5: Session]] — the OSI concept of connection sessions (different from HTTP sessions)
