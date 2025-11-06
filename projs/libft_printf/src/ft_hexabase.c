/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_hexabase.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 15:42:06 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/04 15:45:54 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

void	ft_hexabase(unsigned long int nb, char *hex, int *count)
{
	if (nb == 0)
		return ;
	if (nb >= 16)
		ft_hexabase(nb / 16, hex, count);
	*count += ft_putchar(hex[nb % 16]);
}
