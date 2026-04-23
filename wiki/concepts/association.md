---
title: "Association"
type: concept
tags: [oop, relationships, knows-about]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Association

**Definition:** A "knows-about" relationship between objects where both exist independently. Neither owns or controls the other.

## Real-World Example

Developer ↔ Repository:
- A developer contributes to multiple repositories
- A repository has multiple contributors
- Deleting a developer doesn't delete the repository
- Archiving a repository doesn't delete the developer

## Code Example

```java
public class Developer {
    private String username;
    private List<Repository> repositories;

    public Developer(String username) {
        this.username = username;
        this.repositories = new ArrayList<>();
    }

    public void contributeTo(Repository repo) {
        repositories.add(repo);
    }
}

public class Repository {
    private String name;
    private List<Developer> contributors;

    public Repository(String name) {
        this.name = name;
        this.contributors = new ArrayList<>();
    }

    public void addContributor(Developer dev) {
        contributors.add(dev);
    }
}

// Both objects created independently
Developer dev = new Developer("alice");
Repository repo = new Repository("payment-service");

// They reference each other, but neither owns the other
dev.contributeTo(repo);
repo.addContributor(dev);
```

## Key Property

**Independence** — Both objects exist outside of each other. Deleting one doesn't affect the other.

## Related Relationships

- Association is the **most general** relationship
- Aggregation and composition are **specialized forms**
- Dependency is **weaker** (temporary usage)

## Related Concepts

[[Aggregation]], [[Composition]], [[Dependency]]