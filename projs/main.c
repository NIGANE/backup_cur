/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/15 23:48:20 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./heap/heap.h"
#define sep "//////////\n"
#include <pthread.h>


void *fn(void *)
{
	printf("hello inside the thread");
}

int	main(void)
{
	pthread_t pth;
	
	pthread_create(pth, NULL, fn, NULL);
	pthread_join(pth, NULL);
}