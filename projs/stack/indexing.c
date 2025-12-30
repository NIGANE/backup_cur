/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   indexing.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 00:09:32 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/30 09:57:03 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"
#include "op.h"

t_stack	*indexing(t_stack *a)
{
	int				*arr;
	int				i;
	t_stack_node	*cur;

	if (!a)
		return (NULL);
	i = 0;
	arr = malloc(sizeof(int) * a->size);
	if (!arr)
		return (a);
	to_arr(a, arr);
	sort_arr(arr, a->size);
	while (i < a->size)
	{
		cur = find(arr[i], a);
		cur->index = i;
		i++;
	}
	free(arr);
	return (a);
}
