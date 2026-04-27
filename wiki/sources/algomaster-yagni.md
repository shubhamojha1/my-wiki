---
title: "AlgoMaster: YAGNI Principle"
type: source
tags: [lld, design-principles]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/yagni"]
author: Ashish Pratap Singh
---

# YAGNI Principle

**Source:** AlgoMaster.io Low-Level Design Course — YAGNI Chapter

## Definition

**YAGNI** = "You Aren't Gonna Need It"

> YAGNI is a principle that encourages you to resist the temptation to build features or add flexibility until you are absolutely sure you need them.

---

## Origin

The principle comes from **Extreme Programming (XP)**, one of the earliest Agile methodologies. XP was built around the idea that software requirements change constantly, so spending time building for predicted futures is wasteful.

---

## What YAGNI Means

1. **Don't build speculative features** — Only implement what's required now
2. **Don't add abstraction layers upfront** — Wait until real need justifies them
3. **Deliver simplest thing that works** — Iterate from there

> There's a big difference between writing clean, well-structured code for today's needs and over-engineering for tomorrow's imagined ones.

---

## Violating YAGNI

### Before (Over-Engineered)

```java
// Built support for "future" requirements that never came
public interface MediaHandler {}
public interface ImageHandler extends MediaHandler {}
public interface VideoHandler extends MediaHandler {}
public interface CloudStorageAdapter extends MediaHandler {}

public class MediaProcessor {
    // Multiple empty stubs
    public void processImage(Image img) { /* ... */ }
    public void processVideo(Video vid) { /* ... */ }
    public void uploadToCloud(Object data) { /* built but unused */ }
}
```

### After (YAGNI Applied)

```java
// Simple, meets today's requirements
public class ImageProcessor {
    public void resize(Image img, int width, int height) {
        // Actual implementation for today's need
    }
    
    public void store(Image img) {
        // Store locally for today's need
    }
}
```

> Meets today's requirements completely, easy to read/test/debug, can be extended later when real need arises.

---

## When to Violate YAGNI

YAGNI isn't absolute. Sometimes planning ahead is justified:

1. **Known constraints** — Regulations, contractual obligations
2. **Real requirements** — Not "what if" scenarios
3. **Architectural decisions** — Things that are hard to change later

The key is distinguishing:
- **Speculative features** — Driven by "what if" (skip)
- **Known constraints** — Driven by real requirements (plan)

---

## YAGNI vs Other Principles

| Principle | Meaning |
|-----------|---------|
| DRY | Don't repeat logic |
| KISS | Don't make solution harder than necessary |
| YAGNI | Don't build for requirements that don't exist yet |

---

## Key Takeaways

1. **YAGNI** = Don't build features until you need them
2. Focus on **today's requirements**, not tomorrow's speculation
3. Good code = clean structure for now, extensible when needed
4. Distinguish **speculative** vs **known** requirements