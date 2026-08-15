#include "header.h"

void request_ticket(coder_t *coder)
{
    coder->env->fifo = ft_insert(coder, coder->env->fifo);
}

coder_t *whos_next(env_t *env)
{
    if (!(env->fifo))
        return (NULL);
    return ((coder_t *) (env->fifo->data));
}

void grab_ticket(env_t *env)
{
    ft_pop(&(env->fifo));
}

int in_queue(coder_t *coder)
{
    node_t *cur;
    coder_t *tmp;
    
    cur = coder->env->fifo;
    while (cur)
    {
        tmp = (coder_t *) cur->data;
        if (tmp->id == coder->id)
            return (1);
        cur = cur->next;
    }
    return (0);
}

void lunch_up(env_t *env)
{
    int i;

    i = 0;
    while (i < env->nb_coders)
    {
        if (odd(i))
            pthread_create(&(env->coders[i].thread_id), NULL, routine, &(env->coders[i]));
        i++;
    }
    i = 0;
    while (i < env->nb_coders)
    {
        if (!odd(i))
            pthread_create(&(env->coders[i].thread_id), NULL, routine, &(env->coders[i]));
        i++;
    }
}
