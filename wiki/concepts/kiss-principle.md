---
title: "KISS Principle"
type: concept
tags: [lld, design-principles]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/kiss"]
---

# KISS Principle

**Definition:** "Keep It Simple, Stupid" — Most systems work best when kept simple. Unnecessary complexity introduces failure points and makes things harder to fix.

## Origin

Coined by the **U.S. Navy in the 1960s**.

## Example: Calculator

### Over-Engineered (Violation)

```java
// Interface + 4 classes for 4 operations
public interface Operation {
    double execute(double a, double b);
}

public class AddOperation implements Operation { ... }
public class SubtractOperation implements Operation { ... }
// ... more classes
public class Calculator {
    private Operation operation;
    public void setOperation(Operation op) { ... }
}
```

### KISS Applied

```java
public class Calculator {
    public double calculate(char op, double a, double b) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return b != 0 ? a / b : 0;
        }
    }
}
```

## Why Complexity Is Dangerous

- More failure points
- Harder to understand
- Harder to fix
- More to maintain

## Signs of Violation

- Single-method classes
- Interfaces for trivial operations
- Empty stubs or unused code
- More layers than logic

## Related Principles

[[DRY Principle]], [[YAGNI Principle]]