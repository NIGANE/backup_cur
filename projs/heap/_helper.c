/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   _helper.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/05 16:53:03 by negane            #+#    #+#             */
/*   Updated: 2026/04/06 14:24:46 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "heap.h"

void swap(int *a, int *b)
{
    int tmp;

    tmp = *a;
    *a = *b;
    *b = tmp;
}

void free_heap(t_heap **heap)
{
    if (!heap)
        return;
    free((*heap)->data);
    free(*heap);
    *heap = NULL;
}

int indexof(int *list , int len, int e)
{
    int i;

    if (!list)
        return (-1);
    i = 0;
    while (i < len)
    {
        if (list[i] == e)
            return (i);
        i++;
    }
    return (-1);
}

void	print_arr(int *arr, int len)
{
	int	i;

	if (!arr)
		return;
	i = 0;
	while (i < len)
	{
		printf("(%d) : %d\n", i, arr[i]);
		i++;
	}
}

t_heap	*create_heap(int data)
{
	t_heap	*heap;

	heap = malloc(sizeof(t_heap));
	if (!heap)
		return (NULL);
	heap->len = 0;
	heap->data = malloc(sizeof(int));
	if (!heap->data)
		return (free(heap), NULL);
	return (heap->data[0] = data, heap->len++, heap);
}

void inspect_heap(t_heap *heap)
{
    printf("//+++++||+++++\\\\\n");
    printf("max heap: %s\n", is_max_sorted(heap->data, heap->len) ? "True" : "False");
    printf("min heap: %s\n", is_min_sorted(heap->data, heap->len) ? "True" : "False");
    printf("len: %d\n", heap->len);
    printf("data: \n");
    print_arr(heap->data, heap->len);
}
