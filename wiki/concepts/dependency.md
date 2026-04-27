---
title: "Dependency"
type: concept
tags: [oop, relationships, uses-a]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know", "algomaster.io/learn/lld/dependency"]
---

# Dependency

**Definition:** The weakest relationship between classes. A temporary "uses-a" connection where one class uses another for a brief moment (**method parameter, local variable, or return type**) but **doesn't hold a long-term reference**.

## Real-World Example

Deployment Pipeline ↔ Logger:
- Pipeline uses logger to record what happens
- Pipeline doesn't own the logger
- Logger isn't part of pipeline's state
- Just used during execution, then relationship ends

## UML Representation

- **Symbol**: Dashed arrow (`..->`)
- **Direction**: From dependent class to class it depends on

```
ClassA  ..->  ClassB
```

| Symbol | Relationship |
|--------|--------------|
| `..->` | Dependency (dashed) |
| `---` | Association (solid) |
| `◇---` | Aggregation |
| `◆---` | Composition |

## Code Example

```java
public class DeploymentService {
    // Dependency: uses HttpClient temporarily
    public DeploymentResult deploy(String serviceName, String version, HttpClient client) {
        String url = "https://deploy.internal/" + serviceName;
        HttpResponse response = client.post(url, Map.of("version", version));

        if (response.getStatusCode() == 200) {
            return new DeploymentResult(true, "Deployed " + serviceName + " v" + version);
        }
        return new DeploymentResult(false, "Deployment failed");
    }
}

public class HttpClient {
    public HttpResponse post(String url, Map<String, String> body) {
        System.out.println("POST " + url);
        return new HttpResponse(200, "OK");
    }
}

// DeploymentService uses HttpClient but doesn't store it
DeploymentService deployer = new DeploymentService();
HttpClient client = new HttpClient();
deployer.deploy("payment-service", "2.4.1", client);
```

## Characteristics

| Aspect | Description |
|--------|-------------|
| Duration | Ephemeral (during method call) |
| Reference | Not stored as field |
| Direction | One-way (dependent class uses dependency) |
| Coupling | Temporary, loose |

## Full Comparison

| Aspect | Dependency | Association | Aggregation | Composition |
|--------|------------|-------------|-------------|-------------|
| Relationship | "Uses-A" | "Knows-about" | "Has-A" | "Owns-A" |
| Reference | None | Held as field | Held as field | Held as field |
| UML | `..->` (dashed) | `---` (solid) | `◇---` | `◆---` |
| Coupling | Loosest | Loose | Moderate | Tightest |

## Related Concepts

[[Association]], [[Aggregation]], [[Composition]], [[Dependency Injection]], [[Loose Coupling]]