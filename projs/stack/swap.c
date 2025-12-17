#include <stdlib.h>
#include "../includes/sta1.h"

void swap(t_stack_node **top)
{
    t_stack_node *next;
    t_stack_node *cur;

    if (!*top || !top)
        return;
    cur = *top;
    next = cur->next;
    cur->next = next->next;
    next->next = cur;
    *top = next;
}