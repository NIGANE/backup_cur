#include "header.h"

void compile(coder_t *coder)
{
 
    lock(&(coder->env->print_lock));
    if (coder->env->stop_simulation)
    {
        unlock(&(coder->env->print_lock));
        return;
    }
    printf("[%lld] [%d] is compiling\n", timestamp(coder->env->start_time), coder->id);
    unlock(&(coder->env->print_lock));
    suspend(coder->env->t_compile);
}
void debug(coder_t *coder)
{
    lock(&(coder->env->print_lock));
    if (coder->env->stop_simulation)
    {
        unlock(&(coder->env->print_lock));
        return;
    }
    printf("[%lld] [%d] is debuging\n", timestamp(coder->env->start_time), coder->id);
    unlock(&(coder->env->print_lock));
    suspend(coder->env->t_debug);
}
void refactor(coder_t *coder)
{
    lock(&(coder->env->print_lock));
    if (coder->env->stop_simulation)
    {
        unlock(&(coder->env->print_lock));
        return;
    }
    printf("[%lld] [%d] is refactoring\n", timestamp(coder->env->start_time), coder->id);
    unlock(&(coder->env->print_lock));
    suspend(coder->env->t_refactore);
}

int in_heap(coder_t *coder)
{
    edf_heap_t *heap;
    int i;

    if (!coder)
        return (1);
    heap = coder->env->heap;
    if (!heap)
        return (1);
    i = 0;
    while (i < heap->size)
    {
        if (((coder_t *) heap->array[i]->data)->id == coder->id)
            return (1);
        i++;
    }
    return (0);
}