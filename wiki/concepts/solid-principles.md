---
title: "SOLID Principles"
type: concept
tags: [oop, design-principles, solid]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/dip", "algomaster.io/learn/lld/isp", "blog.algomaster.io/p/solid-principles-explained-with-code"]
---

# SOLID Principles

**Definition:** Five object-oriented design principles for writing maintainable, flexible, and scalable code. Coined by Robert C. Martin (Uncle Bob).

## The Five Principles

| Letter | Principle | Focus |
|--------|-----------|-------|
| **S** | Single Responsibility | One reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must be substitutable |
| **I** | Interface Segregation | Small, focused interfaces |
| **D** | Dependency Inversion | Depend on abstractions |

## 1. Single Responsibility Principle (SRP)

A class should have only one reason to change.

```java
// Bad: Two reasons to change (formatting + saving)
public class Employee {
    public String formatReport() { ... }
    public void saveToDatabase() { ... }
}

// Good: Separate responsibilities
public class ReportFormatter { ... }
public class EmployeeRepository { ... }
```

## 2. Open/Closed Principle (OCP)

Entities should be open for extension, closed for modification.

```java
// Extend behavior without modifying existing code
public abstract class Shape {
    abstract double area();
}

public class Circle extends Shape {
    double radius;
    double area() { return Math.PI * radius * radius; }
}

public class Rectangle extends Shape {
    double width, height;
    double area() { return width * height; }
}
```

## 3. Liskov Substitution Principle (LSP)

Objects of a superclass should be replaceable with objects of subclasses without breaking the application.

```java
// Rectangle can be substituted anywhere Square is expected?
public class Rectangle {
    public void setWidth(double w) { this.width = w; }
    public void setHeight(double h) { this.height = h; }
}

public class Square extends Rectangle {
    // Setting width changes both - violates LSP!
    public void setWidth(double w) {
        super.setWidth(w);
        super.setHeight(w);
    }
}
```

## 4. Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods they do not use.

```java
// Split fat interface into specific ones
public interface Printer { void print(); }
public interface Scanner { void scan(); }

public class SimplePrinter implements Printer { ... }
public class MultiFunctionDevice implements Printer, Scanner { ... }
```

## 5. Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions.

```java
// Bad: High depends directly on low
public class EmailService {
    private GmailClient gmail = new GmailClient();  // Tight coupling
}

// Good: Both depend on abstraction
public interface EmailClient { void send(String to, String body); }
public class EmailService {
    private EmailClient client;  // Depends on interface
}
```

## Quick Reference

| Principle | Key Question |
|-----------|-------------|
| SRP | Does this class have one job? |
| OCP | Can I add features without changing existing code? |
| LSP | Can I substitute subclasses everywhere? |
| ISP | Am I implementing unused methods? |
| DIP | Do high-level modules depend on abstractions? |

## Related Concepts

[[Single Responsibility Principle]], [[Open/Closed Principle]], [[Liskov Substitution Principle]], [[Interface Segregation Principle]], [[Dependency Inversion Principle]]