#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "./../includes/sta1.h"


int main(int ar, char **av)
{

    if( ar <= 1){
        printf("nothing given\n");
        return 1;
    }

    t_stack *a = stack_init();
    t_stack *b = stack_init();
    if (!a || !b)
        return 1;
    a = extract_stack(a, ar, av);
    if (!a)
    {
        free_stack(b);
        ft_putstr("Error\n");
        return 1;
    }
    print_stack(a);
    free_stack(a);
    free_stack(b);
    return 0;
}
