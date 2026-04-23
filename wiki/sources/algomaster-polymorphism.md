---
title: "Polymorphism"
type: source
tags: [lld, oop, many-forms]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/polymorphism"]
---

# Polymorphism

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io/learn/lld/polymorphism](https://algomaster.io/learn/lld/polymorphism)  
**Updated:** February 12, 2026

## Summary

This article covers polymorphism — "many forms" — the ability of objects of different types to be treated through a common interface. It explains compile-time and runtime polymorphism.

## Why Polymorphism Matters

- **Flexible code** — Same interface, different behaviors
- **Extensible** — Add new types without changing callers
- **Clean code** — Avoids type-checking switches

## How Polymorphism Works

### 1. Compile-Time (Method Overloading)

Same method name, different parameters:

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public String add(String a, String b) {
        return a + b;
    }
}
```

Compiler resolves at compile time based on parameter types.

### 2. Runtime (Method Overriding)

Same method signature, different implementations:

```java
public interface Notification {
    void send(String message);
}

public class EmailNotifier implements Notification {
    @Override
    public void send(String message) {
        System.out.println("Email: " + message);
    }
}

public class SmsNotifier implements Notification {
    @Override
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}
```

JVM resolves at runtime based on actual object type.

## Polymorphism with Interfaces

```java
public class AlertService {
    private Notification notification;

    public AlertService(Notification notification) {
        this.notification = notification;
    }

    public void alert(String message) {
        notification.send(message);  // Works with any Notification
    }
}

// Works with any implementation
new AlertService(new EmailNotifier()).alert("Hi");
new AlertService(new SmsNotifier()).alert("Hi");
```

## Key Takeaways

| Type | When Resolved | Mechanism |
|------|-------------|----------|
| Compile-time | Compile time | Method overloading |
| Runtime | Runtime | Method overriding |

## Related Concepts

[[Method Overriding]], [[Method Overloading]], [[Interface]], [[Abstract Class]]