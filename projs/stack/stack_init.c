#include <stdlib.h>
#include "../includes/sta1.h"

t_stack *stack_init()
{
    t_stack *stack;

    stack = (t_stack *)malloc(sizeof(t_stack));
    if (!stack)
        return NULL;
    stack->top = NULL;
    return (stack);
}