---
title: "State Machine"
type: concept
tags: [lld, design, state-transitions]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/enums"]
---

# State Machine

**Definition:** A model of computation where a system can be in one of a finite number of states, and transitions between states occur based on specific inputs/events.

## Order Processing as State Machine

```
┌─────────┐   advance   ┌───────────┐   advance   ┌────────┐   advance   ┌───────────┐
│ PLACED  │ ──────────▶ │ CONFIRMED │ ──────────▶ │ SHIPPED│ ──────────▶ │ DELIVERED │
└─────────┘             └───────────┘             └────────┘             └───────────┘
      │
      │ cancel (if not shipped)
      ▼
┌───────────┐
│ CANCELLED │
└───────────┘
```

## Implementing with Enum

```java
public enum OrderStatus {
    PLACED,       // Initial state
    CONFIRMED,    // Payment verified
    SHIPPED,      // In transit
    DELIVERED,    // Completed
    CANCELLED     // Terminal state
}
```

## Enforcing Valid Transitions

```java
public boolean advanceStatus() {
    switch (status) {
        case PLACED:    status = OrderStatus.CONFIRMED; break;
        case CONFIRMED: status = OrderStatus.SHIPPED; break;
        case SHIPPED:   status = OrderStatus.DELIVERED; break;
        default: return false;  // Can't advance from terminal states
    }
    return true;
}

public boolean cancel() {
    if (status == OrderStatus.SHIPPED || status == OrderStatus.DELIVERED) {
        return false;  // Cancellation not allowed
    }
    status = OrderStatus.CANCELLED;
    return true;
}
```

## Benefits of State Machine Pattern

1. **Explicit valid states** — Enum shows all possible states
2. **Explicit transitions** — Switch statements document valid moves
3. **Impossible states eliminated** — Invalid combinations prevented
4. **Easy to extend** — Add states and update transitions in one place

## Related Concepts

[[Enum]], [[State Pattern]], [[Finite State Machine]]