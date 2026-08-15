#include "header.h"

int validate_args(char **av, int st, int len)
{
    int i;

    i = st;
    while (i < 8)
    {
        if (!is_positive_number(av[i]))
            return (0);
        i++;
    }
    return (1);
}

int extract_args(int ac, char **av)
{
    env_t *env;

    if (!validate_args(av, 1, ac))
        return (printf("error validating args"), 0);
    if (!atoi(av[1]) || !atoi(av[2])
        || !atoi(av[3])
        || !atoi(av[4]) || !atoi(av[5])
        || !atoi(av[6]) || !atoi(av[7]))
        return (0);
    if (strcmp(av[8], "edf") && strcmp(av[8], "fifo"))
        return (0);
    return (1);
}