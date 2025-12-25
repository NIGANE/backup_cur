#include "../includes/sta1.h"
#include "../includes/op.h"


void sort_to_b(t_stack *a, t_stack *b ,int chunk_num)
{
    int chunk_size;
    int i;
    int low;

    low = 0;
    chunk_size = a->size / chunk_num;
    while (chunk_num-- > 0)
    {
        i = 0;
        while (i++ < chunk_size)
            chunking(a, b, low, chunk_size);
        low += chunk_size;
    }
    while (a->size > 0)
    {
        pb(b, a);
        if (b->size > 1 && b->top->index < (a->size + b->size) / 2)
            rb(b);
    }
}


