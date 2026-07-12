/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/07/12 18:02:50 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./heap/heap.h"
#include <sys/time.h>
#include <pthread.h>
#include "./header.h"

long long current_time_ms(void)
{
    struct timeval tv;

    gettimeofday(&tv, NULL);

    return (long long)tv.tv_sec * 1000 + tv.tv_usec / 1000;
}
int timestamp(long long start)
{
    return (current_time_ms() - start);
}

void suspend(long s)
{
    usleep(s * 1000);
}


t_env *extract_args(char **av)
{
    t_env *env;
    
    env = malloc(sizeof(t_env));
    if (!env)
        return (NULL);
    env->nb_coders = ft_atoi(av[1]);
    env->t_burn_out = ft_atoi(av[2]);
    env->t_compile = ft_atoi(av[3]);
    env->t_debug = ft_atoi(av[4]);
    env->t_refactore = ft_atoi(av[5]);
    env->required_compiles = ft_atoi(av[6]);
    env->t_cooldown = ft_atoi(av[7]);
    env->running = 1;
    env->start_time = current_time_ms();
    if (!env->nb_coders || !env->t_burn_out || !env->t_compile
        || !env->t_debug || !env->t_refactore || !env->required_compiles
        || !env->t_cooldown)
        return (NULL);
    return (env);
}

void *routine()
{
    // t_coder *coders = (t_coder *) arg;
    // lock mutex
    printf("Executing thread:\n");
    // unlock mutex
    return NULL;
}

t_coder *create_coders(t_env *env)
{
    t_coder *coders;
    int i;

    if (!env)
        return (NULL);
    coders = malloc(sizeof(t_coder) * env->nb_coders);
    if (!coders)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        coders[i].id = i + 1;
        coders[i].compiles_end = 0;
        coders[i].env = env;
        i++;
    }
    return (coders);
}

int main(int ac, char **av) {
    t_env *env;
    t_coder *coders;
    int i;

    if (ac < 9)
        return (printf("Error: The provided arguments aren't enough.\n"), 0);
    printf("parsing && vlidating\n");
    printf("initializing env, coders and dongles\n");
    printf("runnning the simulation\n");
    printf("waiting for stop sign\n");
    env = extract_args(av);
    if (!env)
        return (free(env), printf("Error: The provided arguments aren't correct.\n"), 0);

    coders = create_coders(env);
    if (!coders)
        return (free(env), 0);
    simulation(env, coders);
    i = 0;

    free(coders);
    free(env);
}
