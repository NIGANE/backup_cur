
#include <stdio.h>
#include "./header.h"

void start(env_t *env, coder_t *coders, int (*fn)(int))
{
    (void) env;
    (void) coders;
    int i;

    i = 0;
    while (i < env->nb_coders)
    {
        if (fn(i))
            thread_call(i, coders, env);
        i++;
    }
}


void thread_call(int index, coder_t *coders, env_t *env)
{
    // check_if_donles_are_available
    (void) coders;
    (void) env;
    printf("index: %d\n", index);
}

void    simulation(env_t *env, coder_t *coders)
{
    (void) env;
    (void) coders;
    printf("running simulation\n");
    // if (env->nb_coders % 2)
    //     start(env, coders, odd);
    // else
    //     start(env, coders, even);
    printf("create all threads\n");
    printf("join in all these threads");
    



}