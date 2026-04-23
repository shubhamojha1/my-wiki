---
title: "Access Modifiers"
type: concept
tags: [oop, visibility, java-basics]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/encapsulation"]
---

# Access Modifiers

**Definition:** Keywords that control the visibility and accessibility of classes, methods, and variables. They are the primary mechanism for implementing encapsulation.

## Java Access Modifiers

| Modifier | Class | Package | Subclass | World |
|----------|-------|---------|----------|-------|
| `private` | ✓ | ✗ | ✗ | ✗ |
| (default) | ✓ | ✓ | ✗ | ✗ |
| `protected` | ✓ | ✓ | ✓ | ✗ |
| `public` | ✓ | ✓ | ✓ | ✓ |

## Level by Level

### private — Most Restrictive

```java
public class BankAccount {
    private double balance;  // Only accessible within BankAccount
    
    private void validateAmount(double amount) {
        // Only BankAccount can call this
    }
}
```

### (default / package-private)

```java
// In same package - accessible
class InternalHelper {
    // In different package - not accessible
}
```

### protected — Inheritance Access

```java
public class Animal {
    protected String name;
    
    protected void makeSound() {
        // Accessible to Animal and its subclasses
    }
}

public class Dog extends Animal {
    public void bark() {
        // Can access name and makeSound()
    }
}
```

### public — No Restrictions

```java
public class Utils {
    public static void helper() {
        // Accessible from anywhere
    }
}
```

## Choosing the Right Level

| Use | Modifier |
|-----|----------|
| Internal data | `private` |
| Package-internal | (default) |
| Inheritance + internal | `protected` |
| Public API | `public` |

## Related Concepts

[[Encapsulation]], [[Private]], [[Public]], [[Protected]]