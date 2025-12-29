/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   add_turk.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 22:09:51 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:24:52 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

t_stack_node	*get_min_target(t_stack *st)
{
	t_stack_node	*cur;
	t_stack_node	*min_node;

	cur = st->top;
	min_node = cur;
	while (cur)
	{
		if (cur->index < min_node->index)
			min_node = cur;
		cur = cur->next;
	}
	return (min_node);
}

void	set_current_pos(t_stack *a, t_stack *b)
{
	t_stack_node	*cur;
	int				i;

	i = 0;
	cur = a->top;
	while (cur)
	{
		cur->cp = i;
		i++;
		cur = cur->next;
	}
	i = 0;
	cur = b->top;
	while (cur)
	{
		cur->cp = i;
		i++;
		cur = cur->next;
	}
}

int	get_actual_cost(int cost_b, int cost_a)
{
	int	max;

	max = abs(cost_a);
	if (abs(cost_b) > abs(cost_a))
		max = abs(cost_b);
	if (cost_b > 0 && cost_a > 0)
		return (max);
	if (cost_b < 0 && cost_a < 0)
		return (max);
	return (abs(cost_b) + abs(cost_a));
}

void	update_target_node(t_stack *a, t_stack *b)
{
	t_stack_node	*cur_b;
	t_stack_node	*cur_a;
	t_stack_node	*target;
	int				chepest;

	cur_b = b->top;
	while (cur_b)
	{
		cur_a = a->top;
		chepest = 2147483647;
		while (cur_a)
		{
			if (cur_a->index > cur_b->index && cur_a->index < chepest)
			{
				chepest = cur_a->index;
				target = cur_a;
			}
			cur_a = cur_a->next;
		}
		if (chepest == 2147483647)
			target = get_min_target(a);
		cur_b->target_node = target;
		cur_b = cur_b->next;
	}
}

t_stack_node	*find_chepest(t_stack *a, t_stack *b)
{
	int				cost;
	int				target_cost;
	int				min_cost;
	t_stack_node	*target_to_move;
	t_stack_node	*cur;

	min_cost = 2147483647;
	cost = 0;
	target_cost = 0;
	cur = b->top;
	target_to_move = cur;
	set_current_pos(a, b);
	while (cur)
	{
		cost = cur->cp - ((cur->cp > b->size / 2) * b->size);
		target_cost = cur->target_node->cp - ((cur->target_node->cp > a->size
					/ 2) * a->size);
		if (get_actual_cost(cost, target_cost) <= min_cost)
		{
			min_cost = get_actual_cost(cost, target_cost);
			target_to_move = cur;
		}
		cur = cur->next;
	}
	return (target_to_move);
}
