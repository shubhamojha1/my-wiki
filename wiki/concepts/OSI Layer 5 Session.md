---
title: "OSI Layer 5: Session"
type: concept
tags: [osi-model, networking, layer-5]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-osi-model"]
---

# OSI Layer 5: Session

**Layer 5** (the Session layer) manages the **dialogues** between applications — establishing, coordinating, and terminating conversations. It sits above the raw transport connection (Layer 4) and below data formatting (Layer 6).

## Responsibilities

| Function | Description |
|----------|-------------|
| **Session establishment** | Negotiate parameters and open a session before data exchange begins |
| **Session maintenance** | Keep the session alive; handle keep-alives and heartbeats |
| **Checkpointing** | Mark points in a long data transfer so a failure can resume from the last checkpoint rather than restarting |
| **Session teardown** | Orderly close of the session when transfer is complete |
| **Authentication** | Some layer-5 protocols handle login/authentication as part of session setup |
| **Dialog control** | Half-duplex (token passing — only one side sends at a time) vs full-duplex |

## Practical Reality

The OSI model is a conceptual reference. In the TCP/IP world, Layers 5, 6, and 7 are collapsed into the Application layer. Session semantics are handled by:

- **TLS**: Negotiates a secure session (TLS handshake), maintains session tickets for resumption after reconnection.
- **HTTP cookies / JWT**: Application-level session identifiers tracking user state across stateless HTTP requests.
- **WebSockets**: Maintain a persistent session over a single upgraded HTTP connection.
- **SIP** (VoIP): Explicitly manages call sessions — setup, hold, transfer, teardown.
- **NFS, SMB**: File-sharing protocols that track open sessions and file locks.

## Checkpointing Example

```
Long file transfer (10 GB):
  T=0:   Session established, transfer begins
  T=5m:  Checkpoint at 2 GB
  T=10m: Checkpoint at 4 GB
  T=11m: Network failure!
  T=12m: Reconnect — resume from 4 GB checkpoint (not start)
```

Without checkpointing, every failure requires restarting from byte 0.

## Position in OSI Stack

```
Layer 7  Application
Layer 6  Presentation
Layer 5  Session      ← session lifecycle, checkpoints
Layer 4  Transport    (TCP/UDP connections)
Layer 3  Network
Layer 2  Data Link
Layer 1  Physical
```

## Related Concepts

- [[OSI Model]] — the full 7-layer framework
- [[OSI Layer 4: Transport]] — provides the underlying connection Session uses
- [[OSI Layer 6: Presentation]] — data format/encryption layer above Session
- [[TLS]] — handles session establishment and resumption in modern stacks
- [[WebSocket]] — maintains a persistent application session
