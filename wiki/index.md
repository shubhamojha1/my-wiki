---
title: "Wiki Index"
type: index
tags: []
created: 2026-04-05
---

# LLM Wiki

A persistent knowledge base for LLM inference systems and distributed databases.

## Sources

- [[Kafka: A Distributed Messaging System for Log Processing]] — Summary of the original Kafka paper from LinkedIn (2011)
- [[Language Models are Few-Shot Learners (GPT-3)]] — The GPT-3 paper demonstrating scaling improves few-shot learning (2020)
- [[Distributed Systems: for fun and profit]] — Mixu's comprehensive intro to distributed systems fundamentals
- [[CS 179: Introduction to GPU Programming - Lecture 1]] — Caltech course intro covering GPU architecture, CUDA, and parallel computing fundamentals
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — GPU internals: SIMD vs SIMT, thread hierarchy, warp divergence, streaming multiprocessors
- [[CS179 Recitation 1 - GPU Overview and Prefix Sum]] — Recitation covering RTX 5090, prefix sum algorithm, VS Code remote setup
- [[Best GPUs for Deep Learning in 2023]] — Tim Dettmers' comprehensive guide on GPU specs, Tensor Cores, precision formats, and recommendations
- [[CS 179: GPU Memory Systems - Lecture 4]] — GPU memory hierarchy, coalescing, bank conflicts, register spilling, computational intensity
- [[CS 179: Synchronization and ILP - Lecture 5]] — CUDA synchronization, atomic operations, ILP, warp scheduler, occupancy, floating point precision
- [[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness]] — Stanford paper: IO-aware exact attention with tiling and recomputation, 3-7x speedup
- [[FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning]] — Tri Dao 2023: 2x faster than FlashAttention, 73% theoretical max, Split-Q warp partitioning
- [[FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision]] — Tri Dao 2024: 740 TFLOPs/s (75% util), FP8 ~1.2 PFLOPs/s, warp specialization, GEMM-softmax overlap
- [[HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN]] — Google: 9.1% byte miss reduction, 1.8% CPU overhead, impact distribution analysis

## Entities

- [[Apache Kafka]] — The open-source distributed messaging system that evolved from the paper
- [[Dynamo]] — Amazon's highly available key-value store (eventual consistency)
- [[Paxos]] — Classic consensus algorithm (Lamport)
- [[Raft]] — Understandable consensus algorithm (Ongaro & Ousterhout 2013)
- [[ZAB]] — Zookeeper Atomic Broadcast protocol
- [[Two-Phase Commit]] — Distributed atomic commit protocol
- [[GPT-3]] — 175B parameter language model from OpenAI that pioneered few-shot learning
- [[OpenAI]] — AI research company that built GPT-3
- [[CUDA]] — NVIDIA's parallel computing platform for GPU programming
- [[H100]] — Hopper architecture data center GPU, fastest for deep learning
- [[A100]] — Ampere data center GPU, workhorse for enterprise deep learning
- [[RTX 4090]] — Ada Lovelace consumer flagship, best single-GPU for individuals
- [[RTX 3090]] — Ampere consumer flagship, popular for 24GB VRAM
- [[LRB]] — Learning Relaxed Belady: learned cache eviction using regression
- [[ARC]] — Adaptive Replacement Cache: balances recency and frequency
- [[Adaptive-TinyLFU]] — Frequency-based cache algorithm
- [[B-LRU]] — LRU with Bloom filter admission control

## Concepts

- [[Distributed Commit Log]] — The append-only, ordered data structure underlying Kafka's architecture
- [[Pub/Sub Messaging]] — The publish-subscribe pattern that Kafka implements
- [[Log Aggregation]] — The original use case that motivated Kafka at LinkedIn
- [[Few-Shot Learning]] — Paradigm where models learn from examples in the prompt without fine-tuning
- [[In-Context Learning]] — Mechanism enabling few-shot learning via attention to examples
- [[Emergent Abilities]] — Capabilities that appear at scale without explicit training

## Distributed Systems Concepts

### Properties & Goals

- [[Scalability]] — Ability to handle growing work without degradation
- [[Availability]] — Proportion of time system is functioning
- [[Latency]] — Time between action and visible impact
- [[Fault Tolerance]] — Well-defined behavior when faults occur
- [[Partitioning]] — Dividing dataset across nodes
- [[Replication (Distributed)]] — Copying data across multiple machines

### Models & Tradeoffs

- [[System Model]] — Assumptions about environment/facilities
- [[Synchronous System Model]] — Known timing bounds
- [[Asynchronous System Model]] — No timing guarantees
- [[CAP Theorem]] — Consistency/Availability/Partition tradeoff
- [[FLP Impossibility Result]] — Consensus impossible in async with failures
- [[Consistency Model]] — Contract between programmer and system

