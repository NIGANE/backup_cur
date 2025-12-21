#include "../includes/sta1.h"
#include "../includes/op.h"

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