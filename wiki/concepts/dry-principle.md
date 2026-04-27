---
title: "DRY Principle"
type: concept
tags: [lld, design-principles,code-quality]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/dry"]
---

# DRY Principle

**Definition:** "Don't Repeat Yourself" — Each piece of knowledge in your system should live in **exactly one place**. Reference the single source rather than creating copies.

## The Problem

Duplication causes:
- Multiple changes for one fix
- Inconsistency as copies drift
- Higher maintenance cost
- Repeated testing

## Applying DRY

### Before (Duplication)

```java
// Three copies of same validation
public boolean validateEmailA(String email) {
    return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}
public boolean validateEmailB(String email) {
    return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}
public boolean validateEmailC(String email) {
    return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}
```

### After (DRY Applied)

```java
public class EmailValidator {
    public boolean isValid(String email) {
        return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }
}

// All use single source
validator.isValid(email);
```

## Rule of Three

Don't extract until you've seen the same pattern **three times**:
1. First occurrence — Just write it
2. Second — Note the pattern
3. Third — Extract into shared logic

## When to Violate DRY

- **Tests** — Clarity over DRY
- **Different domains** — Same logic, different meaning
- **Performance** — Inlining can be faster

## Related Concepts

[[KISS Principle]], [[YAGNI Principle]], [[Single Source of Truth]]