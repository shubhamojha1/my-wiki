---
title: "YAGNI Principle"
type: concept
tags: [lld, design-principles]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/yagni"]
---

# YAGNI Principle

**Definition:** "You Aren't Gonna Need It" — Don't build features or add flexibility until you're absolutely sure you need them.

## What It Means

- Don't build speculative features
- Don't add abstraction layers upfront
- Only implement what's required now
- Deliver simplest thing that works

## Origin

From **Extreme Programming (XP)** — an Agile methodology built on the idea that requirements change constantly. Building for predicted futures is wasteful.

## Violating YAGNI

### Over-Engineered (Violation)

```java
// Built "future" features that never came
public interface MediaHandler {}
public interface CloudStorageAdapter extends MediaHandler {}

public class ImageProcessor {
    public void processImage(Image img) { }
    public void uploadToCloud(Object data) { }  // unused
}
```

### Simple (YAGNI Applied)

```java
// Just what's needed now
public class ImageProcessor {
    public void resize(Image img, int width, int height) { }
    public void store(Image img) { }
}
```

## When Planning Ahead is OK

- **Known constraints** — regulations, contracts
- **Real requirements** — not "what if" scenarios
- Hard-to-change decisions

## Related Principles

[[DRY Principle]], [[KISS Principle]]