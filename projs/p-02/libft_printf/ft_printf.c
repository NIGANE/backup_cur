
#include "ft_printf.h"


static void print_pointer(unsigned long n, int *count, char *hex)
{
    if (n == 0)
        *count += ft_putstr("(nil)");
    else
    {
        *count += ft_putstr("0x");
        ft_hexabase(n, hex, count);
    } 
}

static void print_hexa(unsigned long n, int *count, char *hex)
{
    if (n == 0)
        *count += ft_putchar('0');
    else 
        ft_hexabase(n, hex, count);
}

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
        print_hexa((unsigned int)va_arg(args, unsigned int), cnt, "0123456789abcdef");
    else if (*(s + 1) == 'X')
        print_hexa((unsigned int )va_arg(args, unsigned int), cnt, "0123456789ABCDEF");
    else if (*(s + 1) == 'p')
        print_pointer((unsigned long int )va_arg(args, void *), cnt, "0123456789abcdef");
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
    va_end(args);
    return (count);
}
// if (*(s + 1) == '-')
// {
//     //use atoi to calc padding
// }
// else if (ft_isdigit(*(s + 1)))
// {
//     // know next number if its 0 or diff than 0
//     // using atoi to calc numb of padding
// }
// else

