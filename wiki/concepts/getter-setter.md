---
title: "Getter and Setter Pattern"
type: concept
tags: [oop, encapsulation, java-basics]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/encapsulation"]
---

# Getter and Setter Pattern

**Definition:** Convention where private fields are accessed through public methods — getters for reading, setters for writing — providing controlled access to internal state.

## Purpose

- Provide read-only or write-only access to fields
- Add validation in setters
- Hide internal representation
- Enable internal changes without breaking callers

## Basic Pattern

```java
public class Person {
    private String name;  // Private - can't access directly

    // Getter - read access
    public String getName() {
        return name;
    }

    // Setter - write access with validation
    public void setName(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty");
        }
        this.name = name;
    }
}
```

## Variations

### Read-Only

```java
public class Account {
    private final String id;  // Set only in constructor
    
    public String getId() {
        return id;
    }
    
    // No setId() - read only
}
```

### Write-Only

```java
public class Secret {
    private String value;
    
    public void setSecret(String value) {
        this.value = value;
    }
    
    // No getSecret() - write only
}
```

### Computed Properties

```java
public class Rectangle {
    private double width;
    private double height;
    
    public double getArea() {
        return width * height;
    }
    
    public double getPerimeter() {
        return 2 * (width + height);
    }
}
```

## JavaBeans Convention

Standard for framework compatibility:
1. Public no-arg constructor
2. Private properties
3. Public getters/setters following `getX()`/`setX()` pattern

## Anti-Pattern Warning

Don't automatically add getters/setters for every field:

```java
// Bad: Over-encapsulation
private String name;
private String email;
private String phone;

public String getName() { return name; }
public void setName(String name) { this.name = name; }
public String getEmail() { return email; }  // etc...
```

Only expose what callers actually need.

## Related Concepts

[[Encapsulation]], [[Private]], [[Public]], [[Data Validation]]