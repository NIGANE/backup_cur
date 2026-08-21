#include "header.h"


void clean_env(env_t *env)
{
    if (!env)
        return;
    if (env->coders)
        free(env->coders);
    if (env->dongles)
        free(env->dongles);
    edf_heap_free(env->heap);
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

void edf_heap_free(edf_heap_t *heap)
{
    int i;

    if (!heap)
        return;
    i = 0;
    while (i < heap->size)
    {
        edf_node_free(heap->array[i]);
        i++;
    }
    free(heap->array);
    free(heap);
}

void edf_node_free(edf_node_t *node)
{
    if (!node)
        return;
    node->data = NULL;
    free(node);
}

