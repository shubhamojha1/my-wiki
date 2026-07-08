## [2026-07-08] ingest | Lecture 10. Only a Full Pipeline Run Counts as Real Verification

Ingested Learn Harness Engineering's tenth lecture on why end-to-end testing changes agent behavior, not just defect detection. Created 1 source summary, 3 new concept pages (Architectural Boundary Enforcement Rules, Review Feedback Promotion, Layered Domain Architecture). Recognized the lecture's four unit-test blind-spot categories and unit/integration/e2e validation hierarchy as the same taxonomy already documented from Lecture 09, so folded the one new category (Resource Lifecycle Issues), the alternate test-pyramid framing, and the sharper agent-oriented error message structure directly into Three-Layer Termination Validation instead of creating duplicate pages. Updated OpenAI and Codex entities with the Layered Domain Architecture citation, Capability Gap with the tenth case study (Electron export feature, 0/5 unit-test detection vs 5/5 e2e detection), and Learn Harness Engineering with the lecture-10 summary.

## [2026-07-08] ingest | Lecture 09. Preventing Agents from Declaring Victory Too Early

Ingested Learn Harness Engineering's ninth lecture on premature completion declarations. Created 1 source summary, 6 new concept pages (Premature Completion Declaration, Confidence Calibration Bias — citing Guo et al. 2017 and Anthropic's 2026 self-evaluation research, Worker/Checker Separation, Three-Layer Termination Validation, Verification-Validation Dual Gate, Completion Priority Constraint). Recognized the lecture's planner/generator/evaluator case study as the same experiment already documented from Lecture 01, so updated Harness-Induced Failure and the Anthropic entity with the newly-supplied concrete figures ($9/20min bare vs $200/6hr harnessed) rather than double-counting it. Updated Verification Gap with the sharper framing, Capability Gap with the ninth case study (password-reset feature, 5-10x cost savings from catching defects pre-deployment), and Learn Harness Engineering with the lecture-09 summary.

## [2026-07-08] ingest | Lecture 08. Use Feature Lists to Constrain What the Agent Does

Ingested Learn Harness Engineering's eighth lecture on feature lists as harness primitives. Created 1 source summary, 1 new concept page (Harness Primitive — the documents-vs-primitives distinction and the four dependent harness components). Recognized this lecture's Feature State Machine as the same underlying artifact as Lecture 07's Scope Surface rather than a competing structure, so folded the concrete state names (not_started/active/blocked/passing), pass-state gating, and back-pressure mechanism directly into Scope Surface, Completion Evidence (triple structure + evidence field), and WIP Limit instead of creating duplicate pages. Updated Capability Gap with the eighth case study (45% higher feature completion, zero duplicate implementations) and Learn Harness Engineering with the lecture-08 summary.

## [2026-07-07] ingest | Lecture 07. Draw Clear Task Boundaries for Agents

Ingested Learn Harness Engineering's seventh lecture on why agents overreach and under-finish, and how WIP limits fix it. Created 1 source summary, 4 new concept pages (Overreach and Under-finish, WIP Limit — with Completion Pressure folded in, Completion Evidence — with Verified Completion Rate folded in, Scope Surface). Updated Definition of Done with per-task completion evidence, Context Anxiety with the attention-division framing, Anthropic entity with the 37% "small next step" citation, Capability Gap with the seventh case study (REST API project, 37.5%->87.5% completion under WIP=1), and Learn Harness Engineering with the lecture-07 summary.

## [2026-07-07] ingest | Lecture 06. Make the Agent Initialize Before Every Work Session

Ingested Learn Harness Engineering's sixth lecture arguing initialization deserves its own dedicated phase separate from implementation. Created 1 source summary, 2 new concept pages (Initialization Phase — with Unverified Accumulation folded in as its core failure mode — and Startup Readiness Checklist). Updated Harness Initialization Flow and Rebuild Cost with cross-links distinguishing per-session bookends from one-time project initialization, Capability Gap with the sixth case study (Anthropic: 31% higher feature completion with dedicated init phase), Anthropic entity with the new research citation, and Learn Harness Engineering with the lecture-06 summary.

## [2026-07-07] ingest | Lecture 05. Keeping Context Alive Across Sessions

Ingested Learn Harness Engineering's fifth lecture on cross-session continuity loss. Created 1 source summary, 5 new concept pages (Rebuild Cost, Drift, Compaction vs. Reset, Decision Log, Harness Initialization Flow). Updated Agent State Management with the what/why distinction (PROGRESS.md vs. DECISIONS.md) and the new concepts, Context Anxiety with the "bigger windows can't fix this" point, Capability Gap with the fifth case study (78% rebuild-time reduction, 58%->100% feature completion, 43%->8% defect rate), and Learn Harness Engineering with the lecture-05 summary.

## [2026-07-07] ingest | Lecture 04. Split Instructions Across Files

Ingested Learn Harness Engineering's fourth lecture on why instruction files balloon and how to split them. Created 1 source summary, 4 new concept pages (Instruction Bloat, Lost in the Middle, Instruction Signal-to-Noise Ratio, Entry File). Updated Harness Engineering with the entry-file/topic-docs architecture and the Lost in the Middle mechanism, Capability Gap with the fourth case study (SaaS team, 45%->72% task success, 60%->95% security-constraint compliance), and Learn Harness Engineering with the lecture-04 summary.

## [2026-07-07] ingest | Lecture 03. Making the Repository the Single Source of Truth

Ingested Learn Harness Engineering's third lecture, arguing the repo must be an authoritative System of Record rather than just code storage. Created 1 source summary, 3 new concept pages (Knowledge Visibility Gap, System of Record, Fresh Session Test, Agent State ACID Principles — 4 pages total). Updated Harness Engineering with the recommended repo structure (AGENTS.md/ARCHITECTURE.md/CONSTRAINTS.md/PROGRESS.md) and four documentation principles, Capability Gap with the 30-microservice 70%->much-lower case study, Agent State Management with the ACID-principles checklist, and ACID Transactions with a cross-link to the agent-state analogy.

## [2026-07-07] ingest | Lecture 02. What a Harness Actually Is

Ingested Learn Harness Engineering's follow-up lecture defining the harness as five subsystems (instruction, tool, environment, state, feedback). Created 1 source summary, 1 new concept page (Controlled Variable Exclusion Test), 2 new entity pages (AutoGPT, Cursor). Substantially expanded Harness Engineering with the five-subsystem model, "the repo IS the spec" framing, and the maps-not-manuals/constrain-via-rules principles. Updated Capability Gap with the staged 20%->60%->80%->80-100% case study, Definition of Done with the verification-commands example, Codex with git-worktree/observability detail, and Learn Harness Engineering/index.md to also cover Lecture 01's previously-uningested pages (Harness Engineering, Capability Gap, Verification Gap, Diagnostic Loop, Definition of Done, Context Anxiety, Agent State Management, and related entities were created in an earlier session but never added to the index).

## [2026-07-07] update | Lecture 01. Strong Models Don't Mean Reliable Execution

