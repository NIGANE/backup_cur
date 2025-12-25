#include <stdlib.h>
#include "../includes/sta1.h"

void stack_rev(t_stack_node **top)
{
    t_stack_node *prev;
    t_stack_node *cur;
    t_stack_node *next;

    if (!top || !*top)
        return;
    prev = NULL;
    cur = *top;
    next = cur->next;
    while (cur != NULL)
    {
        cur->next = prev;
        prev = cur;
        cur = next;
        if (next != NULL)
            next = next->next;
    }
    *top = prev;
}

t_stack *indexing(t_stack *a)
{
    int *arr;
    int i;
    t_stack_node *cur;

    if (!a)
        return (NULL);
    i = 0;
    arr = malloc(sizeof(int) * a->size);
    if (!arr)
        return (a);
    to_arr(a, arr);
    sort_arr(arr, a->size);
    while (i < a->size)
    {
        cur = find(arr[i], a);
        cur->index = i;
        i++;
    }
    free(arr);
    return (a);
}

int check(t_stack *a)
{
    t_stack_node *cur;

    if (!a)
        return (-1);
    cur = a->top;
    while (cur->next)
    {
        if (cur->data > cur->next->data)
            return (0);
        cur = cur->next;
    }
    return (1);
}
