---
title: "Thread Safety"
type: concept
tags: [concurrency, thread-safety]
created: 2026-04-24
sources: [introduction-to-concurrency]
---

# Thread Safety

**Thread safety** is the property of code that ensures correct behavior when accessed by multiple threads concurrently, without race conditions or data corruption.

## Definition

From the source: "Thread safety means ensuring correct behavior with multiple threads" — the code works correctly regardless of thread interleaving.

## Ensuring Thread Safety

### 1. Don't Share State
```python
# Each thread gets its own copy
def process(item):
    local_cache = {}  # Thread-local, not shared
```

### 2. Share State Read-Only
```python
# Constants are safe to share
CONFIG = {"rate": 0.05}  # Immutable after init
```

### 3. Synchronize Access
```python
# Mutex protects shared state
lock = Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1
```

### 4. Use Atomic Operations
```python
# Atomic by design
from atomic import AtomicInt
counter = AtomicInt(0)
counter.increment()  # Single hardware instruction
```

### 5. Make State Immutable
```python
# Immutable after construction
class Account:
    def __init__(self, balance):
        self._balance = balance  # No setters
    
    @property
    def balance(self):
        return self._balance
```

## Thread Safety Levels

| Level | Description | Example |
|-------|-------------|---------|
| **Immutable** | No mutable state | `final` classes, strings |
| **Thread-local** | Per-thread state | `threading.local()` |
| **Guarded** | Protected by lock | `Lock()`保护的data |
| **Lock-free** | Atomic ops only | `atomic` operations |

## Common Patterns

- **Stateless functions** — Naturally thread-safe
- **Immutable objects** — Can't be corrupted
- **Connection pools** — Thread-safe allocation

## Related

- [[Race Conditions]] — Incorrect behavior without thread safety
- [[Critical Sections]] — Code requiring protection
- [[Processes vs Threads]] — Where sharing occurs
- [[Introduction to Concurrency]]