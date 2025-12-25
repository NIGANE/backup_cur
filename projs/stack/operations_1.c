/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_1.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:49:18 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/25 21:49:28 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

void rb(t_stack *stack)
{
    rotate(stack);
    printf("rb\n");
}
void rr(t_stack *a, t_stack *b)
{
    rotate(a);
    rotate(b);
    printf("rr\n");
}

void rra(t_stack *stack)
{
    rev_rotate(stack);
    printf("rra\n");
}

void rrb(t_stack *stack)
{
    rev_rotate(stack);
    printf("rrb\n");
}

void rrr(t_stack *a, t_stack *b)
{
    rev_rotate(a);
    rev_rotate(b);
    printf("rrr\n");
}


