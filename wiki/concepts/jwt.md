---
title: "JWT"
type: concept
tags: [api, security, auth]
created: 2026-07-10
sources: ["hellointerview-api-design", "hellointerview-distributed-rate-limiter"]
---

# JWT

**JWT** (JSON Web Token) is a credential format that encodes identity claims directly into the token itself, cryptographically signed with a secret (or key pair) so a recipient can verify it wasn't tampered with.

## Structure

A JWT payload carries claims like:

```json
{
  "user_id": "123",
  "email": "john@example.com",
  "role": "customer",
  "exp": 1640995200
}
```

## Why It Fits Distributed Systems

Because the token is self-contained and signed, any service holding the verification key can validate it independently — no round trip to a central session store is required. This makes JWTs a natural fit for stateless, horizontally scaled backends (see [[Stateless Architecture]]), unlike traditional server-side session IDs that require a shared session store (see [[Session Management]]).

## When to Use

User sessions in web and mobile applications where stateless authentication matters — trading a small amount of token size and revocation complexity (a compromised JWT is valid until `exp`, since there's no central store to invalidate it early without extra infrastructure) for the ability to verify identity anywhere without a database lookup.

## Related Concepts

- [[API Key]] — the alternative credential mechanism, for application/service identification rather than user sessions
- [[Authentication vs. Authorization]] — a JWT authenticates identity; the `role`/claims inside it commonly feed an [[RBAC]] authorization check
- [[Stateless Architecture]] — the architectural style JWTs are designed to support
- [[Session Management]] — the stateful alternative JWTs avoid
