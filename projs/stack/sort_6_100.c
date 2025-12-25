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
    int first_match;
    int last_match;
    t_stack_node *cur;
    int i;

    cur = a->top;
    i = 0;
    while (cur)
    {
        first_match = -1;
        last_match = -1;
        if (cur->index >= low && cur->index <= low + size - 1) // the current low < data < heigh
        {
            if (first_match == -1 && i <= a->size / 2)
                first_match = i;
            else
                last_match = i;
            if (i <= a->size / 2 && first_match != -1)
                movetop_a(a, first_match);
            else
                movebottom_a(a, last_match);
            pb(b, a);
            if (b->top->index < (low + (low + size - 1)) / 2 && b->size > 1 )
                rb(b);
            break ;
        }
        i++;
        cur = cur->next;
    }
}

void sort_6_100(t_stack *a, t_stack *b)
{
    int low;
    int chunk_size;
    int chunk_num;
    int i;

    if (a->size > 5 && a->size <= 100)
        chunk_num = 5;
    else if (a->size > 100 && a->size <= 500)
        chunk_num = 11;
    else
        chunk_num = 13;
    chunk_size = a->size / chunk_num;
    low = 0;
    while (chunk_num-- > 0)
    {
        i = 0;
        while (i++ < chunk_size)
            chunking(a, b, low, chunk_size);
        low += chunk_size;
    }
    i = a->size + b->size;
    while (b->size > 0)
    {
        low = get_pos(b, i - 1);
        if (low > b->size / 2)
            movebottom_b(b, low); 
        else 
            movetop_b(b, low);
        pa(a, b);
        i--;
    }
}