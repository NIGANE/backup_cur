/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker_main.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 10:01:12 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/30 10:19:29 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"
#include "get_line.h"

int	ft_strcmp(const char *s1, const char *s2)
{
	while (*s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

void	start_env(t_stack **a, t_stack **b, int ac, char **av)
{
	*a = stack_init();
	*b = stack_init();
	if (!*a || !*b)
	{
		free_stack(*a);
		free_stack(*b);
		return ;
	}
	*a = extract_stack(*a, ac, av);
	if (!*a)
	{
		free_stack(*b);
		write(2, "Error\n", 6);
		return ;
	}
}

void	sort_call(t_stack *a, t_stack *b, char *fn)
{
	if (!fn)
		return ;
	if (ft_strcmp(fn, "ra\n") == 0)
		ra(a);
	else if (ft_strcmp(fn, "rb\n") == 0)
		rb(b);
	else if (ft_strcmp(fn, "rr\n") == 0)
		rr(a, b);
	else if (ft_strcmp(fn, "rra\n") == 0)
		rra(a);
	else if (ft_strcmp(fn, "rrb\n") == 0)
		rrb(b);
	else if (ft_strcmp(fn, "rrr\n") == 0)
		rrr(a, b);
	else if (ft_strcmp(fn, "sa\n") == 0)
		sa(a);
	else if (ft_strcmp(fn, "sb\n") == 0)
		sb(b);
	else if (ft_strcmp(fn, "ss\n") == 0)
		ss(a, b);
	else if (ft_strcmp(fn, "pa\n") == 0)
		pa(a, b);
	else if (ft_strcmp(fn, "pb\n") == 0)
		pb(b, a);
}

int	main(int ac, char **av)
{
	t_stack	*a;
	t_stack	*b;
	char	*line;

	if (ac <= 1)
		return (1);
	start_env(&a, &b, ac, av);
	if (!a || !b)
		return (1);
	line = get_next_line(0);
	while (line)
	{
		sort_call(a, b, line);
		free(line);
		line = get_next_line(0);
	}
	if (check(a))
		ft_putstr("OK\n");
	else
		ft_putstr("KO\n");
	free_stack(a);
	free_stack(b);
}
