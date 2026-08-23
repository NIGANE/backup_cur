/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/22 18:34:24 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./header.h"

int	ft_resources(coder_t *coder)
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
	env_t	*env;
	int		i;

	if (ac < 8 || ac > 9)
		return (usage_message(), 1);
	if (!extract_args(ac, av))
		return (usage_message(), 1);
	env = init_env(av);
	if (!env)
		return (printf("exiting after cleaing\n"), 1);
	pthread_join(env->monitor_id, NULL);
	i = 0;
	while (i < env->nb_coders)
	{
		pthread_join(env->coders[i].thread_id, NULL);
		i++;
	}
	if (!env->stop_simulation)
		printf("compiles: %ld/%ld\n", env->total_compiles,
			env->target_compiles);
	free_threads_mutexes(env);
	clean_env(env);
	return (0);
}