### Time & Ordering

- [[Total Order]] — Exact order for every element
- [[Partial Order]] — Natural distributed systems state
- [[Lamport Clocks]] — Logical ordering without physical clocks
- [[Vector Clocks]] — Accurate causal ordering
- [[Failure Detector]] — Timeout-based crash detection
- [[Epoch]] — Logical time period for consensus

### Replication & Consensus

- [[Synchronous Replication]] — Wait for all replicas
- [[Asynchronous Replication]] — Replicate later
- [[Primary-Backup Replication]] — Single master replication
- [[Quorum (Distributed)]] — Agreement from subset of nodes
- [[Network Partition]] — Network link failure
- [[Consensus Problem]] — Getting all nodes to agree

### Eventual & Weak Consistency

- [[Eventual Consistency]] — Replicas eventually agree
- [[CRDT]] — Convergent Replicated Data Types (guaranteed convergence)
- [[CALM Theorem]] — Monotonic programs are eventually consistent
- [[Bloom Language]] — Language for disorderly programming
- [[Gossip Protocol]] — Probabilistic replica sync
- [[Merkle Tree]] — Hierarchical hashes for efficient comparison
- [[Consistent Hashing]] — Key-to-node mapping that minimizes remapping

- [[What is In-Context Learning?]] — How LLMs learn from prompt examples without training
- [[GPU Computing]] — Using GPUs for general-purpose parallel computation
- [[Kernel (GPU)]] — Parallel functions that execute across many GPU threads
- [[SIMD]] — Single Instruction, Multiple Data vector processing
- [[SIMT]] — Single Instruction, Multiple Threads (CUDA model)
- [[Streaming Multiprocessor]] — GPU processing unit that executes warps
- [[Warp Divergence]] — Performance issue when threads in a warp branch differently
- [[Prefix Sum]] — Parallel algorithm for computing running sums (scan operation)
- [[Tensor Cores]] — Specialized GPU hardware for efficient matrix multiplication
- [[Memory Bandwidth]] — Critical metric for feeding data to Tensor Cores
- [[L2 Cache]] — On-chip GPU cache that speeds up memory access
- [[BF16]] — BrainFloat16, stable 16-bit format for deep learning
- [[TF32]] — TensorFloat32, NVIDIA's fast 19-bit format
- [[FP8]] — 8-bit float, emerging format for maximum speed
- [[Sparse Network Training]] — 2x speedup via structured sparsity on Ampere+
- [[Memory Hierarchy (GPU)]] — Complete GPU memory types from registers to global memory
- [[Memory Coalescing]] — Optimizing global memory access patterns
- [[Bank Conflicts]] — Avoiding shared memory serialization
- [[Register Spilling]] — When registers overflow to slow local memory
- [[Computational Intensity]] — Ratio of compute to memory I/O
- [[Latency vs Throughput]] — CPU latency-optimized vs GPU throughput-optimized design
- [[CUDA Synchronization]] — Block-level barriers (__syncthreads) and deadlock prevention
- [[Atomic Operations]] — CUDA atomic intrinsics (atomicAdd, atomicCAS) for fine-grained sync
- [[Instruction Dependencies]] — Sequential constraints that limit parallelism
- [[ILP]] — Instruction-level parallelism to hide latency
- [[Warp Scheduler]] — Hardware latency hiding via rapid warp switching
- [[Occupancy]] — Active warps ratio for latency hiding
- [[Floating Point Precision]] — Numerical accuracy, associativity, and FP16/BF16 stability
- [[FlashAttention]] — IO-aware exact attention via tiling and recomputation
- [[IO-Awareness]] — Algorithm design accounting for memory hierarchy
- [[Tiling]] — Block-based computation for fast memory
- [[Recomputation]] — Trading compute for memory via gradient checkpointing
- [[Block-Sparse Attention]] — Approximate attention via structured sparsity
- [[FlashAttention-2]] — Improved algorithm: Split-Q, sequence parallelization, reduced non-matmul FLOPs
- [[Split-Q]] — Warp partitioning scheme that eliminates synchronization overhead
- [[Warp Specialization]] — Producer-consumer asynchrony exploiting TMA and WGMMA
- [[GEMM-Softmax Overlap]] — Pingpong scheduling to hide softmax latency under matmul
- [[FP8 Attention]] — Low-precision attention with block quantization and incoherent processing
- [[Cache Eviction Policy]] — Algorithms for removing data from cache (LRU, LFU, ARC, learned policies)
- [[Pairwise Learning to Rank]] — Learning ranking via pairwise comparisons
- [[Impact Distribution Analysis]] — Measuring algorithm impact in noisy production environments