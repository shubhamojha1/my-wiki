---
title: "AlgoMaster: Composition"
type: source
tags: [lld, oop, relationships]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/composition"]
author: Ashish Pratap Singh
---

# Composition

**Source:** AlgoMaster.io Low-Level Design Course — Composition Chapter

## Definition

**Composition** is a "has-a" relationship where one class contains another, and the contained class **cannot exist independently** of the container. It represents **strong ownership** with tied lifecycles.

> "Parts belong to the whole — when the whole is destroyed, the parts are destroyed too."

---

## UML Representation

- **Symbol**: Filled diamond (◆) + solid line
- **Direction**: From whole to part

```
┌─────────────┐◆──────┐─────────────┐
│    Car    │◆──────│   Engine   │
└─────────────┘       └─────────────┘
```

| Relationship | UML Symbol |
|-------------|-----------|
| Inheritance | Solid line + hollow triangle |
| **Composition** | **Solid line + filled diamond** |
| Aggregation | Solid line + hollow diamond |
| Association | Solid line (plain) |
| Dependency | Dashed arrow |

---

## Composition vs Association vs Aggregation

| Aspect | Association | Aggregation | Composition |
|--------|-------------|-------------|-------------|
| Relationship | "Knows-about" | "Has-A" | "Owns-A" |
| Coupling | Loosest | Moderate | Tightest |
| Lifecycle | Independent | Independent | Parts die with whole |
| Symbol | Solid line | ◇ (hollow) | ◆ (filled) |
| Creation | Both separate | Parts passed in | Whole creates parts |
| Ownership | None | Weak/Shared | Strong |

---

## Code Example

```java
class Room {
    String type;
    Room(String type) { this.type = type; }
}

class House {
    private List<Room> rooms;
    
    House() {
        // Composition: House creates its own rooms
        rooms = Arrays.asList(
            new Room("bedroom"),
            new Room("kitchen"),
            new Room("bathroom")
        );
    }
}

// Room cannot exist outside House
House house = new House();
house = null;  // Rooms automatically "die" with House
```

```java
// Car and Engine - typical composition
class Engine {
    void start() { System.out.println("Starting..."); }
}

class Car {
    private Engine engine;
    
    Car() {
        // Engine created with Car, dies with Car
        engine = new Engine();
    }
    
    void drive() {
        engine.start();
        System.out.println("Driving...");
    }
}
```

---

## Real-World Examples

1. **House ↔ Room**: A room can't exist without a house
2. **Car ↔ Engine**: Engine meaningless without a car
3. **Order ↔ LineItem**: Line items only exist within an order
4. **Document ↔ Paragraph**: Paragraphs only make sense in a document

---

## Key Characteristics

1. **Whole creates parts** — Constructor builds the contained objects
2. **Parts die with whole** — No independent lifecycle
3. **Strong ownership** — Exclusive relationship
4. **No reassignment** — Parts can't move to another whole

---

## Key Takeaways

1. Composition is the **tightest** relationship in OOP
2. Represented by **filled diamond (◆)** in UML
3. Use when parts **cannot exist** without the whole
4. Whole is **responsible** for creating and destroying parts
5. Tighter coupling than Aggregation or Association