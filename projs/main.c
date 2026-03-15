/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/15 07:20:15 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./heap/heap.h"
#define sep "//////////\n"


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

int	main(void)
{
	t_heap *heap = NULL;

	heap = insert_max_heap(heap, 10);
	heap = insert_max_heap(heap, 20);
	heap = insert_max_heap(heap, 15);
	print_arr(heap->data, heap->len);
	printf(sep);
	heap = insert_max_heap(heap, 30);
	print_arr(heap->data, heap->len);		
	free_heap(&heap);
}