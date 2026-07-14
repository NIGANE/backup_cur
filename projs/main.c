/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/07/14 21:32:23 by negane           ###   ########.fr       */
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
        || !ft_atoi(av[2]) || !ft_atoi(av[3])
        || !ft_atoi(av[4]) || !ft_atoi(av[5])
        || !ft_atoi(av[6]) || !ft_atoi(av[7])
        || ft_atoi(av[8]))
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
        coders[i].compiles_end = 0;
        coders[i].env = env;
        i++;
    }
    return (coders);
}

void usage_message(void)
{
    printf("Error: helpful usage error message.");
}

t_env *init_env(t_env *env)
{
    printf("initializing env, coders and dongles\n");
    
}

int main(int ac, char **av) {
    t_env *env;
    if (ac < 8 || ac > 9 )
        return (usage_message(), 1);
    printf("parsing && vlidating\n");
    if (!extract_args(ac, av))
        return (printf("Error"), 1);
    env = init_env(env);
    // printf("runnning the simulation\n");
    // printf("waiting for stop sign\n");
}
