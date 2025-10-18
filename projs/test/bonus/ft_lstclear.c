
#include "libft.h"
#include <stdlib.h>

void ft_lstclear(t_list **lst, void (*del)(void *))
{
    t_list  *cur;
    t_list  *temp;

    if (!lst || !del)
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
    t_list *head = malloc(sizeof(t_list));
    head->content = strdup("Node 1");
    head->next = malloc(sizeof(t_list));
    head->next->content = strdup("Node 2");
    head->next->next = NULL;

    t_list *cur = head;
    while (cur)
    {
        printf("Node content: %s\n", (char *)cur->content);
        cur = cur->next;
    }

    // Clear the list
    ft_lstclear(&head, del);

    // Check if the list is cleared
    if (head == NULL)
        printf("List cleared successfully.\n");
    else
        printf("List not cleared.\n");

    return 0;
}