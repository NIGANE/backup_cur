/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   resources_management.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:35 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/27 15:11:53 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

int	lock(pthread_mutex_t *_lock)
{
	return (pthread_mutex_lock(_lock));
}

int	unlock(pthread_mutex_t *_lock)
{
	return (pthread_mutex_unlock(_lock));
}

int	grab_dongles(t_coder *coder)
{
	t_dongle	*first;
	t_dongle	*seccond;
	t_env		*env;

	dongles_order(coder, &first, &seccond);
	env = coder->env;
	if (simulation_stopped(env))
		return (0);
	cooldown(env, first, seccond);
	if (first->ready_to_use && seccond->ready_to_use
		&& !(simulation_stopped(env)))
	{
		lock(&(first->dongle_lock));
		_log("[%lld] [%d] has taken a dongle\n", timestamp(env->start_time),
			coder);
		if (env->nb_coders == 1)
			return (unlock(&first->dongle_lock), 0);
		lock(&(seccond->dongle_lock));
		_log("[%lld] [%d] has taken a dongle\n", timestamp(env->start_time),
			coder);
		first->ready_to_use = 0;
		seccond->ready_to_use = 0;
		return (1);
	}
	return (0);
}

void	cooldown(t_env *env, t_dongle *left, t_dongle *right)
{
	while ((timestamp(left->last_use) < env->t_cooldown
			|| timestamp(right->last_use) < env->t_cooldown)
		&& !simulation_stopped(env))
		suspend(2);
}

void	leave_dongles(t_coder *coder)
{
	coder->left_dongle->last_use = current_time_ms();
	coder->right_dongle->last_use = current_time_ms();
	unlock(&(coder->left_dongle->dongle_lock));
	unlock(&(coder->right_dongle->dongle_lock));
	lock(&coder->env->env_lock);
	coder->left_dongle->ready_to_use = 1;
	coder->right_dongle->ready_to_use = 1;
	coder->left_dongle->available = 1;
	coder->right_dongle->available = 1;
	unlock(&coder->env->env_lock);
}
