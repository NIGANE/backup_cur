/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   opirations_checker.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:49:52 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/30 00:23:37 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"

void	sa(t_stack *a)
{
	if (a)
	{
		swap(&(a->top));
	}
}

void	sb(t_stack *b)
{
	if (b)
	{
		swap(&(b->top));
	}
}

void	ss(t_stack *a, t_stack *b)
{
	sa(a);
	sb(b);
}

void	pa(t_stack *a, t_stack *b)
{
	t_stack_node	*node;

	if (!a || !b)
		return ;
	node = pop(b);
	if (node)
	{
		node->next = a->top;
		a->top = node;
		a->size++;
	}
}

void	pb(t_stack *b, t_stack *a)
{
	t_stack_node	*node;

	if (!a || !b)
		return ;
	node = pop(a);
	if (node)
	{
		node->next = b->top;
		b->top = node;
		b->size++;
	}
}
