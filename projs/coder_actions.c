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