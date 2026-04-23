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
[Web App] ──publish──▶ [Queue] ──consume──▶ [Workers]
     │                                        │
     └── Fast response to user               └── Process asynchronously
```

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
4. **Fault tolerance** — Messages persist until processed
5. **Priority handling** — Different queues for different urgency levels

## Queue Systems

- **RabbitMQ** — AMQP implementation, flexible routing
- **Kafka** — High-throughput log-based messaging
- **Amazon SQS** — Managed queue service
- **Redis Streams** — Lightweight stream processing

## Architectural Considerations

| Consideration | Recommendation |
|---------------|-----------------|
| Message durability | Persist messages to disk |
| Consumer scalability | Horizontal worker scaling |
| Error handling | Dead letter queues, retries |
| Ordering | Decide if order matters |

## Related Concepts

[[Offline Processing]], [[Scheduling Periodic Tasks]], [[RabbitMQ]], [[Load Balancing]]