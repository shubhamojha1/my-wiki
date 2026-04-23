---
title: "Abstraction"
type: concept
tags: [oop, pillars, complexity-hiding]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Abstraction

**Definition:** Hiding unnecessary complexity and exposing only what the user needs. While encapsulation hides data, abstraction hides implementation details at a higher level.

## Real-World Analogy

Sending a Slack message:
- You type message → hit send
- Behind scenes: WebSocket management, serialization, retries, delivery confirmation, push notifications
- **You don't deal with any of that** — complexity abstracted behind one action

## Example: Cloud Storage

```java
public abstract class CloudStorage {
    // Simple interface caller uses
    public String upload(String fileName, byte[] data) {
        validate(fileName, data);
        String path = generatePath(fileName);
        String url = doUpload(path, data);  // Provider-specific
        logUpload(fileName, url);
        return url;
    }

    // Each provider implements its own upload logic
    protected abstract String doUpload(String path, byte[] data);

    // Supporting logic hidden from caller
    private void validate(String fileName, byte[] data) { ... }
    private String generatePath(String fileName) { ... }
    private void logUpload(String fileName, String url) { ... }
}

public class S3Storage extends CloudStorage {
    @Override
    protected String doUpload(String path, byte[] data) {
        // AWS SDK calls, multipart upload, encryption...
        return "https://s3.amazonaws.com/bucket/" + path;
    }
}
```

## Abstraction vs Encapsulation

| Aspect | Abstraction | Encapsulation |
|--------|-------------|---------------|
| Hides | Implementation details | Internal data |
| Level | Higher-level interfaces | Lower-level data protection |
| Goal | Simplify interaction | Protect state |
| How | Abstract classes, interfaces | Private fields, public methods |

## Related Concepts

[[Interface]], [[Abstract Class]], [[Encapsulation]], [[Polymorphism]]