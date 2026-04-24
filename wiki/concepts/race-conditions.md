---
title: "Race Conditions"
type: concept
tags: [concurrency, race-condition, thread-safety]
created: 2026-04-24
sources: [introduction-to-concurrency]
---

# Race Conditions

A **race condition** occurs when a program's behavior depends on the timing of uncontrolled events (thread interleaving), producing incorrect results.

## Definition

From AlgoMaster: Race conditions happen when "concurrent access to shared data produces incorrect results" — the outcome depends on which thread executes first.

## Classic Example: Bank Account

```python
# Two threads executing concurrently
def withdraw(amount):
    balance = get_balance()  # Thread reads current balance
    balance -= amount     # Thread calculates
    set_balance(balance)  # Thread writes new balance

# Both threads read balance=100, both write balance=80
# Expected: 100 - 50 - 30 = 20
# With race: 100 - 50 = 50, then 100 - 30 = 70 (wrong!)
```

## Types of Race Conditions

### Read-Modify-Write
```python
counter = counter + 1  # Not atomic: read, add, write
```

### Check-Then-Act
```python
if resource_available:  # Check
    allocate(resource)    # Act (but another thread may have taken it)
```

## Conditions for Race

1. **Mutual exclusion** — Multiple threads access same data
2. **At least one write** — Not purely read-only
3. **No synchronization** — Uncoordinated access timing

## Prevention

- **Mutual exclusion** — Only one thread in critical section
- **Memory barriers** — Ensures visibility between threads
- **Atomic operations** — Interlocked read-modify-write

## Related

- [[Critical Sections]] — Code accessing shared resources
- [[Thread Safety]] — Correct behavior under concurrency
- [[Processes vs Threads]] — Where races occur
- [[Introduction to Concurrency]]