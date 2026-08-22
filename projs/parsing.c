#include "header.h"

int is_number(char *s)
{
    if (!s)
        return (0);
    if (*s == '\0')
        return (0);
    while (*s)
    {
        if (*s < '0' || *s > '9')
            return (0);
        s++;
    }
    return (1);
}

void usage_message(void)
{
    printf("Error: helpful usage error message.");
}

int extract_args(int ac, char **av)
{
    env_t *env;
    int i;

    i = 1;
    while (i < ac - 1)
    {
        if (!is_number(av[i]))
            return (printf("Error: '%s' is not a valid number\n", av[i]), 1);
        i++;
    }
    if (strcmp(av[8], "edf") && strcmp(av[8], "fifo"))
        return (printf("Error message: '%s' is not a valid schedular\n", av[8]), 1);
    return (1);
}