/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   move_chepest.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 22:23:37 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:23:37 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

void	rotate_both(t_stack *a, t_stack *b, int *pos, int *target_pos)
{
	while (*pos > 0 && *target_pos > 0)
	{
		rr(a, b);
		(*pos)--;
		(*target_pos)--;
	}
}

void	rev_rotate_both(t_stack *a, t_stack *b, int *pos, int *target_pos)
{
	while (*pos < 0 && *target_pos < 0)
	{
		rrr(a, b);
		(*pos)++;
		(*target_pos)++;
	}
}

void	move_chepest(t_stack *a, t_stack *b, t_stack_node *target)
{
	int	pos;
	int	target_pos;

	pos = target->cp;
	if (pos > b->size / 2)
		pos = pos - b->size;
	target_pos = target->target_node->cp;
	if (target_pos > a->size / 2)
		target_pos = target_pos - a->size;
	if (pos > 0 && target_pos > 0)
		rotate_both(a, b, &pos, &target_pos);
	else if (pos < 0 && target_pos < 0)
		rev_rotate_both(a, b, &pos, &target_pos);
	movetop_b(b, pos);
	while (pos < 0)
	{
		rrb(b);
		pos++;
	}
	movetop_a(a, target_pos);
	while (target_pos < 0)
	{
		rra(a);
		target_pos++;
	}
}
