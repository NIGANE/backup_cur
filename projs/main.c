/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/14 18:20:07 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./heap/heap.h"

void	print_arr(int *arr, int len)
{
	int	i;

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
	int arr[] = {10, 20, 15, 30};
	size_t len = sizeof(arr) / sizeof(arr[0]);
	size_t i;

	i = 0;
	while (i < len)
		heap = insert_max_heap(heap, arr[i++]);
	print_arr(heap->data, heap->len);
	pop_max_heap(heap);
	printf("/////////\n");
	print_arr(heap->data, heap->len);
	free_heap(&heap);
}