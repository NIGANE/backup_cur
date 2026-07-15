/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/07/15 19:23:13 by amerkht          ###   ########.fr       */
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

int	ft_strcmp(const char *s1, const char *s2)
{
	while (*s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

int validate_args(char **av, int st, int len)
{
    int i;

    i = st;
    while (i < 8)
    {
        if (!is_positive_number(av[i]))
            return (0);
        i++;
    }
    return (1);
}
int extract_args(int ac, char **av)
{
    t_env *env;

    if (!validate_args(av, 1, ac))
        return (printf("error validating args"), 0);
    if (!ft_atoi(av[1]) || !ft_atoi(av[2])
        || !ft_atoi(av[3])
        || !ft_atoi(av[4]) || !ft_atoi(av[5])
        || !ft_atoi(av[6]) || !ft_atoi(av[7]))
        return (0);
    if (ft_strcmp(av[8], "edf") && ft_strcmp(av[8], "fifo"))
        return (0);
    return (1);
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
        coders[i].compiles_count = 0;
        coders[i].env = env;
        i++;
    }
    return (coders);
}

void usage_message(void)
{
    printf("Error: helpful usage error message.");
}

t_coder *init_coders(t_env *env)
{
    t_coder *coders;
    int i;
    
    coders = malloc(sizeof(t_coder) * env->nb_coders);
    if (!coders)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        coders[i].id = i + 1;
        coders[i].compiles_count = 0;
        coders[i].req_compiles = env->required_compiles;
        coders[i].left_dongle = &(env->dongles[coders[i].id]);
        coders[i].right_dongle = &(env->dongles[coders[i].id % env->nb_coders]);
        i++;
    }
    return (coders);
}

t_dongle *init_donles(t_env *env)
{
    int i;
    t_dongle *dongles;

    dongles = malloc(sizeof(t_dongle) * env->nb_coders);
    if (!dongles)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        dongles[i].id = i + 1;
        dongles[i].env = env;
        i++;
    }
    return (dongles);
}

void init_threads(t_env *env)
{
    int i;

    i = 0;
    while (i < env->nb_coders)
    {
        pthread_create(&(env->coders[i].thread_id), NULL, routine, env);
        i++;
    }
    i = 0;
    while (i < env->nb_coders)
    {
        pthread_join(env->coders[i].thread_id, NULL);
        i++;
    }
}


t_env *init_env(char **av)
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
    env->dongles = init_donles(env);
    if (!env->dongles)
        return (free(env), NULL);
    env->coders = init_coders(env);
    if (!env->coders)
        return (free(env), NULL);
    init_threads(env);
    
    return (env);
    // printf("initializing env, coders and dongles\n");
}

int main(int ac, char **av) {
    t_env *env;
    if (ac < 8 || ac > 9 )
        return (usage_message(), 1);
    printf("parsing && vlidating\n");
    if (!extract_args(ac, av))
        return (printf("Error"), 1);
    env = init_env(av);
    // printf("runnning the simulation\n");
    // printf("waiting for stop sign\n");
}
