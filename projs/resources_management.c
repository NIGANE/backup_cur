/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   resources_management.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:35 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/23 15:20:23 by amerkht          ###   ########.fr       */
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
	t_dongle	*left;
	t_dongle	*right;
	t_env		*env;

	left = coder->left_dongle;
	right = coder->right_dongle;
	env = coder->env;
	if (env->stop_simulation)
		return (0);
	cooldown(env, left, right);
	if (left->ready_to_use && right->ready_to_use && !(env->stop_simulation))
	{
		lock(&(left->dongle_lock));
		_log("[%lld] [%d] has taken a dongle\n", timestamp(env->start_time),
			coder);
		lock(&(right->dongle_lock));
		_log("[%lld] [%d] has taken a dongle\n", timestamp(env->start_time),
			coder);
		left->ready_to_use = 0;
		right->ready_to_use = 0;
		return (1);
	}
	return (0);
}

void	cooldown(t_env *env, t_dongle *left, t_dongle *right)
{
	while ((timestamp(left->last_use) < env->t_cooldown
			|| timestamp(right->last_use) < env->t_cooldown)
		&& !env->stop_simulation)
		suspend(2);
}

void	leave_dongles(t_coder *coder)
{
	coder->left_dongle->last_use = current_time_ms();
	coder->right_dongle->last_use = current_time_ms();
	coder->left_dongle->ready_to_use = 1;
	coder->right_dongle->ready_to_use = 1;
	unlock(&(coder->left_dongle->dongle_lock));
	unlock(&(coder->right_dongle->dongle_lock));
	lock(&coder->env->env_lock);
	coder->left_dongle->available = 1;
	coder->right_dongle->available = 1;
	unlock(&coder->env->env_lock);
}
