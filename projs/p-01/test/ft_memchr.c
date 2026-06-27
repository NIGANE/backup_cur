/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 13:34:00 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/17 13:24:32 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>
#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	*bf;
	size_t			i;

	i = 0;
	bf = (unsigned char *)s;
	while (i < n)
	{
		if (bf[i] == (unsigned char)c)
			return (&bf[i]);
		i++;
	}
	return (NULL);
}
