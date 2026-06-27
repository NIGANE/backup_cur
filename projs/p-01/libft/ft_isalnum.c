/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 09:54:46 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 09:54:54 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_isalpha_me(int a)
{
	if ((a >= 65 && a <= 90) || (a >= 97 && a <= 122))
		return (1);
	return (0);
}

int	ft_isdigit_me(int a)
{
	if (a >= 48 && a <= 57)
		return (1);
	return (0);
}

int	ft_isalnum(int a)
{
	if (ft_isdigit_me(a) || ft_isalpha_me(a))
		return (1);
	return (0);
}