Re-fetched the lecture URL via WebFetch and diffed against the existing source summary. Added benchmark pass-rate stat (~50-60%), the 20-minute-bare vs 6-hour-harnessed timing detail for the Anthropic case study, a direct quote, and the practical `AGENTS.md`-file recommendation from the "Practical Solution" section, which the original page had omitted.

## [2026-07-07] ingest | Design a Distributed Rate Limiter

Ingested Hello Interview's distributed rate limiter system design breakdown. Created 1 source summary, 2 entity pages (Hello Interview, ZooKeeper), and 6 concept pages (Distributed Rate Limiter, Rate Limit Rule, Rate Limiter Failure Mode, Rate Limiter Hot Key, Dynamic Rate Limit Configuration, DDoS Protection). Updated Rate Limiting, Token Bucket, API Gateway, Redis, Redis Cluster, and Consistent Hashing with gateway placement, Redis/Lua atomicity, sharding, fail-closed behavior, latency, hot-key, and dynamic configuration details.

## [2026-05-12] ingest | Strong vs. Eventual Consistency

Ingested AlgoMaster article on strong vs eventual consistency.
Created 1 source summary, rewrote 2 concept pages (Consistency Model with strong/eventual mechanics, client-centric variants, decision framework; Eventual Consistency with mechanics, examples, conflict resolution strategies, client-centric guarantees).
Key concepts: replication lag, strong consistency via consensus (Paxos/Raft), eventual consistency via async propagation, client-centric variants (causal, RYW, monotonic reads/writes), conflict resolution (LWW, CRDTs, custom merge), decision framework (data criticality, UX, latency, availability, scalability, complexity).

## [2026-05-12] ingest | Stateful vs. Stateless Architecture

Ingested AlgoMaster article on stateful vs stateless architecture.
Created 1 source summary, 2 new concept pages (Stateful Architecture with sticky sessions/centralized store patterns, advantages/challenges/use cases; Stateless Architecture with JWT/idempotent API patterns, scaling benefits, hybrid approach), updated System Design Trade-Offs with deep links.
Key concepts: stateful (retains context, sticky sessions, Redis centralized store), stateless (self-contained requests, JWT auth, idempotent APIs), hybrid (stateless APIs + external session store), decision framework.

## [2026-05-12] ingest | Batch vs Stream Processing - What's the Difference?

Ingested AlgoMaster article on batch vs stream processing.
Created 1 source summary, 2 new concept pages (Batch Processing with full workflow/characteristics/challenges/frameworks; Stream Processing with workflow/state management/windowing/challenges/frameworks), updated Offline Processing with Batch cross-ref.
Key concepts: batch workflow (collect → pre-process → execute → post-process), stream workflow (ingest → transform → state mgmt → output), micro-batch hybrid, decision factors (volume, latency need, complexity, data nature), tools (Hadoop, Spark, Flink, Kafka, Kinesis, AWS Batch).

## [2026-05-12] ingest | Long Polling vs WebSockets

Ingested AlgoMaster article on long polling vs WebSockets for real-time communication.
Created 1 source summary, updated 2 concept pages (Long-Polling with pros/cons/detail/alternatives; WebSockets with decision framework and alternative protocols section).
Key concepts: why HTTP push isn't enough, long polling mechanics (hold-open reconnect loop), WebSocket handshake and full-duplex persistent connection, decision framework (complexity, scalability, interaction type, network constraints), alternatives (SSE, MQTT, Socket.io).

## [2026-05-12] ingest | Concurrency vs Parallelism

Ingested AlgoMaster article on concurrency vs parallelism.
Created 1 source summary, updated concept page with context switching mechanics, 4-combinations matrix (concurrent/parallel permutations), real-world examples (browsers, web servers, ML training, video rendering, Spark), and summary comparison table.
Key insight: concurrency manages tasks via context switching; parallelism executes subtasks on separate cores simultaneously.

## [2026-05-12] ingest | System Design: Vertical vs Horizontal Scaling

Ingested AlgoMaster article on vertical vs horizontal scaling.
Created 1 source summary, updated 2 concept pages (Scalability with detailed pros/cons/decision framework/combining strategies; Horizontal Scalability with comparison table and combining strategies section).
Key concepts: vertical scaling (upgrade CPU/RAM/storage), horizontal scaling (add servers + load balancer), decision factors (cost, workload, complexity, growth), combining both strategies, vertically-scaled clusters, database sharding.

## [2026-05-12] ingest | System Design: Top 15 Trade-Offs

Ingested AlgoMaster article by Ashish Pratap Singh cataloging 15 system design trade-offs.
Created 1 source summary, 1 concept page (System Design Trade-Offs) with cross-references to 30+ existing wiki pages covering all 15 trade-offs.
Key content: every design decision is a trade-off — scalability vs performance, vertical vs horizontal scaling, latency vs throughput, SQL vs NoSQL, CAP theorem, strong vs eventual consistency, cache strategies, batch vs stream processing, sync vs async, stateful vs stateless, long polling vs WebSockets, normalization vs denormalization, monolithic vs microservices, REST vs GraphQL, TCP vs UDP.

## [2026-05-12] ingest | Peer-To-Peer Networks: Features, Pros, and Cons

Ingested Spiceworks article on peer-to-peer networking by Vijay Kanade.
Created 1 source summary, 1 concept page (Peer-to-Peer Network), updated Client-Server Architecture with P2P contrast section.
Key concepts: decentralization, self-organizing systems, resource sharing, direct communication, horizontal scalability, fault tolerance, applications (BitTorrent, Bitcoin, Skype, SETI@home, P2P CDNs, P2P VPNs).

## [2026-05-12] ingest | Event-Driven Architecture (EDA): A Complete Introduction

Ingested Confluent guide on event-driven architecture.
Created 1 source summary (event-driven-architecture-intro), 3 entity pages (Apache Flink, Confluent, updated Apache Kafka with EDA role), 3 new concept pages (Event-Driven Architecture, CQRS, Event-Driven Microservices), updated 2 existing concept pages (Pub/Sub Messaging, Event Sourcing).
Key concepts: EDA definition and mechanics, loose coupling via event brokers, event sourcing + CQRS patterns, pub/sub messaging, EDA advantages (scalability, real-time, fault tolerance, system integration) and disadvantages (complexity, ordering, consistency, debugging), Kafka + Flink + Confluent technology stack, 10 real-world use cases, event-driven microservices.

## [2026-05-01] ingest | REST API Design Best Practices

Ingested source: Abdul Rafee Wahab - REST API Design Best Practices (Oct 2021).
Created 1 source summary, 6 concept pages (REST API Design Best Practices, HTTP 202, Error Response Format, URI Naming Conventions, Query String Filtering, Page Pagination), 1 entity page.
Key concepts: resource-oriented URIs (plural nouns, no verbs, no nesting), Content-Type importance, meaningful HTTP status codes (never 200 with error body), 401 vs 403 distinction, query string filtering + pagination, REST-specific frameworks, trailing slash handling.

## [2026-05-01] ingest | Rate Limiting Algorithms

