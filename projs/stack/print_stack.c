#include <stdio.h>
#include "../includes/sta1.h"

void print_stack(t_stack *stack)
{
    t_stack_node *cur;

    cur = stack->top;
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