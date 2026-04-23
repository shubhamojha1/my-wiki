---
title: "Interfaces"
type: source
tags: [lld, oop, solid]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/interfaces"]
---

# Interfaces

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io/learn/lld/interfaces](https://algomaster.io/learn/lld/interfaces)  
**Updated:** February 12, 2026

## Summary

This article covers interfaces — contracts that define what methods a class must implement without specifying how. It demonstrates interfaces with payment gateway and notification service examples.

## Key Properties of Interfaces

- **Contract** — Define what must be done, not how
- **Multiple implementation** — One interface, many implementations
- **No state** — Cannot hold instance variables (in Java)
- **Polymorphism** — Different behaviors through same interface

## Code Example: Payment Gateway

```java
public interface PaymentGateway {
    PaymentResult initiatePayment(double amount);
}

public class StripePayment implements PaymentGateway {
    @Override
    public PaymentResult initiatePayment(double amount) {
        // Stripe-specific implementation
        return new PaymentResult(true, "stripe_txn_123");
    }
}

public class RazorpayPayment implements PaymentGateway {
    @Override
    public PaymentResult initiatePayment(double amount) {
        // Razorpay-specific implementation
        return new PaymentResult(true, "razorpay_txn_456");
    }
}
```

## Checkout Service (Depends on Interface)

```java
public class CheckoutService {
    private PaymentGateway gateway;

    public CheckoutService(PaymentGateway gateway) {
        this.gateway = gateway;
    }

    public void processPayment(double amount) {
        // Doesn't know or care which implementation
        gateway.initiatePayment(amount);
    }
}
```

## Practical Example: Notification Service

```java
public interface NotificationService {
    void send(String recipient, String message);
}

public class EmailNotifier implements NotificationService {
    @Override
    public void send(String recipient, String message) {
        System.out.println("Email to " + recipient + ": " + message);
    }
}

public class SmsNotifier implements NotificationService {
    @Override
    public void send(String recipient, String message) {
        System.out.println("SMS to " + recipient + ": " + message);
    }
}

public class WebhookNotifier implements NotificationService {
    @Override
    public void send(String recipient, String message) {
        System.out.println("Webhook to " + recipient + ": " + message);
    }
}

public class AlertService {
    private NotificationService notifier;

    public AlertService(NotificationService notifier) {
        this.notifier = notifier;
    }

    public void alert(String recipient, String message) {
        notifier.send(recipient, message);
    }
}
```

## Benefits

- **Adding new channels is trivial** — Create new class implementing interface
- **Each notifier independently testable** — Test without involving other channels
- **Alert service is channel-agnostic** — No imports of concrete classes
- **Configuration drives behavior** — Change notifier via config, not code

## Related Concepts

[[Interface]], [[Dependency Inversion]], [[Interface Segregation]], [[Dependency Injection]], [[Polymorphism]]