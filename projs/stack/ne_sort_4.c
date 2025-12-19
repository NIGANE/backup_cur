#include "../includes/op.h"
#include "../includes/sta1.h"

int indexof(int data, t_stack *a)
{
    t_stack_node *cur;
    int i;

    i = 0;
    cur = a->top;
    while (cur)
    {
        if (data == cur->data)
            return (i);
        i++;
    }
    return (i);
}

void find_smallest_number(t_stack *a)
{
    int s;
    int i;
    t_stack_node *cur;

    cur = a->top;
    s = a->top->data;
    while (cur)
    {
        if (cur->data < s)
        {
            s = cur->data; 
        }
    }

    i = indexof(s, a);
    return (i);
}

void sort_4(t_stack *a, t_stack *b)
{
    t_stack_node *top;

    top = a->top;
    find_smallest_number();


    pb(b, a);
    sort_3(a);
    pa(a, b);
}