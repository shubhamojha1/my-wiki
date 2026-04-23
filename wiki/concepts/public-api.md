---
title: "Public API"
type: concept
tags: [software-design, interface, boundaries]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/abstraction"]
---

# Public API

**Definition:** The set of public methods and types that external consumers can use. It's the contract between your code and its users, hiding internal complexity behind a clean interface.

## What Makes a Good API

1. **Simple** — Fewest possible methods
2. **Consistent** — Predictable naming and behavior
3. **Documented** — Clear contracts
4. **Stable** — Changes rarely break callers

## Example: Payment Gateway API

```java
// Good API - simple, focused
public class PaymentGateway {
    public PaymentResult charge(String customerId, double amount) {
        // HTTP setup, retry logic, logging, fraud checks hidden
        return new PaymentResult(true, "txn_123");
    }

    public PaymentResult refund(String transactionId) {
        // Complexity hidden inside
        return new PaymentResult(true, transactionId);
    }
}

// Caller doesn't know about any of this:
/*
 - HTTP client initialization
 - Authentication tokens
 - Request retry logic
 - Error handling
 - Logging
 - Webhook callbacks
*/
```

## API Design Principles

| Principle | Description |
|-----------|-------------|
| Hide internals | Don't expose implementation details |
| Minimal interface | Only expose what's needed |
| Stable contracts | Don't break existing callers |
| Fail fast | Clear error messages |

## API vs Implementation

```
┌─────────────────────────────────┐
│        External Caller          │
└──────────────┬──────────────────┘
               │ knows only this
               ▼
┌─────────────────────────────────┐
│         Public API               │  ← Simple interface
│   charge(), refund(), etc.       │
└──────────────┬──────────────────┘
               │ hides
               ▼
┌─────────────────────────────────┐
│       Implementation             │  ← Can change anytime
│   HTTP, retries, caching, etc.   │
└─────────────────────────────────┘
```

## Related Concepts

[[Interface]], [[Abstraction]], [[Encapsulation]], [[SemVer]]