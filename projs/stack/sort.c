
#include "../includes/op.h"
#include "../includes/sta1.h"


void sort(t_stack *a, t_stack *b)
{

    if (a->size < 2)
        return ;
    if (check(a))
        return ;
    if (a->size == 2)
    {
        if (a->top->data > a->top->next->data)
            sa(a);
    }
    else if (a->size == 3)
        sort_3(a);
    else if (a->size == 4)
        sort_4(a, b);
    else if (a->size == 5)
        sort_5(a, b);
    else if (a->size > 5)
    {
        indexing(a);
        sort_6_100(a, b);
    }
}