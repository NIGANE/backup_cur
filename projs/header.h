
#include <pthread.h>
#include <stdio.h>
#include "./fifo/fifo.h"
#include <sys/time.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

typedef struct dongle_s dongle_t;
typedef struct env_s env_t;
typedef struct coder_s coder_t;

typedef struct request_s {
    void *data;
    struct request_s *next;
} request_t;


typedef struct dongle_s{
    int id;
    int available;
    int ready_to_use;
    pthread_mutex_t dongle_lock;
    long last_use;
    env_t *env;
} dongle_t;

typedef struct env_s {
    int nb_coders;
    long t_compile;
    long t_debug;
    long t_refactore;
    long long t_burn_out;
    int required_compiles;
    long t_cooldown;
    int running;
    int start_simulation;
    long start_time;
    int stop_simulation;
    long total_compiles;
    long target_compiles;
    pthread_t monitor_id;
    pthread_cond_t monitor_cond;
    node_t *fifo;
    coder_t *coders;
    dongle_t *dongles;
    pthread_mutex_t env_lock;
    pthread_mutex_t print_lock;
} env_t;

typedef struct coder_s {
    int id;
    pthread_t   thread_id;
    int compiles_count;
    int req_compiles;
    long long last_compile_time;
    int ready;
    dongle_t *left_dongle;
    dongle_t *right_dongle;
    pthread_cond_t cond;
    env_t *env;
} coder_t;


//  numbers.c
int odd(int a);
int is_positive_number(char *a);

//  clean.c
void clean_env(env_t *env);
void free_threads_mutexes(env_t *env);
int compiles_end(env_t *env);

//  schedular_management.c
void request_ticket(coder_t *coder);
coder_t *whos_next(env_t *env);
void grab_ticket(env_t *env);
int in_queue(coder_t *coder);
void lunch_up(env_t *env);

//  simulation.c
void *monitor(void *arg);
void *routine(void *arg);
void check_burn_out(env_t *env);
env_t *wake_all(env_t *env);

//  time.c
long long current_time_ms(void);
long long timestamp(long long start);
void suspend(long s);

//  coder_actions.c
void compile(coder_t *coder);
void debug(coder_t *coder);
void refactor(coder_t *coder);

//  resources_management.c
void sleep_coder(coder_t *coder);
int lock(pthread_mutex_t *_lock);
int unlock(pthread_mutex_t *_lock);
void grab_dongles(coder_t *coder);
void leave_dongles(coder_t *coder);

//  parsing.c
int validate_args(char **av, int st, int len);
int extract_args(int ac, char **av);


//  init.c
env_t *init_env(char **av);
dongle_t *init_dongles(env_t *env);
coder_t *init_coders(env_t *env);
void init_threads(env_t *env);
void init_mutexes(env_t *env);


//  main.c
int ft_resources(coder_t *coder);
int odd(int a);
int is_positive_number(char *a);
coder_t *create_coders(env_t *env);
void usage_message(void);

