---
title: "Inheritance"
type: concept
tags: [oop, pillars, code-reuse]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Inheritance

**Definition:** A mechanism where a new class (child/derived) derives from an existing class (parent/base), inheriting its fields and methods. The child can reuse, extend, or override inherited members.

## When to Use

Use when there's a clear **"is-a" relationship**:
- A `UserRegisteredEvent` **is a** `DomainEvent`
- A `StripeGateway` **is a** `PaymentGateway`

## Example: Domain Events

```java
public class DomainEvent {
    protected String eventId;
    protected String source;
    protected long timestamp;

    public DomainEvent(String source) {
        this.eventId = UUID.randomUUID().toString();
        this.source = source;
        this.timestamp = System.currentTimeMillis();
    }

    public String getEventId() { return eventId; }
    public long getTimestamp() { return timestamp; }
}

public class UserRegisteredEvent extends DomainEvent {
    private String userId;
    private String email;

    public UserRegisteredEvent(String userId, String email) {
        super("user-service");
        this.userId = userId;
        this.email = email;
    }

    public String getUserId() { return userId; }
}

public class OrderPlacedEvent extends DomainEvent {
    private String orderId;
    private double totalAmount;

    public OrderPlacedEvent(String orderId, double totalAmount) {
        super("order-service");
        this.orderId = orderId;
        this.totalAmount = totalAmount;
    }

    public String getOrderId() { return orderId; }
}
```

## Inheritance vs Composition

| Aspect | Inheritance | Composition |
|--------|-------------|-------------|
| Relationship | "Is-a" | "Has-a" |
| Coupling | Tight | Loose |
| Flexibility | Less flexible | More flexible |
| When to use | Clear hierarchy | Reuse without coupling |

## Warning

Avoid inheriting just to reuse code. If there's no natural "is-a" relationship, use **composition** instead.

## Related Concepts

[[Class]], [[Polymorphism]], [[Method Overriding]], [[Composition]]