#include "../includes/sta1.h"
#include "../includes/op.h"


void movetop(t_stack *a, int index)
{
    while (index-- > 0)
        ra(a);
}

void movebottom(t_stack *a, int index)
{
    while (index++ < a->size)
        rra(a);
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
            printf("founded on index: %d\n", i);
            if (first_match == -1 && i < a->size / 2)
                first_match = i;
            else
                last_match = i;
            if (first_match < size - last_match && first_match != -1)
                movetop(a, first_match);
            else
                movebottom(a, last_match);
            pb(b, a);
            if (b->top->index < (low + (low + size - 1)) / 2 && b->size > 1 )
                rb(b);
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
    print_stack(a);
    while (chunk_num-- > 0)
    {
        i = 0;
        while (i++ < chunk_size)
            chunking(a, b, low, chunk_size);
        low += chunk_size;
        printf("low had beed updated: %d\n", low);
    }
    print_stack(b);
}