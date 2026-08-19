
#include <stdio.h>
#include "heap.h"

int main(void)
{
    t_heap *head = NULL;
    int* new_data = NULL;

    head = insert_max_heap(head, 5);
    if (!head)
        return (printf("Error\n"), 0);
    head = insert_min_heap(head, 6);
    head = insert_min_heap(head, 2);
    head = insert_min_heap(head, 5);
    head = insert_min_heap(head, 8);
    inspect_heap(head);
    // sort_min_heap(head->data, head->len);
    // inspect_heap(head);
    // sort_max_heap(head->data, head->len);
    // inspect_heap(head);
}