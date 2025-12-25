#include <stdlib.h>
#include <stdio.h>


long ft_atoi(char *str)
{
    long sum;
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

int in_arr(int *arr, int a, int size)
{
    int i;
    
     i = 0;
     while (i < size)
     {
        if (arr[i++] == a)
            return (1);
     }
     return (0);
}

void print_arr(int *arr, int size)
{
    int i = 0;
    while ( i < size)
        printf("%d ", arr[i++]);
    printf("\n");
}

int main(int ac, char **av)
{
    if (ac == 1)
        return (0);
    int size = ft_atoi(av[1]);
    if (size <= 0)
        return (0);
    int *arr = malloc(sizeof(int) * size);
    int i = 0;
    while (i < size)
    {
        int rand_num = rand();
        while (in_arr(arr, rand_num, size))
            rand_num = rand();
        arr[i++] = rand_num;
        
    }
    print_arr(arr, size);
    free(arr);
}