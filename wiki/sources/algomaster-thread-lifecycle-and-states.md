---
title: "Thread Lifecycle and States"
type: source
tags: [thread, lifecycle, state, interview]
created: 2026-04-24
sources: []
---

# Thread Lifecycle and States

**Source:** [AlgoMaster.io - Thread Lifecycle and States](https://algomaster.io/learn/concurrency-interview/thread-lifecycle-and-states)

**Author:** Ashish Pratap Singh

## What is Thread Lifecycle?

A thread's lifecycle is the sequence of states it passes through from creation to termination.

> Employee analogy: Hired (created) → Onboarding (ready) → Working (running) → Waiting for resources (blocked) → Left company (terminated).

A thread doesn't run continuously—it moves between states: ready, running, blocked, waiting, terminated.

## The Thread States

From Java's `Thread.State` enum:

| State | Description | Entry Methods |
|-------|-------------|---------------|
| **NEW** | Created but not started | `new Thread()` |
| **RUNNABLE** | Ready to run, waiting for CPU | `start()` |
| **BLOCKED** | Waiting for monitor lock | `synchronized` contention |
| **WAITING** | Waiting indefinitely | `wait()`, `join()`, `park()` |
| **TIMED_WAITING** | Waiting with timeout | `sleep()`, `wait(timeout)` |
| **TERMINATED** | Finished execution | `run()` completes |

## State Transitions

| From | To | Trigger |
|------|-----|---------|
| NEW | RUNNABLE | `start()` |
| RUNNABLE | RUNNING | Scheduler assigns CPU |
| RUNNING | RUNNABLE | Time slice expires, `yield()` |
| RUNNING | BLOCKED | Acquire held lock |
| RUNNING | WAITING | `wait()`, `join()` |
| RUNNING | TIMED_WAITING | `sleep()`, `wait(timeout)` |
| RUNNING | TERMINATED | Exception or completion |
| BLOCKED | RUNNABLE | Lock acquired |
| WAITING | RUNNABLE | `notify()`, `join()` completes |
| TIMED_WAITING | RUNNABLE | Timeout or notified |

## Key Insights

- **RUNNABLE** ≠ currently executing. It means eligible to run from JVM's perspective—the OS may or may not be running it on a CPU.
- **BLOCKED** specifically means waiting for a monitor lock (synchronized).
- **WAITING** is indefinite—no timeout.
- **TIMED_WAITING** has a bounded wait period.

## Related Concepts

- [[Thread Lifecycle]] — Concept page
- [[algomaster-Processes vs Threads]]
- [[Thread Safety]]
- [[Race Conditions]]