
#include "ft_printf.h"




static void check(const char *s, va_list args, int *cnt)
{
    if (*(s + 1) == '%')
        *cnt += ft_putchar('%');
    else if (*(s + 1) == 's')
        *cnt += ft_putstr(va_arg(args, char *));
    else if (*(s + 1) == 'c')
        *cnt += ft_putchar(va_arg(args, unsigned int));
    else if (*(s + 1) == 'd' || *(s + 1) == 'i')
        ft_putnbr(va_arg(args, int), cnt);
    else if (*(s + 1) == 'u')
        ft_putnbr(va_arg(args, unsigned int), cnt);
    else if (*(s + 1) == 'x')
        ft_hexabase(va_arg(args, unsigned long int), "0123456789abcdef", cnt);
    else if (*(s + 1) == 'X')
        ft_hexabase(va_arg(args, unsigned long int), "0123456789ABCDEF", cnt);
    else if (*(s + 1) == 'p')
    {
        *cnt += ft_putstr("0x");
        ft_hexabase((unsigned long)va_arg(args, void *), "0123456789abcdef", cnt);
    }
}

int ft_printf(const char *s, ...)
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
            count += ft_putchar(*s);
        s++;
    }
    return (count);
}