
#include "../include/ft_printf.h"
long long ft_nbrlen(long long n)
{
    long long len;

    len = 0;
    if (n <= 0)
        len++;
    while (n)
    {
        n /= 10;
        len++;
    }
    return (len);
}