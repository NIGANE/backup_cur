
#include <pthread.h>
#include <stdio.h>

typedef struct s_dongle t_dongle;
typedef struct s_env t_env;
typedef struct s_coder t_coder;

typedef struct s_dongle{
    int id;
    int is_available;
    pthread_t thread_id;
    pthread_mutex_t dongle_lock;
    t_env *env;
} t_dongle;

typedef struct s_env {
    int nb_coders;
    long t_compile;
    long t_debug;
    long t_refactore;
    long t_burn_out;
    int required_compiles;
    long t_cooldown;
    int running;
    long start_time;
    t_coder *coders;
    t_dongle *dongles;
    pthread_mutex_t env_lock;
    pthread_mutex_t print_lock;
} t_env;

typedef struct s_coder {
    int id;
    pthread_t   thread_id;
    int compiles_count;
    int req_compiles;
    t_dongle *left_dongle;
    t_dongle *right_dongle;
    t_env *env;
} t_coder;


long ft_atoi(char *s);
void inspect_env(t_env *env);
void simulation(t_env* env, t_coder *coders);
void thread_call(int index, t_coder *coders, t_env *env);
int odd(int a);
int even(int a);
int is_positive_number(char *a);
