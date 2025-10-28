#include "libft_printf/ft_printf.h"
#include <stdio.h>
#include <limits.h>

int main(void)
{
    int nb = 234;
    int size_ft;
    int size_printf;
    size_ft = ft_printf("hex: %X\n", nb);
    size_printf = printf("hex: %X\n", nb);
    printf("ft_printf size: %d\n", size_ft);
    printf("printf size: %d\n", size_printf);
    return (0);
}
