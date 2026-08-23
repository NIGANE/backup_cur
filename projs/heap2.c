/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap2.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:07 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/23 15:18:40 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

void	swap(t_edf_node *a, t_edf_node *b)
{
	t_edf_node	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

int	check_priority(t_edf_node *a, t_edf_node *b)
{
	if (a->deadline != b->deadline)
		return (a->deadline < b->deadline);
	else if (a->id != b->id)
		return (a->id < b->id);
	return (a->data->id < b->data->id);
}

void	heapify(t_edf_heap *heap, int i)
{
	int	largest;
	int	left;
	int	right;

	largest = i;
	left = 2 * i + 1;
	right = 2 * i + 2;
	if (left < heap->size && check_priority(heap->array[left],
			heap->array[largest]))
		largest = left;
	if (right < heap->size && check_priority(heap->array[right],
			heap->array[largest]))
		largest = right;
	if (largest != i)
	{
		swap(heap->array[largest], heap->array[i]);
		heapify(heap, largest);
	}
}
