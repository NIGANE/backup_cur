/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:52:43 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/25 21:52:52 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"

void rotate(t_stack *stack)
{
    t_stack_node *tmp;
    t_stack_node *cur;

    if (!stack)
        return;
    tmp = pop(stack);
    if (!tmp)
        return ;
    cur = stack->top;
    if (!cur)
        return (push(stack, tmp->data), free(tmp));
    while (cur->next)
        cur = cur->next;
    cur->next = tmp;
    stack->size++;
}


