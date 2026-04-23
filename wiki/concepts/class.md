---
title: "Class"
type: concept
tags: [oop, fundamentals, building-blocks]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/classes-and-objects", "blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Class

**Definition:** A blueprint, template, or recipe that defines the structure (data/fields) and behavior (methods) that objects created from it will have.

## Real-World Analogy

Like an architectural blueprint for a house — specifies rooms, doors, windows. But you can't live in a blueprint; you need to build an actual house from it.

## Anatomy of a Class

```java
public class User {
    // Fields (data/state)
    private String username;
    private String email;
    private String role;

    // Constructor
    public User(String username, String email, String role) {
        this.username = username;
        this.email = email;
        this.role = role;
    }

    // Methods (behavior)
    public boolean isAdmin() {
        return "ADMIN".equals(role);
    }

    public String getDisplayName() {
        return username + " (" + role + ")";
    }
}
```

## Key Characteristics

| Aspect | Description |
|--------|-------------|
| Template | Defines structure but doesn't execute |
| Reusable | One class creates many objects |
| Independent state | Each object from same class has own data |
| Groups related data + behavior | Cohesive unit |

## Class vs Object

| Class | Object |
|-------|--------|
| Blueprint/template | Concrete instance |
| Doesn't hold values | Holds actual values |
| Created once | Created multiple times |
| Logical entity | Physical entity |

## Languages Supporting Classes

Java, Python, C++, C#, Go, TypeScript all use classes to organize code around real-world entities.

## Related Concepts

[[Object]], [[Encapsulation]], [[Interface]], [[Class Diagram]]