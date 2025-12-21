#include "../includes/sta1.h"

t_stack_node *create_stack(int data)
{
    t_stack_node *s;

    s = malloc(sizeof(t_stack));
    if (!s)
        return (NULL);
    s->data = data;
    s->next = NULL;
    return (s);
}

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

#include "../includes/sta1.h"

int in_stack(int a, t_stack *st)
{
    t_stack_node *cur;

    cur = st->top;
    while (cur != NULL)
    {
        if ((int) cur->data ==(int) a)
            return (1);
        cur = cur->next;
    }
    return (0);
}

