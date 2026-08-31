/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:01:31 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/31 18:25:18 by amerkht          ###   ########.fr       */
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

void	usage_message(const char *prog_name)
{
	fprintf(stderr, "\033[1mUsage:\033[0m\n");
	fprintf(stderr,
		"%s <nb_coders> <t_burn_out> <t_compile> <t_code> <t_refactor>",
		prog_name);
	fprintf(stderr, "<nb_compiles> <donor_cooldown> <scheduler>\n\n");
	fprintf(stderr, "\033[1mArguments:\033[0m\n");
	fprintf(stderr, "  nb_coders       Number of coders (N >= 1)\n");
	fprintf(stderr, "  t_burn_out      Time in ms before a coder burns out\n");
	fprintf(stderr, "  t_compile       Time in ms required to compile\n");
	fprintf(stderr, "  t_code          Time in ms spent coding\n");
	fprintf(stderr, "  t_refactor      Time in ms spent refactoring\n");
	fprintf(stderr, "  nb_compiles     Compiles required per coder\n");
	fprintf(stderr, "  donor_cooldown  Cooldown in ms for donor dongle\n");
	fprintf(stderr,
		"  scheduler       Scheduling algorithm ('edf' or 'fifo')\n\n");
	fprintf(stderr, "\033[1mExample:\033[0m\n");
	fprintf(stderr, "  %s 5 3000 200 200 200 10 900 edf\n", prog_name);
}

int	extract_args(int ac, char **av)
{
	int	i;

	i = 1;
	while (i < ac - 1)
	{
		if (!is_number(av[i]))
			return (fprintf(stderr,
					"\033[1;31mError:\033[0m: '%s' is not a valid number\n",
					av[i]), 0);
		i++;
	}
	if ((strcmp(av[8], "edf") && strcmp(av[8], "fifo")) && ((strcmp(av[8],
					"EDF") && strcmp(av[8], "FIFO"))))
		return (fprintf(stderr,
				"\033[1;31mError:\033[0m: '%s' is not a valid schedular\n",
				av[8]), 0);
	return (1);
}
