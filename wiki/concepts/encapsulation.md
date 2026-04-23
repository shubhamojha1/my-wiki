---
title: "Encapsulation"
type: concept
tags: [oop, pillars, data-protection]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Encapsulation

**Definition:** The practice of bundling data and methods together in a class while restricting direct access to internal data. Expose a controlled public interface, hide everything else.

## The Problem: Unprotected Data

```java
public class RateLimiter {
    public int requestCount;       // Anyone can modify
    public long windowStartTime;   // Anyone can reset
    public int maxRequests;
}

// Someone can corrupt the state:
limiter.requestCount = -100;      // Invalid!
limiter.windowStartTime = 0;       // Broken!
```

## Encapsulated Solution

```java
public class RateLimiter {
    private int requestCount;      // Private - no direct access
    private long windowStartTime;  // Private
    private final int maxRequests;
    private final long windowSizeMs;

    public RateLimiter(int maxRequests, long windowSizeMs) {
        this.maxRequests = maxRequests;
        this.windowSizeMs = windowSizeMs;
        this.windowStartTime = System.currentTimeMillis();
    }

    public boolean allowRequest() {
        resetWindowIfExpired();
        if (requestCount < maxRequests) {
            requestCount++;
            return true;
        }
        return false;
    }

    private void resetWindowIfExpired() {
        // Internal logic hidden from callers
    }
}
```

## Benefits

1. **Data protection** — Invalid state impossible
2. **Invariant enforcement** — Business rules enforced by code
3. **Implementation hiding** — Internal changes don't break callers
4. **Reduced complexity** — Callers see simple interface

## Relationship to Abstraction

- Encapsulation hides data
- Abstraction hides complexity
- Both reduce cognitive load on users of your code

## Related Concepts

[[Class]], [[Access Modifiers]], [[Private]], [[Public]], [[Abstraction]]