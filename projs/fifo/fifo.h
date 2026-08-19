#include <stdlib.h>
#include <stdio.h>

typedef struct node_s
{
    int id;
    void *data;
    struct node_s *next;
} node_t;

void ft_free(node_t *fifo);
node_t *ft_create(void *data);
node_t *ft_insert(void *data, node_t *fifo);
node_t *ft_pop(node_t **fifo);
int ft_len(node_t *head);
void inspect_fifo(node_t *head);