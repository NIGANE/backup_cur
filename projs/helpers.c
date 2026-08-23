/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   helpers.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:12 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/23 17:08:23 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

int	fifo_full(t_env *env)
{
	if (!env)
		return (0);
	if (!env->fifo)
		return (0);
	return (ft_len(env->fifo) == env->nb_coders);
}

int	heap_full(t_env *env)
{
	if (!env)
		return (0);
	if (!(env->heap))
		return (0);
	return (env->heap->size == env->heap->capacity);
}

int	int_statics(char **av, t_env *env)
{
	env->req = 0;
	env->nb_coders = atoi(av[1]);
	env->t_burn_out = atoi(av[2]);
	env->t_compile = atoi(av[3]);
	env->t_debug = atoi(av[4]);
	env->t_refactore = atoi(av[5]);
	env->required_compiles = atoi(av[6]);
	env->t_cooldown = atoi(av[7]);
	env->start_simulation = 0;
	env->stop_simulation = 0;
	env->total_compiles = 0;
	env->target_compiles = env->nb_coders * env->required_compiles;
	env->fifo = NULL;
	env->heap = NULL;
	if (!strcmp(av[8], "edf") || !strcmp(av[8], "EDF"))
	{
		env->heap = edf_heap_init(env->nb_coders);
		if (!env->heap)
			return (0);
	}
	return (1);
}
