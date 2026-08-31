/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   clean.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:00:27 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/31 18:24:48 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

void	clean_env(t_env *env)
{
	if (!env)
		return ;
	if (env->coders)
		free(env->coders);
	if (env->dongles)
		free(env->dongles);
	edf_heap_free(env->heap);
	ft_free(env->fifo);
	free(env);
}

void	free_threads_mutexes(t_env *env)
{
	int	i;

	if (!env)
		return ;
	pthread_mutex_destroy(&(env->print_lock));
	pthread_mutex_destroy(&(env->env_lock));
	pthread_cond_destroy(&(env->monitor_cond));
	i = 0;
	while (i < env->nb_coders)
	{
		pthread_cond_destroy(&(env->coders[i].cond));
		pthread_mutex_destroy(&(env->dongles[i].dongle_lock));
		i++;
	}
}

int	compiles_end(t_env *env)
{
	return (env->total_compiles == env->target_compiles);
}

void	edf_heap_free(t_edf_heap *heap)
{
	int	i;

	if (!heap)
		return ;
	i = 0;
	while (i < heap->size)
	{
		edf_node_free(heap->array[i]);
		i++;
	}
	free(heap->array);
	free(heap);
}

void	edf_node_free(t_edf_node *node)
{
	if (!node)
		return ;
	node->data = NULL;
	free(node);
}
