/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:48:43 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/26 15:49:29 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./op.h"
#include "./sta1.h"

int	main(int ar, char **av)
{
	t_stack	*a;
	t_stack	*b;

	if (ar <= 1)
		return (1);
	a = stack_init();
	b = stack_init();
	if (!a || !b)
		return (1);
	a = extract_stack(a, ar, av);
	if (!a)
	{
		free_stack(b);
		ft_putstr("Error\n");
		return (1);
	}
	sort(a, b);
	free_stack(a);
	free_stack(b);
	return (0);
}
