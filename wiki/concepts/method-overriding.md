---
title: "Method Overriding"
type: concept
tags: [oop, inheritance, polymorphism]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/inheritance"]
---

# Method Overriding

**Definition:** When a subclass provides a specific implementation of a method already defined in its parent class. The overriding method has the same signature but different behavior.

## Basic Example

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}
```

## Key Concepts

### @Override Annotation

- Compiler checks signatures match
- Prevents typos causing new methods
- Documents intent

### super Keyword

Call parent's version:

```java
public class Dog extends Animal {
    @Override
    public void makeSound() {
        super.makeSound();  // Call parent first
        System.out.println("Woof!");
    }
}
```

## Covariant Return Types

Return type can be subclass:

```java
public class Animal {
    public Animal clone() { return new Animal(); }
}

public class Dog extends Animal {
    @Override
    public Dog clone() { return new Dog(); }  // Returns Dog, not Animal
}
```

## Rules for Overriding

| Rule | Description |
|------|-------------|
| Signature | Must match exactly |
| Access | Cannot reduce visibility |
| Return | Can be covariant |
| Static | Cannot override (hides instead) |
| Private | Cannot override (not inherited) |

## Related Concepts

[[Inheritance]], [[Polymorphism]], [[Super Keyword]], [[Liskov Substitution Principle]]