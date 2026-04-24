---
title: "Thread Lifecycle"
type: concept
tags: [thread, lifecycle, state]
created: 2026-04-24
sources: [algomaster-thread-lifecycle-and-states]
---

# Thread Lifecycle

A thread moves through different states from creation to termination.

## Java Thread States

| State | Description | Trigger |
|-------|-------------|---------|
| **NEW** | Created but not started | `Thread t = new Thread()` |
| **RUNNABLE** | Ready to run, waiting for CPU | `start()` called |
| **RUNNING** | Actively executing on CPU | Scheduler assigns core |
| **BLOCKED** | Waiting for monitor lock | `synchronized` contention |
| **WAITING** | Waiting indefinitely | `wait()`, `join()`, `park()` |
| **TIMED_WAITING** | Waiting with timeout | `sleep()`, `wait(timeout)` |
| **TERMINATED** | Finished execution | `run()` completes |

## Employee Analogy

- **NEW** → Hired
- **READY/RUNNABLE** → Onboarding, ready to work
- **RUNNING** → Actively working
- **BLOCKED/WAITING** → Waiting for resources/approvals
- **TERMINATED** → Left company

## State Transitions

```
NEW → RUNNABLE (start())
RUNNABLE → RUNNING (scheduler assigns CPU)
RUNNING → RUNNABLE (time slice expires, yield())
RUNNING → BLOCKED (try to acquire held lock)
RUNNING → WAITING (wait(), join())
RUNNING → TIMED_WAITING (sleep(), wait(timeout))
RUNNING → TERMINATED (run() completes, exception)
BLOCKED → RUNNABLE (lock acquired)
WAITING → RUNNABLE (notify(), join() completes)
TIMED_WAITING → RUNNABLE (timeout, notified)
```

## Key Concepts

- **RUNNABLE** ≠ "currently on CPU" — means eligible to run from JVM's perspective
- **BLOCKED** — specifically waiting for monitor lock (`synchronized`)
- **WAITING** — indefinite wait (no timeout)
- **TIMED_WAITING** — bounded wait with timeout

## Related

- [[algomaster-Processes vs Threads]]
- [[Thread Safety]]
- [[Race Conditions]]
- [[Critical Sections]]