---
title: "Atomic Operations"
type: concept
tags: [gpu, cuda, parallelism, synchronization, atomic]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# Atomic Operations

Operations that execute without interruption, completing entirely before any other thread accesses the same memory location. Essential for fine-grained synchronization in parallel programs.

## Overview

### What Makes an Operation Atomic?

An atomic operation guarantees:
1. **Isolation**: No other thread sees partial results
2. **Completion**: Operation finishes before next access
3. **Serialization**: Operations on same address are ordered

### When Atomics Are Needed

**Race Condition Example**:
```cuda
// Race condition!
__global__
void badIncrement(int *counter) {
    int temp = counter[0];  // Thread reads
    temp = temp + 1;         // Thread increments
    counter[0] = temp;       // Thread writes
    // Both threads read 0, both write 1 → Lost update!
}
```

**Correct with Atomics**:
```cuda
// Atomic increment
__global__
void goodIncrement(int *counter) {
    atomicAdd(counter, 1);  // Guaranteed correct
}
```

## CUDA Atomic Functions

### Arithmetic Operations

| Function | Description |
|----------|-------------|
| `atomicAdd(int *addr, int val)` | Add to address |
| `atomicAdd(float *addr, float val)` | Float add |
| `atomicSub(int *addr, int val)` | Subtract |
| `atomicInc(int *addr)` | Increment (wrap to 0) |
| `atomicDec(int *addr)` | Decrement (wrap to max) |
| `atomicMin(int *addr, int val)` | Store minimum |
| `atomicMax(int *addr, int val)` | Store maximum |

### Logical/Bitwise Operations

| Function | Description |
|----------|-------------|
| `atomicAnd(int *addr, int val)` | Bitwise AND |
| `atomicOr(int *addr, int val)` | Bitwise OR |
| `atomicXor(int *addr, int val)` | Bitwise XOR |

### Exchange Operations

| Function | Description |
|----------|-------------|
| `atomicExch(int *addr, int val)` | Exchange values |
| `atomicCAS(int *addr, int compare, int val)` | Compare-and-swap |

## Compare-and-Swap (CAS)

### The Fundamental Primitive

CAS is the building block for all other atomics:

```cuda
int atomicCAS(int *address, int compare, int val) {
    int old = *address;
    if (old == compare) {
        *address = val;
    }
    return old;  // Returns the original value
}
```

### How It Works

```
Thread 1:                          Thread 2:
atomicCAS(addr, 0, 1)             
  old = *addr (=0)                
  *addr == 0? Yes!                
  *addr = 1                       
  return 0                        
                                 atomicCAS(addr, 0, 1)
                                   old = *addr (=1)
                                   *addr == 0? No!
                                   return 1 (no change)
```

### Implementing Atomics with CAS

```cuda
// Atomic add using CAS
int atomicAddCAS(int *addr, int val) {
    int old = *addr;
    int assumed;
    do {
        assumed = old;
        old = atomicCAS(addr, assumed, assumed + val);
    } while (old != assumed);  // Retry if value changed
    return old;
}
```

### Load-Link/Store-Conditional (LL/SC)

Modern GPUs support LL/SC natively:

```cuda
// Pseudo-code concept
int atomicAddLLSC(int *addr, int val) {
    do {
        int old = load_link(addr);      // Read with reservation
    } while (!store_conditional(addr, old + val));  // Retry if lost
    return old;
}
```

## Floating-Point Atomics

### Float-Specific Considerations

```cuda
// Atomic add for floats
atomicAdd(float *addr, float val);

// But: no atomicMul, atomicDiv, atomicSub for floats!

// For other operations, implement manually:
float atomicMul(float *addr, float val) {
    float old, assumed;
    do {
        old = *addr;
        assumed = old;
        old = atomicCAS((int*)addr, 
                        __float_as_int(assumed),
                        __float_as_int(assumed * val));
    } while (old != assumed);
    return old;
}
```

### Double Precision

```cuda
// Double-precision atomics (Kepler+)
// Slower than single precision
atomicAdd(double *addr, double val);
atomicExch(double *addr, double val);
```

## Performance Characteristics

### Why Atomics Are Slow

1. **Serialization**: All threads access same address must serialize
2. **Cache coherency**: Cache lines bounce between SMs
3. **Memory contention**: High traffic on single location
4. **LL/SC retry**: Failed SC causes replay

