/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_6_max.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:53:30 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:28:55 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

int	get_pos(t_stack *st, int index)
{
	t_stack_node	*cur;
	int				i;

	if (!st)
		return (-1);
	cur = st->top;
	i = 0;
	while (cur)
	{
		if (cur->index == index)
			return (i);
		i++;
		cur = cur->next;
	}
	return (-1);
}

void	chunking(t_stack *a, t_stack *b, int low, int size)
{
	t_stack_node	*cur;
	int				i;
	int				first_match;
	int				last_match;

	first_match = -1;
	last_match = -1;
	cur = a->top;
	i = 0;
	while (cur)
	{
		if (cur->index >= low && cur->index <= low + size - 1)
		{
			if (first_match == -1)
				first_match = i;
			last_match = i;
		}
		cur = cur->next;
		i++;
	}
	if (first_match == -1)
		return ;
	move_in_a(a, b, first_match, last_match);
	if (b->size > 1 && b->top->index < (low + (low + size - 1)) / 2)
		rb(b);
}

void	push_3(t_stack *a, t_stack *b)
{
	while (a->size < 5)
		pa(a, b);
}

void	finish_it(t_stack *a)
{
	int	pos;

	pos = get_pos(a, 0);
	if (pos > a->size / 2)
		movebottom_a(a, pos);
	else
		movetop_a(a, pos);
}

void	sort_6_100(t_stack *a, t_stack *b)
{
	int				chunk_num;
	t_stack_node	*chepest;

	if (a->size <= 100)
		chunk_num = 2;
	else
		chunk_num = 9;
	sort_to_b(a, b, chunk_num);
	sort(a, b);
	while (b->size > 0)
	{
		if (a->size == 0)
			pa(a, b);
		update_target_node(a, b);
		chepest = find_chepest(a, b);
		move_chepest(a, b, chepest);
		pa(a, b);
	}
	finish_it(a);
}
