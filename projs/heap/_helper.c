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