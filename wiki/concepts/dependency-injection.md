---
title: "Dependency Injection"
type: concept
tags: [design-pattern, oop, inversion-of-control]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/dependency-injection"]
---

# Dependency Injection (DI)

**Definition:** A design pattern where a class receives its dependencies from external sources (typically constructor) rather than creating them internally. Inverts control of dependency creation.

## The Problem: Tight Coupling

```java
public class OrderService {
    private PaymentGateway gateway;
    
    public OrderService() {
        // Tightly coupled - creates its own dependency
        this.gateway = new StripePayment();
    }
    
    public void process(Order order) {
        gateway.initiatePayment(order.getAmount());
    }
}
```

**Problems:**
- Can't test without Stripe
- Can't swap payment providers without code changes
- OrderService does two jobs: business logic + wiring

## The Solution: Injection

```java
public class OrderService {
    private PaymentGateway gateway;
    
    // Dependencies injected from outside
    public OrderService(PaymentGateway gateway) {
        this.gateway = gateway;
    }
    
    public void process(Order order) {
        gateway.initiatePayment(order.getAmount());
    }
}
```

**Benefits:**
- Test with mock: `new OrderService(new MockPayment())`
- Swap providers: `new OrderService(new RazorpayPayment())`
- OrderService focuses on business logic only

## Injection Methods

### Constructor Injection (Most Common)

```java
public class Service {
    private Dependency dep;
    
    public Service(Dependency dep) {
        this.dep = dep;
    }
}
```

### Setter Injection

```java
public class Service {
    private Dependency dep;
    
    public void setDependency(Dependency dep) {
        this.dep = dep;
    }
}
```

### Interface Injection

```java
public interface Injectable {
    void inject(Dependency dep);
}
```

## Relationship to DIP

DI is a **technique** for achieving the **Dependency Inversion Principle**:

| Principle | DIP | DI |
|-----------|-----|-----|
| What | High-level depends on abstraction | Dependencies passed in |
| How | Interface-based design | Constructor/setter injection |

## Related Concepts

[[Dependency Inversion]], [[Inversion of Control]], [[SOLID]], [[Factory Pattern]]