#include <stdio.h>
#include <stdarg.h>
#include <unistd.h>
#include "libft/libft.h"

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

void ft_hexa_base(unsigned int nb, char *hex)
{
    if (nb == 0)
        return;
    if (nb >= 16)
        ft_hexa_base(nb / 16, hex);
    ft_putchar_fd(hex[nb % 16], 1);
}
void check(char *s, va_list args, int *cnt)
{
    long long nb;

    if (*(s + 1) == '%')
        *cnt += ft_putchar_fd('%', 1);
    if (*(s + 1) == 's')
        *cnt += ft_putstr_fd(va_arg(args, char *), 1);
    if (*(s + 1) == 'c')
        *cnt += ft_putchar_fd(va_arg(args, unsigned int), 1);
    if (*(s + 1) == 'd' || *(s + 1) == 'i')
    {
        nb = va_arg(args, int);
        *cnt += ft_nbrlen(nb);
        ft_putnbr_fd(nb, 1);
    }
    if (*(s + 1) == 'u')
    {
        nb = va_arg(args, unsigned int);
        *cnt += ft_nbrlen(nb);
        ft_putnbr_fd(nb, 1);
    }
    if (*(s + 1) == 'x')
    {
        nb = va_arg(args, unsigned int);
        *cnt += ft_nbrlen(nb);
        ft_hexa_base(nb, "0123456789abcdef");
    }
    if (*(s + 1) == 'X')
    {
        nb = va_arg(args, unsigned int);
        *cnt += ft_nbrlen(nb);
        ft_hexa_base(nb, "0123456789ABCDEF");
    }
    if (*(s + 1) == 'p')
    {
        nb = (unsigned long)va_arg(args, void *);
        ft_putstr_fd("0x", 1);
        ft_hexa_base(nb, "0123456789ABCDEF");
    }
}

int ft_printf(char *s, ...)
{
    int count;
    va_list args;

    count = 0;
    va_start(args, s);
    while (*s)
    {
        if (*s == '%' && *(s + 1))
        {
            check(s, args, &count);
            s++;
        }
        else
            count += ft_putchar_fd(*s, 1);
        s++;
    }
    return (count);
}

int main(void)
{
    int size_ft;
    int size_printf;
    size_ft = ft_printf("hex: %x\n", 2536);
    size_printf = printf("hex: %x\n", 2536);
    printf("ft_printf size: %d\n", size_ft);
    printf("printf size: %d\n", size_printf);
    return (0);
}