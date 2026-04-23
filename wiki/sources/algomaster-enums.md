---
title: "Enums"
type: source
tags: [lld, oop, fundamentals]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/enums"]
---

# Enums

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io/learn/lld/enums](https://algomaster.io/learn/lld/enums)  
**Updated:** February 12, 2026

## Summary

This article covers enumerations (enums) — fixed sets of named constants that bring structure and type safety to domain models. It demonstrates simple enums, enums with properties and methods, and a practical order processing system.

## What is an Enum?

An **enum** (enumeration) is a fixed set of named constants. It defines a type that can only have one of a predefined set of values, bringing compile-time safety to domain concepts.

## Simple Enum

```java
public enum OrderStatus {
    PLACED,
    CONFIRMED,
    SHIPPED,
    DELIVERED,
    CANCELLED
}
```

## Enums with Properties and Methods

Enums can hold additional data and define behavior:

```java
public enum PaymentMethod {
    CREDIT_CARD("Credit Card", 2.5),    // name, fee percentage
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

## Practical Example: Order Processing System

```java
public class Order {
    private String orderId;
    private OrderStatus status;
    private PaymentMethod paymentMethod;
    private double amount;

    public Order(String orderId, PaymentMethod paymentMethod, double amount) {
        this.orderId = orderId;
        this.status = OrderStatus.PLACED;
        this.paymentMethod = paymentMethod;
        this.amount = amount;
    }

    public boolean advanceStatus() {
        switch (status) {
            case PLACED:    status = OrderStatus.CONFIRMED; break;
            case CONFIRMED: status = OrderStatus.SHIPPED; break;
            case SHIPPED:   status = OrderStatus.DELIVERED; break;
            default: return false;
        }
        return true;
    }

    public boolean cancel() {
        if (status == OrderStatus.SHIPPED || status == OrderStatus.DELIVERED) {
            return false;
        }
        status = OrderStatus.CANCELLED;
        return true;
    }
}
```

## Key Insights

1. **Easy to extend** — Add `RETURNED` status or `WALLET` payment method with one line
2. **Status transitions controlled** — Can't jump from PLACED to DELIVERED
3. **Cancellation rules clear** — Only cancel before shipping
4. **Payment fees self-contained** — Each payment method carries its own fee

## Related Concepts

[[Enum]], [[Type Safety]], [[State Machine]], [[Order Processing]]