#include <stdlib.h>
#include "../includes/sta1.h"

t_stack *push(t_stack *stack, int data)
{
    t_stack_node *new_node;

    if (!stack)
        return (NULL);
    new_node = create_stack(data);
    if (!new_node)
        return (free_stack(stack), NULL);
    new_node->next = stack->top;
    stack->top = new_node;
    stack->size++;
    return stack;
}