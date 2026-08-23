/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:31 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/23 17:13:17 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

int	is_number(char *s)
{
	if (!s)
		return (0);
	if (*s == '\0')
		return (0);
	while (*s)
	{
		if (*s < '0' || *s > '9')
			return (0);
		s++;
	}
	return (1);
}

void	usage_message(void)
{
	printf("Error: helpful usage error message.");
}

int	extract_args(int ac, char **av)
{
	int	i;

	i = 1;
	while (i < ac - 1)
	{
		if (!is_number(av[i]))
			return (printf("Error: '%s' is not a valid number\n", av[i]), 1);
		i++;
	}
	if ((strcmp(av[8], "edf") && strcmp(av[8], "fifo")) && ((strcmp(av[8],
					"EDF") && strcmp(av[8], "FIFO"))))
		return (printf("Error: '%s' is not a valid schedular\n", av[8]), 0);
	return (1);
}
