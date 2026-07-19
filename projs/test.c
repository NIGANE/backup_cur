// #include <stdio.h>
// #include <pthread.h>
// #include <unistd.h>


// int x = 0;
// pthread_mutex_t lock;

// void *routine(void *ac)
// {
//     pthread_t *threads;

//     threads = (pthread_t *) ac;
//     for (int i = 0; i < 10000; i++)
//     {
//         pthread_mutex_lock(&lock);
//         x++;
//         pthread_mutex_unlock(&lock);
//     }
//     return NULL;
// }

// // void take_dongles_at_first()


// int main(void)
// {
//     pthread_t p1, p2;
//     pthread_mutex_init(&lock, NULL);
//     pthread_create(&p2, NULL, &routine, NULL);
//     pthread_create(&p1, NULL, &routine, NULL);
//     pthread_join(p2, NULL);
//     pthread_join(p1, NULL);

//     printf("value of x: %d\n", x);
//     pthread_mutex_destroy(&lock);
// }
#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include "fifo/fifo.h"

typedef struct data_s{
	int id;
	int available;
	int cur_ticket;
	node_t fifo;
	pthread_mutex_t	lock;
} data_t;

void reqest()
{

}
void get_ticket()
{
	
}
void *routine(void *arg)
{

	data_t *data = (data_t *) arg;
	if (!data)
		return (printf("no shared data"), NULL);
	
	pthread_mutex_lock(&(data->lock));
	if (data->available)
	{
		data->available = 0;
		printf("hello from thread - ");
		printf("who is the king now hh.\n");
		sleep(5);
		data->available = 1;
	}
	pthread_mutex_unlock(&(data->lock));
}


int main(void)
{
	// pthread_cond_t	*cond;
	pthread_t	th[2];
	data_t *data = malloc(sizeof(data_t));
	data->available = 1;
	// cond = pthread_cond_wait_init
	int re = pthread_mutex_init(&(data->lock), NULL);
	printf("re: %d\n", re);
	
	// printf("initsializing all resources\n");
	// for (int i = 0; i < 2; i++)
	// {
	// 	pthread_create(&(th[i]), NULL, routine, (void *) data);
	// }
	// for (int i= 0; i < 2; i++)
	// {
	// 	pthread_join(th[i], NULL);
	// }
}
