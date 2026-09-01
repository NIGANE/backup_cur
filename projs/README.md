*This project has been created as part of the 42 curriculum by amerkht.*

# Codexion

## Description

**Codexion** is a high-performance concurrent multithreading simulation developed as part of the 42 curriculum. Inspired by Dijkstra's classic **Dining Philosophers Problem**, the project models $N$ software coders contending for shared hardware resources (dongles) to perform continuous compilation workflows under strict timing constraints.

- Deadlock prevention: When acquiring two dongle mutexes the code uses an ordered locking scheme in `lock_dongles_pair()` (compare pointers and always lock the lower pointer first) to avoid cyclic waits and thus prevent deadlocks.
- Starvation prevention: The system supports scheduler types (`fifo` and `edf`): EDF (earliest-deadline-first) is implemented using a heap of requests with explicit deadlines so the monitor can favor soon-to-burnout coders and reduce starvation.
- Cooldown handling: After a coder releases dongles the dongles are set with an `available` timestamp (`release_dongles()`), which prevents immediate re-granting until the cooldown expires.
- Precise burnout detection: The monitor periodically calls `check_burnout()` which compares `get_time()` with each coder's `last_compile` (or simulation start) and marks a burnout (`burned out`) when the elapsed time exceeds `time_to_burnout`.
- Log serialization: All printing to stdout is protected by `print_lock` (see `_log()`), guaranteeing non-interleaved, consistent log lines.

## Instructions

### Compilation
The project is built using standard `make` targets with strict flags (`-Wall -Wextra -Werror -pthread`).

```bash
# Compile the binary
make

# Clean object files
make clean

# Clean object files and binary
make fclean

# Rebuild the binary
make re
## Blocking cases handled
```

## Thread synchronization mechanisms

- `pthread_mutex_t dongle_lock` (per-`t_dongle`): protects each dongle's `ready_to_use` and `available` fields. Dongles are locked in a consistent order via `grab_dongles()` / `leave_dongles()` to avoid deadlocks when a coder needs two dongles.
- `pthread_cond_t cond` (per-`t_coder`): used for waiting and timed-waiting. Coders call `pthread_cond_wait(&coder->cond, &data->env_lock)` inside `sleep_coder()` while inserted in the heap; the monitor later `pthread_cond_signal()`s the corresponding coder(s) when dongles are granted or when the simulation stops.
- `pthread_mutex_t env_lock` (global `t_env`): serializes access to shared scheduler state (the heap of requests), `stop_simulation` flag. The monitor holds `env_lock` while scanning and granting requests , preventing races between monitor and coder request insertion.
- `pthread_mutex_t print_lock` (global `t_data`): serializes all output to stdout via `_log()`, preventing interleaving of output across threads.

Examples of coordination and race prevention:
- A coder wanting dongles: `request()` locks `env_lock`, inserts a `t_coder` into the heap, then waits on its condition with `pthread_cond_wait(&coder->cond, &coder->env->env_lock)`. This ensures the monitor and coder coordinate consistently on the heap state and condition signals without races.
- Granting dongles: `ft_resources()` (called by the monitor while holding `env_lock`) which briefly checks the pair of dongles to inspect `available` atomically, avoiding inconsistent reads while other threads might change those fields.

## Project structure (key files)

- `main.c` — program bootstrap, world initialization and thread creation.
- `simulation.c` — central monitor loop that checks burnout and grants dongles and the main coder lifecycle
- `resources_management.c` / `schedular_management.c` — request handling, heap processing, lock ordering, and release behaviour.
- ... other files includes helper functions 

## Resources

- POSIX threads (`pthread`) documentation: https://man7.org/linux/man-pages/man7/pthreads.7.html —
 https://www.codequoi.com/en/threads-mutexes-and-concurrent-programming-in-c/
- POSIX threads (`pthread`) playlist:https://youtu.be/d9s_d28yJq0?si=eQU8N5v7WpojyPgC — https://youtu.be/KEiur5aZnIM?si=FFEmA6O2WW6LMup1
- EDF scheduling overview: https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling
- Heap / priority queue implementation patterns in C: common data-structure references and lecture notes.: https://youtu.be/HqPJF2L5h9U?si=61dSzWtcKowp4lWe

AI usage disclosure

- An AI assistant was used to help me create this `README.md` file: summarizing the codebase, extracting synchronization and concurrency details, and drafting the usage and sections above. The codebase itself was not modified; the AI only produced documentation and explanations.
- Data Structure Verification: Validating min-heap push/pop/heapify array index operations used in the EDF scheduling queue to avoid edge-case index bugs.

