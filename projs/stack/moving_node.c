/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   moving_node.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:48:57 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:21:15 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

void	movetop_a(t_stack *st, int index)
{
	while (index-- > 0)
		ra(st);
}

void	movebottom_a(t_stack *st, int index)
{
	while (index++ < st->size)
		rra(st);
}

void	movetop_b(t_stack *st, int index)
{
	while (index-- > 0)
		rb(st);
}

void	movebottom_b(t_stack *st, int index)
{
	while (index++ < st->size)
		rrb(st);
}

void	move_in_a(t_stack *a, t_stack *b, int first_match, int last_match)
{
	if (first_match <= (a->size - last_match))
		movetop_a(a, first_match);
	else
		movebottom_a(a, last_match);
	pb(b, a);
}
