/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:24:01 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/28 13:39:18 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putchar_fd_me(char c, int fd)
{
	write(fd, &c, 1);
}

void	ft_putnbr_fd(long long n, int fd)
{
	// static int a;

	// a = 0;
	if (n == -2147483648)
	{
		ft_putchar_fd_me('-', fd);
		ft_putchar_fd_me('2', fd);
		ft_putnbr_fd(147483648, fd);
		return ;
	}
	if (n < 0)
	{
		ft_putchar_fd_me('-', fd);
		n *= -1;
	}
	if (n >= 10)
		ft_putnbr_fd(n / 10, fd);
	ft_putchar_fd_me(n % 10 + '0', fd);
	
}