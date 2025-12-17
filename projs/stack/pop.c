#include <stdlib.h>
#include "../includes/sta1.h"

t_stack_node *pop(t_stack *stack)
{
    t_stack_node *temp;

    if (!stack)
        return (NULL);
    if (stack->size == 0)
        return NULL;
    temp = stack->top;
    stack->top = stack->top->next;
    temp->next = NULL;
    stack->size--;
    return (temp);
}