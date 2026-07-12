
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
    pthread_mutex_t *donles; //list of dongles
} t_env;

typedef struct s_coder {
    int id;
    int compiles_end;
    // pthread_mutex_t donle;
    pthread_t   thread_id;
    t_env *env;
} t_coder;

long ft_atoi(char *s);
void inspect_env(t_env *env);
void simulation(t_env* env, t_coder *coders);
void thread_call(int index, t_coder *coders, t_env *env);
int odd(int a);
int even(int a);