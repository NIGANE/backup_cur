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

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	s_len;
	size_t	d_len;
	size_t	f_size;

	d_len = 0;
	f_size = 0;
	s_len = 0;
	while (src[s_len])
		s_len++;
	while (dst[d_len])
		d_len++;
	f_size = d_len + s_len;
	while ((size - d_len - 1) > 0 && *src)
		dst[d_len++] = *src++;
	dst[d_len] = '\0';
	return (f_size);
}
