
#include <stdlib.h>
#include <stdio.h>
#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
    if (!lst || !new)
    {
        return ;
    }
	new->next = *lst;
	*lst = new;
}

t_list *ft_lstnew(void *content)
{
    t_list*     new_node;

    new_node = malloc(sizeof(t_list));
    if (!new_node)
        return (NULL);
    new_node->content = content;
    new_node->next = NULL;
    return (new_node);
}
int main(void)
{
    t_list  *node;
    t_list  *new;
    t_list *l;

    char *s1 = "hello";
    char *s2 = "world";
    node = ft_lstnew(s1);
    new = ft_lstnew(s2);
    if (new && node)
    {
        ft_lstadd_front(NULL, new);
        l = new;
        while (l)
        {
            printf("cont: %s\n", (char *) l->content);
            l = l->next;
        }
        printf("END\n");
    }
}
