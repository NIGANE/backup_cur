#include "header.h"

void	swap(edf_node_t *a, edf_node_t *b)
{
	edf_node_t	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

int	check_priority(edf_node_t *a, edf_node_t *b)
{
	if (a->deadline != b->deadline)
		return (a->deadline < b->deadline);
	else if (a->id != b->id)
		return (a->id < b->id);
	return (a->data->id < b->data->id);
}

void	heapify(edf_heap_t *heap, int i)
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
