/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:16 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/31 18:25:10 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

t_env	*init_env(char **av)
{
	t_env	*env;

	env = malloc(sizeof(t_env));
	if (!env)
		return (NULL);
	if (!int_statics(av, env))
		return (NULL);
	env->dongles = init_dongles(env);
	env->coders = init_coders(env);
	if (!(env->coders) || !(env->dongles))
		return (clean_env(env), NULL);
	if (!init_mutexes(env))
		return (clean_env(env), NULL);
	if (!init_threads(env))
	{
		free_threads_mutexes(env);
		clean_env(env);
		return (NULL);
	}
	return (env);
}

t_dongle	*init_dongles(t_env *env)
{
	int			i;
	t_dongle	*dongles;

	dongles = malloc(sizeof(t_dongle) * env->nb_coders);
	if (!dongles)
		return (NULL);
	i = 0;
	while (i < env->nb_coders)
	{
		dongles[i].id = i + 1;
		dongles[i].env = env;
		dongles[i].available = 1;
		dongles[i].ready_to_use = 1;
		dongles[i].last_use = env->t_cooldown + 1;
		i++;
	}
	return (dongles);
}

t_coder	*init_coders(t_env *env)
{
	t_coder	*coders;
	int		i;

	if (!env || !(env->dongles))
		return (NULL);
	coders = malloc(sizeof(t_coder) * env->nb_coders);
	if (!coders)
		return (NULL);
	i = 0;
	while (i < env->nb_coders)
	{
		coders[i].id = i + 1;
		coders[i].compiles_count = 0;
		coders[i].req_compiles = env->required_compiles;
		coders[i].left_dongle = &(env->dongles[coders[i].id - 1]);
		coders[i].right_dongle = &(env->dongles[coders[i].id % env->nb_coders]);
		coders[i].env = env;
		coders[i].ready = 0;
		coders[i].last_compile_time = 0;
		i++;
	}
	return (coders);
}

int	init_threads(t_env *env)
{
	if (!lunch_up(env))
		return (0);
	if (pthread_create(&(env->monitor_id), NULL, monitor, env) != 0)
		return (0);
	return (1);
}

int	init_mutexes(t_env *env)
{
	int	i;

	i = 0;
	if (pthread_mutex_init(&(env->env_lock), NULL) != 0)
		return (0);
	if (pthread_mutex_init(&(env->print_lock), NULL) != 0)
		return (0);
	if (pthread_cond_init(&(env->monitor_cond), NULL) != 0)
		return (0);
	while (i < env->nb_coders)
	{
		if (pthread_mutex_init(&(env->dongles[i].dongle_lock), NULL) != 0)
			return (0);
		if (pthread_cond_init(&(env->coders[i].cond), NULL) != 0)
			return (0);
		i++;
	}
	return (1);
}
