#include "header.h"


void *monitor(void *arg)
{
    env_t *env;
    coder_t *next_coder;

    next_coder = NULL;
    env = (env_t *) arg;
    if (!env)
        return (printf("no arg provided"), NULL);
    if (env->required_compiles == 0)
        return (env);
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
        suspend(10);
        lock(&(env->env_lock));
    }
    if (env->stop_simulation)
    {
        wake_all(env);
        unlock(&env->env_lock);
        return (env);
    }
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
        if (env->stop_simulation)
            return (unlock(&(env->env_lock)), coder);
        unlock(&(env->env_lock));
        coder->ready = 0;
        if (grab_dongles(coder))
        {
            // coder->last_compile_time = 0;
            coder->last_compile_time = current_time_ms();
            compile(coder);
            leave_dongles(coder);
            coder->compiles_count++;
            debug(coder);
            refactor(coder);
            lock(&(env->env_lock));
            env->total_compiles++;
            unlock(&(env->env_lock));
        }
    }
    return (coder);
}
