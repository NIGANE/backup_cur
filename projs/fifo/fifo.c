
#include "fifo.h"

node_t *ft_create(void *data)
{
    node_t *node;

    node = malloc(sizeof(node_t));
    if (!node)
        return (NULL);
    node->data = data;
    node->id = 0;
    return (node);
}

node_t *ft_insert(void *data, node_t *fifo)
{
    node_t *node;
    node_t *cur;
    int i;
    if (!data)
        return (fifo);

    if (!fifo)
        return (ft_create(data));
    node = ft_create(data);
    if (!node)
        return (ft_free(fifo), NULL);
    
    cur = fifo;
    while (cur->next)
        cur = cur->next;
    cur->next = node;
    return (fifo);
}
node_t *ft_pop(node_t **fifo)
{
    node_t *re;

    if (!fifo || !*fifo)
        return (NULL);
    re = *fifo;
    *fifo = (*fifo)->next;
    return (re);
}

void ft_free(node_t *fifo)
{
    node_t *tmp;
    if (!fifo)
        return;
    while (fifo)
    {
        tmp = fifo;
        fifo = fifo->next;
        free(tmp);
    }
}
int ft_len(node_t *head)
{
    int i;

    if (!head)
        return (0);
    i = 0;
    while (head)
    {
        i++;
        head = head->next;
    }
    return (i);
}


