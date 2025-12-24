#include "../includes/sta1.h"
#include "../includes/op.h"

t_stack_node *create_stack(int data)
{
    t_stack_node *s;

    s = malloc(sizeof(t_stack_node));
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

t_stack *stack_init()
{
    t_stack *stack;

    stack = (t_stack *)malloc(sizeof(t_stack));
    if (!stack)
        return NULL;
    stack->top = NULL;
    return (stack);
}