---
title: "Method Overloading"
type: concept
tags: [oop, compile-time, polymorphism]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/polymorphism"]
---

# Method Overloading

**Definition:** Multiple methods with the same name but different parameter lists within the same class. Compiler resolves which one to call at compile time.

## Purpose

- Different behaviors with same conceptual operation
- More readable API (one method name vs. addInt, addDouble)

## Examples

```java
public class MathUtils {
    public int max(int a, int b) {
        return a > b ? a : b;
    }

    public double max(double a, double b) {
        return a > b ? a : b;
    }

    public int max(int a, int b, int c) {
        return max(max(a, b), c);
    }
}
```

## Resolution

Based on method signature (name + parameters):

```java
MathUtils m = new MathUtils();
m.max(1, 2);        // Calls max(int, int)
m.max(1.0, 2.0);    // Calls max(double, double)
m.max(1, 2, 3);       // Calls max(int, int, int)
```

## Constructor Overloading

```java
public class User {
    private String name;
    private String email;

    // No args
    public User() { }

    // One param
    public User(String name) {
        this.name = name;
    }

    // Two params
    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }
}
```

## Rules

| Rule | Description |
|------|-------------|
| Name | Same across overloads |
| Parameters | Must differ in number or type |
| Return type | Can be different |
| Not just return type | Changing only return type is not overloading |

## Related Concepts

[[Polymorphism]], [[Method Overriding]], [[Compile-Time]]