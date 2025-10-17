/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:10:04 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/16 19:11:42 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putstr_fd(char *s, int fd)
{
	while (*s)
		write(1, s++, fd);
}

int 	main(void)
{
	ft_putstr_fd("Hello, World!", 1);
	ft_putstr_fd("\n", 1);
	ft_putstr_fd("This is a test of ft_putstr_fd function.", 1);
	ft_putstr_fd("\n", 1);
	ft_putstr_fd("", 1);
	ft_putstr_fd("\n", 1);
	
	return (0);
}