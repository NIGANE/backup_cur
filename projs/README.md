*This project has been created as part of the 42 curriculum by amerkht, amerkht.*

# Codexion

## Description
**Codexion** is a high-performance concurrent multithreading simulation developed as part of the 42 curriculum. Inspired by Dijkstra's classic **Dining Philosophers Problem**, the project models $N$ software coders contending for shared hardware resources (dongles) to perform continuous compilation workflows under strict timing constraints.

Each coder transitions through a cyclic state machine: **Compile**, **Debug**, and **Refactor**. To enter the `compile` state, a coder must acquire two adjacent hardware dongles (left and right). Upon releasing the dongles, they enter a mandatory cooldown phase (`donor_cooldown`). If any coder goes longer than `t_burn_out` milliseconds without compiling, they suffer from burnout, halting the entire system.

The project features a real-time monitoring system and supports two dynamic scheduling paradigms:
* **FIFO (First-In, First-Out):** Coders request execution tickets and acquire resources strictly in order of arrival.
* **EDF (Earliest Deadline First):** Coders are prioritized based on their proximity to burning out ($\text{Deadline} = \text{last\_compile\_time} + \text{t\_burn\_out}$) managed via a dynamic min-heap priority queue.

---

## Instructions

### Compilation
The project is built using standard standard `make` targets with strict standard flags (`-Wall -Wextra -Werror -pthread`).

```bash
# Compile the binary
make

# Clean object files
make clean

# Clean object files and binary
make fclean

# Rebuild the binary
make re
```

## Blocking cases handled

During execution, multithreaded systems face several critical synchronization hazards. Below is a detailed breakdown of the blocking cases and concurrency issues addressed in this implementation:

### 1. Deadlock Prevention & Coffman's Conditions
A system deadlock can only occur if all four **Coffman conditions** are met simultaneously:
1. **Mutual Exclusion:** Resources cannot be shared simultaneously.
2. **Hold and Wait:** A thread holding a resource requests additional resources.
3. **No Preemption:** Resources cannot be forcibly taken from a holding thread.
4. **Circular Wait:** A closed dependency chain exists where Thread $A$ waits for Thread $B$, and Thread $B$ waits for Thread $A$.

**Resolution:** This solution strictly breaks the **Circular Wait** condition by enforcing a global resource acquisition hierarchy (Hierarchical Resource Lock Ordering). Regardless of whether a dongle is to a coder's physical left or right, a coder must **always acquire the lower-ID dongle first, followed by the higher-ID dongle**:

$$\text{First Lock} = \min(\text{dongle\_left}, \text{dongle\_right}), \quad \text{Second Lock} = \max(\text{dongle\_left}, \text{dongle\_right})$$

*Why it works:* Consider the classic wrap-around boundary where the last coder contends for `Dongle 0` and `Dongle N-1`. In a naive implementation, all coders grab their left resource first, creating a cycle. Under this strict rule, the last coder attempts to lock `Dongle 0` first (the smaller ID) instead of `Dongle N-1`. If `Dongle 0` is already held by Coder 0, the last coder blocks *before* picking up `Dongle N-1`, leaving `Dongle N-1` free for the preceding coder. Circular dependency chains become mathematically impossible across the entire simulation.

---

### 2. Starvation Prevention & Scheduling Fairness
* **Hazard:** Adjacent coders repeatedly acquiring available dongles could starve an intermediate coder, causing them to sit in an infinite wait loop.
* **Resolution:** Resource contention is governed by centralized dynamic schedulers (`FIFO` or `EDF`). Coders register execution tickets or burnout priority deadlines. Even if adjacent dongles become physically free, greedy coders cannot claim them unless they hold the active queue ticket/turn (`my_turn()`), ensuring fair and starvation-free scheduling.

---

### 3. Cooldown Handling & Unblocked Waiting
* **Hazard:** If a thread holds global environment or queue mutexes while waiting out a dongle's `donor_cooldown` period, it prevents unrelated coders from updating state or progressing.
* **Resolution:** Cooldown conditions are evaluated using non-blocking timestamp comparisons (`last_release_ms`). Execution queue locks are released prior to timed suspension loops, decoupling state evaluation from resource cooldown delays.

---

### 4. Precise Burnout Detection
* **Hazard:** OS thread creation latency (`pthread_create` jitter) can delay later threads from running their first instruction, resulting in initial timestamp deficits and premature false-positive burnout triggers.
* **Resolution:** Implemented a two-phase **Start-Gate Barrier**. All worker threads spawn, initialize, and block on a `start_lock`. Once all threads report readiness, the central monitor records $T_0$, initializes all `last_compile_time` markers simultaneously, and unlocks the gate to begin simulation execution.

---

### 5. Log Serialization
* **Hazard:** Asynchronous `printf` calls from multiple concurrent threads produce interleaved, corrupted, or out-of-order console outputs.
* **Resolution:** Terminal write operations are funneled through an atomic logging function protected by a dedicated `print_lock` mutex, guaranteeing chronologically coherent and thread-safe output logging.


## Resources

### AI Usage
Artificial Intelligence (Gemini) was utilized as an engineering assistant during the development of this project for the following specific tasks and components:

1. **Debugging & Race Condition Analysis:**
   * *Startup Jitter Diagnosis:* Identified and resolved timer deficits caused by `pthread_create()` thread creation overhead by designing a two-phase Start-Gate synchronization barrier.

2. **Algorithm & Data Structure Verification:**
   * *EDF Min-Heap Operations:* Verified index arithmetic (`2i + 1`, `2i + 2`, `(i-1)/2`) for dynamic push, pop, and heapify routines in the Earliest Deadline First scheduler queue to eliminate off-by-one memory offsets.

3. **Documentation & Deliverables:**
   * Assisted in drafting, structuring, and formatting markdown technical documentation to satisfy 42 subject requirements (`README.md`).