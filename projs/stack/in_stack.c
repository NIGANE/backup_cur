#include "../includes/sta1.h"

int in_stack(int a, t_stack *st)
{
    t_stack_node *cur;

    cur = st->top;
    while (cur != NULL)
    {
        if ((int) cur->data ==(int) a)
            return (1);
        cur = cur->next;
    }
    return (0);
}