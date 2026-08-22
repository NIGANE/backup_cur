#include "header.h"


void check_burn_out(env_t *env)
{
    coder_t *coder;
    node_t *cur;
    int i;

    if (!env)
        return;
    i = 0;
    while (env->nb_coders > i)
    {
        if (env->coders[i].compiles_count == env->required_compiles)
        {
            i++;
            continue;
        }
        if (env->coders[i].last_compile_time != 0 && timestamp(env->coders[i].last_compile_time) > env->t_burn_out)
        {
            lock(&(env->print_lock));
            printf("[%lld] [%d] burned out\n", timestamp(env->start_time), env->coders[i].id);
            unlock(&(env->print_lock));
            env->stop_simulation = 1;
            return;
        }
        i++;
    }
}

env_t *wake_all(env_t *env)
{
    node_t *cur;
    coder_t *coder;
    int i;

    if (env->heap)
    {
        i = 0;
        while (i < env->heap->size)
            pthread_cond_signal(&(((coder_t *) env->heap->array[i++]->data)->cond));
        return (env);
    }
    if (!env->fifo)
        return (env);
    cur = env->fifo;

    while (cur)
    {
        coder = (coder_t *) cur->data;
        pthread_cond_signal(&(coder->cond));
        cur = cur->next;
    }
    return (env);
}
