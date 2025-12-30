/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   array_operations.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:45:56 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:40:28 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

void	to_arr(t_stack *a, int *arr)
{
	t_stack_node	*cur;

	if (!a)
		return ;
	cur = a->top;
	while (cur)
	{
		*arr++ = cur->data;
		cur = cur->next;
	}
}

void	swap_arr(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

void	sort_arr(int *arr, int size)
{
	int	i;
	int	j;

	i = 0;
	while (i < size - 1)
	{
		j = 0;
		while (j < size - 1 - i)
		{
			if (arr[j] > arr[j + 1])
				swap_arr(arr + j, arr + j + 1);
			j++;
		}
		i++;
	}
}

void	free_split_arr(char **arr)
{
	char	**bf;

	bf = arr;
	while (*bf != NULL)
		free(*bf++);
	free(arr);
}
