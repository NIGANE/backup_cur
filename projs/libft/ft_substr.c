/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 19:08:56 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 19:21:54 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*re;
	size_t	i;

	i = 0;
	re = malloc(sizeof(char) * len);
	if (!re)
		return (NULL);
	while (*s)
	{
		if (*s == (char)start)
		{
			while (*s && len-- > 0)
				re[i++] = *s++;
			return (re);
		}
		s++;
	}
	return (malloc(0));
}