### Performance Impact

| Scenario | Performance |
|----------|-------------|
| No contention | ~1-2x slower than non-atomic |
| Light contention (2-4 threads) | ~2-5x slower |
| Heavy contention (32+ threads) | ~10-50x slower |
| Global memory atomics | Slowest |
| Shared memory atomics | Faster (no global traffic) |

### Optimization Strategies

#### 1. Use Shared Memory First

```cuda
// SLOW: Global atomic
__global__
void badGlobalAtomic(int *counter) {
    atomicAdd(counter, 1);
}

// FAST: Shared reduction + one global atomic
__global__
void goodSharedAtomic(int *counters) {
    __shared__ int local[256];
    local[threadIdx.x] = 0;
    __syncthreads();
    
    // Parallel increment in shared memory
    atomicAdd(&local[blockIdx.x], 1);
    __syncthreads();
    
    // One global atomic per block
    if (threadIdx.x == 0) {
        atomicAdd(&counters[0], local[0]);
    }
}
```

#### 2. Hash to Reduce Contention

```cuda
// Instead of one counter, use multiple
#define NUM_BUCKETS 1024

__global__
void hashedAtomic(int *counters) {
    int bucket = threadIdx.x % NUM_BUCKETS;
    atomicAdd(&counters[bucket], 1);
}
```

#### 3. Avoid Floating-Point Atomics

```cuda
// Instead of atomicMul on floats:
// Use fixed-point or manual CAS
```

## Common Patterns

### Pattern 1: Histogram

```cuda
__global__
void histogram(unsigned char *data, int *hist, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        unsigned char val = data[i];
        atomicAdd(&hist[val], 1);
    }
}
```

### Pattern 2: Parallel Reduction (Atomic Version)

```cuda
// Simple but slow
__global__
void atomicReduction(float *data, float *result, int n) {
    if (threadIdx.x == 0 && blockIdx.x * blockDim.x < n) {
        float sum = 0;
        for (int i = blockIdx.x * blockDim.x; 
             i < min(n, (blockIdx.x + 1) * blockDim.x); 
             i++) {
            sum += data[i];
        }
        atomicAdd(result, sum);
    }
}
```

### Pattern 3: Locking with CAS

```cuda
__global__
void acquireLock(int *lock) {
    // Spin until lock acquired
    while (atomicCAS(lock, 0, 1) != 0) {
        // Lock busy, retry
    }
    // Critical section
    // ...
    // Release lock
    atomicExch(lock, 0);
}
```

### Pattern 4: Stack Operations

```cuda
// Thread-safe stack push
__device__
int push(float *stack, int *top, float value) {
    int loc = atomicAdd(top, 1);
    stack[loc] = value;
    return loc;
}
```

## Hardware Implementation

### Fermi: Global Locks

- Global memory bus locked during atomic
- Very slow for global atomics

### Kepler+: Shared Atomic Units

- Dedicated atomic units per memory controller
- Much faster than Fermi

### Maxwell+: Improved Atomics

- Better cache integration
- Reduced contention

### Volta+: Independent Thread Scheduling

- Allows fine-grained atomic behavior within warps
- Better warp-level parallelism

## Caveats and Limitations

### Shared Memory Atomics

```cuda
// Must declare shared memory as volatile for atomics
volatile __shared__ int counter[];
atomicAdd(counter, 1);  // Works in shared memory
```

### Atomic Addition on Floats

```cuda
// May not be fully associative due to rounding!
// Order of addition affects final result
atomicAdd(&x, a);
atomicAdd(&x, b);
// Result ≈ a + b (within rounding error)
```

### No Atomic Operations On:

- Automatic variables (registers)
- Local memory
- Shared memory without volatile

## Best Practices

1. **Avoid atomics when possible** — use parallel algorithms instead
2. **Use shared memory reduction** — single atomic at the end
3. **Hash to reduce contention** — multiple counters
4. **Prefer warp-level primitives** — __shfl_up, etc.
5. **Profile atomic performance** — contention kills throughput
6. **Use double only when needed** — 2x slower than float

## Related

- [[CUDA Synchronization]] — Related synchronization
- [[Instruction Dependencies]] — Why atomics serialize
- [[Occupancy]] — Contention affects occupancy
- [[Bank Conflicts]] — Similar serialization issues
