
#include "libft.h"
#include <stddef.h>
void ft_lstadd_back(t_list **lst, t_list *new)
{
    t_list  *cur;

    if (!new || !lst)
        return ;
    if (!*lst)
    {
        *lst = new;
        return ;
    }    
    cur = *lst;
    while (cur->next)
        cur = cur->next;
    cur->next = new;
}
// #include <stdlib.h>
// #include <stdio.h>
// #include <string.h>
// int main(void)
// {
//     t_list *head = NULL;
//     t_list *node1 = ft_lstnew(strdup("node1"));
//     t_list *node3 = ft_lstnew(strdup("node3"));
//     ft_lstadd_back(&head, node3);
//     ft_lstadd_back(&head, node3);
//     printf("node 1 : %s\n", (char *) head->content);
//     printf("node 3 : %s\n", (char *) head->next->content);
    // printf("%s\n", (char *) head->content);

    // ft_lstadd_back(&head, node2);
    // t_list *cur = head;
    // while (cur)
    // {
    //     printf("- %s\n",(char *) cur->content);
    //     cur = cur->next;
    // }
    // free(head);
    // free(node2);

// }