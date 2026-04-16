---
title: "Best GPUs for Deep Learning in 2023"
type: source
tags: [gpu, deep-learning, hardware, nvidia, tensor-cores]
created: 2026-04-16
sources: [timdettmers_gpu_guide_2023.md]
url: "https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/"
---

# Best GPUs for Deep Learning in 2023

## Article Details

- **Author**: Tim Dettmers
- **Published**: 2023-01-30
- **URL**: https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/

## Summary

An in-depth analysis of GPU specifications for deep learning, explaining what makes GPUs fast, comparing architectures (Hopper, Ampere, Ada), and providing practical recommendations. Tim Dettmers is known for his detailed GPU guides for deep learning practitioners.

## Most Important GPU Specs for Deep Learning

Ranked by importance:

1. **Tensor Cores** — Most critical; perform matrix multiplication in 1 cycle vs 4 cycles for FFMA
2. **Memory Bandwidth** — 2nd most important; determines how fast data reaches Tensor Cores
3. **Cache Hierarchy** — L2, shared memory, L1, registers enable fast data access
4. **FLOPS** — Only matters after the above are considered

## Key Findings

### Tensor Core Performance Impact

Matrix multiplication costs with 32×32 matrices:
- **Without Tensor Cores**: 504 cycles (200 global + 8×34 shared + 8×4 FFMA)
- **With Tensor Cores**: 235 cycles (200 global + 34 shared + 1 Tensor Core)
- **Result**: ~2x speedup from Tensor Cores alone

### Memory Bandwidth Dominates

During GPT-3-sized training, Tensor Core utilization is only 45-65% — meaning Tensor Cores are idle ~50% of the time waiting for memory. This makes memory bandwidth the best predictor of GPU performance for large models.

### Architecture L2 Cache Comparison

| Architecture | Shared Memory | L2 Cache |
|--------------|--------------|----------|
| Volta (Titan V) | 128 KB | 6 MB |
| Turing (RTX 20) | 96 KB | 5.5 MB |
| Ampere (RTX 30) | 128 KB | 6 MB |
| Ada (RTX 40) | 128 KB | **72 MB** |

Ada's 12x larger L2 cache allows models like BERT-Large to fit entirely in cache, providing 1.5-2x speedup during training.

### A100 vs V100 Practical Speedups

From NVIDIA benchmarks (corrected for batch size and multi-GPU overhead):
- SE-ResNeXt101: 1.43x faster
- Masked R-CNN: 1.47x faster
- Transformer (12-layer MT): **1.70x faster**

## Precision Formats

### BF16 (BrainFloat16)
- Same range as FP32 ([-3×10^38, 3×10^38])
- Less precision than FP16
- No loss scaling needed — more stable training
- Drop-in replacement for FP16

### TF32 (TensorFloat32)
- Near FP32 stability with FP16-like speed
- No code changes required
- Lazy format (same speed as old FP32)

### FP8 (8-bit Float)
- Supported on RTX 40 series and H100
- 2x faster data loading than FP16
- 2x more data in caches
- RTX 4090: 0.66 PFLOPS (more than world's fastest supercomputer in 2007)
- Challenge: Instability with very low bits
- Solution: LLM.int8() keeps some dimensions in high precision

## Sparse Network Training

Ampere supports fine-grained structured sparse matrix multiplication at dense speeds:
- Weight matrix sliced into 4-element pieces
- 2 of 4 elements must be zero
- Auto-compressed to half size → 2x effective throughput

Enables algorithms like RigL and Sparse Momentum to achieve actual speedups.

## Practical Multi-GPU Setup Tips

### Cooling (4x GPU systems)
- GPUs throttle at 80°C
- PCIe extenders create space between GPUs
- Very effective (used for 4+ years at UW)

### Power Management
- RTX 3090/4090: 3-slot, 350W/450W TDP
- Power limiting: reduce 50W = only 7% slower
- 4x RTX 3090 needs 1600W+ PSU
- Cryptomining PSUs can work (check form factor)

### RTX 4090 Power Connector Safety
- Only 0.1% had melting issues (user error)
- Insert cable until you hear *click*
- Test by wiggling — cable should not move
- Check visually — no gap between cable and socket

## GPU Recommendations (2023)

### Best Overall: H100 SXM
- Best performance for data center
- FP8 support, TMA unit, largest caches

### Best Consumer GPU: RTX 4090
- Best performance per dollar for individuals
- 24GB VRAM (can fit most models)
- FP8 support

### Best Value: RTX 3090
- Good performance at lower cost
- 24GB VRAM
- Consider used market

### Avoid: Any GPU without Tensor Cores

## Raw Performance Ranking (transformers)

1. H100 SXM (1.0x baseline)
2. H100 PCIe (0.85x)
3. RTX 4090 (0.33x for 8-bit, higher for 16-bit)
4. A100 PCIe (varies by precision)
5. RTX 3090

## Related Entities

- [[H100]] — Hopper architecture flagship
- [[A100]] — Ampere data center GPU
- [[RTX 4090]] — Ada Lovelace consumer flagship
- [[RTX 3090]] — Ampere consumer flagship
- [[Tensor Cores]] — The core hardware feature

## Related Concepts

- [[Tensor Cores]] — Specialized matrix multiplication hardware
- [[Memory Bandwidth]] — Critical for feeding Tensor Cores
- [[BF16]] — Stable 16-bit format
- [[TF32]] — Fast 32-bit format
- [[FP8]] — 8-bit float (RTX 40/H100)
- [[Sparse Network Training]] — 2x speedup via structured sparsity
