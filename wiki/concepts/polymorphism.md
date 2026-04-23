---
title: "Polymorphism"
type: concept
tags: [oop, pillars, many-forms]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Polymorphism

**Definition:** "Many forms" — allows objects of different types to be treated through a common interface, with each type providing its own behavior.

## Two Types

### Compile-Time (Method Overloading)
Same method name, different parameters:
```java
class Calculator {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}
```

### Runtime (Method Overriding)
Same method signature, different implementations in child classes.

## Runtime Polymorphism Example

```java
public interface NotificationChannel {
    void send(String recipient, String message);
}

public class EmailChannel implements NotificationChannel {
    @Override
    public void send(String recipient, String message) {
        System.out.println("Email to " + recipient + ": " + message);
    }
}

public class SlackChannel implements NotificationChannel {
    @Override
    public void send(String recipient, String message) {
        System.out.println("Slack to #" + recipient + ": " + message);
    }
}

public class SmsChannel implements NotificationChannel {
    @Override
    public void send(String recipient, String message) {
        System.out.println("SMS to " + recipient + ": " + message);
    }
}

// Polymorphism in action
List<NotificationChannel> channels = List.of(
    new EmailChannel(), new SlackChannel(), new SmsChannel()
);

for (NotificationChannel channel : channels) {
    channel.send("ops-team", "Server CPU above 90%");
}
```

## Why It Matters

The loop doesn't know or care whether it's sending email, Slack, or SMS. Call `send()`, right implementation runs automatically. Adding `PagerDutyChannel` works without changing the loop.

## Related Concepts

[[Interface]], [[Inheritance]], [[Method Overriding]], [[Duck Typing]]