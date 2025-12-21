#include "../includes/op.h"
#include "../includes/sta1.h"


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