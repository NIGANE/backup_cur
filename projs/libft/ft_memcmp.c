/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 13:35:16 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 13:35:21 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*s1_buf;
	unsigned char	*s2_buf;
	size_t			i;

	i = 0;
	s1_buf = (unsigned char *)s1;
	s2_buf = (unsigned char *)s2;
	while (i < n)
	{
		if (s1_buf[i] != s2_buf[i])
			return (s1_buf[i] - s2_buf[i]);
		i++;
	}
	return (0);
}
