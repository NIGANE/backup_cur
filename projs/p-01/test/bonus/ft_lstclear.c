
#include "libft.h"
#include <stdlib.h>

void ft_lstclear(t_list **lst, void (*del)(void *))
{
    t_list  *cur;
    t_list  *temp;

    if (!lst || !del)
        return ;
    if (!*lst)
        return ;
    cur = *lst;
    while (cur->next)
    {
        temp = cur;
        cur = cur->next;
        del(temp->content);
        temp->next = NULL;
        free(temp);
    }
    *lst = NULL;
}

// Test cases for ft_lstclear
#include <stdio.h>
#include <string.h>

void del(void *content)
{
    free(content);
}
int main()
{
    // Create a simple linked list for testing
    t_list *head = NULL;
    ft_lstclear(&head, NULL);
    
}