#include "../includes/sta1.h"

void sa(t_stack *a)
{
    if (a)
        swap(&(a->top));
}

void sb(t_stack *b)
{
    if (b)
        swap(&(b->top));
}

void ss(t_stack *a, t_stack *b)
{
    sa(a);
    sb(b);
}

void pa(t_stack *a, t_stack *b)
{
    t_stack_node *node;

    if (!a || !b)
        return ;
    node = pop(b);
    if (node)
    {
        node->next = a->top;
        a->top = node;
        a->size++;
        b->size--;
    }
}

void pb(t_stack *b, t_stack *a)
{
    t_stack_node *node;

    if (!a || !b)
        return ;
    node = pop(a);
    if (node)
    {
        node->next = b->top;
        b->top = node;
        b->size++;
        a->size--;
    }
}

void ra(t_stack *stack)
{
    rotate(stack);
}

void rb(t_stack *stack)
{
    rotate(stack);
}
void rr(t_stack *a, t_stack *b)
{
    rotate(a);
    rotate(b);
}

void rra(t_stack *stack)
{
    rev_rotate(stack);
}

void rrb(t_stack *stack)
{
    rev_rotate(stack);
}

void rrr(t_stack *a, t_stack *b)
{
    rev_rotate(a);
    rev_rotate(b);
}