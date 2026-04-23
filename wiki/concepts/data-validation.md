---
title: "Data Validation"
type: concept
tags: [programming, correctness, business-rules]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/encapsulation"]
---

# Data Validation

**Definition:** Checking and enforcing that data meets required constraints before accepting or processing it. Crucial for maintaining object integrity.

## Where to Validate

### 1. In Setters

```java
public void setAge(int age) {
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException("Invalid age");
    }
    this.age = age;
}
```

### 2. In Constructors

```java
public BankAccount(double initialBalance) {
    if (initialBalance < 0) {
        throw new IllegalArgumentException("Balance cannot be negative");
    }
    this.balance = initialBalance;
}
```

### 3. In Business Methods

```java
public boolean withdraw(double amount) {
    if (amount <= 0) {
        return false;
    }
    if (amount > balance) {
        return false;
    }
    balance -= amount;
    return true;
}
```

## Validation Principles

| Principle | Example |
|-----------|---------|
| Fail fast | Check at boundary, throw immediately |
| Fail-safe | Return false on invalid input |
| Single source | Validate once, not everywhere |

## Types of Validation

| Type | Example |
|------|---------|
| Range | `0 <= age <= 150` |
| Format | Email regex |
| Required | Non-null, non-empty |
| Business | `withdraw <= balance` |
| Cross-field | `endDate >= startDate` |

## Related Concepts

[[Encapsulation]], [[Getter Setter Pattern]], [[Business Rules]]