/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_1_5.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:53:21 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/25 21:53:26 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./sta1.h"
#include "./op.h"

void sort_3(t_stack *a)
{
    int index;

    if (!a)
        return ;
    index = find_largest(a);
    if (index == 0)
        ra(a);
    else if (index == 1)
        rra(a);
    if (a->top->data > a->top->next->data)
        sa(a);
}

void sort_4(t_stack *a, t_stack *b)
{
    int index;

    index = find_smallest(a);
    if (index == 1)
        ra(a);
    else if (index == 2)
    {
        rra(a);
        rra(a);
    }
    else if (index == 3)
        rra(a);
    pb(b, a);
    sort_3(a);
    pa(a, b);
}

void sort_5(t_stack *a, t_stack *b)
{
    int index;

    index = find_smallest(a);
    if (index == 1)
        ra(a);
    else if (index == 2)
    {
        ra(a);
        ra(a);
    }
    else if (index == 3)
    {
        rra(a);
        rra(a);
    }
    else if (index == 4)
        rra(a);
    pb(b, a);
    sort_4(a, b);
    pa(a, b);
}


