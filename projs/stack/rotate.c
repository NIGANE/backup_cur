#include <stdlib.h>
#include "../includes/sta1.h"

void rotate(t_stack *stack)
{
    t_stack_node *tmp;
    t_stack_node *cur;

    if (!stack)
        return;
    tmp = pop(stack);
    cur = stack->top;
    while (cur->next)
        cur = cur->next;
    cur->next = tmp;
}