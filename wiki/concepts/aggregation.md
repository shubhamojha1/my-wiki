---
title: "Aggregation"
type: concept
tags: [oop, relationships, has-a]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Aggregation

**Definition:** A specialized form of association representing a "has-a" relationship where the whole contains parts, but **parts can exist independently** of the whole.

## Real-World Example

Team ↔ Microservice:
- A team owns multiple microservices
- If the team is reorganized, the services don't disappear
- Services get reassigned, not deleted

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

## Aggregation vs Composition

| Aspect | Aggregation | Composition |
|--------|-------------|-------------|
| Part existence | Independent | Dependent on whole |
| Lifecycle | Parts survive whole | Parts die with whole |
| Creation | Parts created outside | Whole creates parts |
| Reassignment | Allowed | Not applicable |

## Related Concepts

[[Association]], [[Composition]], [[Has-A Relationship]]