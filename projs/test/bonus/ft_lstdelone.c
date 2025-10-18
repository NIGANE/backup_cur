#include <stdlib.h>
#include "libft.h"

void ft_lstdelone(t_list *lst, void (*del)(void*))
{
    if (!lst || !del)
        return ;
    del(lst->content);
    lst->content = NULL;
    free(lst);
}

#include <string.h>

void rm(void *content)
{
    free(content);
}
int main(void)
{
    #include <stdio.h>
    t_list *a = malloc(sizeof(t_list));
    printf("sizeof(node) = %zu\n", sizeof(a));
    char *s = strdup("negane");
    a->content = s;
    ft_lstdelone(a, &rm);
    if (a)
    {
        printf("node still alive\n");
        printf("size of (node) : %zu\n", sizeof(a));
    }
    else
        printf("node is dead\n");
}

