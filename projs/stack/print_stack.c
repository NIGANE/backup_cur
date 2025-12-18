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
    printf("Stack contents (top to bottom):\n");
    while (cur != NULL)
    {
        printf("|");
        printf("%d", cur->data);
        printf("|\n");
        cur = cur->next;
    }
    printf("\\--/\n");
}