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