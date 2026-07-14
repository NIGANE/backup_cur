// #include "../header.h"
#include <stdio.h>
int odd(int a)
{
    return (a % 2);
}

int even(int a)
{
    return !(a % 2);
}

int is_positive_number(char *a)
{
    while (*a)
    {
        if (*a < 48 || *a > 57)
        {
            printf("this isnt valid number: %c\n", *a);
            return (0);
        }
        a++;
    }
    
    return (1);
}