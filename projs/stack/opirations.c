/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   opirations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:49:52 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/25 21:50:01 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"

void sa(t_stack *a)
{
    if (a)
    {
        swap(&(a->top));
        printf("sa\n");
    }
    
}

void sb(t_stack *b)
{
    if (b)
    {
        swap(&(b->top));
        printf("sb\n");
    }
}

void ss(t_stack *a, t_stack *b)
{
    sa(a);
    sb(b);
    printf("ss\n");
}

void pa(t_stack *a, t_stack *b)
{
    t_stack_node *node;

    if (!a || !b)
        return ;
    node = pop(b);
    if (node)
    {
        node->next = a->top;
        a->top = node;
        a->size++;
    }
    printf("pa\n");
}

void pb(t_stack *b, t_stack *a)
{
    t_stack_node *node;

    if (!a || !b)
        return ;
    node = pop(a);
    if (node)
    {
        node->next = b->top;
        b->top = node;
        b->size++;
    }
    printf("pb\n");
}

void ra(t_stack *stack)
{
    rotate(stack);
    printf("ra\n");
}
