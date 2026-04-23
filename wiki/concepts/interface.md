---
title: "Interface"
type: concept
tags: [oop, abstraction, contracts]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Interface

**Definition:** A contract that defines a set of methods that a class must implement, without specifying how those methods should work.

## Purpose

Allows defining **what** classes must do without dictating **how**. Enables swapping implementations without changing calling code.

## Real-World Example

Payment processing — define a contract for charging and refunding, then plug in Stripe, PayPal, or future providers:

```java
public interface PaymentGateway {
    PaymentResult charge(String customerId, double amount);
    PaymentResult refund(String transactionId);
}

public class StripeGateway implements PaymentGateway {
    @Override
    public PaymentResult charge(String customerId, double amount) {
        // Stripe-specific implementation
        return new PaymentResult(true, "txn_stripe_123");
    }

    @Override
    public PaymentResult refund(String transactionId) {
        // Stripe-specific implementation
        return new PaymentResult(true, transactionId);
    }
}
```

## Interface vs Implementation

| Aspect | Interface | Implementation |
|--------|-----------|----------------|
| Purpose | Contract | Concrete behavior |
| Methods | Declared (what) | Implemented (how) |
| Instantiation | No | Yes |
| Multiple | A class can implement many | - |

## Polymorphism via Interfaces

```java
// Code depends on interface, not implementation
public class CheckoutService {
    public void process(PaymentGateway gateway) {
        gateway.charge(customerId, amount);
    }
}

// Swap implementations without changing CheckoutService
CheckoutService checkout = new CheckoutService();
checkout.process(new StripeGateway());    // Use Stripe
checkout.process(new PayPalGateway());   // Or PayPal
```

## Benefits

1. **Loose coupling** — Depends on abstraction, not concrete classes
2. **Swappable implementations** — Change one line of config
3. **Testability** — Easy to mock interfaces
4. **Extensibility** — Add new implementations without modifying existing code

## Related Concepts

[[Realization]], [[Abstraction]], [[Polymorphism]], [[Contract Pattern]]