#include "./../includes/sta1.h"
#include "./../includes/op.h"

void sep(char *a)
{
    int i;

    i = 0;
    while (i++ < 20)
        ft_putstr(a);
    printf("\n");
}

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
    sort(a, b);
    print_stack(a);
    sep("+");
    if (check(a))
        printf("OK\n");
    else
        printf("KO\n");
    
    free_stack(a);
    free_stack(b);
    return 0;
}
