---
title: "Aggregation"
type: concept
tags: [oop, relationships, has-a]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know", "algomaster.io/learn/lld/aggregation"]
---

# Aggregation

**Definition:** A "Has-A" relationship where the whole contains parts, but **parts can exist independently** of the whole.

## Real-World Example

Team ↔ Microservice:
- A team owns multiple microservices
- If the team is reorganized, the services don't disappear
- Services get reassigned, not deleted

## UML Representation

- **Symbol**: Hollow diamond (◇) on containing class side + solid line
- **Direction**: From containing class to contained class

| Symbol | Meaning |
|--------|---------|
| ◇ (hollow) | Aggregation (independent parts) |
| ◆ (filled) | Composition (dependent parts) |
| Solid line | Association (knows-about) |

## Code Example

```java
public class Team {
    private String name;
    private List<Microservice> services;

    public Team(String name) {
        this.name = name;
        this.services = new ArrayList<>();
    }

    // Services passed in from outside - created independently
    public void addService(Microservice service) {
        services.add(service);
    }

    public void removeService(Microservice service) {
        services.remove(service);
    }
}

public class Microservice {
    private String name;
    private String repoUrl;
    // Service has its own lifecycle
}

// Microservice exists independently
Microservice paymentService = new Microservice("payment-service", "github.com/org/payments");

// Team references but doesn't own
Team platformTeam = new Team("Platform");
platformTeam.addService(paymentService);

// Service can be reassigned
Team checkoutTeam = new Team("Checkout");
checkoutTeam.addService(paymentService);  // Reassigned, not recreated
```

## Aggregation vs Composition vs Association

| Aspect | Association | Aggregation | Composition |
|--------|------------|-------------|-------------|
| Relationship | "Knows-about" | "Has-A" | "Owns-A" |
| Coupling | Loosest | Moderate | Tightest |
| Lifecycle | Independent | Independent | Parts die with whole |
| UML Symbol | Solid line | ◇ (hollow diamond) | ◆ (filled diamond) |
| Creation | Both created separately | Parts created outside | Whole creates parts |
| Reassignment | N/A | Allowed | Not applicable |

## Comparison with Code

```java
// Aggregation: part passed in, can be reassigned
Team team = new Team("Platform");
Microservice svc = new Microservice("payment");
team.addService(svc);  // svc created externally

// Another team can use the same service
Team other = new Team("Checkout");
other.addService(svc);  // Reassigned, not recreated
```

## Related Concepts

[[Association]], [[Composition]], [[Has-A Relationship]]