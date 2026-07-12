
#include <stdio.h>
#include "./header.h"

void start(t_env *env, t_coder *coders, int (*fn)(int))
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


void thread_call(int index, t_coder *coders, t_env *env)
{
    // check_if_donles_are_available
    (void) coders;
    (void) env;
    printf("index: %d\n", index);
}

void    simulation(t_env *env, t_coder *coders)
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