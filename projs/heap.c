#include "header.h"

edf_node_t	*edf_node_create(coder_t *coder)
{
	edf_node_t	*node;

	if (!coder)
		return (NULL);
	node = malloc(sizeof(edf_node_t));
	if (!node)
		return (NULL);
	node->data = coder;
	node->id = ++coder->env->req;
	node->deadline = coder->env->start_time + coder->env->t_burn_out;
	if (coder->last_compile_time != 0)
		node->deadline = coder->last_compile_time + coder->env->t_burn_out;
	return (node);
}

edf_heap_t	*edf_heap_init(int capacity)
{
	edf_heap_t	*heap;

	if (capacity <= 0)
		return (NULL);
	heap = malloc(sizeof(edf_heap_t));
	if (!heap)
		return (NULL);
	heap->array = malloc(sizeof(edf_node_t *) * capacity);
	if (!heap->array)
	{
		free(heap);
		return (NULL);
	}
	heap->size = 0;
	heap->capacity = capacity;
	return (heap);
}

edf_heap_t	*edf_heap_push(edf_heap_t *heap, coder_t *coder)
{
	int	cur;
	int	parent;

	if (!coder || !heap)
		return (NULL);
	if (heap->size + 1 > heap->capacity)
	{
		return (heap);
	}
	heap->array[heap->size] = edf_node_create(coder);
	if (!(heap->array[heap->size]))
	{
		return (NULL);
	}
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

edf_node_t	*edf_heap_pop(edf_heap_t *heap)
{
	edf_node_t	*root;

	if (!heap || heap->size == 0)
		return (NULL);
	root = heap->array[0];
	heap->array[0] = heap->array[heap->size - 1];
	heap->size--;
	if (heap->size)
		heapify(heap, 0);
	return (root);
}
