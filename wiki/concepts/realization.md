---
title: "Realization"
type: concept
tags: [oop, relationships, contract]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Realization

**Definition:** The relationship between an interface and the class that implements it. The class "realizes" the contract by providing concrete implementations of all interface methods.

## Role

Realization is the bridge between abstract contracts and concrete behavior. It enables polymorphism through interfaces.

## Code Example

```java
public interface CacheStore {
    void put(String key, String value, int ttlSeconds);
    String get(String key);
    void evict(String key);
}

public class RedisCache implements CacheStore {
    private String connectionUrl;

    @Override
    public void put(String key, String value, int ttlSeconds) {
        // Redis SETEX command
        System.out.println("Redis SET " + key + " EX " + ttlSeconds);
    }

    @Override
    public String get(String key) {
        // Redis GET command
        System.out.println("Redis GET " + key);
        return null;
    }

    @Override
    public void evict(String key) {
        // Redis DEL command
        System.out.println("Redis DEL " + key);
    }
}
```

## Why It Matters

Application code depends on `CacheStore`:
- Use Redis in production
- Use in-memory Map in tests
- Swap to Memcached later

**None of this changes calling code** — only the configuration.

## Realization vs Inheritance

| Aspect | Realization | Inheritance |
|--------|-------------|-------------|
| From | Interface | Class |
| What inherits | Method signatures | Fields + methods |
| Relationship | "Implements" | "Extends" |
| Purpose | Contract fulfillment | Code reuse |

## Related Concepts

[[Interface]], [[Polymorphism]], [[Contract Pattern]], [[Inheritance]]