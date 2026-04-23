---
title: "Classes and Objects"
type: source
tags: [lld, oop, fundamentals]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/classes-and-objects", "blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Classes and Objects

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io](https://algomaster.io/learn/lld/classes-and-objects)  
**Updated:** February 12, 2026

## Summary

This article covers the foundational building blocks of Object-Oriented Programming: classes and objects. It demonstrates how these concepts translate real-world entities into code, with a practical example of an order management system.

## What is a Class?

A **class** is a blueprint, template, or recipe for creating objects. It defines:
- **What an object will contain** — its data (fields/attributes)
- **What an object will be able to do** — its behavior (methods)

A class is not an object itself — it's a template used to create many objects with similar structure but independent state.

```java
public class User {
    private String username;
    private String email;
    private String role;

    public User(String username, String email, String role) {
        this.username = username;
        this.email = email;
        this.role = role;
    }

    public boolean isAdmin() {
        return "ADMIN".equals(role);
    }
}
```

## What is an Object?

An **object** is a concrete instance of a class. It has:
- Actual values for the fields defined in the class
- The same structure and behavior as other instances
- Independent state from other objects

```java
User alice = new User("alice", "alice@example.com", "ADMIN");
User bob = new User("bob", "bob@example.com", "DEVELOPER");

alice.isAdmin();  // true
bob.isAdmin();    // false
```

## Practical Example: Online Food Order

Order management system demonstrating encapsulation:

```java
public class Order {
    private List<Item> items = new ArrayList<>();
    private double total = 0;
    private boolean placed = false;

    public void addItem(Item item) {
        if (placed) {
            throw new IllegalStateException("Cannot modify placed order");
        }
        items.add(item);
        total += item.getPrice() * item.getQuantity();
    }

    public void place() {
        if (items.isEmpty()) {
            throw new IllegalStateException("Cannot place empty order");
        }
        placed = true;
    }
}
```

### Benefits Demonstrated

1. **Encapsulates order state** — Items, total, and placement status live together
2. **Enforces business rules** — `addItem()` prevents modifications after `place()`
3. **Reusable** — One class creates thousands of order objects
4. **Easy to extend** — Add new fields without changing calling code

## Related Concepts

[[Class]], [[Object]], [[Encapsulation]], [[State Enforcing Methods]]