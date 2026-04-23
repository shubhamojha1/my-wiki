---
title: "Enum"
type: concept
tags: [lld, oop, type-safety]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/enums"]
---

# Enum

**Definition:** A fixed set of named constants that defines a type with a limited number of possible values. Enums bring compile-time type safety to domain concepts.

## Why Use Enums?

| Without Enum | With Enum |
|--------------|-----------|
| `String status = "placed"` | `OrderStatus status = PLACED` |
| Typos cause runtime errors | Compiler catches invalid values |
| No IDE autocomplete | Full autocomplete support |
| Hard to discover valid values | All valid values documented |

## Simple Enum

```java
public enum OrderStatus {
    PLACED,
    CONFIRMED,
    SHIPPED,
    DELIVERED,
    CANCELLED
}

// Usage
OrderStatus currentStatus = OrderStatus.PLACED;
```

## Enum with Properties

Enums can hold data and behavior:

```java
public enum PaymentMethod {
    CREDIT_CARD("Credit Card", 2.5),
    DEBIT_CARD("Debit Card", 1.0),
    UPI("UPI", 0.0),
    CASH_ON_DELIVERY("Cash on Delivery", 3.0);

    private final String displayName;
    private final double feePercentage;

    PaymentMethod(String displayName, double feePercentage) {
        this.displayName = displayName;
        this.feePercentage = feePercentage;
    }

    public String getDisplayName() {
        return displayName;
    }

    public double getFee(double amount) {
        return (amount * feePercentage) / 100.0;
    }
}
```

## Enum as State Machine

Enums combined with switch statements enforce valid transitions:

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
```

## Benefits

1. **Type safety** — Only valid values accepted
2. **Self-documenting** — All valid values visible
3. **IDE support** — Autocomplete, refactoring
4. **Comparable** — Can compare with `==`
5. **Extensible** — Add values without breaking existing code

## Language Support

| Language | Syntax |
|----------|--------|
| Java | `enum OrderStatus { PLACED, CONFIRMED }` |
| Python | `class OrderStatus(enum.Enum): PLACED = "placed"` |
| TypeScript | `enum OrderStatus { Placed, Confirmed }` |
| C# | `enum OrderStatus { Placed, Confirmed }` |

## Related Concepts

[[Type Safety]], [[State Machine]], [[Class]], [[Constants]]