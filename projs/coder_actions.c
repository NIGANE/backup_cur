/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:00:33 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/23 16:54:25 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

void	compile(t_coder *coder)
{
	if (coder->env->stop_simulation)
		return ;
	_log("[%lld] [%d] is compiling\n", timestamp(coder->env->start_time),
		coder);
	suspend(coder->env->t_compile);
}

void	debug(t_coder *coder)
{
	if (coder->env->stop_simulation)
		return ;
	_log("[%lld] [%d] is debuging\n", timestamp(coder->env->start_time), coder);
	suspend(coder->env->t_debug);
}

void	refactor(t_coder *coder)
{
	if (coder->env->stop_simulation)
		return ;
	_log("[%lld] [%d] is refactoring\n", timestamp(coder->env->start_time),
		coder);
	suspend(coder->env->t_refactore);
}

int	in_heap(t_coder *coder)
{
	t_edf_heap	*heap;
	int			i;

	if (!coder)
		return (0);
	heap = coder->env->heap;
	if (!heap)
		return (0);
	i = 0;
	while (i < heap->size)
	{
		if (heap->array[i]->data->id == coder->id)
			return (1);
		i++;
	}
	return (0);
}

void	_log(char *s, long long time, t_coder *coder)
{
	lock(&(coder->env->print_lock));
	printf(s, time, coder->id);
	unlock(&(coder->env->print_lock));
}
