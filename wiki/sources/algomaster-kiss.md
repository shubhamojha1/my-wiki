---
title: "AlgoMaster: KISS Principle"
type: source
tags: [lld, design-principles]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/kiss"]
author: Ashish Pratap Singh
---

# KISS Principle

**Source:** AlgoMaster.io Low-Level Design Course — KISS Chapter

## Definition

**KISS** = "Keep It Simple, Stupid" (or "Keep It Simple, Smart")

> Most systems work best when they are kept simple. Unnecessary complexity introduces failure points, slows down understanding, and makes things harder to fix when they break.

---

## Origin

The KISS principle was coined by the **U.S. Navy in the 1960s**.

---

## Example: The Calculator

### Over-Engineered (Violation)

A junior developer builds a calculator for basic arithmetic (add, subtract, multiply, divide) but makes it "future-proof" with an inheritance-based framework:

```java
public interface Operation {
    double execute(double a, double b);
}

public class AddOperation implements Operation {
    public double execute(double a, double b) { return a + b; }
}

public class SubtractOperation implements Operation {
    public double execute(double a, double b) { return a - b; }
}

public class Calculator {
    private Operation operation;
    
    public void setOperation(Operation op) {
        this.operation = op;
    }
    
    public double calculate(double a, double b) {
        return operation.execute(a, b);
    }
}
```

What would be a few `if` statements now requires:
- An interface
- Four separate classes
- An extra layer of indirection
- To add modulo: create new class, implement interface, wire it up

> **This is KISS violation** — too much ceremony for little gain.

---

### KISS Applied

```java
public class Calculator {
    public double calculate(char operator, double a, double b) {
        switch (operator) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return b != 0 ? a / b : 0;
            default: return 0;
        }
    }
}
```

Simple, works, easy to read, easy to test. Want to add modulo? Add one case.

---

## Why Complexity Is Dangerous

1. **More failure points** — More code means more bugs
2. **Harder to understand** — New developers get lost
3. **Harder to fix** — Tracing through multiple layers
4. **More to maintain** — Every piece needs testing

---

## Signs You're Violating KISS

- Classes with single responsibilities spread over many files
- Interfaces for simple operations
- Empty method stubs or unused code
- More indirection than actual logic
- "Just in case" abstractions

---

## How to Apply KISS

1. **Start simple** — If-else or switch is fine for small problems
2. **Keep functions short** — One task per function
3. **Avoid premature abstraction** — Wait until pattern emerges
4. **Clear over clever** — Readable code beats smart code

---

## When Not to Simplify

- **Real complexity** — Some problems ARE complex
- **Frameworks** — Libraries need abstraction
- **Scale** — Large systems may need structure

---

## Related Principles

| Principle | Meaning |
|-----------|---------|
| DRY | Don't repeat logic |
| KISS | Don't make solution harder than necessary |
| YAGNI | Don't build for future needs |

---

## Key Takeaways

1. **Simplicity first** — Start with the simplest working solution
2. **Avoid over-engineering** — Don't add layers "just in case"
3. **Clear > Clever** — Readable code wins
4. **Small functions** — One task per function