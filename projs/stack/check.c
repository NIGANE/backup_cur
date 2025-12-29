/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 22:09:24 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:19:04 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

int	check(t_stack *a)
{
	t_stack_node	*cur;

	if (!a)
		return (-1);
	cur = a->top;
	while (cur->next)
	{
		if (cur->data > cur->next->data)
			return (0);
		cur = cur->next;
	}
	return (1);
}
