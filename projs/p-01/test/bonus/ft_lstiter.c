#include "libft.h"
#include <stdlib.h>

void ft_lstiter(t_list *lst, void (*f)(void *))
{
    if (!lst)
        return ;
    while (lst)
    {
        f(lst->content);
        lst = lst->next;
    }
    
}
#include <stdio.h>
#include <string.h>
void    print_content(void *s)
{
    printf("- %s\n", (char *) s);
}

int main(void)
{
    t_list  *node = malloc(sizeof(t_list));
    node->content = strdup("achraf");
    node->next = malloc(sizeof(t_list));
    node->next->content = strdup("negane");
    node->next->next = malloc(sizeof(t_list));
    node->next->next->content = strdup("nohriner");

    ft_lstiter(node, &print_content);
}