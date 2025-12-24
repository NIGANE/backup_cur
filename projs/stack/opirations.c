#include "../includes/sta1.h"

void sa(t_stack *a)
{
    if (a)
    {
        swap(&(a->top));
        printf("sa\n");
    }
    
}

void sb(t_stack *b)
{
    if (b)
    {
        swap(&(b->top));
        printf("sb\n");
    }
}

void ss(t_stack *a, t_stack *b)
{
    sa(a);
    sb(b);
    printf("ss\n");
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
    }
    printf("pa\n");
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
    }
    printf("pb\n");
}

void ra(t_stack *stack)
{
    rotate(stack);
    printf("ra\n");
}

void rb(t_stack *stack)
{
    rotate(stack);
    printf("rb\n");
}
void rr(t_stack *a, t_stack *b)
{
    rotate(a);
    rotate(b);
    printf("rr\n");
}

void rra(t_stack *stack)
{
    rev_rotate(stack);
    printf("rra\n");
}

void rrb(t_stack *stack)
{
    rev_rotate(stack);
    printf("rrb\n");
}

void rrr(t_stack *a, t_stack *b)
{
    rev_rotate(a);
    rev_rotate(b);
    printf("rrr\n");
}