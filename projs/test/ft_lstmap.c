
#include "libft.h"
#include <stdlib.h>

void    lst_clear(t_list **head, void (*del)(void *))
{
    t_list  *temp;
    if (!head || !del)
        return ;
    while (*head)
    {
        temp = *head;
        *head = (*head)->next;
        if (temp->content)
            del(temp->content);
        free(temp);
    }
    *head = NULL;
}

t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
    t_list  *cur;
    t_list  *head;

    if (!lst || !f || !del)
        return (NULL);
    cur = malloc(sizeof(t_list));
    if (!cur)
        return (NULL);
    cur->content = f(lst->content);
    if (!cur->content)
    {
        free(cur);
        return (NULL);
    }
    cur->next = NULL;
    head = cur;
    lst = lst->next;
    while (lst)
    {
        cur->next = malloc(sizeof(t_list));
        if (!cur->next)
        {
            lst_clear(&head, del);
            return (NULL);
        }
        cur->next->content = f(lst->content);
        if (!cur->next->content)
        {
            lst_clear(&head, del);
            return (NULL);
        }
        cur->next->next = NULL;
        lst = lst->next;
        cur = cur->next;
    }
    return (head);
}
#include <stdio.h>
#include <string.h>
void    *ft_memset(void *data, int c, size_t size)
{
        unsigned char   *buf;

        buf = (unsigned char *) data;
        while (size-- > 0)
                *buf++ = (unsigned int) c;
        return (data);
}

void    *change(void *data)
{
    return (ft_memset(strdup((char *) data), 'x', 3));
}

void    del(void * data)
{
    free(data);
}

int    main(void)
{
    t_list  *head = malloc(sizeof(t_list));
    head->content = strdup("achraf");
    head->next = malloc(sizeof(t_list));
    head->next->content = strdup("merkht");
    head->next->next = malloc(sizeof(t_list));
    head->next->next->content = strdup("negane");
    
    t_list *cur = head;
    printf("Before: ----\n");
    while (cur)
    {
        printf("- %s\n",(char *) cur->content);
        cur = cur->next;
    }
    printf("After: ----\n");
    t_list *head2 = ft_lstmap(head, &change, &del);

    cur = head2;
    while (cur)
    {
        printf("- %s\n",(char *) cur->content);
        cur = cur->next;
    }
    printf("test: --------\n");
    head->content = memset(head->content, 'g', 4);

    printf("changed head\n");
    cur = head;
    while (cur)
    {
        printf("- %s\n",(char *) cur->content);
        cur = cur->next;
    }

    printf("not changed head\n");
    cur = head2;
    while (cur)
    {
        printf("- %s\n",(char *) cur->content);
        cur = cur->next;
    }

}
