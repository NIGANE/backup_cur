/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_op2.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:54:09 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/30 00:09:21 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"

void	stack_rev(t_stack_node **top)
{
	t_stack_node	*prev;
	t_stack_node	*cur;
	t_stack_node	*next;

	if (!top || !*top)
		return ;
	prev = NULL;
	cur = *top;
	next = cur->next;
	while (cur != NULL)
	{
		cur->next = prev;
		prev = cur;
		cur = next;
		if (next != NULL)
			next = next->next;
	}
	*top = prev;
}

