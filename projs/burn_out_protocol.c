#include "header.h"


void check_burn_out(env_t *env)
{
    coder_t *coder;
    node_t *cur;

    if (!env)
        return;
    if (env->heap)
        return (check_heap_burn_out(env));
    if (!(env->fifo))
        return;
    coder = NULL;
    cur = env->fifo;
    while (cur)
    {
        coder = (coder_t *) cur->data;
        if (timestamp(coder->last_compile_time) > env->t_burn_out)
        {
            lock(&(env->print_lock));
            printf("[%lld] [%d] burned out\n", timestamp(env->start_time), coder->id);
            unlock(&(env->print_lock));
            env->stop_simulation = 1;
            return;
        }
        cur = cur->next;
    }
}

void check_heap_burn_out(env_t *env)
{
    int i;
    coder_t *coder;

    if (!env)
        return;
    if (!env->heap)
        return;
    i = 0;
    while (i < env->heap->size)
    {
        coder = (coder_t *) env->heap->array[i]->data;
        if (timestamp(coder->last_compile_time) > env->t_burn_out)
        {
            lock(&(env->print_lock));
            printf("[%lld] [%d] burned out\n", timestamp(env->start_time), coder->id);
            unlock(&(env->print_lock));
            env->stop_simulation = 1;
            return;
        }
        i++;
    }
    return;
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
