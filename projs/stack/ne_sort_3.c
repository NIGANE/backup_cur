#include "../includes/sta1.h"
#include "../includes/op.h"

void sort_3(t_stack *a)
{
    if (!a)
        return ;
    if (a->top->data > a->top->next->data && a->top->data > a->top->next->next->data)
        ra(a);
    else if (a->top->next->data > a->top->data && a->top->next->data > a->top->next->next->data)
        rra(a);
}