/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/04/12 21:34:25 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./heap/heap.h"
#include <sys/time.h>
#include <pthread.h>
#include "./header.h"

long get_time()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return ((tv.tv_sec * 1000) + (tv.tv_usec / 1000));
}

long timestamp(long start)
{
    return (get_time() - start);
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
    env->start_time = get_time();
    printf("start at [%ld]\n", env->start_time);
    if (!env->nb_coders || !env->t_burn_out || !env->t_compile
        || !env->t_debug || !env->t_refactore || !env->required_compiles
        || !env->t_cooldown)
        return (NULL);
    return (env);
}

void *life_cycle(void * arg)
{
    // t_coder *coders = (t_coder *) arg;
    printf("Executing thread:\n");
}

t_coder *create_coders(t_env *env)
{
    t_coder *coders;
    int i;
    int re;

    if (!env)
        return (NULL);
    coders = malloc(sizeof(t_coder) * env->nb_coders);
    if (!coders)
        return (NULL);
    i = 0;
    re = 0;
    while (i < env->nb_coders)
    {
        coders[i].id = i + 1;
        coders[i].compiles_end = 0;
        coders[i].env = env;
        re = pthread_create(&(coders[i].thread_id), NULL, &life_cycle, &coders[i]);
        if (re)
            return (free(coders), NULL);
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
    env = extract_args(av);
    if (!env)
        return (free(env), printf("Error: The provided arguments aren't correct.\n"), 0);

    inspect_env(env);

    coders = create_coders(env);
    if (!coders)
        return (free(env), 0);
    i = 0;
    while (i < env->nb_coders)
    {
        pthread_join(coders[i++].thread_id, NULL);

    }
    free(coders);
    free(env);
}
