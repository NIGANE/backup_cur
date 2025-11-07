#include <stdio.h>
#include "include/ft_printf.h"

int main(void)
{
    int ret1, ret2;
    char c = 'A';
    char *str = "Hello, World!";
    char *null_str = NULL;
    int num = 42;
    int neg = -42;
    unsigned int u = 4294967295U;
    void *ptr = &num;

    printf("----- %%c tests -----\n");
    ret1 = printf("Original: char = %c\n", c);
    ret2 = ft_printf("Custom  : char = %c\n", c);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    printf("----- %%s tests -----\n");
    ret1 = printf("Original: string = %s\n", str);
    ret2 = ft_printf("Custom  : string = %s\n", str);
    printf("Return values: printf=%d | ft_printf=%d\n", ret1, ret2);

    ret1 = printf("Original: NULL string = %s\n", null_str);
    ret2 = ft_printf("Custom  : NULL string = %s\n", null_str);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    printf("----- %%p tests -----\n");
    ret1 = printf("Original: pointer = %p\n", ptr);
    ret2 = ft_printf("Custom  : pointer = %p\n", ptr);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    printf("----- %%d / %%i tests -----\n");
    ret1 = printf("Original: int = %d, %i\n", num, neg);
    ret2 = ft_printf("Custom  : int = %d, %i\n", num, neg);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    printf("----- %%u tests -----\n");
    ret1 = printf("Original: unsigned = %u\n", u);
    ret2 = ft_printf("Custom  : unsigned = %u\n", u);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    printf("----- %%x / %%X tests -----\n");
    ret1 = printf("Original: hex lowercase = %x\n", u);
    ret2 = ft_printf("Custom  : hex lowercase = %x\n", u);
    printf("Return values: printf=%d | ft_printf=%d\n", ret1, ret2);

    ret1 = printf("Original: hex uppercase = %X\n", u);
    ret2 = ft_printf("Custom  : hex uppercase = %X\n", u);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    printf("----- %% percent sign tests -----\n");
    ret1 = printf("Original: 100%% sure\n");
    ret2 = ft_printf("Custom  : 100%% sure\n");
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    // Critique / edge cases
    printf("----- Edge Cases -----\n");
    ret1 = printf("Original: empty string = '%s'\n", "");
    ret2 = ft_printf("Custom  : empty string = '%s'\n", "");
    printf("Return values: printf=%d | ft_printf=%d\n", ret1, ret2);

    ret1 = printf("Original: zero int = %d\n", 0);
    ret2 = ft_printf("Custom  : zero int = %d\n", 0);
    printf("Return values: printf=%d | ft_printf=%d\n", ret1, ret2);

    ret1 = printf("Original: negative unsigned = %u\n", -1);
    ret2 = ft_printf("Custom  : negative unsigned = %u\n", -1);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);

    ret1 = printf(NULL);
    ret2 = ft_printf(NULL);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);
    
    ret1 = printf("Original: negative unsigned = %s\n", NULL);
    ret2 = ft_printf("Custom  : negative unsigned = %s\n", NULL);
    printf("Return values: printf=%d | ft_printf=%d\n\n", ret1, ret2);
    return 0;
}