Ingested source: AlgoMaster.io Rate Limiting Algorithms (Jul 2024).
Created 1 source summary, 5 concept pages (Token Bucket, Leaky Bucket, Fixed Window Counter, Sliding Window Log, Sliding Window Counter). Updated existing Rate Limiting page with cross-references.
Key concepts: Token Bucket (burst-friendly, simple), Leaky Bucket (smooths traffic, drops excess), Fixed Window Counter (boundary problem allows 2x rate), Sliding Window Log (accurate but memory-heavy), Sliding Window Counter (hybrid: weighted approximation with O(1) memory).

## [2026-05-01] ingest | Idempotency

Ingested source: AlgoMaster.io Idempotency (Nov 2024).
Created 1 source summary, 4 concept pages (Idempotency, Idempotency Key, Deduplication Store, Upsert).
Key concepts: idempotent operations (GET/PUT/DELETE vs POST), idempotency keys for deduplication, database upsert patterns, deduplication store design, two-phase reservation pattern, handling race conditions in distributed systems.

## [2026-05-01] ingest | Webhooks

Ingested source: AlgoMaster.io Webhooks (Apr 2025).
Created 1 source summary, 4 concept pages (Webhooks, Event Idempotency, Dead Letter Queue, Exponential Backoff).
Key concepts: event-driven push notifications, webhook anatomy (POST, JSON, HMAC signature), receiver setup (idempotency, signature verification), scalable pipeline (queue → store → async workers → retry with backoff → DLQ → observability).

## [2026-04-28] ingest | REST vs GraphQL

Ingested source: AlgoMaster.io REST vs GraphQL (March 2025).
Created 1 source summary, 2 concept pages (Over-fetching, Under-fetching).
Key differences: over-fetching, under-fetching, single vs multiple endpoints, caching.

## [2026-04-28] ingest | API Gateway

Ingested source: AlgoMaster.io API Gateway (December 2024).
Created 1 source summary, 1 concept page (Rate Limiting).
Key features: request validation, auth, rate limiting, routing.

## [2026-04-28] ingest | API

Ingested source: AlgoMaster.io API (October 2025).
Created 1 source summary, 4 concept pages (REST API, GraphQL, gRPC, API Gateway).
Key concepts: request-response model, REST, GraphQL, gRPC, API Gateway.

## [2026-04-28] ingest | Checksums

Ingested source: AlgoMaster.io Checksums (October 2025).
Created 1 source summary, 4 concept pages (CRC, MD5, SHA-256, Cryptographic Hash).
Key concepts: CRC for errors, cryptographic hashes, SHA-256 standard.

## [2026-04-28] ingest | Load Balancing Algorithms

Ingested source: AlgoMaster.io Load Balancing Algorithms (June 2024).
Created 1 source summary, 4 concept pages (Round Robin, Weighted Round Robin, Least Connections, Health Check).
Key concepts: algorithms (round robin, weighted, least connections), L4 vs L7, health checks.

## [2026-04-28] ingest | TCP vs UDP

Ingested source: AlgoMaster.io TCP vs UDP (November 2025).
Created 1 source summary, 2 concept pages (TCP, UDP).
Key concepts: three-way handshake, reliable vs fastest, use cases.

## [2026-04-28] ingest | HTTP and HTTPS

Ingested source: AlgoMaster.io HTTP and HTTPS (October 2025).
Created 1 source summary, 5 concept pages (HTTP, HTTPS, TLS, HTTP/2, HTTP/3).
Key concepts: HTTP methods, TLS handshake, HTTP/2 multiplexing, HTTP/3 QUIC.

## [2026-04-28] ingest | Proxy vs Reverse Proxy

Ingested source: AlgoMaster.io Proxy vs Reverse Proxy (October 2024).
Created 1 source summary, 4 concept pages (Proxy, Reverse Proxy, SSL Termination, WAF).
Key concepts: forward proxy vs reverse proxy, load balancing, SSL termination.

## [2026-04-28] ingest | DNS

Ingested source: AlgoMaster.io DNS (September 2025).
Created 1 source summary, 4 concept pages (DNS Record, Recursive Resolver, Authoritative Name Server, DNS Caching).
Key concepts: resolution process, DNS hierarchy, record types, caching levels.

## [2026-04-28] ingest | IP Address

Ingested source: AlgoMaster.io IP Address (March 2026).
Created 1 source summary, 6 concept pages (IPv4, IPv6, CIDR, NAT, Private/Public IP).
Key concepts: 32-bit IPv4, 128-bit IPv6, CIDR notation, subnetting, NAT, RFC 1918.

## [2026-04-28] ingest | OSI Model

Ingested source: AlgoMaster.io OSI Model (March 2026).
Created 1 source summary, 9 concept pages (7 layers + encapsulation + OSI vs TCP/IP), updated index.
Key concepts: 7-layer framework, MAC/IP/ports, encapsulation, decapsulation, troubleshooting value.

## [2026-04-27] ingest | CockroachDB: Fault Tolerance

Ingested source: CockroachDB Fault Tolerance (2023).
Created 1 source summary, updated 1 concept page.
Key concepts: quorum, replication factor, automatic recovery.

## [2026-04-27] ingest | Druva: Failover

Ingested source: Druva Failover Definition (2026).
Created 1 source summary, 1 concept page.
Key concepts: heartbeat, active-active vs active-passive, cluster.

## [2026-04-27] ingest | AlgoMaster: CAP Theorem

