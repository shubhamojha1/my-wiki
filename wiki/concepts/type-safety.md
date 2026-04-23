---
title: "Type Safety"
type: concept
tags: [programming, type-systems, correctness]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/enums"]
---

# Type Safety

**Definition:** A property of a programming language where the compiler prevents operations on values of inappropriate types. Type-safe code cannot perform invalid operations even if the programmer attempts to do so.

## Without Type Safety

```java
// Using strings for status
String status = "placed";
status = "typo";  // No compiler error
status = 123;     // Type allows this

// Later, comparing:
if (status == "plced") {  // Typo! Runtime bug
    // ...
}
```

## With Type Safety

```java
// Using enum
OrderStatus status = OrderStatus.PLACED;
status = OrderStatus.TYPO;  // Compiler error: TYPO doesn't exist
status = 123;               // Compiler error: type mismatch

// Comparing is safe
if (status == OrderStatus.PLACED) {  // Always correct
    // ...
}
```

## What Type Safety Provides

| Benefit | Description |
|---------|-------------|
| Compile-time errors | Catch bugs before runtime |
| Self-documenting code | Types communicate intent |
| Refactoring safety | Compiler finds all usages |
| IDE support | Autocomplete based on types |

## Levels of Type Safety

| Level | Example Languages |
|-------|-------------------|
| Static, strong | Haskell, Rust, Java |
| Static, weak | C, C++ (with casts) |
| Dynamic | Python, JavaScript, Ruby |
| Duck typing | Python, Ruby (runtime) |

## Type Safety and Enums

Enums are a simple way to add type safety to domain concepts:

```java
// Before: arbitrary strings
String paymentMethod = "credit_card";

// After: typed enum
PaymentMethod method = PaymentMethod.CREDIT_CARD;
```

## Related Concepts

[[Enum]], [[Type System]], [[Compile-Time Checking]], [[Runtime Type Checking]]