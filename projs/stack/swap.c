/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:54:42 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/25 21:54:51 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"

void swap(t_stack_node **top)
{
    t_stack_node *next;
    t_stack_node *cur;

    if (!*top || !top)
        return;
    cur = *top;
    next = cur->next;
    cur->next = next->next;
    next->next = cur;
    *top = next;
}


