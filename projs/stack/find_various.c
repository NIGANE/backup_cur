#include "../includes/sta1.h"
#include "../includes/op.h"

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
        cur = cur->next;
    }
    return (i);
}

int find_smallest(t_stack *a)
{
    int s;
    int i;
    t_stack_node *cur;

    if (!a)
        return (-1);
    cur = a->top;
    s = a->top->data;
    while (cur)
    {
        if (cur->data < s)
            s = cur->data;
        cur = cur->next;
    }

    i = indexof(s, a);
    return (i);
}

int find_largest(t_stack *a)
{
    int l;
    int i;
    t_stack_node *cur;

    if (!a)
        return (-1);
    cur = a->top;
    l = a->top->data;
    while (cur)
    {
        if (cur->data > l)
            l = cur->data;
        cur = cur->next;
    }

    i = indexof(l, a);
    return (i);
}

t_stack_node *find(int data, t_stack *a)
{
    t_stack_node *cur;

    if (!a)
        return (NULL);

    cur = a->top;
    while(cur)
    {
        if (cur->data == data)
            return (cur);
        cur = cur->next;
    }
    return (NULL);
}