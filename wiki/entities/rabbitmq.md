---
title: "RabbitMQ"
type: entity
tags: [tool, infrastructure, message-queue]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# RabbitMQ

**Type:** Message queue / broker  
**Website:** [rabbitmq.com](http://www.rabbitmq.com/)

## Overview

RabbitMQ is an open-source message broker implementing the AMQP (Advanced Message Queuing Protocol). It enables loose coupling between services by allowing applications to publish messages to a queue for asynchronous processing.

## Role in Offline Processing

RabbitMQ allows web applications to:
1. Publish messages quickly to a queue
2. Return control to the user immediately
3. Have separate consumers process messages asynchronously

This decouples slow operations from the request-response timeline.

## Common Patterns

### Pure Offline (Schedule Only)
```python
# Web app: schedule task and inform user
queue.publish({"task": "send_email", "user_id": 123})
return {"status": "scheduled", "check_at": "/status/abc"}
```

### Optimistic Inline (Appear Complete)
```python
# Web app: do minimal work inline
post_tweet(tweet)
queue.publish({"task": "update_followers", "tweet_id": 456})
return {"status": "posted"}
# Followers see update after delay
```

## Benefits

- **Decoupled processing** — producers and consumers independent
- **Load leveling** — smooths burst traffic
- **Fault tolerance** — messages persist until processed
- **Separate resource pools** — worker machines can be scaled independently

## Architecture

```
[Web App] --> [RabbitMQ] --> [Worker Pool 1] (email processing)
                    |
                    +--> [Worker Pool 2] (analytics)
                    |
                    +--> [Worker Pool 3] (notifications)
```

## Related Concepts

[[Message Queue]], [[Offline Processing]], [[Scheduling Periodic Tasks]], [[Load Balancing]]