#include "../includes/sta1.h"
#include "../includes/op.h"


void indexing(t_stack *a)
{
    int *arr;
    int i;
    t_stack_node *cur;

    if (!a)
        return ;
    i = 0;
    arr = malloc(sizeof(int) * a->size);
    if (!arr)
        return ;
    to_arr(a, arr);
    sort_arr(arr, a->size);
    while (i < a->size)
    {
        cur = find(arr[i], a);
        cur->index = i;
        i++;
    }
    free(arr);
}