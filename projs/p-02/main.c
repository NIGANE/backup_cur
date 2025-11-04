#include "libft_printf/include/ft_printf.h"
#include <stdio.h>
#include <limits.h>


int main(void)
{

    
    // int ft_size = ft_printf("%d\n", 435);
    // int size = printf("%d\n", 435);

    // int ft_size = ft_printf("%c\n", 0);
    // int size = printf("%c\n", 0);

    // int ft_size = ft_printf("%s\n", NULL);
    // int size = printf("%s\n", NULL);

    // int ft_size = ft_printf("%s\n", "");
    // int size = printf("%s\n", "");

    // int ft_size = ft_printf("%p\n", NULL);
    // int size = printf("%p\n", NULL);
    
    // int a = 334;
    // int ft_size = ft_printf("%p\n", &a);
    // int size = printf("%p\n", &a);

    #include <limits.h>
    // int ft_size = ft_printf("%red%\n", INT_MIN);
    // int size = printf("%red%\n", INT_MIN);

    // int ft_size = ft_printf("%u\n", -1);
    // int size = printf("%u\n", -1);

    // int ft_size = ft_printf("%X\n", 255);
    // int size = printf("%X\n", 255);
    char *s = "%  red  %";

    int ft_size = ft_printf(s);
    int size = printf(s);
    
    printf("\nft_size = %d\n", ft_size);
    printf("size = %d\n", size);
}
// detect digit after %
// if d == 0 padd with 0
// if seccond number padd until d2 - nbrlen > 0
// else padd with ' '