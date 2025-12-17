#include <stdlib.h>
#include "../includes/sta1.h"

void free_stack(t_stack *stack)
{
    t_stack_node *curr;

    if (!stack)
        return;
    curr = stack->top;
    while (curr != NULL)
    {
        t_stack_node *temp = curr;
        curr = curr->next;
        free(temp);
    }
    free(stack);
    stack = NULL;
}