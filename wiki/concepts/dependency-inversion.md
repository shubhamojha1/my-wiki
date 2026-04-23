---
title: "Dependency Inversion Principle"
type: concept
tags: [solid, oop, design-principles]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/dip"]
---

# Dependency Inversion Principle (DIP)

**Definition:** 
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

## The "Inversion"

The **direction of dependency** is inverted:

```
Without DIP:
[High-Level] ──────▶ [Low-Level]
   (depends on)      (concrete)

With DIP:
[High-Level] ──────▶ [Abstraction] ◀────── [Low-Level]
   (depends on)      (interface)     (implements)
```

## Wrong Way: Low-Level Defines Interface

```java
// GmailClient defines its own interface
public class GmailClient {
    public interface IGmailClient {
        void sendEmail(String to, String body);
    }
}

// High-level module tied to Gmail's namespace
public class EmailService {
    private IGmailClient gmailClient;  // Tied to Gmail!
}
```

**Problem:** High-level module is still coupled to low-level module's namespace.

## Right Way: High-Level Defines Interface

```java
// Interface defined in shared/neutral module
public interface EmailClient {
    void send(String to, String body);
}

// High-level module defines what it needs
public class EmailService {
    private EmailClient emailClient;
    
    public EmailService(EmailClient emailClient) {
        this.emailClient = emailClient;
    }
    
    public void sendNotification(String user, String message) {
        emailClient.send(user, message);
    }
}

// Low-level modules implement the abstraction
public class GmailClientImpl implements EmailClient {
    @Override
    public void send(String to, String body) {
        // Gmail-specific implementation
    }
}

public class OutlookClientImpl implements EmailClient {
    @Override
    public void send(String to, String body) {
        // Outlook-specific implementation
    }
}
```

## Dependency Injection

The wiring happens outside, typically near `main()` or in a DI framework:

```java
// Only place that knows concrete classes
EmailClient client = new GmailClientImpl();
EmailService service = new EmailService(client);
```

## Key Points

1. **Abstractions defined by high-level** — What is needed, not how
2. **Source code dependency inverted** — Both depend on interface
3. **Low-level implements abstraction** — Adapts to high-level's needs
4. **Wiring in one place** — Configuration-driven behavior

## Related Concepts

[[Interface]], [[Dependency Injection]], [[SOLID]], [[Loose Coupling]]