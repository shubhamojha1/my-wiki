---
title: "Abstract Class"
type: concept
tags: [oop, abstraction, inheritance]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/abstraction"]
---

# Abstract Class

**Definition:** A class that cannot be instantiated directly and serves as a blueprint for related classes. It can contain both abstract methods (declared without implementation) and concrete methods (fully implemented).

## Purpose

- Define common structure for related classes
- Provide shared behavior (concrete methods)
- Force subclasses to implement abstract methods

## Syntax

```java
public abstract class Animal {
    // Abstract method - no implementation
    public abstract void makeSound();

    // Concrete method - has implementation
    public void display() {
        System.out.println("This is an animal");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}
```

## Abstract + Concrete Methods

```java
public abstract class MediaPlayer {
    public abstract void play();
    public abstract void pause();
    public abstract void stop();

    // Shared behavior - all subclasses inherit
    public void displayStatus() {
        System.out.println("Status: " + getClass().getSimpleName());
    }
}
```

## When to Use

- Clear "is-a" relationship (Dog is-a Animal)
- Common behavior to share
- Partial implementation
- Not just for code reuse (use composition)

## Abstract Class vs Interface

| Aspect | Abstract Class | Interface |
|--------|---------------|-----------|
| Inheritance | Single | Multiple possible |
| State | Can have fields | Cannot have instance fields |
| Constructors | Can have | Cannot have |
| Methods | Abstract + concrete | Abstract + default (Java 8+) |
| When to use | Shared implementation | Just contracts |

## Related Concepts

[[Interface]], [[Inheritance]], [[Polymorphism]], [[Abstraction]]