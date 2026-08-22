
#include <stdio.h>
#include "../header.h"

int main(void)
{
    int i;
    coder_t *poped_node;
    env_t *env = malloc(sizeof(env_t));
    if (!env)
        return (printf("error env malloc\n"), 1);
    env->coders = malloc(sizeof(coder_t) * 3);
    env->nb_coders = 3;
    env->heap = edf_heap_init(env->nb_coders);
    i = 0;
    env->start_time = current_time_ms();
    while (i < env->nb_coders)
    {
        env->coders[i].id = i + 1;
        env->coders[i].env = env;
        env->coders[i].last_compile_time = 0;
        edf_heap_push(env->heap, &(env->coders[i]));
        i++;
    }
    inspect_heap(env->heap);
    poped_node = (coder_t *) edf_heap_pop(env->heap)->data;
    inspect_heap(env->heap);
    suspend(100);
    poped_node->last_compile_time = timestamp(env->start_time);
    edf_heap_push(env->heap, poped_node);
    inspect_heap(env->heap);


    printf("hello world\n");
}