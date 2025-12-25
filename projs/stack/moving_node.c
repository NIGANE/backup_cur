#include "../includes/sta1.h"
#include "../includes/op.h"

void movetop_a(t_stack *st, int index)
{
    while (index-- > 0)
        ra(st);
}

void movebottom_a(t_stack *st, int index)
{
    while (index++ < st->size)
       rra(st);
}

void movetop_b(t_stack *st, int index)
{
    while (index-- > 0)
        rb(st);
}

void movebottom_b(t_stack *st, int index)
{
    while (index++ < st->size)
       rrb(st);
}
