---
title: "Inheritance"
type: source
tags: [lld, oop, code-reuse]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/inheritance"]
---

# Inheritance

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io/learn/lld/inheritance](https://algomaster.io/learn/lld/inheritance)  
**Updated:** February 12, 2026

## Summary

This article covers inheritance — a mechanism where a class derives from another class, inheriting fields and methods. It demonstrates single, multilevel, and hierarchical inheritance with a notification system example.

## Why Inheritance Matters

- **Code reuse** — Don't repeat common fields/methods
- **Clear relationships** — "is-a" semantics
- **Polymorphism** — Treat related objects uniformly

## How Inheritance Works

```java
public class Notification {
    protected String recipient;
    protected String message;
    protected long timestamp;

    public Notification(String recipient, String message) {
        this.recipient = recipient;
        this.message = message;
        this.timestamp = System.currentTimeMillis();
    }

    public String formatHeader() {
        return "To: " + recipient + " at " + timestamp;
    }

    public abstract void send();  // Each channel implements differently
}

public class EmailNotification extends Notification {
    private String subject;

    public EmailNotification(String recipient, String message, String subject) {
        super(recipient, message);
        this.subject = subject;
    }

    @Override
    public void send() {
        // Email-specific sending logic
    }
}
```

## Types of Inheritance

| Type | Description | Example |
|------|-------------|---------|
| Single | One parent, one child | `Dog extends Animal` |
| Multilevel | Chain of inheritance | `Dog extends Mammal extends Animal` |
| Hierarchical | One parent, multiple children | `Email extends Notification`, `SMS extends Notification` |

## When to Use Inheritance

- Clear "is-a" relationship (EmailNotification **is a** Notification)
- Shared behavior to inherit
- Not just for code reuse (prefer composition otherwise)

## Practical Example: Notification System

```java
public abstract class Notification {
    protected String recipient;
    protected String message;
    protected long timestamp;

    public Notification(String recipient, String message) {
        this.recipient = recipient;
        this.message = message;
        this.timestamp = System.currentTimeMillis();
    }

    public String formatHeader() {
        return "To: " + recipient + " at " + timestamp;
    }

    public abstract void send();
}

public class EmailNotification extends Notification {
    private String subject;

    public EmailNotification(String recipient, String message, String subject) {
        super(recipient, message);
        this.subject = subject;
    }

    @Override
    public void send() { /* Email sending */ }
}

public class SMSNotification extends Notification {
    private static final int MAX_LENGTH = 160;

    public SMSNotification(String recipient, String message) {
        super(recipient, message);
    }

    @Override
    public void send() {
        // Handle 160 char limit internally
    }
}

public class PushNotification extends Notification {
    private String deviceToken;
    private int priority;

    public PushNotification(String recipient, String message, String deviceToken) {
        super(recipient, message);
        this.deviceToken = deviceToken;
    }

    @Override
    public void send() { /* Push sending */ }
}
```

### Benefits

1. **Shared logic written once** — `formatHeader()` inherited by all
2. **Each child encapsulates complexity** — SMS handles char limit, Push handles tokens
3. **Adding new channels simple** — New class extends Notification

## Related Concepts

[[Class]], [[Polymorphism]], [[Composition]], [[Single Responsibility Principle]]