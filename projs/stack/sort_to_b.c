/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_to_b.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 22:32:04 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:32:08 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

void	sort_to_b(t_stack *a, t_stack *b, int chunk_num)
{
	int	chunk_size;
	int	i;
	int	low;

	low = 0;
	chunk_size = a->size / chunk_num;
	while (chunk_num-- > 0)
	{
		i = 0;
		while (i++ < chunk_size)
			chunking(a, b, low, chunk_size);
		low += chunk_size;
	}
	while (a->size > 3)
	{
		pb(b, a);
		if (b->size > 1 && b->top->index < (a->size + b->size) / 2)
			rb(b);
	}
}
