#include "../includes/sta1.h"
#include <stdio.h>


int some_digit(char *s)
{
    while (*s)
    {
        if (*s >= 48 && *s <= 57)
            return (1);
        s++;
    }
    return (0);
}

int valid(char *s)
{
    char *bf;

    bf = s;
    while (*bf)
    {
        if (!(*bf >= 48 && *bf <= 57) && *bf != '-' && *bf != '+')
            return (0);
        bf++;
    }
    if (!some_digit(s))
        return (0);
    return (1);
}

int long_num(char *s)
{
    if (ft_atoi(s) > 2147483647 || ft_atoi(s) < -2147483648)
        return (1);
    return (0);
}

t_stack *extract_stack(t_stack *st, int count, char **av)
{
    int i;
    char **splited_arr;
    char **buffer;

    i = 0;
    if (!st || !av || !*av)
        return (NULL);
    while (++i < count)
    {
        splited_arr = ft_split(av[i], ' ');
        buffer = splited_arr;
        while (*splited_arr != NULL)
        {
            if (!valid(*splited_arr) || in_stack(ft_atoi(*splited_arr), st) || long_num(*splited_arr))
                return (free_split_arr(buffer),free_stack(st),NULL);
            push(st, ft_atoi(*splited_arr++));
        }
        free_split_arr(buffer);
    }
    stack_rev(&(st->top));
    return (st);
}