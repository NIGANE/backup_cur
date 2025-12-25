#include <stdlib.h>
#include "../includes/sta1.h"

void rotate(t_stack *stack)
{
    t_stack_node *tmp;
    t_stack_node *cur;

    if (!stack)
        return;
    tmp = pop(stack);
    if (!tmp)
        return ;
    cur = stack->top;
    if (!cur)
        return (push(stack, tmp->data), free(tmp));
    while (cur->next)
        cur = cur->next;
    cur->next = tmp;
    stack->size++;
}