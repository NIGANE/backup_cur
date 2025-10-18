
#include "libft.h"
#include <stdlib.h>

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
#include <stdio.h>
int main(void)
{
    t_list  *node;
    char *str = NULL;
    node = ft_lstnew(str);
    if (node)
    {
        printf("data of the node: %s\n", (char *) node->content);
        free(node);
    }
    else
        printf("allocations Faild\n");
}