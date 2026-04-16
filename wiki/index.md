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
- [[CS 179: Introduction to GPU Programming - Lecture 1]] — Caltech course intro covering GPU architecture, CUDA, and parallel computing fundamentals
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — GPU internals: SIMD vs SIMT, thread hierarchy, warp divergence, streaming multiprocessors
- [[CS179 Recitation 1 - GPU Overview and Prefix Sum]] — Recitation covering RTX 5090, prefix sum algorithm, VS Code remote setup
- [[Best GPUs for Deep Learning in 2023]] — Tim Dettmers' comprehensive guide on GPU specs, Tensor Cores, precision formats, and recommendations

## Entities

- [[Apache Kafka]] — The open-source distributed messaging system that evolved from the paper
- [[GPT-3]] — 175B parameter language model from OpenAI that pioneered few-shot learning
- [[OpenAI]] — AI research company that built GPT-3
- [[CUDA]] — NVIDIA's parallel computing platform for GPU programming
- [[H100]] — Hopper architecture data center GPU, fastest for deep learning
- [[A100]] — Ampere data center GPU, workhorse for enterprise deep learning
- [[RTX 4090]] — Ada Lovelace consumer flagship, best single-GPU for individuals
- [[RTX 3090]] — Ampere consumer flagship, popular for 24GB VRAM

## Concepts

- [[Distributed Commit Log]] — The append-only, ordered data structure underlying Kafka's architecture
- [[Pub/Sub Messaging]] — The publish-subscribe pattern that Kafka implements
- [[Log Aggregation]] — The original use case that motivated Kafka at LinkedIn
- [[Few-Shot Learning]] — Paradigm where models learn from examples in the prompt without fine-tuning
- [[In-Context Learning]] — Mechanism enabling few-shot learning via attention to examples
- [[Emergent Abilities]] — Capabilities that appear at scale without explicit training

## Queries

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