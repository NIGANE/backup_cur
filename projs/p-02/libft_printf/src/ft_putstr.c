/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 15:42:39 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/04 15:46:59 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

int	ft_putstr(char *s)
{
	if (s == NULL)
		return ((int)write(1, "(null)", 6));
	return ((int)write(1, s, ft_strlen(s)));
}
