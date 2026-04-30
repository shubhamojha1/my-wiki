---
title: "AlgoMaster: Idempotency"
type: source
tags: [system-design, reliability, distributed-systems]
created: 2026-05-01
sources: [algomaster-idempotency.md]
---

# AlgoMaster: Idempotency

Source: [blog.algomaster.io/p/idempotency-in-distributed-systems](https://blog.algomaster.io/p/idempotency-in-distributed-systems) by Ashish Pratap Singh (Nov 2024).

## Summary

Idempotency is a property of operations where executing the same request multiple times produces the same result as executing it once. This is critical in distributed systems where network failures trigger automatic retries, potentially leading to duplicate charges, messages, or data entries.

## Key Takeaways

### What is Idempotency?
An operation is idempotent if re-applying it has no additional side effects. 
- **GET**: Naturally idempotent (read-only)
- **PUT**: Idempotent (replaces resource with same state)
- **DELETE**: Idempotent (resource deleted once; subsequent deletes are no-ops)
- **POST**: Not naturally idempotent (creates new resource each time) — requires explicit handling via [[Idempotency Key]]

### Strategies to Implement Idempotency

1. **Unique Request Identifiers (Idempotency Key)**
   - Client generates a unique ID (e.g., UUID) per request
   - Server tracks processed IDs; if ID seen before, return cached result instead of re-processing
   - Used by Stripe, PayPal, and payment gateways

2. **Database Design Adjustments (Upsert)**
   - Use `UPSERT` (e.g., SQL `INSERT ... ON CONFLICT`) to update if exists or insert if new
   - Apply unique constraints to prevent duplicate entries
   - Ensures database operations are inherently idempotent

3. **Messaging Systems**
   - Store log of processed message IDs
   - Check `messageId` before processing; ignore if already in `processedMessages` set

### Challenges
- **Performance Overhead**: Storing/checking keys adds latency
- **Distributed Systems**: Requires distributed locking or consensus algorithms for multi-node consistency
- **Time Window**: Determining how long to maintain idempotency guarantees (TTL for keys)
- **Concurrency**: Race conditions between simultaneous duplicate requests

### Best Practices
- Design for idempotency from the start
- Use locks (Redis Redlock) or optimistic concurrency control for concurrent safety
- Implement retry with [[Exponential Backoff]]
- Document which API operations are idempotent
- Test thoroughly with edge cases and failure scenarios
