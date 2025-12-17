#include "../includes/sta1.h"

int ft_atoi(char *str)
{
    int sum;
    int sign;

    sum = 0;
    sign = 1;
    while (*str == ' ' || *str == '\t' || *str == '\n' || *str == '\f' || *str == '\r')
        str++;
    if (*str == '-' || *str == '+')
    {
        if (*str == '-')
            sign = -1;
        str++;
    }
    while (*str >= '0' && *str <= '9')
    {
        sum = sum * 10 + (*str - '0');
        str++;
    }
    return (sign * sum);
}
