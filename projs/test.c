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



int main(void)
{

    long long start = current_time_ms();
    int i = 1;
    while (i < 10)
    {
        printf("time: [%d]\n", timestamp(start));
        usleep(1000 * 400);
        i++;
    }

    return 0;
}
