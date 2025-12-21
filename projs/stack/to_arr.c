#include "../includes/sta1.h"

void to_arr(t_stack *a, int *arr)
{
    t_stack_node *cur;

    if (!a)
        return ;
    cur = a->top;
    while (cur)
    {
        *arr++ = cur->data;
        cur = cur->next;
    }
}