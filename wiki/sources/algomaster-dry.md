---
title: "AlgoMaster: DRY Principle"
type: source
tags: [lld, design-principles]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/dry"]
author: Ashish Pratap Singh
---

# DRY Principle

**Source:** AlgoMaster.io Low-Level Design Course — DRY Chapter

## Definition

**DRY** = "Don't Repeat Yourself"

> The DRY principle says that each piece of knowledge in your system should live in **exactly one place**. When you need that knowledge somewhere else, you reference the single source rather than creating a second copy.

---

## The Problem with Duplication

When the same logic exists in multiple places:
- **Updates require multiple changes** — Fixing a bug or updating a rule means finding all copies
- **Inconsistency** — Different copies drift apart over time
- **Higher maintenance cost** — More places to touch for any change
- **Testing burden** — Same logic tested multiple times

---

## Applying DRY in Code

### Before (Violation)

```java
// Module A: Email validation
public boolean isValidEmail(String email) {
    if (email == null || email.isEmpty()) return false;
    return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}

// Module B: Same logic copied
public boolean validateEmailAddress(String email) {
    if (email == null || email.isEmpty()) return false;
    return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}

// Module C: Another copy
public boolean checkEmailFormat(String email) {
    if (email == null || email.isEmpty()) return false;
    return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}
```

### After (DRY Applied)

```java
// Single source of truth
public class EmailValidator {
    public boolean isValid(String email) {
        if (email == null || email.isEmpty()) return false;
        return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }
}

// All modules use the same validator
EmailValidator validator = new EmailValidator();
validator.isValid(email);  // Used everywhere
```

**Benefits:**
- Single place to update validation logic
- Easy to add new top-level domains
- All modules stay consistent automatically
- Tested once

---

## The Rule of Three

> "Before extracting shared logic, wait until you see the same pattern **three times**."

Don't premature abstract:
1. First occurrence — Just write it
2. Second occurrence — Note the pattern, don't extract yet
3. Third occurrence — Now extract into shared logic

**Why wait?**
- Patterns may not repeat as expected
- First two instances may reveal design flaws
- Premature abstraction is harder to get right

---

## When to Violate DRY

DRY is a **guideline**, not a strict rule. Some situations allow intentional duplication:

### 1. Tests Need Clarity

Tests should be readable in isolation. Don't force abstraction that makes tests harder to understand.

```java
// Tests should be self-explanatory, even if some logic repeats
@Test
void shouldRejectInvalidEmail() {
    assertFalse(validator.isValid(null));
    assertFalse(validator.isValid(""));
    assertFalse(validator.isValid("not-email"));
}
```

### 2. Different Domains

When the same logic has different meanings in different contexts, duplication may be intentional.

### 3. Performance Optimization

In hot paths, inlining can be faster than virtual dispatch.

---

## Key Takeaways

1. **DRY** = Each piece of knowledge in one place
2. Use the **Rule of Three** — Don't extract until third occurrence
3. Duplication leads to inconsistency and maintenance nightmares
4. But DRY is a **guideline**, not a strict rule
5. Tests may need explicit duplication for clarity