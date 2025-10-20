
#include "libft.h"
#include <stdlib.h>

t_list  *lst_clear(t_list **head, void (*del)(void *))
{
        t_list  *temp;

        if (!head || !del)
                return (NULL);
        while (*head)
        {
                temp = *head;
                *head = (*head)->next;
                if (temp->content)
                        del(temp->content);
                free(temp);
        }
        *head = NULL;
        return (*head);
}

t_list  *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
        t_list  *cur;
        t_list  *head;
        t_list  *new;

        if (!lst || !f || !del)
                return (NULL);
        cur = NULL;
        head = NULL;
        while (lst)
        {
                new = malloc(sizeof(t_list));
                if (!new)
                        return (lst_clear(&head, del));
                if (head == NULL)
                        head = new;
                else
                        cur->next = new;
                new->content = f(lst->content);
                if (!new->content)
                        return (lst_clear(&head, del));
                new->next = NULL;
                cur = new;
                lst = lst->next;
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
    

}
