/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   min_heap.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 16:41:29 by negane            #+#    #+#             */
/*   Updated: 2026/04/06 14:46:17 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "heap.h"

int is_min_sorted(int *list, int len)
{
	while (--len > 0)
	{
		if (list[len] < list[(len - 1) / 2])
			return (0);
	}
	return (1);
}

int	*sort_min_heap(int *list, int len)
{
	int	i;
	int	tmp;

	if (!list)
		return (NULL);
	if (is_min_sorted(list, len))
		return (list);
	i = len - 1;
	while (i > 0)
	{
		if (list[i] < list[(i - 1) / 2])
		{
			tmp = list[i];
			list[i] = list[(i - 1) / 2];
			list[(i - 1) / 2] = tmp;
		}
		i--;
	}
	return (sort_min_heap(list, len));
}

t_heap	*insert_min_heap(t_heap *heap, int data)
{
	int	i;
	int	*new_list;

	i = 0;
	if (!heap)
		return (create_heap(data));
	new_list = malloc(sizeof(int) * (heap->len + 1));
	if (!new_list)
		return (NULL);
	while (i < heap->len)
	{
		new_list[i] = heap->data[i];
		i++;
	}
	//	insert the new record...
	new_list[i] = data;
	while (i != 0 && new_list[i] < new_list[(i - 1) / 2])
	{
		swap(new_list + i, new_list + ((i - 1) / 2));
		i = (i - 1) / 2;
	}
	free(heap->data);
	heap->data = new_list;
	heap->len++;
	return (heap);
}

t_heap	*pop_min_heap(t_heap *heap)
{
	int index;
	int minimum;
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
		minimum = min(new[L(i)], new[R(i)]);
		if (new[i] > minimum)
		{
			index = indexof(new, len, minimum);
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
