/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max_heap.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/14 19:52:36 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/14 19:53:33 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "heap.h"

int	is_max_sorted(int *list, int len)
{
	while (--len > 0)
	{
		if (list[len] > list[(len - 1) / 2])
			return (0);
	}
	return (1);
}

int	*sort_max_heap(int *list, int len)
{
	int	i;
	int	tmp;

	if (!list)
		return (NULL);
	if (is_max_sorted(list, len))
		return (list);
	i = len - 1;
	while (i > 0)
	{
		if (list[i] > list[(i - 1) / 2])
		{
			tmp = list[i];
			list[i] = list[(i - 1) / 2];
			list[(i - 1) / 2] = tmp;
		}
		i--;
	}
	return (sort_max_heap(list, len));
}

t_heap	*create_max_heap(int data)
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

t_heap	*insert_max_heap(t_heap *heap, int data)
{
	int	i;
	int	*new_list;

	i = 0;
	if (!heap)
		return (create_max_heap(data));
	new_list = malloc(sizeof(int) * (heap->len + 1));
	if (!new_list)
		return (NULL);
	while (i < heap->len)
	{
		new_list[i] = heap->data[i];
		i++;
	}
	new_list[i] = data;
	while (i != 0 && new_list[i] > new_list[(i - 1) / 2])
	{
		swap(new_list + i, new_list + ((i - 1) / 2));
		i = (i - 1) / 2;
	}
	free(heap->data);
	heap->data = new_list;
	heap->len++;
	return (heap);
}

t_heap	*pop_max_heap(t_heap *heap)
{
	int index;
	int biggest;
	int i;
	int *new;
	int len;

	if (!heap)
		return (NULL);
	if (heap->len == 1)
		return (free_heap(&heap), NULL);
	len = heap->len - 1;
	i = 0;
	swap(heap->data, heap->data + heap->len - 1);
	new = malloc(sizeof(int) * (len));
	while (i++ < heap->len)
		new[i - 1] = heap->data[i - 1];
	i = 0;
	while (1)
	{
		if (L(i) >= len || R(i) >= len)
			break ;
		printf("main cell: %d\n", new[i]);
		printf("left cell: %d\n", new[L(i)]);
		printf("right cell: %d\n", new[R(i)]);
		biggest = max(new[L(i)], new[R(i)]);
		if (new[i] < biggest)
		{
			index = indexof(new, len, biggest);
			swap(new + i, new + index);
		}
		else
			break ;
		i = index;
	}
	free(heap->data);
	heap->data = new;
	heap->len--;
	return (heap);
}