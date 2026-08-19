#include "header.h"


void inspect_fifo(node_t *head)
{
    int i;

    if (!head)
        return;
    i = 0;
    printf("inpsecting fifo\n");
    while (head)
    {
        printf("%d => %d\n", i, ((coder_t *) head->data)->id);
        head = head->next;
        i++;
    }

}

void *monitor(void *arg)
{
    env_t *env;
    coder_t *next_coder;

    next_coder = NULL;
    env = (env_t *) arg;
    if (!env)
        return (printf("no arg provided"), NULL);
    lock(&(env->env_lock));
    while (!fifo_full(env) && !heap_full(env))
    {
        unlock(&(env->env_lock));
        suspend(20);
        lock(&(env->env_lock));
    }
    env->start_time = current_time_ms();
    while (!(env->stop_simulation) && !compiles_end(env))
    {
        check_burn_out(env);
        if (env->stop_simulation)
            break;
        next_coder = whos_next(env);
        while (next_coder && ft_resources(next_coder) && !(env->stop_simulation))
        {
            grab_ticket(env);
            next_coder->ready = 1;
            pthread_cond_signal(&(next_coder->cond));
            next_coder = whos_next(env);
        }
        if (env->stop_simulation)
            break;
        unlock(&(env->env_lock));
        usleep(20);
        lock(&(env->env_lock));
    }
    if (env->stop_simulation)
        return (unlock(&env->env_lock), wake_all(env));
    unlock(&env->env_lock);
    return (env);
}

void *routine(void *arg)
{
    coder_t *coder = (coder_t *) arg;
    env_t *env = coder->env;
    if (!coder)
        return (printf("no arg provided\n"), NULL);
    while (coder->compiles_count < coder->req_compiles && !(env->stop_simulation))
    {
        lock(&(env->env_lock));
        if (!in_queue(coder) && (coder->compiles_count + 1 <= coder->req_compiles))
            request_ticket(coder);
        while (!(coder->ready) && !(env->stop_simulation))
            sleep_coder(coder);
        unlock(&(env->env_lock));
        coder->ready = 0;
        grab_dongles(coder);
        compile(coder);
        leave_dongles(coder);
        coder->compiles_count++;
        coder->last_compile_time = current_time_ms();
        debug(coder);
        refactor(coder);
        lock(&(env->env_lock));
        env->total_compiles++;
        unlock(&(env->env_lock));
    }
    return (coder);
}

void check_burn_out(env_t *env)
{
    coder_t *coder;
    node_t *cur;
    
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

env_t *wake_all(env_t *env)
{
    node_t *cur;
    coder_t *coder;
    int i;

    if (env->heap)
    {
        i = 0;
        while (i < env->heap->size)
            pthread_cond_signal(&(((coder_t *) env->heap->array[i++])->cond));
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
    usleep(10);
    return (env);
}
