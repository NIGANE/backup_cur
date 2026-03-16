/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/16 09:45:33 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./heap/heap.h"
#define sep "//////////\n"
#include <pthread.h>

pthread_t tid[2];
int counter;
pthread_mutex_t lock;

void* trythis(void* arg) {
	(void) arg;
    counter += 1;
    printf("Job %d started\n", counter);
	counter++;
    printf("Job %d finished\n", counter);
    return NULL;

}

int main() {

    pthread_mutex_init(&lock, NULL);
    for (int i = 0; i < 2; i++)
	{
        pthread_create(&tid[i], NULL, trythis, NULL);
	}
	pthread_mutex_lock(&lock);
	pthread_join(tid[0], NULL);
    pthread_mutex_unlock(&lock);
    pthread_join(tid[1], NULL);
    pthread_mutex_destroy(&lock);
    return 0;

} 