/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   schedular_management.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:40 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/24 10:03:56 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

void	request_ticket(t_coder *coder)
{
	if (!coder || coder->env->stop_simulation)
		return ;
	if (coder->env->heap)
	{
		coder->env->heap = edf_heap_push(coder->env->heap, coder);
		if (!coder->env->heap)
			coder->env->stop_simulation = 1;
		return ;
	}
	coder->env->fifo = ft_insert(coder, coder->env->fifo);
	if (!coder->env->fifo)
		coder->env->stop_simulation = 1;
}

t_coder	*whos_next(t_env *env)
{
	if ((env->heap) && env->heap->size > 0)
		return (env->heap->array[0]->data);
	if (!(env->fifo))
		return (NULL);
	return ((t_coder *)(env->fifo->data));
}

void	grab_ticket(t_env *env)
{
	t_edf_node	*node;

	if (env->heap && env->heap->size > 0)
	{
		node = edf_heap_pop(env->heap);
		edf_node_free(node);
		return ;
	}
	free(ft_pop(&(env->fifo)));
}

int	in_queue(t_coder *coder)
{
	t_node	*cur;
	t_coder	*tmp;

	if (coder->env->heap)
		return (in_heap(coder));
	cur = coder->env->fifo;
	while (cur)
	{
		tmp = (t_coder *)cur->data;
		if (tmp->id == coder->id)
			return (1);
		cur = cur->next;
	}
	return (0);
}

int	lunch_up(t_env *env)
{
	int	i;

	i = 0;
	while (i < env->nb_coders)
	{
		if (odd(i))
		{
			if (pthread_create(&(env->coders[i].thread_id), NULL, routine,
					&(env->coders[i])) != 0)
				return (0);
		}
		i++;
	}
	i = 0;
	while (i < env->nb_coders)
	{
		if (!odd(i))
		{
			if (pthread_create(&(env->coders[i].thread_id), NULL, routine,
					&(env->coders[i])) != 0)
				return (0);
		}
		i++;
	}
	return (1);
}
