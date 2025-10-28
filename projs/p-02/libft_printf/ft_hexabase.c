
#include "ft_printf.h"

void ft_hexabase(unsigned long int nb, char *hex, int *count)
{
    if (nb == 0)
        return;
    if (nb >= 16)
        ft_hexabase(nb / 16, hex, count);
    *count += ft_putchar(hex[nb % 16]);
}