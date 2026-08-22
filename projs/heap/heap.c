#include "../header.h"

edf_node_t *edf_node_create(void *coder)
{
	edf_node_t *node;

	if (!coder)
		return (NULL);
	node = malloc(sizeof(edf_node_t));
	if (!node)
		return (NULL);
	node->data = coder;
	// if (((coder_t *) coder)->last_compile_time == 0)
	// {
	// 	printf("passed\n");
	// 	node->elapsed_time = timestamp(((coder_t *) coder)->env->start_time);
	// }
	// else
    node->elapsed_time = timestamp(((coder_t *) coder)->last_compile_time);
	return (node);
}

edf_heap_t *edf_heap_init(int capacity)
{
	edf_heap_t *heap;

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

edf_heap_t *edf_heap_push(edf_heap_t *heap, void *coder)
{
	int			i;
	int			parent;
	edf_node_t	*tmp;

	if (!coder || !heap)
		return (NULL);
    if (heap->size + 1 > heap->capacity)
        return (heap);
	i = heap->size;
	heap->array[i] = edf_node_create(coder);
	// inspect_heap(heap);
    if (!(heap->array[i]))
        return (NULL);
	heap->size++;
	while (i > 0)
	{
		parent = (i - 1) / 2;
		if (heap->array[i]->elapsed_time <= heap->array[parent]->elapsed_time)
			break;

		tmp = heap->array[i];
		heap->array[i] = heap->array[parent];
		heap->array[parent] = tmp;

		i = parent;
	}
    return (heap);
}

edf_node_t *edf_heap_pop(edf_heap_t *heap)
{
	edf_node_t	*root;
	edf_node_t	*tmp;
	int			i;
	int			largest;
	int			left;
	int			right;

	if (!heap || heap->size == 0)
		return (NULL);
	root = heap->array[0];
	heap->array[0] = heap->array[heap->size - 1];
	heap->size--;
	i = 0;
	while (1)
	{
		largest = i;
		left = 2 * i + 1;
		right = 2 * i + 2;
		if (left < heap->size && heap->array[left]->elapsed_time > heap->array[largest]->elapsed_time)
			largest = left;
		if (right < heap->size && heap->array[right]->elapsed_time > heap->array[largest]->elapsed_time)
			largest = right;

		if (largest == i)
			break;
		tmp = heap->array[i];
		heap->array[i] = heap->array[largest];
		heap->array[largest] = tmp;

		i = largest;
	}
	printf("poing: %d\n", ((coder_t *) root->data)->id);
	return (root);
}

void inspect_heap(edf_heap_t *heap)
{
    int i;

    if (!heap)
	{
		printf("heap not exists\n");
        return;
	}
    i = 0;
	printf("inspecting heap\n");
	if (heap->size == 0)
		printf("=> heap empty\n");
    while (i < heap->size)
    {
        printf("coder: %d, elapsed: %lld\n", ((coder_t *) heap->array[i]->data)->id, heap->array[i]->elapsed_time);
        i++;
    }
}
