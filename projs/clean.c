#include "header.h"

void clean_env(env_t *env)
{
    if (!env)
        return;
    if (env->coders)
        free(env->coders);
    if (env->dongles)
        free(env->dongles);
    ft_free(env->fifo);
    free(env);
}

void free_threads_mutexes(env_t *env)
{
    int i;

    if (!env)
        return;
    pthread_mutex_destroy(&(env->print_lock));
    pthread_mutex_destroy(&(env->env_lock));
    pthread_cond_destroy(&(env->monitor_cond));
    i = 0;
    while (i < env->nb_coders)
    {
        pthread_cond_destroy(&(env->coders[i].cond));
        pthread_mutex_destroy(&(env->dongles[i].dongle_lock));
        i++;
    }
}

int compiles_end(env_t *env)
{
    return (env->total_compiles == env->target_compiles);
}

