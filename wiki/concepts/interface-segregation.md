---
title: "Interface Segregation Principle"
type: concept
tags: [solid, oop, design-principles]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/isp"]
---

# Interface Segregation Principle (ISP)

**Definition:** Clients should not be forced to depend on methods they do not use. Keep interfaces small, focused, and specific to what each client actually needs.

## The Problem: Fat Interfaces

A "fat" interface forces implementers to provide methods they don't need:

```java
// Fat interface - forces all methods on every implementer
public interface MediaPlayer {
    void playAudio();
    void playVideo();
    void streamLiveVideo();
    void downloadContent();
}

// SilentVideoPlayer doesn't play audio, but must implement it
public class SilentVideoPlayer implements MediaPlayer {
    public void playAudio() {
        throw new UnsupportedOperationException();  // Bad!
    }
    
    public void playVideo() { /* ... */ }
    public void streamLiveVideo() { /* ... */ }
    public void downloadContent() { /* ... */ }
}
```

## The Solution: Small, Focused Interfaces

Split fat interfaces into specific ones:

```java
// Focused interfaces
public interface AudioPlayer {
    void playAudio();
}

public interface VideoPlayer {
    void playVideo();
    void streamLiveVideo();
}

public interface Downloadable {
    void downloadContent();
}

// Players implement only what they need
public class SilentVideoPlayer implements VideoPlayer {
    public void playVideo() { /* ... */ }
    public void streamLiveVideo() { /* ... */ }
}

// ModernAudioPlayer needs both
public class ModernAudioPlayer implements AudioPlayer, Downloadable {
    public void playAudio() { /* ... */ }
    public void downloadContent() { /* ... */ }
}
```

## Benefits

1. **No empty methods** — Implementers only define what's relevant
2. **No UnsupportedOperationException** — No fake implementations
3. **LSP compliance** — Clean substitutability
4. **Reduced coupling** — Classes only know about what they use
5. **Composable** — Classes pick up only what they can honor

## Before vs After

| Aspect | Fat Interface | Segregated Interfaces |
|--------|--------------|---------------------|
| Implementers | Force-fitted | Fit naturally |
| Unused methods | Empty or exception | Don't exist |
| Coupling | High | Low |
| Testing | Harder | Easier |

## Related Concepts

[[Interface]], [[SOLID]], [[Liskov Substitution Principle]], [[Single Responsibility Principle]]