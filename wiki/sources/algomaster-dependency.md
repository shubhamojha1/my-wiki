---
title: "AlgoMaster: Dependency"
type: source
tags: [lld, oop, relationships]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/dependency"]
author: Ashish Pratap Singh
---

# Dependency

**Source:** AlgoMaster.io Low-Level Design Course — Dependency Chapter

## Definition

**What happens when a class needs to use another class for a brief moment to get a job done, without needing to hold onto it forever?**

That's **Dependency** — the **weakest form of relationship** between classes.

> Unlike association, aggregation, or composition, a dependency isn't a structural "we belong together" relationship. There's no shared lifecycle and no long-term connection. Instead, it reflects a **one-time interaction**, often through method parameters, local variables, or return types.

---

## Real-World Analogy

**Chef and Knife:**
- The chef picks up a Knife to chop vegetables
- Once the chopping is done, the knife is put away or reused elsewhere
- The chef doesn't own the knife or keep it stored long-term

---

## UML Representation

- **Symbol**: Dashed arrow (`..>`)
- **Direction**: From dependent class (Client) to class it depends on (Supplier)

```
ClassA  ..->  ClassB
```

| Symbol | Relationship |
|--------|--------------|
| `------>` | Dependency (dashed) |
| `---` | Association (solid) |
| `◇---` | Aggregation (hollow diamond) |
| `◆---` | Composition (filled diamond) |

---

## How Dependency Occurs

1. **Method parameter**: Class receives dependency as parameter
2. **Local instance**: Class creates temporary local instance
3. **Static method**: Class calls static methods of another class
4. **Return type**: Class returns another class type

---

## Code Examples

### Method Parameter

```java
public class OrderService {
    // Dependency: PaymentProcessor passed as parameter
    public void processPayment(Order order, PaymentProcessor processor) {
        processor.process(order.getAmount());
    }
}

public class PaymentProcessor {
    public void process(double amount) { }
}
```

### Local Instance

```java
public class ReportGenerator {
    public byte[] generate(String data) {
        // Dependency: created locally, used once
        PDFGenerator generator = new PDFGenerator();
        return generator.create(data);
    }
}
```

### Static Method

```java
public class MathUtils {
    public static double calculate(double value) { return value * 2; }
}

public class Calculator {
    // Dependency: static method call
    public double compute(double x) {
        return MathUtils.calculate(x);  // Static dependency
    }
}
```

---

## Dependency vs Association vs Aggregation vs Composition

| Aspect | Dependency | Association | Aggregation | Composition |
|--------|------------|-------------|-------------|-------------|
| Relationship | "Uses-A" (temporary) | "Knows-about" | "Has-A" | "Owns-A" |
| Reference | None (method scope) | Held as field | Held as field | Held as field |
| Lifecycle | Ephemeral | Independent | Independent | Dependent |
| UML Symbol | `..->` (dashed) | `---` (solid) | `◇---` | `◆---` |
| Coupling | Loosest | Loose | Moderate | Tightest |
| Duration | Method call | Long-term | Long-term | Long-term |

---

## Key Characteristics

1. **Temporary relationship** - Only needed for a specific operation
2. **No ownership** - Doesn't manage lifecycle of dependency
3. **Passed via parameters** - Often received through method parameters
4. **Method scope** - Dependency might only exist within a single method call

---

## Key Takeaways

1. Dependency is the **weakest** relationship between classes
2. Represented by **dashed arrow** (`..->`) in UML
3. Used when class needs another class **temporarily** (method parameter, local variable)
4. Avoid holding references — pass dependencies as parameters when possible
5. Static method calls are also dependencies
6. Most loosely coupled — easiest to change