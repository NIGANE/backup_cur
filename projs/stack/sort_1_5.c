#include "../includes/sta1.h"
#include "../includes/op.h"

void sort_3(t_stack *a)
{
    int index;

    if (!a)
        return ;
    index = find_largest(a);
    if (index == 0)
        ra(a);
    else if (index == 1)
        rra(a);
    
    
    if (a->top->data > a->top->next->data)
        sa(a);
}

void sort_4(t_stack *a, t_stack *b)
{
    t_stack_node *top;
    int index;

    top = a->top;
    index = find_smallest(a);
    if (index == 1)
        ra(a);
    else if (index == 2)
    {
        rra(a);
        rra(a);
    }
    else if (index == 3)
        rra(a);
    pb(b, a);
    sort_3(a);
    pa(a, b);
}

void sort_5(t_stack *a, t_stack *b)
{
    int index;

    index = find_smallest(a);
    if (index == 1)
        ra(a);
    else if (index == 2)
    {
        ra(a);
        ra(a);
    }
    else if (index == 3)
    {
        rra(a);
        rra(a);
    }
    else if (index == 4)
        rra(a);
    pb(b, a);
    sort_4(a, b);
    pa(a, b);
}

void sort_6_100()