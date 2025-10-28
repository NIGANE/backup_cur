/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:24:01 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/28 18:50:26 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putnbr(long long n, int *count)
{
	if (n < 0)
	{
		ft_putchar('-');
		n *= -1;
		*count += 1;
	}
	if (n >= 10)
		ft_putnbr(n / 10, count);
	*count += ft_putchar(n % 10 + '0');
}