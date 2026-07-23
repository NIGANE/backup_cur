
#include <pthread.h>
#include <stdio.h>
#include "./fifo/fifo.h"
#include <sys/time.h>
#include <unistd.h>

typedef struct dongle_s dongle_t;
typedef struct env_s env_t;
typedef struct coder_s coder_t;

typedef struct request_s {
    void *data;
    struct request_s *next;
} request_t;


typedef struct dongle_s{
    int id;
    int is_available;
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



long ft_atoi(char *s);
void inspecenv_t(env_t *env);
void simulation(env_t* env, coder_t *coders);
void thread_call(int index, coder_t *coders, env_t *env);
int odd(int a);
int even(int a);
int is_positive_number(char *a);

int lock(pthread_mutex_t *_lock);
int unlock(pthread_mutex_t *_lock);
int timestamp(long long start);
