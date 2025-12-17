#include <stdlib.h>
#include "../includes/sta1.h"

t_stack_node *create_stack(int data)
{
    t_stack_node *s;

    s = malloc(sizeof(t_stack));
    if (!s)
        return (NULL);
    s->data = data;
    s->next = NULL;
    return (s);
}