#include <stdio.h>
#include "../includes/sta1.h"

void print_stack(t_stack *stack)
{
    t_stack_node *cur;

    if (!stack)
        return ;
    cur = stack->top;
    if (!cur)
        return ;
    while (cur != NULL)
    {
        printf("|");
        printf("%d (%d)", cur->data, cur->index);
        printf("|\n");
        cur = cur->next;
    }
    printf("\\--/\n");
}