Ingested source: AlgoMaster.io CAP Theorem (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: C/A/P tradeoff, CP vs AP systems.

## [2026-04-27] ingest | AlgoMaster: Consistent Hashing

Ingested source: AlgoMaster.io Consistent Hashing (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: hash ring, virtual nodes, minimal remapping on scaling.

## [2026-04-27] ingest | AlgoMaster: Latency vs Throughput vs Bandwidth

Ingested source: AlgoMaster.io Latency vs Throughput vs Bandwidth (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: delay vs volume vs capacity, BDP, bottleneck.

## [2026-04-27] ingest | AlgoMaster: Single Point of Failure (SPOF)

Ingested source: AlgoMaster.io SPOF (2026).
Created 1 source summary, 1 concept page.
Key concepts: single points of failure, redundancy, load balancing, strategies to eliminate.

## [2026-04-27] ingest | AlgoMaster: Scalability, Availability, Reliability

Ingested sources: AlgoMaster.io Scalability, Availability, Reliability (2026).
Created 3 source summaries, updated 2 concept pages.
Key concepts: vertical/horizontal scaling, stateless services, redundancy, nines, circuit breakers.

## [2026-04-27] ingest | AlgoMaster: SOLID Principles

Ingested source: AlgoMaster.io SOLID Principles (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: SRP, OCP, LSP, ISP, DIP with code examples.

## [2026-04-27] ingest | AlgoMaster: KISS Principle

Ingested source: AlgoMaster.io KISS Principle (2026).
Created 1 source summary, 1 concept page.
Key concepts: "keep it simple", over-engineering, clear over clever.

## [2026-04-27] ingest | AlgoMaster: YAGNI Principle

Ingested source: AlgoMaster.io YAGNI Principle (2026).
Created 1 source summary, 1 concept page.
Key concepts: "you aren't gonna need it", build for now not later.

## [2026-04-27] ingest | AlgoMaster: DRY Principle

Ingested source: AlgoMaster.io DRY Principle (2026).
Created 1 source summary, 1 concept page.
Key concepts: don't repeat yourself, single source of truth, Rule of Three.

## [2026-04-27] ingest | AlgoMaster: Composition

Ingested source: AlgoMaster.io Composition (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: strong "owns-a", filled diamond UML, parts die with whole, tight coupling.

## [2026-04-27] ingest | AlgoMaster: Dependency

Ingested source: AlgoMaster.io Dependency (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: temporary "uses-a", UML dashed arrow, method parameters, loose coupling.

## [2026-04-27] ingest | AlgoMaster: Aggregation

Ingested source: AlgoMaster.io Aggregation (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: "has-a" with independent parts, hollow diamond UML symbol, reassignment allowed.

## [2026-04-27] ingest | AlgoMaster: Association

Ingested source: AlgoMaster.io Association (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: "knows-about" relationship, UML representation, multiplicity (1-to-1, 1-to-many, many-to-many), unidirectional vs bidirectional, intermediary pattern for many-to-many.

## [2026-04-24] ingest | Race Conditions and Critical Sections

Ingested source: AlgoMaster.io race conditions (2026).
Created 1 source summary, updated 2 concept pages.

## [2026-04-24] ingest | Thread Lifecycle and States

Ingested source: AlgoMaster.io thread lifecycle (2026).
Created 1 source summary, 1 concept page.

## [2026-04-24] ingest | Processes vs Threads

Ingested source: AlgoMaster.io processes vs threads (2026).
Enhanced concept page with context switching details.
Created 1 source summary, updated 1 concept page.

## [2026-04-24] update | Concurrency vs Parallelism

Enhanced concept page with AlgoMaster's restaurant analogy, four scenarios, and levels of parallelism.

## [2026-04-24] ingest | Introduction to Concurrency

Ingested source: AlgoMaster.io intro to concurrency (2026).
Created 1 source summary, 6 concept pages.
Key concepts: concurrency vs parallelism, processes vs threads, race conditions, critical sections, thread safety.

## [2026-04-05] init | Wiki initialized

Empty wiki created, ready for first ingest.

## [2026-04-05] ingest | Kafka: A Distributed Messaging System for Log Processing

Ingested source: Kafka paper (2011) from LinkedIn.
Created 1 source summary, 1 entity page, 3 concept pages.
Key concepts: distributed commit log, pub/sub messaging, log aggregation.

## [2026-04-05] ingest | Language Models are Few-Shot Learners (GPT-3)

Ingested source: GPT-3 paper (2020) from OpenAI.
Created 1 source summary, 2 entity pages, 3 concept pages.
Key concepts: few-shot learning, in-context learning, emergent abilities.

## [2026-04-16] ingest | CS 179: Introduction to GPU Programming - Lecture 1

Ingested source: Caltech CS 179 Lecture 1 (2026) covering GPU architecture and CUDA.
Created 1 source summary, 1 entity page, 2 concept pages.

## [2026-04-19] ingest | Distributed Systems: for fun and profit

Ingested source: Mixu's distributed systems book (2013).
Created 1 source summary, 5 entity pages, 25+ concept pages.
Key concepts: scalability, availability, CAP, FLP, partitions, replication, consensus, eventual consistency, CRDTs, CALM.
Key concepts: GPU computing, kernel functions, CPU vs GPU architecture, thread indexing.

## [2026-04-16] ingest | CS 179: Intro to SIMD and GPU Internals - Lecture 2

Ingested source: Caltech CS 179 Lecture 2 (2026) covering GPU hardware internals.
Created 1 source summary, 4 concept pages.
Key concepts: SIMD vs SIMT, thread hierarchy, warp divergence, streaming multiprocessors.

## [2026-04-16] ingest | CS179 Recitation 1 - GPU Overview and Prefix Sum

Ingested source: CS 179 Recitation 1 (2025) covering GPU hardware and prefix sum.
Created 1 source summary, 1 concept page.
Key concepts: prefix sum (scan), RTX 5090 Blackwell architecture.

## [2026-04-16] query | What is In-Context Learning?

Saved answer explaining ICL mechanism, few-shot relation, and scaling behavior.

## [2026-04-16] ingest | Best GPUs for Deep Learning in 2023

Ingested source: Tim Dettmers' GPU guide (2023).
Created 1 source summary, 4 entity pages, 8 concept pages.
Key concepts: Tensor Cores, memory bandwidth, precision formats (BF16/TF32/FP8), sparse training, L2 cache.

## [2026-04-16] ingest | CS 179: GPU Memory Systems - Lecture 4

Ingested source: CS 179 Lecture 4 (2026) covering GPU memory systems.
Created 1 source summary, 6 concept pages.
Key concepts: Memory hierarchy, coalescing, bank conflicts, register spilling, computational intensity, latency vs throughput.

## [2026-04-17] ingest | CS 179: Synchronization and ILP - Lecture 5

Ingested source: CS 179 Lecture 5 (2026) covering synchronization and ILP.
Created 1 source summary, 8 concept pages.
Key concepts: CUDA synchronization, atomic operations, instruction dependencies, ILP, warp scheduler, occupancy, floating point precision.

## [2026-04-17] ingest | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Ingested source: FlashAttention paper by Dao et al. (Stanford, 2022).
Created 1 source summary, 5 concept pages.
Key concepts: FlashAttention, IO-awareness, tiling, recomputation, block-sparse attention.

## [2026-04-17] ingest | FlashAttention-2: Faster Attention with Better Parallelism

Ingested source: FlashAttention-2 paper by Tri Dao (2023).
Created 1 source summary, 2 concept pages.
Key concepts: FlashAttention-2, Split-Q warp partitioning, sequence-length parallelization.

## [2026-04-17] ingest | FlashAttention-3: Fast and Accurate Attention with Asynchrony

Ingested source: FlashAttention-3 paper by Shah et al. (2024).
Created 1 source summary, 4 concept pages.
Key concepts: FlashAttention-3, warp specialization, GEMM-softmax overlap, FP8 attention with block quantization.

## [2026-04-19] ingest | HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN

Ingested source: Google paper (USENIX NSDI 2024).
Created 1 source summary, 3 concept pages, 2 entity pages.
Key concepts: learned cache eviction, pairwise learning to rank, impact distribution analysis.
Key entities: HALP, LRB, ARC.

## [2026-04-20] ingest | Redis Cluster: Architecture, Replication, Sharding and Failover

Ingested source: Redis Cluster article by Sajal Jain (2019).
Created 1 source summary, 2 entity pages, 2 concept pages.
Key concepts: Redis Cluster, hash slots (16384), failover, Redis Sentinel, master-slave.

## [2026-04-21] query | How does YouTube HALP work?

Saved answer to wiki/queries/HALP.md describing HALP's hybrid ML+heuristic cache eviction.

## [2026-04-21] ingest | Dynamo: Amazon's Highly Available Key-Value Store

Ingested source: SOSP 2007 paper (DeCandia et al.).
Created 1 source summary, 3 new concept pages (Sloppy Quorum, Hinted Handoff).
Key techniques: consistent hashing, vector clocks, sloppy quorum, hinted handoff, Merkle trees.
Key concepts: eventual consistency, application-assisted conflict resolution.

## [2026-04-22] ingest | CS 179: Matrix Transpose Optimization - Lecture 6

Ingested source: CS 179 Recitation 2 (2025) covering matrix transpose optimization.
Created 1 source summary, 3 concept pages.
Key concepts: matrix transpose, warp, shared memory, bank conflict resolution via padding.

## [2026-04-22] ingest | CMU 15-445: Relational Model & Algebra

Ingested source: CMU 15-445 Lecture 1 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 1 entity page, 7 concept pages.
Key concepts: relational model, relational algebra (select/project/union/join), primary key, foreign key, SQL, document/vector databases.

## [2026-04-22] ingest | CMU 15-445: Modern SQL

Ingested source: CMU 15-445 Lecture 2 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: aggregates, GROUP BY, HAVING, window functions, CTEs, recursive CTEs, lateral joins.

## [2026-04-23] ingest | CMU 15-445: Database Storage I

Ingested source: CMU 15-445 Lecture 3 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 1 entity page, 5 concept pages.
Key concepts: disk-oriented DBMS, database pages, heap files, storage manager, buffer pool.

## [2026-04-23] ingest | CMU 15-445: Memory Management & Buffer Pools

Ingested source: CMU 15-445 Lecture 4 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: buffer pool organization, page table, frame, dirty page, LRU, clock replacement, memory-mapped I/O.

## [2026-04-23] ingest | CMU 15-445: Database Storage II

Ingested source: CMU 15-445 Lecture 5 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: slotted pages, index-organized tables, B+Tree, log-structured storage, tuple storage.

## [2026-04-23] ingest | CMU 15-445: Storage Models & Compression

Ingested source: CMU 15-445 Lecture 6 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 7 concept pages.
Key concepts: row store, column store, OLTP, OLAP, data compression, run-length encoding.

## [2026-04-23] ingest | CMU 15-445: Hash Tables

Ingested source: CMU 15-445 Lecture 7 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: hash tables, linear probe, chained hashing, extendible hashing, linear hashing.

## [2026-04-23] ingest | CMU 15-445: B+Tree Indexes

Ingested source: CMU 15-445 Lecture 8 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 3 concept pages.
Key concepts: B+Tree, clustered index, secondary index, index scan.

## [2026-04-23] ingest | CMU 15-445: Indexes & Filters II

Ingested source: CMU 15-445 Lecture 9 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 4 concept pages.
Key concepts: inverted index, vector index, partial index, covering index.

## [2026-04-23] ingest | CMU 15-445: Index Concurrency Control

Ingested source: CMU 15-445 Lecture 10 (Spring 2026) by Jignesh Patel.
Created 1 source summary, 3 concept pages.
Key concepts: latch vs lock, reader-writer latch, latch crabbing.

## [2026-04-23] ingest | CMU 15-445: Query Processing

Ingested source: CMU 15-445 Lecture 11 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 3 concept pages.
Key concepts: query plan, iterator model, sequential scan.

## [2026-04-23] ingest | CMU 15-445: Join Algorithms

Ingested source: CMU 15-445 Lecture 12 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 3 concept pages.
Key concepts: nested loop join, sort-merge join, hash join.

## [2026-04-23] ingest | A Survey of Deep Learning: From Activations to Transformers

Ingested source: arXiv paper by Schneider & Vlachos (2023/2024).
Created 1 source summary, 9 concept pages, 1 entity page.
Key concepts: transformer, self-attention, vision transformer, self-supervised learning.
Additional: activation functions, normalization, skip connections, multi-head attention, positional encoding.

## [2026-04-23] ingest | Inheritance + Polymorphism

Ingested sources: AlgoMaster articles on Inheritance and Polymorphism (2026).
Created 2 source summaries, 3 concept pages.
Key concepts: extends, inheritance types, method overriding, method overloading, compile-time vs runtime polymorphism.
Key examples: Notification system (Email/SMS/Push), Calculator.

Ingested source: AlgoMaster article on Abstraction (2026).
Created 1 source summary, 3 concept pages.
Key concepts: abstract classes (shared behavior + abstract methods), public APIs, abstraction vs encapsulation.
Key example: MediaPlayer with PlayerController (player-agnostic).

Ingested source: AlgoMaster article on Encapsulation (2026).
Created 1 source summary, 4 concept pages.
Key concepts: access modifiers (private/protected/public), getter/setter pattern, data validation.
Key examples: BankAccount (balance protection), PaymentProcessor (sensitive data masking).

Ingested sources: AlgoMaster articles on interfaces and SOLID principles (2026).
Created 1 source summary, 5 concept pages.
Key concepts: interface contracts, interface segregation (ISP), dependency inversion (DIP), dependency injection pattern, SOLID principles.
Key examples: payment gateway, notification service.

Ingested source: AlgoMaster article on Enums (2026).
Created 1 source summary, 3 concept pages.
Key concepts: enum with properties/methods, type safety, state machine pattern.
Key example: order processing system with OrderStatus and PaymentMethod enums.

Ingested sources: AlgoMaster.io articles on OOP fundamentals (2026).
Created 2 source summaries, 1 entity page, 12 concept pages.
Key concepts: class, object, interface, four pillars (encapsulation, abstraction, inheritance, polymorphism), five object relationships (association, aggregation, composition, dependency, realization).
Key entity: Ashish Pratap Singh (AlgoMaster.io creator).

Ingested source: Will Larson's foundational article on scalable system architecture (2011).
Created 1 source summary, 6 entity pages, 18 concept pages.
Key concepts: load balancing (smart clients, hardware, software), caching (application, database, in-memory, CDN), cache invalidation, offline processing (message queues, cron, map-reduce), platform layer.
## [2026-05-08] ingest | SQL vs NoSQL

Ingested source: AlgoMaster.io article by Ashish Pratap Singh (Oct 2025).
Created 1 source summary, 1 concept page (NoSQL). Updated SQL concept page with comparison table and when-to-choose guidance.
Key concepts: 7 SQL vs NoSQL differences (data model, schema, scalability, query language, transactions, performance, use cases), 4 NoSQL models (key-value, document, column-family, graph), BASE vs ACID tradeoffs.

## [2026-05-08] ingest | ACID Transactions

Ingested source: AlgoMaster.io article by Ashish Pratap Singh (Oct 2025).
Created 1 source summary, 1 concept page (ACID Transactions).
Key concepts: atomicity (WAL, commit/rollback), consistency (integrity constraints), isolation (dirty/non-repeatable/phantom reads, levels Read Uncommitted through Serializable, MVCC, snapshot isolation, locking), durability (WAL, sync/async replication, backups).

## [2026-05-08] ingest | RFC 2308: DNS Negative Caching

Ingested source: RFC 2308 (Mark Andrews, March 1998).
Created 1 source summary, 1 concept page (DNS Negative Caching). Updated algomaster-dns source with RFC reference.
Key concepts: negative caching of NXDOMAIN (name error) and NODATA (no records of type), SOA-derived TTL (min of SOA.MINIMUM and SOA.TTL), SOA MINIMUM redefined as negative TTL only, $TTL directive, security risks (DoS via injected NXDOMAIN), optional server failure caching (5-minute max).

## [2026-05-08] ingest | Broadcasting Live Video to Millions

Ingested source: Facebook Engineering blog (Dec 2015).
Created 1 source summary, 1 concept page (Edge Cache). Updated Cache Stampede page with request coalescing strategy and Facebook Live case study.
Key concepts: multi-layer edge cache architecture (98%+ hit rate), request coalescing for thundering herd prevention, HLS 3-second segments vs RTMP push model (4KB chunks, 5x latency reduction), nginx-rtmp modification for Facebook Live.

## [2026-05-08] ingest | Cache Invalidation Strategies

Ingested source: Medium article by CoVaib DeepLearn (Sep 2025).
Created 1 source summary, 5 concept pages (Write-Around Cache, Tag-Based Invalidation, Version-Based Invalidation, Cache Warming, Cache Stampede). Updated Cache Invalidation page with purge/ban methods, event-driven strategy, dependency-based invalidation.
Key concepts: purge vs ban, TTL/event-driven/write-through/write-around/write-behind/lazy-loading strategies, tag-based/dependency-based/version-based advanced patterns, cache warming (scheduled/event-driven/JIT), cache stampede (thundering herd) with 5 mitigations.

## [2026-05-08] ingest | Two Hard Things

Ingested source: Martin Fowler's bliki (2009, updated 2021).
Created 1 source summary, 1 entity page (Martin Fowler). Updated Cache Invalidation page with the Phil Karlton quote.
Key content: famous Phil Karlton quote "there are only two hard things: cache invalidation and naming things", 4 notable variations.

## [2026-05-08] ingest | HTTP Caching: Cache-Control & Vary

Ingested source: freeCodeCamp article by Léo Jacquemin (Oct 2019), Part 2 of series.
Created 1 source summary, 5 concept pages (Cache-Control, Vary Header, Conditional Request, ETag). Updated HTTP Caching, Web Caching, Browser Caching, and Caching pages.
Key concepts: 4-outcome caching decision tree, Cache-Control directives (max-age, no-store, no-cache, must-revalidate, public/private, s-maxage, stale-while-revalidate, stale-if-error), Vary header for content negotiation, normalization (44 Accept-Encoding values, 8000+ User-Agent values), strong vs weak ETags, freshness vs validation distinction, conditional request flow (304 vs 200).

## [2026-05-08] ingest | HTTP Caching In-Depth Part 1

Ingested source: freeCodeCamp article by Léo Jacquemin (Dec 2018).
Created 1 source summary, 3 concept pages (HTTP Caching, Browser Caching, Proxy Cache). Updated Caching, Web Caching, and CDN pages.
Key concepts: 3 HTTP caching actors (browser, CDN, private proxy), latency vs bandwidth as bottleneck, web request anatomy (DNS + TCP + TLS + slow-start = ~8 RT per request), TCP slow-start and congestion window evolution, cache abstraction (all proxies speak HTTP), browser cache multi-layer complexity, private proxy caches as first solution (Varnish, Squid, Nginx), CDN programmatic purging.

## [2026-05-08] ingest | System Design Primer: Cache

Ingested source: Donne Martin's system-design-primer cache section (GitHub).
Created 1 source summary, 3 concept pages (Cache-Aside, Write-Behind Cache, Refresh-Ahead Cache). Updated Caching and Application Caching pages.
Key concepts: 4 cache update strategies (cache-aside/lazy loading, write-through, write-behind/write-back, refresh-ahead), 2 caching levels (database query hashing vs object-level), 5 cache locations (client, CDN, web server, database, application).

## [2026-05-08] ingest | AWS Caching Overview

Ingested source: AWS Caching Overview page (2026).
Created 1 source summary, 3 entity pages (Amazon ElastiCache, Amazon CloudFront, Amazon Route 53), 2 concept pages (Web Caching, Session Management). Updated Caching and CDN concept pages.
Key concepts: 5-layer caching stack (client, DNS, web, app, database), distributed caching with independent lifecycle, 5 benefits (performance, cost, predictability, hotspots, IOPS), use cases across 9 domains and 10 industries, AWS caching services (ElastiCache for Redis/Memcached, CloudFront CDN, Route 53 DNS).

## [2026-05-01] ingest | WebSockets

- 

## [2026-05-10] update | OSI Model

Re-ingested AlgoMaster.io OSI Model article from Wayback Machine archive (Dec 2025) since current version is paywalled.
Updated source page with factory assembly line analogy, HTTPS L5-7 blurring insight, and additional protocol mentions.
Updated 5 concept pages: Encapsulation (HTTP GET walkthrough), OSI vs TCP/IP (HTTPS spanning L5-7), OSI Layer 7 (gRPC, WebSocket), OSI Layer 6 (JSON, XML, Protobuf), OSI Layer 5 (RPC/WebSocket sessions).

## [2026-05-10] ingest | IP Address

Re-ingested AlgoMaster.io IP Address article from Wayback Machine archive (Dec 2025).
Created 5 new concept pages: IP Address (postal analogy, Network ID + Host ID structure), Subnet Mask, Static vs Dynamic IP (DHCP), Broadcast Address, Multicast Address.
Updated 4 existing pages: source page with SLAAC/IPsec/static-DHCP details, IPv4 (address exhaustion), IPv6 (SLAAC, mandatory IPsec, simplified header), Private IP Address (NAT gateway for internet access).
Key concepts: Network ID vs Host ID, DHCP DORA flow, broadcast vs multicast, SLAAC.

## [2026-05-10] ingest | How DNS Actually Works

Ingested AlgoMaster blog post by Ashish Pratap Singh (Sep 2025).
Created 3 new concept pages: DNS (hierarchy overview), Anycast (global routing, DNS use case), GeoDNS (geographic resolution, compliance).
Updated 4 existing pages: source page (anycast, GeoDNS, CDN, load balancing), DNS Caching (TTL/propagation), Recursive Resolver (anycast), Authoritative Name Server (GeoDNS).
Key concepts: anycast routing for DNS, GeoDNS for region-aware resolution, DNS load balancing with multiple A records, CDN edge server resolution.

## [2026-05-10] ingest | Proxy vs Reverse Proxy Explained

Ingested AlgoMaster blog post by Ashish Pratap Singh (Oct 2024).
Updated 3 existing pages: source page (Nginx config, TTL caching, middleman/gatekeeper analogies, VPN vs proxy), Proxy (TTL caching, VPN comparison), Reverse Proxy (Nginx config with upstream, gatekeeper analogy, Cloudflare WAF/DDoS).
Key additions: Nginx configuration examples (basic reverse proxy, upstream load balancing with ip_hash), proxy caching with TTL-based expiration, "middleman" vs "gatekeeper" framing.

## [2026-05-10] ingest | HTTP and HTTPS

Ingested AlgoMaster.io article (Oct 2025) via Wayback Machine (Dec 2025).
Updated 5 existing pages: source page (full methods table, status code categories, idempotency, HTTP vs HTTPS comparison, attack vectors), HTTP (PUT/DELETE/PATCH methods, idempotency, full status codes, statelessness tradeoffs, security risks), HTTPS (PKI details, HTTP vs HTTPS comparison table), HTTP/2 (TCP HoL blocking explanation, system design impact), HTTP/3 (why UDP, TCP HoL persistence, system design impact, major adopters).
Key additions: idempotency concept for distributed retries, HTTP/2 and HTTP/3 system design impacts, MITM/eavesdropping/injection attack vectors, HTTP vs HTTPS feature comparison.

## [2026-05-10] ingest | TCP vs UDP

Ingested AlgoMaster.io article (Nov 2025) via Wayback Machine (Jan 2026).
Updated 3 existing pages: source page (QUIC details with TLS 1.3/multiplexing, decision framework, hybrid approach, TCP termination, security TLS vs DTLS), TCP (connection termination four-step, sliding window, error detection, TLS foundation), UDP (fire-and-forget model, datagram routing, DTLS security).
Key additions: TCP graceful shutdown, QUIC as best-of-both-worlds with mandatory encryption, TCP vs UDP decision matrix for system design, hybrid approach patterns, DTLS for UDP security.

## [2026-05-10] ingest | Load Balancing Algorithms Explained with Code

Ingested AlgoMaster blog post by Ashish Pratap Singh (Jun 2024).
Created 2 new concept pages: Least Response Time (fastest server routing, response time monitoring), IP Hash (MD5 hash modulo, sticky sessions).
Updated 5 existing pages: source page (code links to GitHub, decision summary), Round Robin (Python implementation with index tracking), Weighted Round Robin (Python code with weight iteration), Least Connections (Python code with release_connection).
All 5 algorithm concept pages now include Python implementations.

## [2026-05-10] ingest | Checksums

Ingested AlgoMaster.io article (Oct 2025) via Wayback Machine (Jan 2026).
Created 2 new concept pages: Checksums (photo analogy, parity bit, data backups), Parity Bit (single-bit error detection, even/odd parity, limitation).
Updated source page with photo analogy, parity bit entry in algorithm table, data backups use case.

## [2026-05-10] ingest | Publish-Subscribe (Pub/Sub)

Ingested AlgoMaster.io article (Jan 2026) via Wayback Machine (Jan 2026).
Created new source page: Pub/Sub (broker as intermediary, ack flow, 7 benefits, IoT use case).
Updated Pub/Sub Messaging concept page with message flow (publish → store → deliver → ack), benefits list, IoT data aggregation use case.
Key additions: acknowledgment pattern, broker durability, real-time notifications and event logging use cases.

## [2026-05-10] ingest | Message Queues

Ingested AlgoMaster.io article (Oct 2025) via Wayback Machine (Feb 2026).
Created new source page: Message Queues (5 components, 6-step flow, queue types, best practices).
Updated message-queue concept page with broker component, 6-step flow (create → enqueue → store → dequeue → ack → delete), queue types (P2P, Pub/Sub, priority, DLQ), best practices (idempotency, durability, security, monitoring), when-to-use scenarios, missing systems (Google Cloud Pub/Sub, ActiveMQ), throttling benefit.

## [2026-05-10] ingest | Change Data Capture (CDC)

Ingested AlgoMaster.io article (Oct 2025) via Wayback Machine (Feb 2026).
Created source page, CDC concept page (3 approaches: timestamp/trigger/log-based, 4 use cases, Debezium/Kafka implementation, challenges), Event Sourcing concept page (immutable event sequences, audit trail, temporal query), Debezium entity page (log-based CDC, Kafka Connect integration, schema evolution handling).
Key concepts: timestamp CDC misses deletes and has clock skew, trigger CDC slows writes, log-based CDC (WAL/binlog) is preferred for production, Debezium + Kafka as standard CDC stack.

Ingested source: AlgoMaster.io WebSockets (Aug 2024).
Created 1 source summary, 5 concept pages (WebSockets, HTTP 101, Polling, Long-Polling, Frame).
Key concepts: full-duplex bidirectional communication, HTTP handshake with 101 switch, persistent connections vs HTTP/polling/long-polling, use cases (chat, gaming, notifications, financial feeds, collaboration, IoT), challenges (scalability, security, network reliability, proxy compatibility).

Key entities: Will Larson, HAProxy, Memcached, RabbitMQ, Hadoop.

## [2026-05-11] ingest | AlgoMaster: Indexing

Ingested AlgoMaster.io article by Ashish Pratap Singh (Oct 2025) via Wayback Machine (Jan 2026).
Created 1 source summary, 10 new concept pages (Database Index, Primary Index, Dense Index, Sparse Index, Bitmap Index, Hash Index, Filtered Index, Function-Based Index, Full-Text Index, Spatial Index).
Updated 3 existing pages: Clustered Index, Secondary Index (added non-clustered alias), Covering Index.
Key concepts: book index analogy, B-Tree/B+Tree vs Hash Table vs Bitmap data structures, dense vs sparse indexing, best practices (selective columns, composite indexes, avoid over-indexing).

## [2026-05-11] ingest | AlgoMaster: Sharding

Ingested AlgoMaster.io article by Ashish Pratap Singh (Oct 2025) via Wayback Machine (Dec 2025).
Created 1 source summary, 8 new concept pages (Database Sharding, Shard Key, Hash-Based Sharding, Range-Based Sharding, Geo-Based Sharding, Directory-Based Sharding, Cross-Shard Query, Data Rebalancing).
Updated 2 existing pages: Partitioning (added sharding links), Consistent Hashing (added sharding use case).
Key concepts: Instagram/Amazon/Google sharding examples, 4 strategies (hash/range/geo/directory), consistent hashing for rebalancing, cross-shard query challenges, best practices for shard key selection.

## [2026-05-11] ingest | Redis: Data Replication Explained

Ingested Redis blog post by Paula Dallabetta (Apr 2026).
Created 1 source summary, 11 new concept pages (Data Replication, Transactional Replication, Snapshot Replication, Merge Replication, Key-Based Replication, Full Replication, Partial Replication, Active-Active Geo Distribution, Replication Lag, RPO and RTO).
Updated 5 existing pages: Synchronous Replication (RPO/RTO), Asynchronous Replication (lag), Replication (Distributed) (types/scope), Redis (Active-Active), CRDT (production use in Redis).
Key concepts: replication vs backup, CDC-based change capture, 6 replication types, sync vs async trade-offs, partial resync, Active-Active Geo Distribution with CRDTs, RPO/RTO metrics.

## [2026-05-11] ingest | AlgoMaster: How to Scale a Database

Ingested AlgoMaster blog post by Ashish Pratap Singh (Jul 2024).
Created 1 source summary, 3 new concept pages (Vertical Partitioning, Materialized View, Data Denormalization).
Key concepts: 8 database scaling strategies overview — vertical scaling, indexing, sharding, vertical partitioning (split columns by access frequency), caching, replication, materialized views (pre-computed query results), data denormalization (redundancy to avoid joins).

## [2026-05-11] ingest | AlgoMaster: 15 Types of Databases

Ingested AlgoMaster blog post by Ashish Pratap Singh (Mar 2024).
Created 1 source summary, 10 new concept pages (Key-Value Store, Graph Database, Wide-Column Store, In-Memory Database, Time-Series Database, Object-Oriented Database, Blob Datastore, Ledger Database, Hierarchical Database, Embedded Database).
Key concepts: 15 database types covering data models, use cases, examples (including relational, document, vector which were already in wiki). New additions complete the landscape from key-value through embedded databases.

## [2026-05-11] ingest | AlgoMaster: Bloom Filters

Ingested AlgoMaster.io article by Ashish Pratap Singh (Oct 2025) via Wayback Machine (Feb 2026).
Created 1 source summary, 2 new concept pages (Bloom Filter, Counting Bloom Filter).
Key concepts: bit array + k hash functions for probabilistic membership, no false negatives but false positives possible, no deletions in standard form, applications in web caching (Apache), databases (Cassandra, HBase, Redis), recommendations (Netflix), social networks (Facebook), Counting Bloom Filter variant for deletion support.

## [2026-05-11] ingest | MongoDB Atlas Architecture Center

Ingested MongoDB Atlas Well-Architected Framework docs (v20260330).
Created 1 source summary, 1 entity page (MongoDB Atlas).
Updated 1 existing concept page: Document Database (added MongoDB Atlas link).
Key concepts: 5-pillar framework (Operational Efficiency, Security, Reliability, Performance, Cost Optimization), 3-node replica sets across AZs, automatic failover in seconds, `majority` write concern, auto-scaling compute/storage, sharding strategies, Performance Advisor, data tiering, zero-downtime vertical scaling, IaC (Terraform, CLI, K8s Operator).

## [2026-05-11] ingest | AlgoMaster: Heartbeats in Distributed Systems

Ingested AlgoMaster blog post by Ashish Pratap Singh (Apr 2024).
Created 1 source summary, 1 new concept page (Heartbeat).
Updated 1 existing page: Failure Detector (added heartbeat link).
Key concepts: push vs pull heartbeats, frequency/timeout trade-offs, false positives, split-brain challenges, real-world uses (Kubernetes node → control plane, Elasticsearch gossip, DB replication).

## [2026-05-11] ingest | AlgoMaster: Service Discovery

Ingested AlgoMaster blog post by Ashish Pratap Singh (Dec 2024).
Created 1 source summary, 1 new concept page (Service Discovery).
Key concepts: service registry, 5 registration options (manual/self/sidecar/orchestrator/config), client-side (Eureka) vs server-side (AWS ELB) discovery models, best practices for HA, health checks, caching, naming conventions.

## [2026-05-11] ingest | Consensus in Distributed System

Ingested Medium article by Bhattacharjee & Mahapatra (Jan 2023).
Created 1 source summary, 3 new concept pages (Consensus, Byzantine Failure, Practical Byzantine Fault Tolerance).
Key concepts: 3 consensus properties (agreement, validity, termination), crash vs Byzantine failure models, pBFT 3-phase protocol (pre-prepare, prepare, commit), 2/3 majority rule, view change, proof-based algorithms (PoW, PoS).

## [2026-05-11] ingest | How to Do Distributed Locking

Ingested Martin Kleppmann's blog post (Feb 2016).
Created 1 source summary, 3 new concept pages (Distributed Lock, Fencing Token, Redlock).
Key concepts: efficiency vs correctness locks, process pause/GC pause problem, fencing tokens (monotonically increasing IDs validated by storage server), Redlock critique (no fencing tokens, clock dependency, synchronous assumptions), recommendation (single Redis for efficiency, ZooKeeper/etcd for correctness).

## [2026-05-11] ingest | Gossip Protocol Explained

Ingested High Scalability article by NK (Jul 2023).
Created 1 source summary, significantly expanded existing Gossip Protocol concept page (from 28 to 120 lines).
Key concepts: anti-entropy vs rumor-mongering vs aggregation models, push/pull/push-pull strategies, fanout and cycle performance (O(log n) convergence), peer sampling service, seed nodes, generation clocks, gossip digest format, real-world uses (Cassandra, Consul, Dynamo, S3, CockroachDB, Bitcoin, Redis Cluster, Riak, Hyperledger Fabric).

## [2026-05-11] ingest | Circuit Breaker Pattern

Ingested Geek Culture article by Hasitha Subhashana (Jun 2021).
Created 1 source summary, 1 new concept page (Circuit Breaker Pattern).
Key concepts: 3 states (closed/open/half-open), threshold-based tripping (latency or failure rate), fail-fast during open state, background health probes for self-healing, cascading failure prevention.

## [2026-05-11] ingest | Google Cloud: What Is Disaster Recovery?

Ingested Google Cloud article on disaster recovery.
Created 1 source summary, 1 new concept page (Disaster Recovery).
Updated 1 existing page: RPO and RTO (added link to DR).
Key concepts: 5-step DR planning (risk assessment, BIA, planning, implementation, testing), 3-2-1 backup rule, DR types (backups, BaaS, DRaaS, snapshots, virtual DR, DR sites), preventive/detective/corrective recovery elements.

## [2026-05-11] ingest | Dynatrace: What Is Distributed Tracing?

Ingested Dynatrace knowledge base article (Apr 2026).
Created 1 source summary, 1 new concept page (Distributed Tracing).
Key concepts: trace IDs spanning all services, spans as units of work (name, timestamps, parent-child hierarchy), three pillars of observability (logs, metrics, traces), head-based vs tail-based sampling, centralized vs distributed logging, MTTD/MTTR reduction.

## [2026-05-11] ingest | AlgoMaster: Client-Server Architecture

Ingested AlgoMaster.io article by Ashish Pratap Singh (Oct 2025) on client-server architecture.
Created 1 source summary, 5 concept pages (Client-Server Architecture, One-Tier Architecture, Two-Tier Architecture, Three-Tier Architecture, N-Tier Architecture). Updated Ashish Pratap Singh entity with new publication.
Key concepts: 3 components (client, server, network), 4-tier model from 1T to NT, 5-step communication flow, scaling techniques (load balancing, caching, horizontal scaling, microservices).

## [2026-05-11] ingest | Hashmap: The What, Why, and How of a Microservices Architecture

Ingested Medium article by Jetinder Singh (Hashmap, Jun 2018) on microservices architecture.
Created 1 source summary, 1 concept page (Microservices) — this fills a previously dangling [[Microservices]] WikiLink from distributed-tracing.md and ntier-architecture.md.
Key concepts: loosely coupled services, independent deployment, fault isolation, polyglot flexibility, domain-driven decomposition, 8-key implementation framework, smart endpoints/dumb pipes, design for failure.

## [2026-05-11] ingest | AlgoMaster: Serverless Architecture

Ingested unpublished Substack draft by Ashish Pratap Singh on serverless architecture (tagged System Design, ~1689 words).
Created 1 source summary, 2 concept pages (Serverless Architecture, FaaS). Updated Microservices concept page with serverless cross-link.
Key concepts: FaaS model, event-driven stateless functions, pay-per-use billing, auto-scaling, cold start latency, vendor lock-in, use cases (APIs, data processing, microservices, CI/CD).
