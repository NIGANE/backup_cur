

#include "libft.h"
#include <stdlib.h>

t_list  *ft_lstlast(t_list *lst)
{
    if (!lst)
        return (NULL);
    while (lst->next)
        lst = lst->next;
    return (lst);
}
#include <stdio.h>
int main(void)
{
    char *s1 = "hello world";
    t_list  *node1 = malloc(sizeof(t_list));
    node1->content = s1;

    char *s2 = "me";
    t_list  *node2 = malloc(sizeof(t_list));
    node2->content = s2;
    
    char *s3 = "negane";
    t_list  *node3 = malloc(sizeof(t_list));
    node3->content = s3;

    node1->next = node2;
    node2->next = node3;
    t_list  *last = ft_lstlast(node1);
    if (last)
        printf("last node: %s\n",(char *) last->content);
    
}