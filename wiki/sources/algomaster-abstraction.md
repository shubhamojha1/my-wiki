---
title: "Abstraction"
type: source
tags: [lld, oop, complexity-hiding]
created: 2026-04-23
sources: ["algomaster.io/learn/lld/abstraction"]
---

# Abstraction

**Author:** Ashish Pratap Singh  
**Source:** [algomaster.io/learn/lld/abstraction](https://algomaster.io/learn/lld/abstraction)  
**Updated:** February 12, 2026

## Summary

This article covers abstraction — hiding implementation details and exposing only essential features. It demonstrates abstraction through abstract classes, interfaces, and public APIs using a media player example.

## Why Abstraction Matters

- **Manages complexity** — Users see simple interface, not internal details
- **Enables change** — Implementation can change without breaking callers
- **Decouples** — High-level code depends on abstractions, not details

## How Abstraction Is Achieved

### 1. Abstract Classes

A blueprint with both abstract (no implementation) and concrete methods:

```java
public abstract class MediaPlayer {
    // Abstract methods - subclasses must implement
    public abstract void play();
    public abstract void pause();
    public abstract void stop();

    // Concrete methods - inherited for free
    public void displayStatus() {
        System.out.println("Status: " + getClass().getSimpleName());
    }

    public void logAction(String action) {
        System.out.println("User action: " + action);
    }
}

public class AudioPlayer extends MediaPlayer {
    public void play() { System.out.println("Playing audio"); }
    public void pause() { System.out.println("Pausing audio"); }
    public void stop() { System.out.println("Stopping audio"); }
}
```

### 2. Interfaces

Contracts without implementation (Java 8+ has default methods):

```java
public interface PaymentProcessor {
    boolean process(double amount);
    boolean refund(String transactionId);
}
```

### 3. Public APIs

Simplified interface for external consumers:

```java
// Simple API, hides complexity
public class StripeGateway {
    public PaymentResult process(double amount) {
        // 50 lines of HTTP, retry logic, logging hidden
        return new PaymentResult(true, "txn_123");
    }
}
```

## Abstraction vs Encapsulation

| Aspect | Abstraction | Encapsulation |
|--------|-------------|---------------|
| What hides | Implementation details | Internal data |
| How | Abstract classes, interfaces | Private fields |
| Goal | Simple interface | Data protection |
| Level | High-level design | Low-level code |

## Practical Example: Media Player

```java
public class PlayerController {
    private MediaPlayer player;

    public PlayerController(MediaPlayer player) {
        this.player = player;
    }

    public void play() {
        player.play();
        player.displayStatus();
    }
}

// Controller works with any MediaPlayer
PlayerController controller = new PlayerController(new AudioPlayer());
controller.play();  // Works!

controller = new PlayerController(new VideoPlayer());
controller.play();  // Still works! No controller changes
```

### Benefits

1. **Controller is player-agnostic** — No imports of specific players
2. **Shared behavior written once** — In abstract class
3. **Each player encapsulates complexity** — Controller doesn't know details

## Related Concepts

[[Abstract Class]], [[Interface]], [[Public API]], [[Encapsulation]]