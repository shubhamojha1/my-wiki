---
title: "Encapsulation"
type: source
tags: [lld, oop, fundamentals]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/encapsulation"]
---

# Encapsulation

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io/learn/lld/encapsulation](https://algomaster.io/learn/lld/encapsulation)  
**Updated:** February 12, 2026

## Summary

This article covers encapsulation — bundling data with methods that operate on that data while restricting direct access to internal state. It demonstrates how access modifiers and getters/setters achieve encapsulation with BankAccount and PaymentProcessor examples.

## Why Encapsulation Matters

- **Protects data integrity** — Invalid state impossible
- **Enforces business rules** — Changes go through controlled methods
- **Enables change** — Internal implementation can change without breaking callers

## How Encapsulation is Achieved

### Access Modifiers

| Modifier | Access |
|----------|--------|
| `private` | Same class only |
| `protected` | Same class + subclasses |
| `public` | Anywhere |
| (default) | Same package |

### Getters and Setters

- **Getter** (`getBalance()`): Read-only access
- **Setter** (`setAmount()`): Modify with validation

## Example: BankAccount

```java
public class BankAccount {
    private double balance;  // Private - can't access directly

    public BankAccount(double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Balance cannot be negative");
        }
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit must be positive");
        }
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount <= 0 || amount > balance) {
            return false;
        }
        balance -= amount;
        return true;
    }

    public double getBalance() {
        return balance;
    }
}
```

### Key Points

1. `balance` is `private` — No direct access
2. `deposit()`/`withdraw()` validate before modifying
3. `getBalance()` provides read-only access

## Example: PaymentProcessor

```java
public class PaymentProcessor {
    private String cardNumber;  // Private - sensitive data

    public PaymentProcessor(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public void processPayment(double amount) {
        // Process payment without exposing card number
        System.out.println("Processing $" + amount);
    }

    // Public interface - masks the sensitive data
    @Override
    public String toString() {
        return "PaymentProcessor{" +
            "cardNumber='" + maskCardNumber() + "'}";
    }

    private String maskCardNumber() {
        // Show only last 4 digits: ****-****-****-1234
        return "****-****-****-" + cardNumber.substring(12);
    }
}
```

### Key Points

1. `cardNumber` kept private — Raw number never exposed
2. `maskCardNumber()` is private — Internal logic hidden
3. `toString()` controlled — Debug output is safe

## Related Concepts

[[Access Modifiers]], [[Private]], [[Public]], [[Getter Setter Pattern]], [[Data Validation]]