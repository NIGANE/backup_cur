#include "../stack/sta1.h"
#include "../stack/op.h"

int check(t_stack *a)
{
    t_stack_node *cur;

    if (!a)
        return (-1);
    cur = a->top;
    while (cur->next)
    {
        if (cur->data > cur->next->data)
            return (0);
        cur = cur->next;
    }
    return (1);
}