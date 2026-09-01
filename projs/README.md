*This project has been created as part of the 42 curriculum by aamajjou.*

# Codexion

## Description

`Codexion` is a multithreaded C simulation of coders competing for limited hardware dongles to perform compilation, debugging and refactoring cycles. The project models concurrency, scheduling (FIFO or EDF), cooldowns for shared resources, burnout detection, and log serialization. The goal is to implement a safe, deadlock-free scheduler/emulator that demonstrates correct handling of classic concurrency problems (resource allocation, starvation, and timed waits).

## Instructions

- Build: run `make` at the project root. The produced binary is `codexion`.
- Usage: `./codexion [number_of_coders] [time_to_burnout] [time_to_compile] [time_to_debug] [time_to_refactor] [number_of_compiles_required] [dongle_cooldown] [scheduler]`
  - Example: `./codexion 5 800 200 100 100 3 50 fifo`

Notes:
- The `Makefile` compiles with `-pthread` and produces `codexion`.
- The program prints timestamped events to stdout; see `logs.c` for message formatting.

## Blocking cases handled

- Deadlock prevention: When acquiring two dongle mutexes the code uses an ordered locking scheme in `lock_dongles_pair()` (compare pointers and always lock the lower pointer first) to avoid cyclic waits and thus prevent deadlocks.
- Starvation prevention: The system supports scheduler types (`fifo` and `edf`): EDF (earliest-deadline-first) is implemented using a heap of requests with explicit deadlines so the monitor can favor soon-to-burnout coders and reduce starvation.
- Cooldown handling: After a coder releases dongles the dongles are set with an `available` timestamp (`release_dongles()`), which prevents immediate re-granting until the cooldown expires.
- Precise burnout detection: The monitor periodically calls `check_burnout()` which compares `get_time()` with each coder's `last_compile` (or simulation start) and marks a burnout (`burned out`) when the elapsed time exceeds `time_to_burnout`.
- Log serialization: All printing to stdout is protected by `prt_mtx` (see `log_line()` and `log_state()`), guaranteeing non-interleaved, consistent log lines.

## Thread synchronization mechanisms

- `pthread_mutex_t dgl_mtx` (per-`t_dongle`): protects each dongle's `busy` and `available` fields. Dongles are locked in a consistent order via `lock_dongles_pair()` / `unlock_dongles_pair()` to avoid deadlocks when a coder needs two dongles.
- `pthread_mutex_t cdr_mtx` (per-`t_coder`): protects coder-local fields such as `last_compile`, `compiled`, `situation`, and `took_them`. Example: `is_coder_burned_out()` locks `cdr_mtx` while checking `situation` and `last_compile` to avoid races with the coder thread.
- `pthread_cond_t cond_cdr` (per-`t_coder`): used for waiting and timed-waiting. Coders call `pthread_cond_wait(&coder->cond_cdr, &data->data_mtx)` inside `request()` while inserted in the heap; the monitor later `pthread_cond_broadcast()`s the corresponding coder(s) when dongles are granted or when the simulation stops.
- `pthread_mutex_t data_mtx` (global `t_data`): serializes access to shared scheduler state (the heap of requests), `stop_simulation` flag, and `id_req`. The monitor holds `data_mtx` while scanning and granting requests (`check_simulation_status()` and `try_grant_dongles()`), preventing races between monitor and coder request insertion.
- `pthread_mutex_t prt_mtx` (global `t_data`): serializes all output to stdout via `log_line()` and `log_state()`, preventing interleaving of output across threads.

Examples of coordination and race prevention:
- A coder wanting dongles: `request()` locks `data_mtx`, inserts a `t_cdr_node` into the heap, then waits on its condition with `pthread_cond_wait(&coder->cond_cdr, &coder->data->data_mtx)`. This ensures the monitor and coder coordinate consistently on the heap state and condition signals without races.
- Granting dongles: `try_grant_dongles()` (called by the monitor while holding `data_mtx`) uses `can_grant_dongles()` which briefly locks the pair of dongles (`lock_dongles_pair()`) to inspect `busy` and `available` atomically, avoiding inconsistent reads while other threads might change those fields.
- Timed sleeps and interrupts: `smart_sleep()` uses `pthread_cond_timedwait()` on the coder's condition variable while holding `data_mtx` to allow early wake-ups (e.g., on burnout or stop) while still being interruptible and race-free.

## Project structure (key files)

- `main.c` — program bootstrap, world initialization and thread creation.
- `monitor.c` — central monitor loop that checks burnout and grants dongles.
- `routine.c` — `coder_routine()` and the main coder lifecycle (request → compile → debug → refactor).
- `take_dongles.c` / `request_release.c` — request handling, heap processing, lock ordering, and release behaviour.
- `logs.c` — serialized logging helpers.
- `parse.c` — command-line parsing and validation.

## Resources

- POSIX threads (`pthread`) documentation: https://man7.org/linux/man-pages/man7/pthreads.7.html —
 https://www.codequoi.com/en/threads-mutexes-and-concurrent-programming-in-c/
- POSIX threads (`pthread`) playlist:https://youtu.be/d9s_d28yJq0?si=eQU8N5v7WpojyPgC — https://youtu.be/KEiur5aZnIM?si=FFEmA6O2WW6LMup1
- Classic concurrency problems: Dining Philosophers (lock ordering, starvation) — numerous references, e.g. Dijkstra and standard OS textbooks (Silberschatz et al.).
- EDF scheduling overview: https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling
- Heap / priority queue implementation patterns in C: common data-structure references and lecture notes.

AI usage disclosure

- An AI assistant was used to help me create this `README.md` file: summarizing the codebase, extracting synchronization and concurrency details, and drafting the usage and sections above. The codebase itself was not modified; the AI only produced documentation and explanations.

