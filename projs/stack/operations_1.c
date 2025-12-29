/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_1.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:49:18 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:36:50 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

void	rb(t_stack *stack)
{
	rotate(stack);
	ft_putstr("rb\n");
}

void	rr(t_stack *a, t_stack *b)
{
	rotate(a);
	rotate(b);
	ft_putstr("rr\n");
}

void	rra(t_stack *stack)
{
	rev_rotate(stack);
	ft_putstr("rra\n");
}

void	rrb(t_stack *stack)
{
	rev_rotate(stack);
	ft_putstr("rrb\n");
}

void	rrr(t_stack *a, t_stack *b)
{
	rev_rotate(a);
	rev_rotate(b);
	ft_putstr("rrr\n");
}
