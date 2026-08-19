#include "header.h"

env_t *init_env(char **av)
{
    env_t *env;

    env = malloc(sizeof(env_t));
    if (!env)
        return (NULL);
    env->nb_coders = atoi(av[1]);
    env->t_burn_out = atoi(av[2]);
    env->t_compile = atoi(av[3]);
    env->t_debug = atoi(av[4]);
    env->t_refactore = atoi(av[5]);
    env->required_compiles = atoi(av[6]);
    env->t_cooldown = atoi(av[7]);
    env->start_simulation = 0;
    env->stop_simulation = 0;
    env->total_compiles = 0;
    env->target_compiles = env->nb_coders * env->required_compiles;
    env->fifo = NULL;
    env->heap = NULL;
    if (!strcmp(av[8], "edf"))
        env->heap = edf_heap_init(env->nb_coders);
    env->dongles = init_dongles(env);
    env->coders = init_coders(env);
    if (!(env->coders) || !(env->dongles))
        return (clean_env(env), NULL);
    init_mutexes(env);
    init_threads(env);
    return (env);
}

dongle_t *init_dongles(env_t *env)
{
    int i;
    dongle_t *dongles;

    dongles = malloc(sizeof(dongle_t) * env->nb_coders);
    if (!dongles)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        dongles[i].id = i + 1;
        dongles[i].env = env;
        dongles[i].available = 1;
        dongles[i].ready_to_use = 1;
        dongles[i].last_use = env->t_cooldown + 1;
        i++;
    }
    return (dongles);
}

coder_t *init_coders(env_t *env)
{
    coder_t *coders;
    int i;
    
    if (!(env->dongles))
        return (NULL);
    coders = malloc(sizeof(coder_t) * env->nb_coders);
    if (!coders)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        coders[i].id = i + 1;
        coders[i].compiles_count = 0;
        coders[i].req_compiles = env->required_compiles;
        coders[i].left_dongle = &(env->dongles[coders[i].id - 1]);
        coders[i].right_dongle = &(env->dongles[coders[i].id % env->nb_coders]);
        coders[i].env = env;
        coders[i].ready = 0;
        coders[i].last_compile_time = odd(coders[i].id) ? 1 : 2;
        i++;
    }
    return (coders);
}

void init_threads(env_t *env)
{
    lunch_up(env);
    pthread_create(&(env->monitor_id), NULL, monitor, env);

}

void init_mutexes(env_t *env)
{
    int i;

    i = 0;
    pthread_mutex_init(&(env->env_lock), NULL);
    pthread_mutex_init(&(env->print_lock), NULL);
    pthread_cond_init(&(env->monitor_cond), NULL);
    while (i < env->nb_coders)
    {
        pthread_mutex_init(&(env->dongles[i].dongle_lock), NULL);
        pthread_cond_init(&(env->coders[i].cond), NULL);
        i++;
    }
}
