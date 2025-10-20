
#include "libft.h"
#include <stdlib.h>

int ft_lstsize(t_list *lst)
{
    int count;

    if (!lst)
    return (0);
    count = 0;
    while (lst)
    {
        lst = lst->next;
        count++; 
    }
    return (count);
}

#include <stdio.h>
int main(void)
{
    t_list *node1;
    t_list *node2;
    t_list *node3;
    int size;

    node1 = (t_list *)malloc(sizeof(t_list));
    node2 = (t_list *)malloc(sizeof(t_list));
    node3 = (t_list *)malloc(sizeof(t_list));

    node1->next = node2;
    node2->next = node3;
    node3->next = NULL;

    size = ft_lstsize(node1);
    if (size == 3)
    {
        printf("Test passed: List size is %d\n", size);
        free(node1);
        free(node2);
        free(node3);
        return (0);
    }
    printf("Test failed: Expected size 3 but got %d\n", size);
}