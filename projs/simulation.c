/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:44 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/26 10:27:05 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

void	*monitor(void *arg)
{
	t_env	*env;

	env = (t_env *)arg;
	if (!env)
		return (printf("Error detected!\n"), NULL);
	if (env->required_compiles == 0)
		return (env);
	lock(&(env->env_lock));
	while (!fifo_full(env) && !heap_full(env))
	{
		unlock(&(env->env_lock));
		suspend(10);
		lock(&(env->env_lock));
	}
	monitor_body(env);
	if (env->stop_simulation)
	{
		wake_all(env);
		unlock(&env->env_lock);
		return (env);
	}
	unlock(&env->env_lock);
	return (env);
}

void	monitor_body(t_env *env)
{
	t_coder	*next_coder;

	next_coder = NULL;
	env->start_time = current_time_ms();
	while (!(env->stop_simulation) && !compiles_end(env))
	{
		check_burn_out(env);
		if (env->stop_simulation)
			break ;
		next_coder = whos_next(env);
		while (next_coder && ft_resources(next_coder)
			&& !(env->stop_simulation))
		{
			grab_ticket(env);
			next_coder->ready = 1;
			pthread_cond_signal(&(next_coder->cond));
			next_coder = whos_next(env);
		}
		if (env->stop_simulation)
			break ;
		unlock(&(env->env_lock));
		suspend(1);
		lock(&(env->env_lock));
	}
}

void	*routine(void *arg)
{
	t_coder	*coder;
	t_env	*env;

	coder = (t_coder *)arg;
	env = coder->env;
	if (!coder)
		return (printf("Error detected!\n"), NULL);
	while (coder->compiles_count < coder->req_compiles
		&& !(env->stop_simulation))
	{
		lock(&(env->env_lock));
		if (!in_queue(coder) && (coder->compiles_count
				+ 1 <= coder->req_compiles))
			request_ticket(coder);
		while (!(coder->ready) && !(env->stop_simulation))
			sleep_coder(coder);
		if (env->stop_simulation)
			return (unlock(&(env->env_lock)), coder);
		unlock(&(env->env_lock));
		routine_body(coder);
	}
	return (coder);
}

void	routine_body(t_coder *coder)
{
	coder->ready = 0;
	if (grab_dongles(coder))
	{
		coder->last_compile_time = current_time_ms();
		compile(coder);
		leave_dongles(coder);
		coder->compiles_count++;
		debug(coder);
		refactor(coder);
		lock(&(coder->env->env_lock));
		coder->env->total_compiles++;
		unlock(&(coder->env->env_lock));
	}
}
