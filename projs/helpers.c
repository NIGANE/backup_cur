#include "header.h"

int fifo_full(env_t *env)
{
    if (!env)
        return (0);
    if (!env->fifo)
        return (0);
    return (ft_len(env->fifo) == env->nb_coders);
}
int heap_full(env_t *env)
{
    if (!env)
        return (0);
    if (!(env->heap))
        return (0);
    return (env->heap->size == env->heap->capacity);
}