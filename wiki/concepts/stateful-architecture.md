---
title: "Stateful Architecture"
type: concept
tags: [architecture, stateful, sessions, state]
created: 2026-05-12
sources: ["stateful-vs-stateless-architecture"]
---

# Stateful Architecture

A system design where the server retains client or process data (state) across multiple requests. State information — sessions, preferences, cart contents, auth tokens — persists between interactions so the client doesn't resend everything each time.

## Common Patterns

### Sticky Sessions
Load balancer pins a client to a specific server after the first request, using in-memory session storage on that server.

**Trade-off**: Simple but creates a [[Single Point of Failure]] — if the server fails, the user's session data is lost. Inflexible for scaling (can't redistribute traffic).

### Centralized Session Store
Session data lives in an external shared store (e.g., [[Redis]]). Any server can handle any request by reading/writing to the shared store.

**Trade-off**: Network overhead per request, external dependency — if the store fails, all sessions are lost without a fallback.

## Advantages
- **Personalized experiences** — remembers user preferences and history
- **Contextual continuity** — users resume where they left off after disconnect
- **Reduced round trips** — less data sent per request since server already knows context

## Challenges
- **Scalability** — session data must be replicated or centralized, adding complexity
- **Failure points** — server failure loses in-memory sessions (without centralized store)
- **Complexity** — synchronizing state across multiple servers requires external infrastructure

## Use Cases
- E-commerce shopping carts (persist across page navigation)
- Video streaming (Netflix: watch progress, recommendations)
- Messaging apps (WhatsApp, Slack: active sessions, message history)

## Related
- [[Stateless Architecture]] — The contrasting design
- [[Session Management]] — Techniques for handling state at scale
- [[Redis]] — Common centralized session store
- [[System Design Trade-Offs]] — Trade-off #10: Stateful vs Stateless
