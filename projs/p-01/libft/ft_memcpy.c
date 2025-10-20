/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 11:49:45 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/18 10:28:17 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>
#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t size)
{
	unsigned char	*dest_buf;
	unsigned char	*src_buf;

	dest_buf = (unsigned char *) dest;
	src_buf = (unsigned char *) src;
	while (size-- > 0)
		*dest_buf++ = *src_buf++;
	return (dest);
}
