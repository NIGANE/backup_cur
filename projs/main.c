/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/27 12:51:55 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./header.h"

int	ft_resources(t_coder *coder)
{
	if (coder->left_dongle->available && coder->right_dongle->available)
	{
		coder->left_dongle->available = 0;
		coder->right_dongle->available = 0;
		return (1);
	}
	return (0);
}

int	odd(int a)
{
	return (a % 2);
}

int	main(int ac, char **av)
{
	t_env	*env;
	int		i;

	if (ac < 9)
		return (fprintf(stderr,
				"\033[1;31mError:\033[0m: missing required args\n"),
			usage_message(av[0]), 1);
	if (ac > 9)
		return (fprintf(stderr, "\033[1;31mError:\033[0m: to long args\n"),
			usage_message(av[0]), 1);
	if (!extract_args(ac, av))
		return (usage_message(av[0]), 1);
	if (atoi(av[1]) == 0)
		return (0);
	env = init_env(av);
	if (!env)
		return (fprintf(stderr,
				"\033[1;31mError:\033[0m: Failing allocating ressources\n"), 1);
	pthread_join(env->monitor_id, NULL);
	i = 0;
	while (i < env->nb_coders)
		pthread_join(env->coders[i++].thread_id, NULL);
	free_threads_mutexes(env);
	clean_env(env);
	return (0);
}
