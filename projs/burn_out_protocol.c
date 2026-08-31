/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   burn_out_protocol.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:00:15 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/31 18:24:46 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

void	check_burn_out(t_env *env)
{
	long long	flag;
	int			i;

	if (!env)
		return ;
	i = 0;
	flag = 0;
	while (env->nb_coders > i)
	{
		if (env->coders[i].compiles_count == env->required_compiles)
		{
			i++;
			continue ;
		}
		flag = env->coders[i].last_compile_time;
		if (flag == 0)
			flag = env->start_time;
		burned_out(&(env->coders[i]), flag);
		i++;
	}
}

void	burned_out(t_coder *coder, long long flag)
{
	if (timestamp(flag) > coder->env->t_burn_out)
	{
		coder->env->stop_simulation = 1;
		lock(&(coder->env->print_lock));
		printf("[%lld] [%d] burned out\n", timestamp(coder->env->start_time),
			coder->id);
		unlock(&(coder->env->print_lock));
		return ;
	}
}

t_env	*wake_all(t_env *env)
{
	t_node	*cur;
	t_coder	*coder;
	int		i;

	if (env->heap)
	{
		i = 0;
		while (i < env->heap->size)
			pthread_cond_signal(&(env->heap->array[i++]->data->cond));
		return (env);
	}
	if (!env->fifo)
		return (env);
	cur = env->fifo;
	while (cur)
	{
		coder = (t_coder *)cur->data;
		pthread_cond_signal(&(coder->cond));
		cur = cur->next;
	}
	return (env);
}

void	update_start_time(t_env *env)
{
	int	i;

	i = 0;
	env->start_time = current_time_ms();
	while (i < env->nb_coders)
	{
		env->coders[i].last_compile_time = env->start_time;
		i++;
	}
}
