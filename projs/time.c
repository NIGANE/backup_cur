/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   time.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:48 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/31 18:25:41 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

long long	current_time_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return ((long long)tv.tv_sec * 1000 + tv.tv_usec / 1000);
}

long long	timestamp(long long start)
{
	if (!start)
		return (0);
	return (current_time_ms() - start);
}

void	suspend(long s)
{
	usleep(s * 1000);
}

void	sleep_coder(t_coder *coder)
{
	pthread_cond_wait(&(coder->cond), &(coder->env->env_lock));
}
