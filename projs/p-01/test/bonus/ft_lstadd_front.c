
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

// #include <string.h>
// int main(void)
// {
//     t_list  *node1;
//     t_list  *node2;
//     t_list *head = NULL;

//     node1 = ft_lstnew(strdup("node 1"));
//     ft_lstadd_front(&head, NULL);
//     // printf("node: %s\n", (char *) head->content);

// }
