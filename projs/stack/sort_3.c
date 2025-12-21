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