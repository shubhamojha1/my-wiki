---
title: "Object"
type: concept
tags: [oop, fundamentals, building-blocks]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/classes-and-objects", "blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Object

**Definition:** A concrete instance of a class with actual values for the fields defined in the class. It is the actual thing you can interact with, store data in, and invoke methods on.

## Object vs Class

| Class | Object |
|-------|--------|
| Template/blueprint | Filled-in copy |
| Defines structure | Has actual state |
| Created once | Created many times |
| "User class" | "alice user object" |

## Creating Objects

```java
// User class → objects
User alice = new User("alice", "alice@example.com", "ADMIN");
User bob = new User("bob", "bob@example.com", "DEVELOPER");
User carol = new User("carol", "carol@example.com", "DEVELOPER");

alice.isAdmin();          // true
bob.isAdmin();            // false
alice.getDisplayName();   // "alice (ADMIN)"
```

## Key Properties

1. **Own copy of fields** — Changing `alice`'s role doesn't affect `bob`
2. **Independent state** — Each object operates independently
3. **Same structure** — All share class's fields and methods
4. **Same behavior** — Methods behave the same way

## Visual Representation

```
┌─────────────────────┐
│      User           │  ← Class (blueprint)
├─────────────────────┤
│ username            │
│ email               │
│ role                │
├─────────────────────┤
│ isAdmin()           │
│ getDisplayName()    │
└─────────────────────┘

┌─────────────────────┐    ┌─────────────────────┐
│ Object: alice       │    │ Object: bob          │
│ username: "alice"   │    │ username: "bob"      │
│ email: "alice@..."  │    │ email: "bob@..."     │
│ role: "ADMIN"       │    │ role: "DEVELOPER"    │
└─────────────────────┘    └─────────────────────┘
```

## Related Concepts

[[Class]], [[Instance]], [[State]], [[Encapsulation]]