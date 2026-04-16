---
title: "GEMM-Softmax Overlap"
type: concept
tags: [gpu, performance, softmax, matmul, overlap, asynchrony]
created: 2026-04-17
sources: [flash-attention-3.md]
---

# GEMM-Softmax Overlap

Overlapping matrix multiplication (GEMM) operations with softmax computation across warpgroups using pingpong scheduling, exploiting the different throughput characteristics of these operations.

## Overview

**GEMM-Softmax Overlap** = Executing softmax operations during GEMM cycles by scheduling across two warpgroups.

**Key insight**: Softmax (specifically exp) has 256x lower throughput than matmul, so we schedule it during matmul time.

## The Throughput Problem

### H100 FP16 Performance

| Operation | Throughput | Relative Cost |
|-----------|------------|---------------|
| FP16 WGMMA (matmul) | 989 TFLOPs/s | 1x |
| FP16 special functions (exp) | 3.9 TFLOPs/s | **254x** |

### Why This Matters for Attention

For head dimension 128, attention forward pass:

```
Matmul FLOPs: 512 × more than exp FLOPs
Exp throughput: 256 × slower than matmul
─────────────────────────────────────
Exp takes: (512 / 256) = 50% of runtime!
```

**Problem**: Half the GPU cycles wasted waiting for softmax!

## FlashAttention-2: Sequential Execution

### Inner Loop (FA-2)

```python
for j in range(T_c):
    # 1. Load K_j, V_j (wait)
    K_j = load(K, j)
    V_j = load(V, j)
    
    # 2. GEMM: S = Q @ K_j^T
    S = wgmma(Q, K_j.T)
    wait(S)  # Must wait
    
    # 3. Softmax on S (exp is slow!)
    P = softmax(S)  # 50% of runtime!
    m, l = statistics(S)
    
    # 4. GEMM: O += P @ V_j
    O = wgmma(P, V_j)
    wait(O)
```

**Timeline**:
```
[GEMM][Softmax][GEMM][Softmax][GEMM][Softmax]...
         ↑
    Exp blocks here
```

## Pingpong Scheduling Solution

### Two Warpgroups

```
Warpgroup 1 (WG1): [GEMM][GEMM][GEMM][GEMM]...
Warpgroup 2 (WG2):        [GEMM][GEMM][GEMM][GEMM]...

Sync barrier between them
```

### Adding Softmax

```
Timeline:

WG1: [GEMM1][Softmax1][GEMM2][Softmax2][GEMM3]...
                   ↑ overlap with WG2's GEMM
WG2:        [GEMM1][Softmax1][GEMM2][Softmax2]...
                   ↑
            Exp scheduled during GEMM
```

### How It Works

```python
# Initialize with barrier synchronization
# Forces WG1 GEMM to complete before WG2 starts

for iteration in range(T_c):
    # Barrier: WG1 must complete GEMM before WG2
    barrier.sync()
    
    # WG1: Do softmax while WG2 does GEMM
    if warpgroup == 1:
        # Previous iteration's GEMM done, now softmax
        softmax(previous_S)  # Overlapped with WG2's GEMM
    else:  # WG2
        # Previous softmax done, now GEMM
        S = wgmma(Q, K.T)  # Overlapped with WG1's softmax
    
    # Barrier: WG2 must complete GEMM before WG1
    barrier.sync()
    
    # Swap roles
```

## 2-Stage GEMM-Softmax Pipeline

### Algorithm

```python
def attention_forward_2stage(Q, K, V):
    # S_cur: current S block (being computed)
    # S_next: next S block (in flight)
    
    # Initial: compute first S
    S_cur = wgmma(Q, K_0.T)
    commit_and_wait(S_cur)
    
    # Main loop with 2-stage pipeline
    for i in range(1, T_c - 1):
        # Start next GEMM (doesn't block)
        S_next = wgmma(Q, K_i.T)  # Stage 2
        commit(but_dont_wait())  # Issue, don't wait
        
        # Meanwhile: compute softmax on S_cur
        m, l, P = softmax(S_cur)  # Stage 1
        
        # Also: previous PV GEMM might still be running
        
        # Wait for previous PV to complete
        wait(previous_PV)
        
        # Update output
        O = update(O, P, V_prev)
        
        # Wait for S_next
        wait(S_next)
        
        # Advance pipeline
        S_cur = S_next
    
    # Final iterations
    for i in range(T_c - 1, T_c):
        # Complete remaining softmax and PV
        ...
```

### Instruction Overlap

