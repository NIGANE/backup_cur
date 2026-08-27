/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:01 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/27 12:12:37 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

t_edf_node	*edf_node_create(t_coder *coder)
{
	t_edf_node	*node;

	if (!coder)
		return (NULL);
	node = malloc(sizeof(t_edf_node));
	if (!node)
		return (NULL);
	node->data = coder;
	node->id = ++coder->env->req;
	node->deadline = coder->env->start_time + coder->env->t_burn_out;
	if (coder->last_compile_time != 0)
		node->deadline = coder->last_compile_time + coder->env->t_burn_out;
	return (node);
}

t_edf_heap	*edf_heap_init(int capacity)
{
	t_edf_heap	*heap;

	if (capacity <= 0)
		return (NULL);
	heap = malloc(sizeof(t_edf_heap));
	if (!heap)
		return (NULL);
	heap->array = malloc(sizeof(t_edf_node *) * capacity);
	if (!heap->array)
		return (free(heap), NULL);
	heap->size = 0;
	heap->capacity = capacity;
	return (heap);
}

t_edf_heap	*edf_heap_push(t_edf_heap *heap, t_coder *coder)
{
	int	cur;
	int	parent;

	if (!coder || !heap)
		return (NULL);
	if (heap->size + 1 > heap->capacity)
		return (heap);
	heap->array[heap->size] = edf_node_create(coder);
	if (!(heap->array[heap->size]))
		return (NULL);
	heap->size++;
	cur = heap->size - 1;
	while (cur > 0)
	{
		parent = (cur - 1) / 2;
		if (check_priority(heap->array[cur], heap->array[parent]))
		{
			swap(heap->array[cur], heap->array[parent]);
			cur = parent;
		}
		else
			break ;
	}
	return (heap);
}

t_edf_node	*edf_heap_pop(t_edf_heap *heap)
{
	t_edf_node	*root;

	if (!heap || heap->size == 0)
		return (NULL);
	root = heap->array[0];
	heap->array[0] = heap->array[heap->size - 1];
	heap->size--;
	if (heap->size)
		heapify(heap, 0);
	return (root);
}
