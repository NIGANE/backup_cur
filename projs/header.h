
#include <pthread.h>
#include <stdio.h>

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
    pthread_mutex_t dongles[2];
} t_env;

typedef struct s_coder {
    int id;
    int compiles_end;
    t_env *env;
    pthread_t   thread_id;
} t_coder;

long ft_atoi(char *s);
void inspect_env(t_env *env);