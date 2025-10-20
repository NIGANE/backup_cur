
#include "libft.h"

void ft_lstadd_back(t_list **lst, t_list *new)
{
    t_list  *cur;

    if (!lst || !new)
        return ;
    cur = *lst;
    while (cur->next)
        cur = cur->next;
    cur->next = new;
}
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
    char *s1 = "hello";
    t_list  *node1 = malloc(sizeof(t_list));
    node1->content = s1;void ft_lstadd_back(t_list **lst, t_list *new)

    char *s2 = "world";
    t_list *node2 = malloc(sizeof(t_list));
    node2->content = s2;

    ft_lstadd_back(&node1, node2);
    t_list *cur = node1;
    while (cur)
    {
        printf("content: %s\n",(char *) cur->content);
        cur = cur->next;
    }
    free(node1);
    free(node2);

}