```cuda
// Pseudocode showing overlap

// While WGMMA is in flight:
wgmma S_next = ...;
commit();  // Issue but don't wait

// Meanwhile, on different execution unit:
// (exp runs on multi-function unit, not Tensor Core)
m_new = rowmax(S_cur);
P = exp(S_cur - m_new);
l_new = rowsum(P);

// When WGMMA completes:
wait(S_next);
```

## Intra-Warpgroup Pipelining

### Beyond Pingpong: Deeper Pipeline

```python
# 3-stage pipeline: GEMM1 → Softmax1 → GEMM2 → Softmax2 → GEMM3
#                   └──S_next───┘       └──S_cur───┘

for i in range(T_c):
    # Issue next GEMM
    S_next = wgmma(Q, K_i.T)
    commit_nowaits()
    
    # Compute softmax on current S
    m, l, P = softmax(S_cur)
    
    # Issue PV GEMM
    O_next = wgmma(P, V_i)
    commit_nowaits()
    
    # Wait for previous O
    wait(O_prev)
    O = update(O, O_prev)
    
    # Advance
    S_cur = S_next
    O_prev = O_next
```

## Practical Considerations

### Compiler Reordering

**Challenge**: NVCC may reorder instructions, disrupting overlap.

**Solution**: SASS code analysis shows expected behavior; careful implementation required.

### Register Pressure

2-stage pipeline requires:
- S_cur and S_next buffers
- P_cur buffer
- Multiple m, l statistics

**Trade-off**: Better overlap vs register spilling.

### Number of Warpgroups

| Configuration | Warpgroups | Warps/WG |
|---------------|------------|----------|
| FA-2 | 1 | 8 |
| FA-3 | 2 | 4 |

**Note**: More warps per WG = more parallelism within GEMM, but no overlap.

## Performance Impact

### Ablation Results

| Configuration | TFLOPs/s | Improvement |
|---------------|-----------|-------------|
| FA-3 (baseline) | 570 | - |
| + Warp specialization only | 582 | +2% |
| + GEMM-Softmax overlap | 661 | +16% |
| + Both | 740 | +30% |

### Theoretical Analysis

For head dim 128:
- Without overlap: 50% time on exp
- With overlap: ~0% time on exp (hidden in GEMM)
- **Expected speedup**: ~2x

In practice: 16-30% improvement (exp not perfectly overlapped).

## Softmax Operations Breakdown

### What Softmax Does

```python
def softmax(S):
    # 1. Row max (comparisons)
    m = rowmax(S)           # Fast
    
    # 2. Subtract max (addition)
    S_norm = S - m          # Fast
    
    # 3. Exponential (SLOW)
    S_exp = exp(S_norm)     # 256x slower than matmul!
    
    # 4. Row sum (addition)
    l = rowsum(S_exp)       # Fast
    
    # 5. Normalize (division)
    P = S_exp / l           # Division also slow
```

### Bottleneck: exp()

```cuda
// exp() runs on multi-function unit, not Tensor Core
// Throughput: 3.9 TFLOPS vs 989 TFLOPS
// Ratio: 254x slower!
```

## Implementation in FlashAttention-3

### Pingpong Scheduling

```cuda
__global__
void flash_attention_3_kernel(...) {
    if (warpgroup_id == 0) {
        // Warpgroup 1: Do GEMM first, then softmax
        for (int i = 0; i < T_c; i++) {
            // Wait for barrier
            bar.sync(0);
            
            // Do GEMM (S = Q @ K^T)
            wgmma(S_i, Q, K_i.T);
            commit_and_wait();
            
            // Do softmax
            softmax(S_i);
            
            // Signal barrier for warpgroup 2
            bar.arrive(0);
        }
    } else {
        // Warpgroup 2: Do softmax first, then GEMM
        for (int i = 0; i < T_c; i++) {
            // Wait for warpgroup 1's softmax
            bar.arrive(0);  // Arrive at barrier
            
            // Do GEMM (O += P @ V)
            wgmma(O_i, P_i, V_i);
            commit_and_wait();
            
            // Signal barrier
            bar.arrive(0);
        }
    }
}
```

### Barrier Synchronization

```cuda
// Barriers force sequential GEMM execution
// but allow softmax overlap

// After GEMM1:
// WG1: starts softmax
// WG2: can start GEMM1

// After softmax1:
// WG1: starts GEMM2
// WG2: starts softmax1
```

## Related

- [[FlashAttention-3]] — Uses GEMM-softmax overlap
- [[Warp Specialization]] — Related technique
- [[Softmax]] — The operation being overlapped
- [[WGMMA]] — Matrix multiply being scheduled
