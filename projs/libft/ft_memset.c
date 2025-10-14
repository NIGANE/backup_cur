/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 11:21:15 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 11:22:03 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

void	*ft_memset(void *data, int c, size_t size)
{
	unsigned char	*buf;

	buf = (unsigned char *) data;
	while (size-- > 0)
		*buf++ = (unsigned int) c;
	return (data);
}
