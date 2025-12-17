#include "../includes/sta1.h"
#include <stdio.h>

t_stack *extract_stack(t_stack *st, int count, char **av)
{
    int i;

    i = 0;
    if (!st || !av || !*av)
        return (NULL);
    while (++i < count)
    {
        push(st, ft_atoi(av[i]));
    }
    stack_rev(&(st->top));
    return (st);
}