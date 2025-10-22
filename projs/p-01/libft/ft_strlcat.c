/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 10:01:27 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 10:01:31 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>
#include "libft.h"

size_t	ne_strlen(const char *str)
{
	size_t	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	sr_len;
	size_t	ds_len;
	size_t	i;

	i = 0;
	sr_len = ne_strlen(src);
	if (!dest && size == 0)
		return (sr_len);
	ds_len = ne_strlen(dest);
	if (size != 0)
	{
		while (src[i] != '\0' && i + ds_len < size - 1)
		{
			dest[ds_len + i] = src[i];
			i++;
		}
		dest[ds_len + i] = '\0';
	}
	if (ds_len < size)
		return (sr_len + ds_len);
	else
		return (size + sr_len);
}
