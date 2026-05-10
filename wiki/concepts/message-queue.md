---
title: "Message Queue"
type: concept
tags: [messaging, async, architecture]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Message Queue

**Definition:** Asynchronous communication channel that allows web applications to publish messages for processing by separate consumers, decoupling slow processing from user requests.

## Architecture

```
[Producer] ──enqueue──▶ [Broker/Queue Manager] ──dequeue──▶ [Consumer]
                                │
                          [Message Store]
```

A **broker** (or queue manager) manages the queue, handles message routing, and ensures delivery.

## Message Structure

Each message contains:
- **Payload**: The actual data being sent
- **Metadata**: Headers, timestamps, priority, message ID

## Message Flow

1. **Create**: Producer generates message with payload and metadata
2. **Enqueue**: Producer sends message to the queue
3. **Store**: Queue stores message (persistent to disk or transient in memory)
4. **Dequeue**: Consumer retrieves message (sequentially, by priority, or in parallel)
5. **Ack**: Consumer sends acknowledgment confirming successful processing
6. **Delete**: Broker removes acknowledged message from the queue

## Queue Types

- **Point-to-Point (P2P)**: One producer, one consumer — task processing
- **Pub/Sub**: One publisher, multiple consumers — broadcasting notifications
- **Priority Queue**: Higher-priority messages processed before lower ones
- **Dead Letter Queue (DLQ)**: Holds messages that fail after max retries for troubleshooting

## Two Processing Patterns

### Pattern 1: Pure Offline
Complete nothing inline; inform user the task will happen later.

```python
# Web app
def create_vm(user_request):
    task_id = queue.publish({
        'action': 'provision_vm',
        'spec': user_request
    })
    return {'status': 'scheduled', 'task_id': task_id}

# UI shows: "Your VM will be ready in a few minutes"
# User polls /tasks/{task_id} to check progress
```

### Pattern 2: Optimistic Inline
Do minimal inline work, finish remaining work async.

```python
# Web app
def post_tweet(tweet):
    # Save tweet immediately
    db.save(tweet)
    # Queue follower updates
    queue.publish({
        'action': 'update_followers',
        'tweet_id': tweet.id
    })
    return {'status': 'posted'}

# User sees tweet instantly
# Followers see it after delay (could be minutes for large accounts)
```

## Benefits

1. **Decoupled processing** — Web app and workers run independently
2. **Load leveling** — Smooths burst traffic
3. **Separate resource pools** — Workers can scale independently
4. **Fault tolerance** — Messages persist until processed; retries on failure
5. **Priority handling** — Different queues for different urgency levels
6. **Throttling** — Controls message processing rate to prevent consumer overload

## When to Use

- **Microservices**: Async communication between services without tight coupling
- **Task scheduling**: Offload background work (image processing, email sending)
- **Event-driven**: Broadcast events to multiple interested consumers
- **Load leveling**: Smooth request spikes by queuing and processing steadily
- **Reliable communication**: Persistent queues survive failures; retry until success

## Best Practices

- **Idempotent consumers**: Handle duplicate messages gracefully
- **Message durability**: Choose persistent vs transient based on criticality
- **Error handling**: Retries with backoff, DLQ for failed messages, alerting
- **Security**: Encryption in transit and at rest, authentication, access control
- **Monitoring**: Track throughput, queue length, consumer lag
- **Scalability**: Plan horizontal consumer scaling and partitioning

## Queue Systems

- **RabbitMQ** — AMQP implementation, flexible routing
- **Kafka** — High-throughput log-based messaging
- **Amazon SQS** — Managed queue service, AWS-integrated
- **Google Cloud Pub/Sub** — Managed, real-time analytics
- **Redis Streams** — Lightweight stream processing
- **ActiveMQ** — Enterprise, multi-protocol broker

## Architectural Considerations

| Consideration | Recommendation |
|---------------|-----------------|
| Message durability | Persist messages to disk |
| Consumer scalability | Horizontal worker scaling |
| Error handling | Dead letter queues, retries |
| Ordering | Decide if order matters |

## Related Concepts

[[Offline Processing]], [[Scheduling Periodic Tasks]], [[RabbitMQ]], [[Load Balancing]]