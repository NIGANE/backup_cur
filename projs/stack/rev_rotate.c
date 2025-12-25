#include <stdlib.h>
#include "../includes/sta1.h"

void rev_rotate(t_stack *stack)
{
    t_stack_node *last;
    t_stack_node *cur;

    if (!stack)
        return;
    cur = stack->top;
    if (!cur)
        return ;

    if (!cur->next)
        return ;
    else
    {
        while (cur->next->next)
            cur = cur->next;
    }
    last = cur->next;
    cur->next = NULL;
    last->next = stack->top;
    stack->top = last;
}


