
#include "../includes/op.h"
#include "../includes/sta1.h"


void sort(t_stack *a, t_stack *b)
{
    if (a->size <2)
        return ;
    if (a->size == 2)
    {
        if (a->top->data > a->top->next->data)
            sp(a);
    }
    else if (a->size == 3)
    {
        sort_3(a);
    }
    else if (a->size == 4)
    {
        sort_4(a, b);
    }
}