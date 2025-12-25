#include "../includes/sta1.h"
#include "../includes/op.h"


int get_pos(t_stack *st, int index)
{
    t_stack_node *cur;
    int i;

    if (!st)
        return (-1);
    cur = st->top;
    i = 0;
    while (cur)
    {
        if (cur->index == index)
            return (i);
        i++;
        cur = cur->next;
    }
    return (-1);
}

void chunking(t_stack *a, t_stack *b, int low, int size)
{
    t_stack_node *cur;
    int i;
    int first_match = -1;
    int last_match = -1;

    cur = a->top;
    i = 0;
    while (cur)
    {
        if (cur->index >= low && cur->index <= low + size - 1)
        {
            if (first_match == -1)
                first_match = i;
            last_match = i;
        }
        cur = cur->next;
        i++;
    }
    if (first_match == -1) 
        return;
    move_in_a(a, first_match, last_match);
    pb(b, a);
    if (b->size > 1 && b->top->index < (low + (low + size - 1)) / 2)
        rb(b);
}

void sort_6_100(t_stack *a, t_stack *b)
{
    int pos;
    int chunk_num;
    int i;

    if (a->size > 5 && a->size <= 100)
        chunk_num = 5;
    else if (a->size > 100 && a->size <= 500)
        chunk_num = 11;
    else
        chunk_num = 13;
    sort_to_b(a, b, chunk_num);
    i = b->size;
    while (b->size > 0)
    {
        pos = get_pos(b, i - 1);
        if (pos > b->size / 2)
            movebottom_b(b, pos); 
        else 
            movetop_b(b, pos);
        pa(a, b);
        i--;
    }
}


